"""Generate API reference markdown files from OptumGX docstrings.

Reads docstrings from the OptumGX Python source files via static AST parsing
(no OptumGX imports required), renders each into a .md file under
optum-gx/python/functions/<category>/<name>.md matching the format used
elsewhere in the repo.

Change detection: this script always regenerates every .md file from source.
Use `git status` / `git diff` in the docs repo to see which files actually
changed -- only those whose docstring content differs from what's currently
on disk get rewritten, so the git diff is minimal.

Source-of-truth policy: docstrings in the OptumGX Python source win. If a
generated .md disagrees with a hand-edited one, fix the docstring upstream.

Usage:
    python gen_python_docs.py                # regenerate, write changes
    python gen_python_docs.py --dry-run      # show what would change
    python gen_python_docs.py --source PATH  # point at a different install
    python gen_python_docs.py -v             # list every touched file
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path


# ---- Configuration ----------------------------------------------------------

DEFAULT_SOURCE = Path(r"C:\Users\Public\OPTUM CE\OPTUM GX\library\OptumGX")
SOURCE_FILES = ["v2.py", "ContractV2_gen.py", "DataModelV2.py"]

# Class name in the source -> doc folder(s) under optum-gx/python/functions/.
# StageBase methods are inherited by both Model and Stage, so duplicate them.
# _RemoteStage (in ContractV2_gen.py) holds set/get_analysis_properties, which
# the existing docs place under stage/.
CLASS_TO_CATEGORIES = {
    "GX": ["application"],
    "Project": ["project"],
    "Model": ["model"],
    "Stage": ["stage"],
    "StageBase": ["model", "stage"],
    "_RemoteStage": ["stage"],
    "AnalysisProperties": ["model","stage"],
    "Shape": ["geometry"],
    "ShapeList": ["geometry"],
}

# Classes rendered as a SINGLE page (overview + Properties + Methods) instead of
# one page per method. Properties come from a numpy-style "Attributes" section in
# the class docstring; methods are the public, non-@property callables.
CLASS_PAGE_CLASSES = {"Shape", "ShapeList"}

SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_ROOT = SCRIPT_DIR.parent / "python" / "functions"
REPO_ROOT = DOCS_ROOT.parent.parent.parent

SECTION_RE = re.compile(r'^(Parameters|Returns|Examples|See Also|Notes)\s*$', re.MULTILINE)
ATTR_HEADER_RE = re.compile(r'^Attributes\s*$', re.MULTILINE)
PARAM_RE = re.compile(r'^\s*(\w+)\s*:\s*(.+?)\s*$')
SEPARATOR_RE = re.compile(r'^-{5,}\s*$')
INDEX_FILES = {"index.md", "index.yaml", "index.yml"}


# ---- Data model -------------------------------------------------------------

@dataclass
class FuncDoc:
    class_name: str
    func_name: str
    docstring: str
    categories: list


@dataclass
class ClassDoc:
    """A class rendered as a single page (overview + Properties + Methods)."""
    class_name: str
    docstring: str          # full class docstring (overview + Attributes section)
    categories: list
    methods: list           # list of (name, one-line summary)


def _is_property(func: ast.FunctionDef) -> bool:
    """True if the def is decorated with @property (so it's a data attribute,
    documented via the class Attributes section rather than as a method)."""
    return any(isinstance(d, ast.Name) and d.id == "property"
               for d in func.decorator_list)


# ---- Extraction (AST) -------------------------------------------------------

def extract_docs(source_root: Path) -> list:
    """Walk the configured source files and pull every (class, method, docstring)
    we know how to route to a doc category. Returns a mix of FuncDoc (one page per
    method) and ClassDoc (one page per class, for CLASS_PAGE_CLASSES)."""
    docs = []
    for fname in SOURCE_FILES:
        path = source_root / fname
        if not path.exists():
            print(f"warning: source file not found: {path}", file=sys.stderr)
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            cats = CLASS_TO_CATEGORIES.get(node.name)
            if not cats:
                continue

            if node.name in CLASS_PAGE_CLASSES:
                methods = []
                for sub in node.body:
                    if not isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    if sub.name.startswith("_") or _is_property(sub):
                        continue
                    ds = ast.get_docstring(sub, clean=True) or ""
                    summary = ds.strip().split("\n")[0] if ds else ""
                    methods.append((sub.name, summary))
                class_ds = ast.get_docstring(node, clean=True) or ""
                docs.append(ClassDoc(node.name, class_ds, cats, methods))
                continue

            for sub in node.body:
                if not isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if sub.name.startswith("_"):
                    continue
                ds = ast.get_docstring(sub, clean=True)
                if not ds:
                    continue
                docs.append(FuncDoc(node.name, sub.name, ds, cats))
    return docs


def parse_attributes(docstring: str):
    """Split a class docstring into (overview_text, [(name, type, desc), ...]).
    The attribute list is parsed from a numpy-style 'Attributes' section."""
    m = ATTR_HEADER_RE.search(docstring)
    if not m:
        return docstring, []
    overview = docstring[:m.start()]
    rest = docstring[m.end():]
    nxt = SECTION_RE.search(rest)          # stop at any following named section
    block = rest[:nxt.start()] if nxt else rest

    attrs = []
    name = typ = None
    desc_buf = []

    def flush():
        if name is not None:
            attrs.append((name, typ, " ".join(desc_buf)))

    for line in block.split("\n"):
        s = line.strip()
        if not s or SEPARATOR_RE.match(s):
            continue
        indented = line[:1] in (" ", "\t")
        pm = PARAM_RE.match(s)
        if not indented and pm:
            flush()
            name, typ, desc_buf = pm.group(1), pm.group(2).strip(), []
        elif not indented and name is None:
            flush()
            name, typ, desc_buf = s, "", []
        else:
            desc_buf.append(s)
    flush()
    return overview, attrs


# ---- Rendering --------------------------------------------------------------

def render_markdown(doc: FuncDoc, func_to_cat: dict) -> str:
    """Render a FuncDoc to markdown matching the repo's existing style."""
    parts = [f"# {doc.func_name}", ""]

    sections = SECTION_RE.split(doc.docstring)

    overview = sections[0].strip()
    if overview:
        parts.append(overview)
        parts.append("")

    for i in range(1, len(sections), 2):
        title = sections[i].strip()
        content = sections[i + 1].strip()

        if title == "Parameters":
            parts.append("## Parameters")
            parts.append("")
            parts.append("<dl>")
            desc_buf = []
            for line in content.split("\n"):
                line = line.strip()
                if not line or SEPARATOR_RE.match(line):
                    continue
                m = PARAM_RE.match(line)
                if m:
                    if desc_buf:
                        parts.append(f"<dd>{' '.join(desc_buf)}</dd>")
                        desc_buf = []
                    name, typ = m.groups()
                    parts.append(f"<dt>{name} : {typ.strip()}</dt>")
                else:
                    desc_buf.append(line)
            if desc_buf:
                parts.append(f"<dd>{' '.join(desc_buf)}</dd>")
            parts.append("</dl>")
            parts.append("")

        elif title == "Returns":
            # numpy style: a non-indented line is a return type (or "name : type"),
            # following indented lines are its description.
            parts.append("## Returns")
            parts.append("")
            parts.append("<dl>")
            desc_buf = []
            for line in content.split("\n"):
                if not line.strip() or SEPARATOR_RE.match(line.strip()):
                    continue
                if line[:1] in (" ", "\t"):
                    desc_buf.append(line.strip())
                else:
                    if desc_buf:
                        parts.append(f"<dd>{' '.join(desc_buf)}</dd>")
                        desc_buf = []
                    parts.append(f"<dt>{line.strip()}</dt>")
            if desc_buf:
                parts.append(f"<dd>{' '.join(desc_buf)}</dd>")
            parts.append("</dl>")
            parts.append("")

        elif title == "Examples":
            parts.append("## Examples")
            parts.append("")
            parts.append("```python")
            for line in content.split("\n"):
                if SEPARATOR_RE.match(line.strip()):
                    continue
                # strip interactive prompts: '>>>' and '...' continuation
                line = re.sub(r'^\s*(?:>>>|\.\.\.)\s?', '', line)
                parts.append(line)
            parts.append("```")
            parts.append("")

        elif title == "See Also":
            parts.append("## See also")
            parts.append("")
            for raw in re.split(r'[,;\n]', content):
                ref = raw.strip()
                if not ref or SEPARATOR_RE.match(ref):
                    continue
                cat = func_to_cat.get(ref, doc.categories[0])
                parts.append(f"- [{ref}](/python/functions/{cat}/{ref})")
            parts.append("")

        elif title == "Notes":
            parts.append("## Notes")
            parts.append("")
            for line in content.split("\n"):
                if SEPARATOR_RE.match(line.strip()):
                    continue
                parts.append(line)
            parts.append("")

    while parts and parts[-1] == "":
        parts.pop()
    parts.append("")
    return "\n".join(parts)


def render_class_markdown(doc: ClassDoc, func_to_cat: dict) -> str:
    """Render a ClassDoc to a single page: overview, Properties, Methods."""
    parts = [f"# {doc.class_name}", ""]

    overview, attrs = parse_attributes(doc.docstring)
    overview = overview.strip()
    if overview:
        parts.append(overview)
        parts.append("")

    if attrs:
        parts.append("## Properties")
        parts.append("")
        parts.append("<dl>")
        for name, typ, desc in attrs:
            parts.append(f"<dt>{name} : {typ}</dt>" if typ else f"<dt>{name}</dt>")
            if desc:
                parts.append(f"<dd>{desc}</dd>")
        parts.append("</dl>")
        parts.append("")

    if doc.methods:
        parts.append("## Methods")
        parts.append("")
        parts.append("<dl>")
        for name, summary in doc.methods:
            parts.append(f"<dt>{name}()</dt>")
            if summary:
                parts.append(f"<dd>{summary}</dd>")
        parts.append("</dl>")
        parts.append("")

    while parts and parts[-1] == "":
        parts.pop()
    parts.append("")
    return "\n".join(parts)


# ---- Writer -----------------------------------------------------------------

def _doc_name(d) -> str:
    """Output base name (without .md) for a FuncDoc or ClassDoc."""
    return d.class_name if isinstance(d, ClassDoc) else d.func_name


def write_docs(docs: list, dry_run: bool, verbose: bool):
    """Render each doc and write only files whose content changed.
    Returns (written, unchanged, set_of_touched_paths)."""
    # See-also link resolution: which category does each name live in?
    # If a method exists in multiple categories (e.g. StageBase), prefer the
    # one that appears first in CLASS_TO_CATEGORIES (model before stage).
    func_to_cat = {}
    for d in docs:
        key = _doc_name(d)
        if key not in func_to_cat:
            func_to_cat[key] = d.categories[0]

    written = 0
    unchanged = 0
    touched = set()
    for d in docs:
        if isinstance(d, ClassDoc):
            rendered = render_class_markdown(d, func_to_cat)
        else:
            rendered = render_markdown(d, func_to_cat)
        for cat in d.categories:
            target = DOCS_ROOT / cat / f"{_doc_name(d)}.md"
            touched.add(target)
            if target.exists() and target.read_text(encoding="utf-8") == rendered:
                unchanged += 1
                continue
            rel = target.relative_to(REPO_ROOT)
            if dry_run:
                if verbose:
                    print(f"would write {rel}")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(rendered, encoding="utf-8")
                if verbose:
                    print(f"wrote {rel}")
            written += 1
    return written, unchanged, touched


def find_orphans(touched: set) -> list:
    """List .md files in category folders that weren't (re)generated this run --
    likely candidates for deletion, but never deleted automatically."""
    orphans = []
    for cat_dir in DOCS_ROOT.iterdir():
        if not cat_dir.is_dir():
            continue
        for md in cat_dir.glob("*.md"):
            if md.name in INDEX_FILES:
                continue
            if md not in touched:
                orphans.append(md)
    return sorted(orphans)


# ---- Entrypoint -------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "--source", default=str(DEFAULT_SOURCE),
        help=f"OptumGX package directory (default: {DEFAULT_SOURCE})",
    )
    ap.add_argument(
        "--dry-run", action="store_true",
        help="Show what would change without writing files",
    )
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="Print each touched file")
    args = ap.parse_args()

    docs = extract_docs(Path(args.source))
    if not docs:
        print("No docstrings found.", file=sys.stderr)
        return 1

    written, unchanged, touched = write_docs(docs, args.dry_run, args.verbose)
    orphans = find_orphans(touched)

    action = "Would write" if args.dry_run else "Wrote"
    n_targets = sum(len(d.categories) for d in docs)
    print(f"{action} {written} files, {unchanged} unchanged "
          f"({len(docs)} functions, {n_targets} doc targets)")

    if orphans:
        print()
        print(f"Possibly orphaned ({len(orphans)} .md files have no matching source function):")
        for o in orphans:
            print(f"  {o.relative_to(REPO_ROOT)}")
        print("  -- delete by hand if these are no longer wanted.")

    print()
    print("Run `git status` / `git diff` in the docs repo to review changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
