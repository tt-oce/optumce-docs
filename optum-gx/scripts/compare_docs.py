"""Report which OptumGX docstrings are out of sync with the markdown docs.

Reuses gen_python_docs to render each docstring to markdown, then diffs the
rendered output against the .md currently on disk. The on-disk .md is treated
as the reference ("what the docs should say"); a difference means the source
docstring is stale and should be updated.

For each out-of-sync function it reports:
  * which sections differ (Overview / Parameters / Examples / Notes / See also)
  * how many lines changed
  * a severity rating

Usage:
    py compare_docs.py            # summary table
    py compare_docs.py --diff     # also print the unified diff per function
"""
from __future__ import annotations

import argparse
import difflib
import re
from pathlib import Path

import gen_python_docs as g


SECTION_HEADING_RE = re.compile(r'^##\s+(.*)$')


def split_sections(md: str) -> dict:
    """Break rendered markdown into {section_name: body}. The text before the
    first '## ' heading is the Overview (the first line is the '# name' title)."""
    sections = {}
    current = "Overview"
    buf = []
    for line in md.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            continue  # the title line
        m = SECTION_HEADING_RE.match(line)
        if m:
            sections[current] = "\n".join(buf).strip()
            current = m.group(1).strip()
            buf = []
        else:
            buf.append(line)
    sections[current] = "\n".join(buf).strip()
    return {k: v for k, v in sections.items() if v}


def changed_sections(existing: str, rendered: str) -> list:
    a = split_sections(existing)
    b = split_sections(rendered)
    names = []
    for key in ["Overview", "Parameters", "Examples", "Notes", "See also"]:
        if a.get(key, "") != b.get(key, ""):
            if key in a and key not in b:
                names.append(f"{key} (removed from docstring)")
            elif key in b and key not in a:
                names.append(f"{key} (only in docstring)")
            else:
                names.append(key)
    # catch any sections we didn't name explicitly
    for key in set(a) | set(b):
        if key not in ["Overview", "Parameters", "Examples", "Notes", "See also"]:
            if a.get(key, "") != b.get(key, ""):
                names.append(key)
    return names


def line_stats(existing: str, rendered: str):
    a = existing.splitlines()
    b = rendered.splitlines()
    sm = difflib.SequenceMatcher(None, a, b)
    added = removed = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("replace", "delete"):
            removed += (i2 - i1)
        if tag in ("replace", "insert"):
            added += (j2 - j1)
    ratio = sm.ratio()
    return added, removed, ratio


def severity(added, removed, ratio, total_lines, sections):
    changed = added + removed
    if ratio < 0.5 or changed > max(20, total_lines):
        return "HIGH"
    if ratio < 0.85 or changed > 6 or len(sections) >= 2:
        return "MEDIUM"
    return "LOW"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default=str(g.DEFAULT_SOURCE))
    ap.add_argument("--diff", action="store_true", help="print unified diff per file")
    args = ap.parse_args()

    docs = g.extract_docs(Path(args.source))
    func_to_cat = {}
    for d in docs:
        func_to_cat.setdefault(d.func_name, d.categories[0])

    rows = []
    for d in docs:
        rendered = g.render_markdown(d, func_to_cat)
        for cat in d.categories:
            target = g.DOCS_ROOT / cat / f"{d.func_name}.md"
            if not target.exists():
                rows.append((d.func_name, cat, "MISSING", "no .md on disk yet",
                             0, 0, 0.0, rendered, ""))
                continue
            existing = target.read_text(encoding="utf-8")
            if existing == rendered:
                continue
            secs = changed_sections(existing, rendered)
            added, removed, ratio = line_stats(existing, rendered)
            total = max(len(existing.splitlines()), len(rendered.splitlines()))
            sev = severity(added, removed, ratio, total, secs)
            rows.append((d.func_name, cat, sev, ", ".join(secs) or "formatting only",
                         added, removed, ratio, rendered, existing))

    order = {"MISSING": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    rows.sort(key=lambda r: (order.get(r[2], 9), -(r[4] + r[5]), r[0]))

    print(f"{'SEVERITY':<8} {'FUNCTION':<28} {'CAT':<11} {'+/-':<9} CHANGED SECTIONS")
    print("-" * 100)
    for fn, cat, sev, secs, added, removed, ratio, *_ in rows:
        pm = f"+{added}/-{removed}"
        print(f"{sev:<8} {fn:<28} {cat:<11} {pm:<9} {secs}")

    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    print("-" * 100)
    print("Totals: " + ", ".join(f"{k}={v}" for k, v in
                                  sorted(counts.items(), key=lambda x: order.get(x[0], 9))))
    print(f"({len(rows)} out-of-sync doc targets)")

    if args.diff:
        for fn, cat, sev, secs, added, removed, ratio, rendered, existing in rows:
            print("\n" + "=" * 100)
            print(f"{sev}  {cat}/{fn}.md   ({secs})")
            print("=" * 100)
            diff = difflib.unified_diff(
                existing.splitlines(), rendered.splitlines(),
                fromfile=f"{cat}/{fn}.md (on disk / docs)",
                tofile=f"{fn} docstring (source)", lineterm="")
            for line in diff:
                print(line)
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
