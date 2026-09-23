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
Where a .pyi stub sits next to a .py, the stub is read (it's what IDEs show);
edit the stub, not the .py.

Coverage report: after writing, the script lists API it could NOT document --
.py docstrings that never made it into the .pyi, public methods without a
docstring, unmapped classes and inherited bases, pages with no subcategory.
Nothing there is silent any more, so review it on every run.

Full workflow (where each docstring lives, recipes, pitfalls):
Docstring_generation.md at the root of this repo.

Usage:
    python gen_python_docs.py                # regenerate, write changes
    python gen_python_docs.py --dry-run      # show what would change
    python gen_python_docs.py --source PATH  # point at a different install
    python gen_python_docs.py -v             # list every touched file
"""
from __future__ import annotations

import argparse
import ast
import functools
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


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
    "Output.py",     # per-element results (StageResults and friends)
    "ResultV2.py",   # Result (stage.output.global_results)
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
    # Objects returned by the API (class pages under objects/<sub>/).
    "MaterialPoint": ["objects"], "AnalysisProgress": ["objects"],
    "Regional": ["objects"],
    "StageOutput": ["objects"], "StepOutput": ["objects"],
    "MaterialPointOutput": ["objects"], "StageResults": ["objects"],
    "Result": ["objects"], "CriticalResults": ["objects"],
    "ResultIndexer": ["objects"], "ElementIndexer": ["objects"],
    "GeneralProperties": ["objects"], "Topology": ["objects"],
    "PropertyContainer": ["objects"], "ElementResult": ["objects"],
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
        "get_current_project": "operations", "screenshot": "operations",
        "create_material_point": "operations",
        "get_material_point": "operations",
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
        "regional": "operations",
    },
    "model": {
        # Geometry creation
        "add_arc": "geometry", "add_box": "geometry", "add_circle": "geometry",
        "add_line": "geometry",
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
        "take_picture": "operations", "get_plots": "operations",
        "get_run_flag": "analysis", "set_run_flag": "analysis",
    },
    "objects": {
        # Materials/ and RemoteFeatures/ pages are registered at runtime
        # (see OBJECT_DIRS); everything else is listed here.
        "Shape": "geometry", "ShapeList": "geometry",
        "MaterialPoint": "analysis", "AnalysisProgress": "analysis",
        "Regional": "settings",
        # stage.output object graph: StageOutput -> StepOutput -> StageResults
        # -> ResultIndexer -> ElementIndexer -> GeneralProperties / Topology /
        # PropertyContainer -> ElementResult.
        "StageOutput": "results", "StepOutput": "results",
        "MaterialPointOutput": "results", "StageResults": "results",
        "Result": "results", "CriticalResults": "results",
        "ResultIndexer": "results", "ElementIndexer": "results",
        "GeneralProperties": "results", "Topology": "results",
        "PropertyContainer": "results", "ElementResult": "results",
    },
}

# Classes rendered as a SINGLE page (overview + Properties + Methods) instead of
# one page per method. Properties come from a numpy-style "Attributes" section in
# the class docstring; methods are the public, non-@property callables.
CLASS_PAGE_CLASSES = {
    "Shape", "ShapeList", "ParameterMap", "Profile", "Gradient",
    "MaterialPoint", "AnalysisProgress", "Regional",
    "StageOutput", "StepOutput", "MaterialPointOutput", "StageResults",
    "Result", "CriticalResults", "ResultIndexer", "ElementIndexer",
    "GeneralProperties", "Topology", "PropertyContainer", "ElementResult",
}

SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_ROOT = SCRIPT_DIR.parent / "python" / "functions"
REPO_ROOT = DOCS_ROOT.parent.parent.parent

SECTION_RE = re.compile(
    r'^(Parameters|Returns|Raises|Examples|See Also|Notes|Attributes)\s*$',
    re.MULTILINE,
)
ATTR_HEADER_RE = re.compile(r'^Attributes\s*$', re.MULTILINE)
# "name : type", or numpy's grouped form "sx, sy, sz : float".
PARAM_RE = re.compile(r'^\s*(\w+(?:\s*,\s*\w+)*)\s*:\s*(.+?)\s*$')
SEPARATOR_RE = re.compile(r'^-{5,}\s*$')
INDEX_FILES = {"index.md", "index.yaml", "index.yml"}

# Files the script is allowed to KNOW ABOUT (so they don't appear as orphans)
# but never overwrites. Use for pages with overload signatures or other
# structure the auto-renderer can't capture faithfully -- hand-maintained.
# Paths are relative to DOCS_ROOT, forward-slash separated.
SKIP_REGENERATE_PATHS = {
    "model-and-stage/geometry/select.md",
}

# Names the coverage report stays quiet about: a whole class ("RemoteCacheMixin")
# or one method ("GX.app_version"). For plumbing that is public only by naming
# convention -- not a place to park real API that lacks a docstring.
COVERAGE_IGNORE = {
    "RemoteCacheMixin",   # caching/batching base of AnalysisProperties
}


# ---- Data model -------------------------------------------------------------

@dataclass
class FuncDoc:
    class_name: str
    func_name: str
    docstring: str
    categories: list


@dataclass
class ClassDoc:
    """A class rendered as a single self-contained page: docstring body +
    Properties + Methods (each method's full docstring inlined)."""
    class_name: str
    docstring: str          # full class docstring (overview + sections)
    categories: list
    methods: list           # list of (name, one-line summary, full_docstring)
    properties: list = None # list of (name, type, attribute_docstring); may be []
    bases: list = None      # base class names; documented ones get linked
    dynamic: bool = False   # exposes data via indexing/runtime attributes


def _decorator_names(func: ast.FunctionDef) -> set:
    """Last dotted component of each decorator: @property -> 'property',
    @material.setter -> 'setter', @typing.overload -> 'overload'."""
    out = set()
    for d in func.decorator_list:
        if isinstance(d, ast.Call):
            d = d.func
        if isinstance(d, ast.Name):
            out.add(d.id)
        elif isinstance(d, ast.Attribute):
            out.add(d.attr)
    return out


def _annotation_str(node) -> str:
    """Annotation as display text: unquoted and without module prefixes
    ('DM.UnitSystem' -> UnitSystem, RV2.Result -> Result)."""
    if node is None:
        return ""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        text = node.value
    else:
        try:
            text = ast.unparse(node)
        except Exception:
            return ""
    return re.sub(r"\b[A-Za-z_]\w*\.(?=[A-Za-z_])", "", text)


def _base_names(class_node: ast.ClassDef) -> list:
    """Bare names of a class's bases (output.StageResults -> StageResults)."""
    return [b.id if isinstance(b, ast.Name) else b.attr
            for b in class_node.bases
            if isinstance(b, (ast.Name, ast.Attribute))]


def _is_dynamic(class_node: ast.ClassDef) -> bool:
    """True if the class exposes its data through indexing/iteration or
    attributes created at runtime (__getitem__, __iter__, __getattr__ or
    setattr calls) -- so "no declared properties" doesn't mean "no data"."""
    for n in ast.walk(class_node):
        if (isinstance(n, ast.FunctionDef)
                and n.name in ("__getitem__", "__iter__", "__getattr__")):
            return True
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                and n.func.id == "setattr"):
            return True
    return False


def _is_property(func: ast.FunctionDef) -> bool:
    """True if the def is a @property getter (so it's a data attribute,
    documented under the class Properties rather than as a method)."""
    return bool(_decorator_names(func) & {"property", "cached_property"})


def _public_defs(class_node: ast.ClassDef) -> list:
    """One def per public name, in source order. Picks the implementation
    over @overload stubs and the @property getter over its setter/deleter,
    so a name never renders twice to the same page."""
    chosen = {}
    for sub in class_node.body:
        if not isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if sub.name.startswith("_"):
            continue
        if _decorator_names(sub) & {"setter", "deleter"}:
            continue
        prev = chosen.get(sub.name)
        if prev is None or ("overload" in _decorator_names(prev)
                            and "overload" not in _decorator_names(sub)):
            chosen[sub.name] = sub
    return list(chosen.values())


def _extract_class_methods(class_node: ast.ClassDef) -> list:
    """Return [(name, summary, full_docstring), ...] for public non-property
    methods of a class. Used when the class itself is rendered as a single
    page (ClassDoc) -- the summary feeds the Methods list on the class page,
    the full docstring feeds the per-method sub-page."""
    out = []
    for sub in _public_defs(class_node):
        if _is_property(sub):
            continue
        ds = ast.get_docstring(sub, clean=True) or ""
        summary = ds.strip().split("\n")[0] if ds else ""
        out.append((sub.name, summary, ds))
    return out


def _extract_class_properties(class_node: ast.ClassDef) -> list:
    """Return [(name, type, attribute_docstring), ...] in source order for:

    - class-level annotated assignments (PEP 258 attribute-docstring pattern):

        name: type
        \"\"\"Description.\"\"\"
        name = prop(...)         # optional binding line

      The attribute docstring is the string Expr immediately following the
      AnnAssign in the class body.
    - @property getters; type from the return annotation, description from
      the getter's docstring.

    Skips private names."""
    out = []
    body = class_node.body
    for i, node in enumerate(body):
        if not isinstance(node, ast.AnnAssign):
            continue
        if not isinstance(node.target, ast.Name):
            continue
        name = node.target.id
        if name.startswith("_"):
            continue
        type_str = _annotation_str(node.annotation)
        ds = ""
        if i + 1 < len(body):
            nxt = body[i + 1]
            if (isinstance(nxt, ast.Expr)
                    and isinstance(nxt.value, ast.Constant)
                    and isinstance(nxt.value.value, str)):
                ds = nxt.value.value.strip()
        out.append((node.lineno, name, type_str, ds))
    for sub in _public_defs(class_node):
        if not _is_property(sub):
            continue
        type_str = _annotation_str(sub.returns)
        # Summary text only: sections (Examples, ...) don't fit in a <dd>.
        ds = SECTION_RE.split(ast.get_docstring(sub, clean=True) or "")[0]
        ds = " ".join(ds.split())
        out.append((sub.lineno, sub.name, type_str, ds))
    return [entry[1:] for entry in sorted(out, key=lambda e: e[0])]


# ---- Extraction (AST) -------------------------------------------------------

@functools.lru_cache(maxsize=None)
def _parse(path: Path) -> ast.Module:
    """Parse a source file once; shared by extraction and the coverage report."""
    return ast.parse(path.read_text(encoding="utf-8"))


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
        for node in _parse(path).body:
            if not isinstance(node, ast.ClassDef):
                continue
            cats = CLASS_TO_CATEGORIES.get(node.name)
            if not cats:
                continue

            if node.name in CLASS_PAGE_CLASSES:
                methods = _extract_class_methods(node)
                properties = _extract_class_properties(node)
                class_ds = ast.get_docstring(node, clean=True) or ""
                docs.append(ClassDoc(node.name, class_ds, cats, methods,
                                     properties, _base_names(node),
                                     _is_dynamic(node)))
                continue

            for sub in _public_defs(node):
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
            properties = _extract_class_properties(cls_node)
            docs.append(ClassDoc(class_name, class_ds, ["objects"], methods,
                                 properties, _base_names(cls_node),
                                 _is_dynamic(cls_node)))
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

def _doc_url(cat: str, sub, name: str) -> str:
    """Site URL of a generated page."""
    return f"/python/functions/{cat}/{sub}/{name}" if sub \
        else f"/python/functions/{cat}/{name}"


def _render_body(docstring: str, link_map: dict, fallback_cat: str,
                 h_level: int = 2, skip_attributes: bool = False) -> list:
    """Render the body of a docstring (everything after the title) as a list of
    markdown lines. `h_level` controls the depth of section headers (2 for a
    function/class top-level page, 4 when inlined under a class's Methods).
    `skip_attributes=True` suppresses the Attributes section -- used by the
    class renderer, which renders properties separately from a merged source
    (docstring Attributes + AnnAssign attribute docstrings)."""
    parts = []
    h = "#" * h_level

    sections = SECTION_RE.split(docstring)
    overview = sections[0].strip()
    if overview:
        parts.append(overview)
        parts.append("")

    for i in range(1, len(sections), 2):
        title = sections[i].strip()
        content = sections[i + 1].strip()

        if title == "Attributes" and skip_attributes:
            continue

        if title in ("Parameters", "Attributes"):
            # Attributes is rendered as "Properties" to match the existing
            # class-page convention; Parameters keeps its name.
            label = "Properties" if title == "Attributes" else "Parameters"
            parts.append(f"{h} {label}")
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

        elif title in ("Returns", "Raises"):
            parts.append(f"{h} {title}")
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
            parts.append(f"{h} Examples")
            parts.append("")
            parts.append("```python")
            for line in content.split("\n"):
                if SEPARATOR_RE.match(line.strip()):
                    continue
                line = re.sub(r'^\s*(?:>>>|\.\.\.)\s?', '', line)
                parts.append(line)
            parts.append("```")
            parts.append("")

        elif title == "See Also":
            parts.append(f"{h} See also")
            parts.append("")
            for raw in re.split(r'[,;\n]', content):
                ref = raw.strip()
                if not ref or SEPARATOR_RE.match(ref):
                    continue
                loc = link_map.get(ref)
                if loc:
                    cat, sub = loc
                else:
                    cat = fallback_cat
                    sub = SUBCATEGORIES.get(cat, {}).get(ref)
                parts.append(f"- [{ref}]({_doc_url(cat, sub, ref)})")
            parts.append("")

        elif title == "Notes":
            parts.append(f"{h} Notes")
            parts.append("")
            for line in content.split("\n"):
                if SEPARATOR_RE.match(line.strip()):
                    continue
                parts.append(line)
            parts.append("")

    return parts


def render_markdown(doc: FuncDoc, link_map: dict) -> str:
    """Render a FuncDoc to markdown matching the repo's existing style."""
    parts = [f"# {doc.func_name}", ""]
    parts.extend(_render_body(doc.docstring, link_map, doc.categories[0],
                              h_level=2))
    while parts and parts[-1] == "":
        parts.pop()
    parts.append("")
    return "\n".join(parts)


def render_class_markdown(doc: ClassDoc, link_map: dict) -> str:
    """Render a ClassDoc to a single self-contained page: class docstring body
    + Properties (merged from docstring Attributes + AnnAssign attribute
    docstrings) + Methods (each method's full docstring inlined)."""
    parts = [f"# {doc.class_name}", ""]
    fallback_cat = doc.categories[0]

    # Link documented base classes -- their members apply here too but are
    # only listed on the base's own page.
    inherited = [b for b in (doc.bases or []) if b in link_map]
    if inherited:
        links = ", ".join(f"[{b}]({_doc_url(*link_map[b], b)})"
                          for b in inherited)
        parts.append(f"Inherits from {links} -- all of its properties and "
                     f"methods are available too.")
        parts.append("")

    # Class-level docstring -> body sections at H2. Skip the Attributes
    # section here; it's rendered explicitly below alongside AnnAssign props.
    # If the class has no docstring at all, leave a punch list reminder.
    if doc.docstring.strip():
        parts.extend(_render_body(doc.docstring, link_map, fallback_cat,
                                  h_level=2, skip_attributes=True))
    else:
        parts.append("*No docstring yet — add one in source to "
                     "populate this section.*")
        parts.append("")

    # Properties: union of docstring Attributes and AnnAssign attribute
    # docstrings. Docstring entries come first (they tend to be hand-curated);
    # AnnAssign entries fill in the rest. De-dupe by name.
    _doc_overview, doc_attrs = parse_attributes(doc.docstring)
    seen = set()
    merged_props = []
    for name, typ, desc in doc_attrs:
        if name in seen:
            continue
        merged_props.append((name, typ, desc))
        seen.add(name)
    for name, typ, desc in (doc.properties or []):
        if name in seen:
            continue
        merged_props.append((name, typ, desc))
        seen.add(name)

    if merged_props:
        parts.append("## Properties")
        parts.append("")
        parts.append("<dl>")
        for name, typ, desc in merged_props:
            parts.append(f"<dt>{name} : {typ}</dt>" if typ
                         else f"<dt>{name}</dt>")
            if desc:
                parts.append(f"<dd>{desc}</dd>")
        parts.append("</dl>")
        parts.append("")
    elif (not doc.dynamic
          and "Parameters" not in SECTION_RE.findall(doc.docstring)):
        # Make the absence explicit rather than just leaving the page bare.
        # Plain text (not italic) -- this is a factual statement, not a
        # punch-list placeholder like the missing-docstring note.
        # Suppressed when the docstring has a Parameters section, since
        # that already documents the object's constituents (the __init__
        # args become instance attributes -- e.g. Profile.data, Gradient.zref)
        # and for dynamic classes (ResultIndexer, PropertyContainer), whose
        # data is reached by indexing or runtime attributes.
        parts.append("Object without properties.")
        parts.append("")

    # Method docstrings inlined under a Methods section. Each method's title
    # is H3, its docstring's own sub-sections drop to H4 so they don't clash
    # with the H2 class-level headers above. Methods without a docstring are
    # still listed (so the API surface is visible) with a placeholder note
    # that doubles as a punch list for upstream docstring work.
    if doc.methods:
        parts.append("## Methods")
        parts.append("")
        for name, _summary, ds in doc.methods:
            parts.append(f"### {name}()")
            parts.append("")
            if ds:
                parts.extend(_render_body(ds, link_map, fallback_cat,
                                          h_level=4))
            else:
                parts.append("*No docstring yet — add one in source to "
                             "populate this section.*")
                parts.append("")

    while parts and parts[-1] == "":
        parts.pop()
    parts.append("")
    return "\n".join(parts)


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
        # Carve-out: pages in SKIP_REGENERATE_PATHS are hand-maintained.
        # Mark them as touched so they're not flagged as orphans, but never
        # write over them.
        rel_skip = str(target.relative_to(DOCS_ROOT)).replace("\\", "/")
        if rel_skip in SKIP_REGENERATE_PATHS:
            unchanged += 1
            return
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


# ---- Coverage report --------------------------------------------------------

def _module_file(source_root: Path, from_rel: str, level: int,
                 module: str):
    """Package-relative file for a relative import, preferring the .pyi stub
    (what IDEs show, and what SOURCE_FILES lists) over the .py."""
    base = PurePosixPath(from_rel).parent
    for _ in range(level - 1):
        base = base.parent
    stem = base / module.replace(".", "/")
    for ext in (".pyi", ".py"):
        if (source_root / f"{stem}{ext}").exists():
            return f"{stem}{ext}"
    return None


def _resolve_bases(source_root: Path, rel: str, class_node: ast.ClassDef):
    """Yield (rel_path, ClassDef) for each base of class_node that traces to a
    class in the package, following the defining module's relative imports
    (`from .X import Base`, or `from . import X as x` + `x.Base`)."""
    names, modules = {}, {}
    for n in _parse(source_root / rel).body:
        if not (isinstance(n, ast.ImportFrom) and n.level):
            continue
        for a in n.names:
            local = a.asname or a.name
            if n.module is None:
                modules[local] = _module_file(source_root, rel, n.level, a.name)
            else:
                names[local] = (_module_file(source_root, rel, n.level,
                                             n.module), a.name)
    for b in class_node.bases:
        if isinstance(b, ast.Name):
            target_rel, target_name = names.get(b.id, (rel, b.id))
        elif isinstance(b, ast.Attribute) and isinstance(b.value, ast.Name):
            target_rel, target_name = modules.get(b.value.id), b.attr
        else:
            continue
        if not target_rel:
            continue
        for n in _parse(source_root / target_rel).body:
            if isinstance(n, ast.ClassDef) and n.name == target_name:
                yield target_rel, n
                break


def _words(text: str) -> set:
    return set(re.findall(r"[a-z0-9_]+", text.lower()))


def _param_names(func: ast.FunctionDef) -> set:
    a = func.args
    return {p.arg for p in a.posonlyargs + a.args + a.kwonlyargs}


def coverage_report(source_root: Path, docs: list) -> dict:
    """Collect public API the generator could not document. Returns
    {heading: [message, ...]}, empty groups omitted."""
    DRIFT = ".py docstring has text the .pyi lacks (edit the .pyi)"
    PARAMS = "Parameter names differ between .py and .pyi (docs show the .pyi)"
    STUB_MISSING = "In the .py but missing from the .pyi"
    NO_DOC_STUB = "No docstring in the .pyi, but the .py has one (copy it over)"
    NO_DOC = "Public methods without a docstring"
    UNMAPPED = "Classes not in CLASS_TO_CATEGORIES (docstring'd methods)"
    BASES = "Inherited from a base class the generator doesn't read"
    ROOT = "No SUBCATEGORIES entry (page lands at category root)"
    COLLISION = "Several sources render to the same page (last one wins)"
    SEE_ALSO = "See Also names with no generated page (broken link)"
    report = {h: [] for h in (DRIFT, PARAMS, STUB_MISSING, NO_DOC_STUB, NO_DOC,
                              UNMAPPED, BASES, ROOT, COLLISION, SEE_ALSO)}

    def ignored(cls, meth=None):
        return cls in COVERAGE_IGNORE or f"{cls}.{meth}" in COVERAGE_IGNORE

    seen_bases = set()

    def check_bases(rel, cls, via):
        for base_rel, base in _resolve_bases(source_root, rel, cls):
            key = (base_rel, base.name)
            if ignored(base.name) or key in seen_bases:
                continue
            seen_bases.add(key)
            if base.name in CLASS_TO_CATEGORIES and base_rel in SOURCE_FILES:
                continue  # documented in its own right
            public = [d.name for d in _public_defs(base)]
            if public:
                report[BASES].append(f"{via} <- {base.name} ({base_rel}): "
                                     f"{', '.join(public)}")
            check_bases(base_rel, base, f"{via} <- {base.name}")

    for fname in SOURCE_FILES:
        path = source_root / fname
        if not path.exists():
            continue
        impl_classes = {}
        impl_rel = None
        if path.suffix == ".pyi" and path.with_suffix(".py").exists():
            impl_rel = fname[:-1]
            impl_classes = {n.name: n for n in _parse(path.with_suffix(".py")).body
                            if isinstance(n, ast.ClassDef)}

        for node in _parse(path).body:
            if not isinstance(node, ast.ClassDef) or ignored(node.name):
                continue
            defs = {d.name: d for d in _public_defs(node)}
            if node.name not in CLASS_TO_CATEGORIES:
                with_ds = [d for d in defs.values() if ast.get_docstring(d)]
                if with_ds:
                    methods = [d.name for d in with_ds if not _is_property(d)]
                    n_props = len(with_ds) - len(methods)
                    summary = ", ".join(methods)
                    if n_props:
                        summary = f"{summary} (+{n_props} properties)".strip()
                    report[UNMAPPED].append(f"{fname}: {node.name} -- {summary}")
                continue
            check_bases(fname, node, node.name)
            if node.name in CLASS_PAGE_CLASSES:
                continue  # class pages already flag missing method docstrings

            impl = impl_classes.get(node.name)
            impl_defs = {d.name: d for d in _public_defs(impl)} if impl else {}
            no_doc, no_doc_stub = [], []
            for name, d in defs.items():
                if ignored(node.name, name) or ast.get_docstring(d):
                    continue
                if name in impl_defs and ast.get_docstring(impl_defs[name]):
                    no_doc_stub.append(name)
                else:
                    no_doc.append(name)
            if no_doc:
                report[NO_DOC].append(f"{fname}: {node.name} -- {', '.join(no_doc)}")
            if no_doc_stub:
                report[NO_DOC_STUB].append(
                    f"{fname}: {node.name} -- {', '.join(no_doc_stub)}")

            for name, d_impl in impl_defs.items():
                if ignored(node.name, name):
                    continue
                if name not in defs:
                    report[STUB_MISSING].append(f"{impl_rel}: {node.name}.{name}")
                    continue
                p_impl, p_stub = _param_names(d_impl), _param_names(defs[name])
                if p_impl != p_stub:
                    report[PARAMS].append(
                        f"{node.name}.{name} -- only in .py: "
                        f"{', '.join(sorted(p_impl - p_stub)) or '-'}; only in "
                        f".pyi: {', '.join(sorted(p_stub - p_impl)) or '-'}")
                ds_impl = ast.get_docstring(d_impl, clean=True) or ""
                ds_stub = ast.get_docstring(defs[name], clean=True) or ""
                if ds_impl and ds_stub and not _words(ds_impl) <= _words(ds_stub):
                    report[DRIFT].append(f"{impl_rel}: {node.name}.{name} -- "
                                         f"\"{ds_impl.splitlines()[0][:90]}\"")

    by_target = defaultdict(set)
    for d in docs:
        name = _doc_name(d)
        for cat in d.categories:
            if SUBCATEGORIES.get(cat) and name not in SUBCATEGORIES[cat]:
                report[ROOT].append(f"{cat}/{name}.md")
            by_target[_resolve_path(cat, name)].add((d.class_name, d.docstring))
    for target, owners in by_target.items():
        if len(owners) > 1:
            classes = ", ".join(sorted({c for c, _ in owners}))
            report[COLLISION].append(
                f"{target.relative_to(DOCS_ROOT).as_posix()} <- {classes}")

    link_map = _build_link_map(docs)
    for d in docs:
        texts = [d.docstring]
        if isinstance(d, ClassDoc):
            texts += [ds for _name, _summary, ds in d.methods]
        for text in texts:
            parts = SECTION_RE.split(text)
            for i in range(1, len(parts), 2):
                if parts[i].strip() != "See Also":
                    continue
                for raw in re.split(r'[,;\n]', parts[i + 1]):
                    ref = raw.strip()
                    if ref and not SEPARATOR_RE.match(ref) and ref not in link_map:
                        report[SEE_ALSO].append(f"{_doc_name(d)}: {ref}")

    return {h: msgs for h, msgs in report.items() if msgs}


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

    report = coverage_report(Path(args.source), docs)
    if report:
        print()
        n = sum(len(msgs) for msgs in report.values())
        print(f"Coverage warnings ({n}) -- public API that is missing or "
              f"incomplete in the docs:")
        for heading, msgs in report.items():
            print(f"  {heading}:")
            for m in msgs:
                print(f"    {m}")

    print()
    print("Run `git status` / `git diff` in the docs repo to review changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
