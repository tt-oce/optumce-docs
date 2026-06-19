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

# Default source path. Switch back to the release install path
# (C:\Users\Public\OPTUM CE\OPTUM GX\library\OptumGX) once the release is
# reinstalled. Both layouts are identical -- the script doesn't care.
DEFAULT_SOURCE = Path(r"C:\Optum\OptumGX\Rpc\src\OptumGX")
SOURCE_FILES = [
    "v2.py",
    "ContractV2_gen.py",
    "DataModelV2.py",
    "Common.py",
    "Materials/RemoteMaterialAPI.pyi",
    "RemoteFeatures/FeatureAPI.pyi",
]

# Directory walks producing one Object class page per .py file. Each file is
# assumed to define a single class with the same name as the file (e.g.
# Materials/MohrCoulomb.py -> class MohrCoulomb). Helper bases / API wrappers
# are filtered out via the SKIP list.
OBJECT_DIRS = [
    {
        "subdir": "Materials",
        "subcategory": "materials",
        "skip": {"RemoteMaterial.py", "RemoteMaterialAPI.py",
                 "RemoteMaterialAPI.pyi", "_docloader.py", "__init__.py"},
    },
    {
        "subdir": "RemoteFeatures",
        "subcategory": "features",
        "skip": {"Feature.py", "FeatureAPI.py", "FeatureAPI.pyi",
                 "__init__.py"},
    },
]

# Class name in the source -> doc folder(s) under optum-gx/python/functions/.
# StageBase methods are inherited by both Model and Stage. Instead of writing
# them to both model/ and stage/, they go to a shared "model-and-stage/" folder.
# _RemoteStage (in ContractV2_gen.py) holds set/get_analysis_properties (stage/).
# RemoteMaterialAPI holds the material factories (project/).
# FeatureAPI holds set_solid/set_plate/... (model/).
# ModelFeatureAPI extends with model-only methods.
# StageFeatureAPI extends with stage-only ones (toggle_features).
CLASS_TO_CATEGORIES = {
    "GX": ["application"],
    "Project": ["project"],
    "Model": ["model"],
    "Stage": ["stage"],
    "StageBase": ["model-and-stage"],
    "_RemoteStage": ["model-and-stage"],
    "AnalysisProperties": ["stage"],
    "Shape": ["objects"],
    "ShapeList": ["objects"],
    "RemoteMaterialAPI": ["project"],
    "FeatureAPI": ["model"],
    "ModelFeatureAPI": ["model"],
    "StageFeatureAPI": ["stage"],
    # Parameter variation classes (Common.py) -- flat under utilities/.
    "ParameterMap": ["utilities"],
    "Profile": ["utilities"],
    "Gradient": ["utilities"],
}

# Per-category function-name -> subcategory mapping. The renderer composes
# the target path as DOCS_ROOT / category / subcategory / name.md when a match
# exists, otherwise DOCS_ROOT / category / name.md (i.e. unmapped functions
# land at the category root -- useful as a "fix me" surface for new methods).
SUBCATEGORIES = {
    "application": {
        # All five Application/GX methods are workflow ops; flat layout is fine,
        # but expose under operations/ for consistency with the other categories.
        "create_project": "operations", "open_project": "operations",
        "save_project": "operations", "write_step": "operations",
        "get_current_project": "operations",
    },
    "project": {
        # Material factories (one entry per MaterialType -- same name as the
        # generated material class).
        "AUS": "materials", "Beam": "materials", "Connector": "materials",
        "DruckerPrager": "materials", "FlatPlateConcrete": "materials",
        "FlatPlateSteel": "materials", "GeneralPlate": "materials",
        "Geogrid": "materials", "HMC": "materials", "HardeningSoil": "materials",
        "HoekBrown": "materials", "LinearElastic": "materials",
        "ModifiedCamClay": "materials", "MohrCoulomb": "materials",
        "MohrCoulombEngineering": "materials", "MultiMohrCoulomb": "materials",
        "NGIADP": "materials", "NailRow": "materials", "PileRow": "materials",
        "ReinforcedConcrete": "materials", "Rigid": "materials",
        "RigidBeam": "materials", "RigidPlate": "materials",
        "SheetPile": "materials", "Tresca": "materials", "Water": "materials",
        "get_material": "materials",
        # Coordinate-system creation -- geometry domain.
        "create_csys_2d": "geometry", "create_csys_3d": "geometry",
        "get_csys": "geometry",
        # Running analyses.
        "run_analysis": "analysis", "run_analysis_async": "analysis",
        "get_current_result_set": "analysis",
        # Project / model / stage management.
        "create_model": "operations", "get_model": "operations",
        "get_current_model": "operations", "set_current_model": "operations",
        "get_current_stage": "operations", 
        "get_file_path": "operations", "get_python_code": "operations",
    },
    "model": {
        # Geometry creation
        "add_arc": "geometry", "add_box": "geometry", "add_circle": "geometry",
        "add_connector": "geometry", "add_line": "geometry",
        "add_lines": "geometry", "add_ncone": "geometry",
        "add_nprism": "geometry", "add_polygon": "geometry",
        "add_polygons": "geometry", "add_polyline": "geometry",
        "add_prism": "geometry", "add_rectangle": "geometry",
        "add_sphere": "geometry", "add_vertex": "geometry",
        # Geometry modification
        "delete_interior": "geometry", "delete_shapes": "geometry",
        "extrude": "geometry", "extrude_2d_to_3d_model": "geometry",
        "extrude_along": "geometry", "revolve": "geometry",
        "revolve_2d_to_3d_model": "geometry",
        "slice_3d_to_2d_model": "geometry",
        "mirror": "geometry", "polar_array": "geometry",
        "rectangular_array": "geometry", "rotate": "geometry",
        "scale": "geometry", "move": "geometry", "copy": "geometry",
        "set_vertex_position": "geometry",
        # 2D-to-3D extrude configuration
        "get_extrude_to_3d": "geometry", "set_extrude_to_3d": "geometry",
        # Features (FeatureAPI)
        "set_solid": "features", "set_plate": "features",
        "set_interface": "features", "set_geogrid": "features",
        "set_nailrow": "features", "set_connector": "features",
        "add_connector": "features",
        "set_support": "features", "set_water_table": "features",
        "set_no_flow": "features", "set_seepage_face": "features",
        "set_surface_load": "features", "set_line_load": "features",
        "set_point_load": "features", "set_body_load": "features",
        "set_line_moment": "features", "set_point_moment": "features",
        "set_six_dof_load": "features",
        "set_fixed_head": "features", "set_fixed_pressure": "features",
        "set_fixed_excess_pressure": "features",
        "set_point_bc": "features", "set_plate_bc": "features",
        "set_resultpoint": "features",
        "set_prestress": "features", "set_reaction_relaxation": "features",
        "set_fixed_end_anchor": "features", "add_fixed_end_anchor": "features",
        "set_pilerow": "features",
        "set_hinge_2d": "features", "set_hinge_3d": "features",
        "set_standard_fixities": "features", "get_features": "features",
        "remove_features": "features",
        # Feature getters (mirror of the setters above)
        "get_solid": "features", "get_plate": "features",
        "get_interface": "features", "get_geogrid": "features",
        "get_nailrow": "features", "get_connector": "features",
        "get_support": "features", "get_water_table": "features",
        "get_no_flow": "features", "get_seepage_face": "features",
        "get_surface_load": "features", "get_line_load": "features",
        "get_point_load": "features", "get_body_load": "features",
        "get_line_moment": "features", "get_point_moment": "features",
        "get_six_dof_load": "features",
        "get_fixed_head": "features", "get_fixed_pressure": "features",
        "get_fixed_excess_pressure": "features",
        "get_point_bc": "features", "get_plate_bc": "features",
        "get_resultpoint": "features",
        "get_prestress": "features", "get_reaction_relaxation": "features",
        "get_fixed_end_anchor": "features", "get_pilerow": "features",
        # Meshing
        "set_mesh_size": "meshing", "set_mesh_fan": "meshing",
        "get_mesh_size": "meshing", "get_mesh_fan": "meshing",
        # Analysis (stage-inheritance settings on Model)
        "from_model": "analysis", "set_from_model": "analysis",
        # Operations
        "model_type": "operations",
        "get_current_stage": "operations", "set_current_stage": "operations",
        "get_stage": "operations", 
        "hide_shapes": "operations", "unhide_shapes": "operations",
        "unhide_all_shapes": "operations",
        "enable_transparency": "operations",
        "disable_transparency": "operations",
        "disable_global_transparency": "operations",
    },
    "stage": {
        # Analysis settings on Stage itself (not the inherited ones).
        "set_analysis_properties": "analysis",
        "get_analysis_properties": "analysis",
        "set_from_stage": "analysis",
        # Stage-only features API.
        "toggle_features": "features",
        # Stage-only operations.
        "create_stage": "operations", "model": "operations",
    },
    "model-and-stage": {
        # StageBase methods: geometry / analysis / operations buckets.
        "select": "geometry",
        "edges": "geometry", "faces": "geometry",
        "vertices": "geometry", "volumes": "geometry",
        "get_active_csys": "geometry", "set_active_csys": "geometry",
        "get_selected_shapes": "geometry", "get_shape_by_id": "geometry",
        "get_shapes": "geometry", "get_shapes_by_vertices": "geometry",
        "get_shared_edges": "geometry", "get_shared_faces": "geometry",
        "get_sub_shapes": "geometry", "get_vertices": "geometry",
        "output": "analysis", "set_solver_settings": "analysis",
        # Methods inherited from _RemoteStage (set/get_analysis_properties).
        "set_analysis_properties": "analysis",
        "get_analysis_properties": "analysis",
        "clone": "operations", "delete": "operations",
        "undo": "operations", "redo": "operations", "zoom_all": "operations",
        "create_stage": "operations",
        "get_run_flag": "analysis", "set_run_flag": "analysis",
    },
    "objects": {
        # The two existing Object class pages live under geometry/ in objects/.
        "Shape": "geometry", "ShapeList": "geometry",
    },
}

# Classes rendered as a SINGLE page (overview + Properties + Methods) instead of
# one page per method. Properties come from a numpy-style "Attributes" section in
# the class docstring; methods are the public, non-@property callables.
CLASS_PAGE_CLASSES = {"Shape", "ShapeList", "ParameterMap", "Profile", "Gradient"}

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
    """A class rendered as a single page (overview + Properties + Methods).
    Each entry in `methods` carries the full method docstring so per-method
    sub-pages can be emitted at <ClassName>/<method>.md when present."""
    class_name: str
    docstring: str          # full class docstring (overview + Attributes section)
    categories: list
    methods: list           # list of (name, one-line summary, full_docstring)


def _is_property(func: ast.FunctionDef) -> bool:
    """True if the def is decorated with @property (so it's a data attribute,
    documented via the class Attributes section rather than as a method)."""
    return any(isinstance(d, ast.Name) and d.id == "property"
               for d in func.decorator_list)


def _extract_class_methods(class_node: ast.ClassDef) -> list:
    """Return [(name, summary, full_docstring), ...] for public non-property
    methods of a class. Used when the class itself is rendered as a single
    page (ClassDoc) -- the summary feeds the Methods list on the class page,
    the full docstring feeds the per-method sub-page."""
    out = []
    for sub in class_node.body:
        if not isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if sub.name.startswith("_") or _is_property(sub):
            continue
        ds = ast.get_docstring(sub, clean=True) or ""
        summary = ds.strip().split("\n")[0] if ds else ""
        out.append((sub.name, summary, ds))
    return out


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
                methods = _extract_class_methods(node)
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

    # Object class pages from per-file dirs (Materials/, RemoteFeatures/).
    # Each .py file in such a dir is assumed to define a class with the same
    # name as the file. We register the subcategory at runtime so the path
    # resolver and link map pick them up without manual SUBCATEGORIES entries.
    objects_subs = SUBCATEGORIES.setdefault("objects", {})
    for cfg in OBJECT_DIRS:
        dir_path = source_root / cfg["subdir"]
        if not dir_path.exists():
            print(f"warning: object dir not found: {dir_path}", file=sys.stderr)
            continue
        for py in sorted(dir_path.glob("*.py")):
            if py.name in cfg["skip"]:
                continue
            class_name = py.stem
            try:
                tree = ast.parse(py.read_text(encoding="utf-8"))
            except SyntaxError as e:
                print(f"warning: skipping {py}: {e}", file=sys.stderr)
                continue
            cls_node = next(
                (n for n in tree.body
                 if isinstance(n, ast.ClassDef) and n.name == class_name),
                None,
            )
            if cls_node is None:
                continue
            class_ds = ast.get_docstring(cls_node, clean=True) or ""
            methods = _extract_class_methods(cls_node)
            docs.append(ClassDoc(class_name, class_ds, ["objects"], methods))
            objects_subs[class_name] = cfg["subcategory"]

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

def render_markdown(doc: FuncDoc, link_map: dict) -> str:
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
                # Look the ref up in the global (name -> (category, sub)) map.
                # Fallback: same category and subcategory as the current doc.
                loc = link_map.get(ref)
                if loc:
                    cat, sub = loc
                else:
                    cat = doc.categories[0]
                    sub = SUBCATEGORIES.get(cat, {}).get(ref)
                path = f"/python/functions/{cat}/{sub}/{ref}" if sub \
                       else f"/python/functions/{cat}/{ref}"
                parts.append(f"- [{ref}]({path})")
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


def render_class_markdown(doc: ClassDoc, link_map: dict) -> str:
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

    # Methods entries link to per-method sub-pages when the method has a
    # docstring (so the sub-page actually exists). Plain text otherwise.
    if doc.methods:
        cat = doc.categories[0]
        sub = SUBCATEGORIES.get(cat, {}).get(doc.class_name)
        base = f"/python/functions/{cat}/{sub}/{doc.class_name}" if sub \
               else f"/python/functions/{cat}/{doc.class_name}"
        parts.append("## Methods")
        parts.append("")
        parts.append("<dl>")
        for name, summary, ds in doc.methods:
            if ds:
                parts.append(f'<dt><a href="{base}/{name}">{name}()</a></dt>')
            else:
                parts.append(f"<dt>{name}()</dt>")
            if summary:
                parts.append(f"<dd>{summary}</dd>")
        parts.append("</dl>")
        parts.append("")

    while parts and parts[-1] == "":
        parts.pop()
    parts.append("")
    return "\n".join(parts)


def render_class_method_markdown(class_name: str, method_doc: FuncDoc,
                                 link_map: dict) -> str:
    """Render a method of an Object class as its own page. Same body as
    render_markdown but the H1 is class-qualified (e.g. '# Shape.center')."""
    md = render_markdown(method_doc, link_map)
    return md.replace(
        f"# {method_doc.func_name}\n",
        f"# {class_name}.{method_doc.func_name}\n",
        1,
    )


# ---- Writer -----------------------------------------------------------------

def _doc_name(d) -> str:
    """Output base name (without .md) for a FuncDoc or ClassDoc."""
    return d.class_name if isinstance(d, ClassDoc) else d.func_name


def _resolve_path(category: str, name: str) -> Path:
    """Compose the target md path, honoring SUBCATEGORIES if a match exists.
    Unmapped names land at the category root."""
    sub = SUBCATEGORIES.get(category, {}).get(name)
    if sub:
        return DOCS_ROOT / category / sub / f"{name}.md"
    return DOCS_ROOT / category / f"{name}.md"


def _build_link_map(docs: list) -> dict:
    """name -> (category, subcategory_or_None) for See-also link resolution.
    A function that appears in multiple categories is resolved to the first
    one listed in CLASS_TO_CATEGORIES (e.g. StageBase's "model-and-stage")."""
    out = {}
    for d in docs:
        name = _doc_name(d)
        if name in out:
            continue
        cat = d.categories[0]
        sub = SUBCATEGORIES.get(cat, {}).get(name)
        out[name] = (cat, sub)
    return out


def write_docs(docs: list, dry_run: bool, verbose: bool):
    """Render each doc and write only files whose content changed.
    Returns (written, unchanged, set_of_touched_paths)."""
    link_map = _build_link_map(docs)

    written = 0
    unchanged = 0
    touched = set()

    def _emit(target: Path, rendered: str):
        nonlocal written, unchanged
        touched.add(target)
        if target.exists() and target.read_text(encoding="utf-8") == rendered:
            unchanged += 1
            return
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

    for d in docs:
        if isinstance(d, ClassDoc):
            rendered = render_class_markdown(d, link_map)
        else:
            rendered = render_markdown(d, link_map)
        for cat in d.categories:
            target = _resolve_path(cat, _doc_name(d))
            _emit(target, rendered)

        # Per-method sub-pages for Object classes (only when the method has
        # a docstring -- skips creating the <Class>/ folder otherwise).
        if isinstance(d, ClassDoc):
            for method_name, _summary, method_ds in d.methods:
                if not method_ds:
                    continue
                method_doc = FuncDoc(d.class_name, method_name, method_ds,
                                     d.categories)
                method_rendered = render_class_method_markdown(
                    d.class_name, method_doc, link_map)
                for cat in d.categories:
                    parent = _resolve_path(cat, d.class_name).with_suffix("")
                    method_target = parent / f"{method_name}.md"
                    _emit(method_target, method_rendered)

    return written, unchanged, touched


def find_orphans(touched: set) -> list:
    """List .md files anywhere under DOCS_ROOT that weren't (re)generated this
    run -- likely candidates for deletion, but never deleted automatically.
    Recurses into subcategory folders."""
    orphans = []
    for cat_dir in DOCS_ROOT.iterdir():
        if not cat_dir.is_dir():
            continue
        for md in cat_dir.rglob("*.md"):
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
