# OPTUM GX Python API docs: docstring generation workflow

How the OPTUM GX Python API reference (`optum-gx/python/functions/`) is produced
from docstrings in the OptumGX source, how to change it, and what to watch out
for. Written so a person or an AI agent can pick up the work without prior
context.

> This file sits at the repo root on purpose. Retype publishes **every** `.md`
> under `optum-gx/` (`optum-gx/retype.yml` has `input: .` and no excludes), so
> notes placed there would go live on docs.optumce.com.

---

## 1. At a glance

| | |
|---|---|
| Source of truth | Docstrings in the OptumGX Python package, `C:\Optum\OptumGX\Rpc\src\OptumGX` (repo `OptumGX`, Azure DevOps). |
| Generator | [optum-gx/scripts/gen_python_docs.py](optum-gx/scripts/gen_python_docs.py). Parses the source statically with `ast`; it never imports OptumGX. Python 3.9+. |
| Output | One `.md` per function or class under `optum-gx/python/functions/<category>/[<subcategory>/]<name>.md`, published at `docs.optumce.com/optum-gx/python/functions/...`. |
| Direction | Source → docs, always. A generated page is overwritten on the next run, so fix the docstring upstream instead of editing the page. Exception: pages listed in `SKIP_REGENERATE_PATHS` (currently only `model-and-stage/geometry/select.md`). |
| Size | 318 API targets; pages are generated only at their configured locations. |

## 2. The normal loop

```powershell
# 1. Edit the docstring in the right source file (section 3).
# 2. Preview what changes in the docs repo:
python optum-gx/scripts/gen_python_docs.py --dry-run -v
# 3. Write the pages:
python optum-gx/scripts/gen_python_docs.py -v
# 4. Review:
git diff -- optum-gx/python/functions
```

Then:

1. Read the **"Possibly orphaned"** list: pages on disk that no source function
   produced any more. Delete them by hand if they're really gone, or add a
   mapping if they were moved.
2. Read the **coverage report** (section 7) and fix what it flags, or knowingly
   leave it.
3. Run the generator once more. It must say `Wrote 0 files`, otherwise
   something isn't stable (typically two sources writing to one page).
4. Commit both repos: the docstring change in `OptumGX`, and the generated pages
   (plus any script change) in `Optumce-docs`.

Options: `--strict` (exit nonzero on coverage warnings or orphaned pages),
`--dry-run` (write nothing), `-v` (list each written file),
`--source PATH` (another OptumGX checkout; the default is the dev checkout
`C:\Optum\OptumGX\Rpc\src\OptumGX`, and the release install layout
`C:\Users\Public\OPTUM CE\OPTUM GX\library\OptumGX` works too).

## 3. Where to edit a docstring

For the configured API modules, the `.pyi` stub is the generator's current
**input**, not necessarily the authoritative place to author documentation.
If another script generates that stub, update its templates or documentation
inputs: regenerating the stub can overwrite hand edits. The generator for
`FeatureAPI.pyi` and `RemoteMaterialAPI.pyi` has not been located in this checkout;
`Rpc/src/gen.bat` generates protobuf stubs, not those two API stubs.
The generator reads it, VS Code/Pylance shows it on hover, and for materials
`Materials/_docloader.py` copies stub docstrings into the module at runtime for
`help()` in normal (non-optimized) Python runs. The loader fills only empty
runtime docstrings; existing `.py` text takes precedence. FeatureAPI does not
currently call that loader. Stub-only text therefore does not automatically
reach runtime help for feature methods. Editing only the `.py` changes nothing
in the generated docs. That's exactly
why `toggle_features` didn't update (section 9).

| API (docs location) | Edit here (under `Rpc/src/OptumGX/` unless noted) | Notes |
|---|---|---|
| `GX` (`application/`), `Project` (`project/`), `Model` (`model/`), `Stage` (`stage/`), `StageBase` (`model-and-stage/`) | `v2.py` | Hand-written. `@property` getters are documented as pages too (e.g. `regional`, `output`). |
| `MaterialPoint`, `AnalysisProgress` (`objects/analysis/`), `Regional` (`objects/settings/`), `StageOutput`, `StepOutput`, `MaterialPointOutput` (`objects/results/`) | `v2.py` | Class pages. |
| `set_analysis_properties`, `get_analysis_properties` (`model-and-stage/analysis/`) | **`Rpc/src/docstrings/<name>.txt`**, then regenerate with `Rpc/src/gen.bat` | `ContractV2_gen.py` is **generated** by ProxyGen (`gen.bat`: `--gen-set-params -d "docstrings"`). Hand edits to it are lost on the next regeneration. |
| Material factories `project.MohrCoulomb(...)` etc. and `get_material` (`project/materials/`) | `Materials/RemoteMaterialAPI.pyi` | The `docstrings/<Material>.txt` files are older copies (last changed 2025-09 to 2026-03; the `.pyi` changed 2026-07-10). The stub is consumed by the docs; confirm its generating inputs before editing it as an authoring source. |
| Material classes (`objects/materials/`) | `Materials/<Name>.py` | One class per file; the file name must equal the class name. |
| Feature setters/getters `set_solid`, `get_plate`, … (`model/features/`), `remove_features`, `toggle_features` (`stage/features/`) | `RemoteFeatures/FeatureAPI.pyi` | Keep declarations compatible with `FeatureAPI.py`; update the stub generator/documentation inputs when available. Runtime doc loading is not configured for this module. |
| Feature classes (`objects/features/`) | `RemoteFeatures/<Name>.py` | One class per file. Originally produced by a codegen that isn't in the repo ("python codegen feature set", 2026-03-19); edited by hand since. Ask Dang Thai Hung before regenerating them. |
| `Shape`, `ShapeList` (`objects/geometry/`) | `DataModelV2.py` | |
| `ParameterMap`, `Profile`, `Gradient` (`utilities/`) | `Common.py` | |
| `StageResults`, `ResultIndexer`, `ElementIndexer`, `GeneralProperties`, `Topology`, `PropertyContainer`, `ElementResult`, `CriticalResults` (`objects/results/`) | `Output.py` | |
| `Result` (`stage.output.global_results`, `objects/results/`) | `ResultV2.py` | |

Not documented on purpose: `DataModel.py`, `Result.py`, `Output.Output`,
`Output.ModelResults` and `GxClient.py` are the legacy v1 API. `DataModel.py`
reuses the class names `Model`, `Stage` and `Shape`, and routing is by class
name, so never add it to `SOURCE_FILES`.

## 4. Docstring format that renders correctly

NumPy style. A section header is the bare word on its own line, followed by a
line of 5+ dashes. Recognised sections: **Parameters, Returns, Raises,
Examples, See Also, Notes, Attributes**. Anything else (Google-style `Args:`,
`Yields`, `Warns`, …) isn't recognised, and its text is glued into the
previous section.

```python
def set_line_load(self, shapes, value=..., direction=...):
    '''
    One-line summary (first line; also used in method lists).

    Optional longer description.

    Parameters
    ----------
    shapes : Shape | ShapeList
        Shapes to load.
    fx, fy, fz : float
        Grouped names are fine.

    Returns
    -------
    LineLoads
        The created feature.

    Raises
    ------
    ValueError
        When ...

    Examples
    --------
    >>> model.set_line_load(sel, value=10)

    See Also
    --------
    get_line_load, LineLoads
    '''
```

- **Examples**: the `>>>` / `...` prompts are stripped and the block renders
  as Python code.
- **See Also**: comma- or newline-separated names. Each becomes a link to that
  generated page, whether a function or a class. Qualified methods and class members resolve to their generated pages or
  anchors. Unknown names remain plain text and appear in the coverage report.
- **Class pages** (classes in `CLASS_PAGE_CLASSES`, plus everything under
  `Materials/` and `RemoteFeatures/`) render as: title → "Inherits from …"
  (only for documented bases) → class docstring → Properties → Methods.
  - **Properties** combine, in this order: the `Attributes` section of the
    class docstring; class-level annotations followed by a string literal
    (`name: type` then `'''Description.'''` on the next line); and `@property`
    getters (type from the return annotation, description from the getter
    docstring's summary; sections are dropped, and setter docstrings are
    ignored). Duplicates are removed by name.
  - Attributes created at runtime (`__getattr__`, `setattr`, e.g.
    `MaterialPoint.sx0`) are invisible to the parser. List them in the class
    docstring's `Attributes` section.
  - **Methods**: public functions (no leading `_`), excluding properties.
    For `@overload` stubs, the implementation is used.
  - "Object without properties." is added when a class has no properties, no
    `Parameters` section and isn't dynamic (no `__getitem__`, `__iter__`,
    `__getattr__` or `setattr`).
- Type text is cleaned: string annotations are unquoted and module prefixes
  removed (`'DM.UnitSystem'` → `UnitSystem`, `RV2.Result` → `Result`).

## 5. How the generator works

Pipeline in `main()`: **extract → route → render → write → orphans → coverage report**.

1. **Extract** (`extract_docs`): for each file in `SOURCE_FILES`, each top-level
   class listed in `CLASS_TO_CATEGORIES` produces either
   - one `FuncDoc` per public method with a docstring (one page each), or
   - one `ClassDoc` if the class is in `CLASS_PAGE_CLASSES` (one page).

   Then each `.py` in the `OBJECT_DIRS` folders (`Materials/`,
   `RemoteFeatures/`) becomes a `ClassDoc`, with its subcategory registered
   automatically. `_public_defs` picks one definition per name: the
   implementation over `@overload` stubs, and the getter over `@x.setter`.
2. **Route** (`_resolve_path`):
   `functions/<category>/<SUBCATEGORIES[category][name]>/<name>.md`, or the
   category root when no subcategory is mapped (reported as a warning).
3. **Render** (`render_markdown` / `render_class_markdown` → `_render_body`).
4. **Write** (`write_docs`): a file is written only when its content changed,
   so `git diff` shows exactly what moved.
5. **Orphans** (`find_orphans`): `.md` files on disk that no source produced.
   Nothing is deleted automatically.
6. **Coverage report** (`coverage_report`): section 7.

### Configuration (top of the script)

| Setting | Purpose |
|---|---|
| `DEFAULT_SOURCE` | OptumGX package directory. |
| `SOURCE_FILES` | Files scanned for mapped classes. Paths relative to the package, forward slashes, and the `.pyi` when a stub exists. |
| `OBJECT_DIRS` | Folders where each file defines one class of the same name, plus the subcategory and the files to skip. |
| `CLASS_TO_CATEGORIES` | Class name → doc category(ies). Classes not listed are ignored (and reported if they have docstrings). |
| `SUBCATEGORIES` | Per category, name → subfolder. Keys are function names, or class names for class pages. |
| `CLASS_PAGE_CLASSES` | Classes rendered as one page instead of one page per method. |
| `SKIP_REGENERATE_PATHS` | Hand-maintained pages: never overwritten, never orphaned. |
| `COVERAGE_IGNORE` | Classes (`"RemoteCacheMixin"`) or methods (`"GX.app_version"`) the coverage report should skip. Only for plumbing that is public by naming accident. |

Navigation: the folder order and labels come from `index.yaml` files
(`order:`, `label:`). New subfolders work without one; Retype derives the
label from the folder name.

## 6. Recipes

**New method on an already-mapped class** (e.g. `Model.add_torus`):
write the docstring → add `"add_torus": "geometry"` under `SUBCATEGORIES["model"]`
→ run. Without the mapping the page lands at `model/add_torus.md` and the
report says so.

**New class page** (e.g. a new result object):
1. Write the class docstring (+ `Attributes` / property docstrings) upstream.
2. Make sure its file is in `SOURCE_FILES`.
3. Add it to `CLASS_TO_CATEGORIES` (`["objects"]`), `CLASS_PAGE_CLASSES` and
   `SUBCATEGORIES["objects"]` (pick or create a subfolder).
4. Add `See Also` links from the functions that return it, so readers can find
   it.

**New material or feature class**: just add `Materials/<Name>.py` or
`RemoteFeatures/<Name>.py` with a class of the same name. Add helper files to
that folder's `skip` set in `OBJECT_DIRS`.

**New mixin/base on `Model`/`Stage`/`Project`**: the coverage report
("Inherited from a base class the generator doesn't read") flags it. Add its
file to `SOURCE_FILES` and the class to `CLASS_TO_CATEGORIES`.

**Move a page to another folder**: change `SUBCATEGORIES`, run, then delete the
old file (it shows up as an orphan). **Never move generated pages by hand.**
The generator recreates them at the old path and you end up with duplicates.

**Page needs a layout the renderer can't produce** (e.g. overload signatures):
hand-write it and add its path to `SKIP_REGENERATE_PATHS`.

**Docs were edited by hand and the edits must go back upstream**: run
`python optum-gx/scripts/compare_docs.py [--diff]`. It treats the pages on
disk as the reference and lists, per page, which sections the source
docstrings disagree with, with a severity. Right after a regeneration it
reports 0.

## 7. Coverage report: what each warning means

Printed after every run. Before 2026-09-23 all of these were skipped
silently.

| Warning | Meaning | Fix |
|---|---|---|
| `.py docstring has text the .pyi lacks` | The `.py` was edited but the stub the docs read wasn't. The check fires when the `.py` docstring contains words that don't appear in the `.pyi` docstring. | Copy the change into the `.pyi`. |
| `Parameter names differ between .py and .pyi` | The stub's signature doesn't match the implementation, so the docs (and IDE hints) show wrong parameter names. | Fix the stub (or the code). |
| `In the .py but missing from the .pyi` | A public method exists only in the implementation, so it's invisible in the docs and IDE. | Add it to the stub. |
| `No docstring in the .pyi, but the .py has one` | Undocumented in the stub; the text exists in the `.py`. | Copy it to the stub. |
| `Public methods without a docstring` | Silently missing from the docs. | Write one, or add the method to `COVERAGE_IGNORE` if it's internal. |
| `Classes not in CLASS_TO_CATEGORIES` | A class in a read file has documented members but no page. | Add a class page (section 6), or `COVERAGE_IGNORE`. |
| `Inherited from a base class the generator doesn't read` | A mapped class gets public members from a base whose file or class isn't configured. | Add the file and class, or `COVERAGE_IGNORE`. |
| `No SUBCATEGORIES entry` | The page lands at the category root. | Add the mapping. |
| `Several sources render to the same page` | Two classes (or overloads) produce the same file, and the last one wins. | Rename or remap one of them. |
| `See Also names with no generated page` | The link on the published page 404s. Usually a qualified or misspelt name (`prj.create_csys_2d` instead of `create_csys_2d`). | Use the bare name of a documented function or class. |

Limitations: only `SOURCE_FILES` are scanned for unmapped classes; classes with
no docstrings at all (e.g. `GxSettings`, `Csys`, `StageList`, `PlottedResult`)
don't appear; bases are followed through relative imports only.

## 8. Pitfalls

1. **`.py` vs `.pyi` drift.** This is the most common cause of "I changed it
   but the docs didn't update". See section 3.
2. **Generated sources.** `ContractV2_gen.py`, `*_pb2*.py(i)` and
   `Contract_pb2_ext_gen.py` are produced by `Rpc/src/gen.bat`. Edit
   `Rpc/src/docstrings/*.txt` or the `.proto` files instead.
3. **Hand-moving generated pages** creates duplicates (it happened with
   `screenshot`, `take_picture` and `get_plots`). Use `SUBCATEGORIES`.
4. **Retype publishes everything under `optum-gx/`.** Keep notes and tool
   docs out of it.
5. **Line endings.** OptumGX sources are CRLF except `Output.py` (LF). When
   editing by script, read and write bytes, or use `newline=""` on a file
   that is already LF, so you don't rewrite every line.
6. **Routing is by class name only.** Two read files defining the same class
   name both get routed to the same pages.
7. **Property setters used to render as fake methods** (e.g.
   "### tension_cutoff() — Set the tension cutoff."). Fixed; setter
   docstrings are now ignored, so put the description on the getter.
8. **Grouped parameters** (`a, b : float`) used to be merged into the previous
   description. Fixed in `PARAM_RE`.

## 9. Worked example: why `toggle_features` didn't update (2026-09-23)

- Symptom: a docstring change to `toggle_features` (commit `fb5fa3c27`,
  2026-09-21) never reached `stage/features/toggle_features.md`.
- Cause: the commit edited `RemoteFeatures/FeatureAPI.py`. The generator (and
  IDE hover) read `RemoteFeatures/FeatureAPI.pyi`, which still had the old
  text.
- Fix: the text was added to the `.pyi` and the `.py` wording was synced.
  The generator now prints a drift warning whenever this happens.

## 10. Remaining documentation

The locations below identify current missing text. For generated stubs, make durable edits in the generating templates or documentation inputs, then regenerate the stubs and docs. Paths in this section are
relative to `C:/Optum/OptumGX/Rpc/src/OptumGX/`. The generator's five remaining
warning entries group six methods; they do not represent a complete assessment
of parameter or property descriptions.

### Methods with no docstring

| Source | Methods | Content to write |
|---|---|---|
| `v2.py`, `Stage` | `from_stage` (property getter) | Meaning, returned stage, and relationship to stage inheritance. Put the docstring on the getter. |
| `v2.py`, `Model` | `initialize_geometry` | Purpose, parameters, effects on existing geometry, and example. |
| `v2.py`, `Project` | `get_models_and_stages` | Return structure, ordering, and example. |
| `v2.py`, `GX` | `create_report`, `app_version` | Report input/output file formats and requirements; version return format. |
| `Materials/RemoteMaterialAPI.pyi`, `RemoteMaterialAPI` | `FlatPlateSteel` | Factory parameters, units, defaults, return value, and a practical example. The implementation accepts `gamma`, not `weight`. |

### Existing docstrings that need more detail

- `RemoteFeatures/FeatureAPI.pyi`: complete the parameter descriptions for
  `set_point_moment`, `set_line_moment`, and `set_six_dof_load`. Signatures now
  match runtime names, order, and defaults; moment magnitude is named `m`.
- `RemoteFeatures/FeatureAPI.pyi`, `set_solid`: explain the `append` option,
  including its effects when solids/materials already exist. The declaration
  now includes `append: bool = False`; the implementation forwards it to the server.
- `Materials/RemoteMaterialAPI.pyi`, `PileRow`: document `gamma` (the runtime
  factory does not accept `gamma_dry` or `gamma_sat`).
- `Materials/RemoteMaterialAPI.pyi`, `get_material`: convert the existing
  Google-style sections to NumPy style so parameter/return/exception sections
  render correctly. Reconcile the corresponding runtime docstring as part of
  the runtime-loading policy below.
- Material getter pages now contain their existing one-line source docstrings.
  Add return values, not-found behavior, and examples where useful.

### Properties without descriptions

Add a string literal after the class-level annotation, document the property
getter, or add a NumPy-style `Attributes` section to the class docstring.
The generator reads descriptor `doc=` strings too. These gaps are separate
from missing-method warnings.

- `DataModelV2.py`, `ShapeList`: `values`, `id`, `type`, `length`, `area`, `volume`, `location`.
- `Output.py`, `CriticalResults`: describe all result fields, units, and aggregation semantics. Review suspicious names such as `u_solid_Z_min`, `u_plate_Z_min`, `txyx_plate3d_max`, and the `du_solid_z_min` entry in the plate block against runtime behavior before documenting them.
- `RemoteFeatures/Connectors.py`: `p0`, `p1`, `material_id`.
- `RemoteFeatures/FixedEndAnchors.py`: `length`, `inclination_angle`, `direction`, `material_id`, `point`.
- `RemoteFeatures/FixedExcessPressures.py`: `pressure`.
- `RemoteFeatures/FixedHeads.py`: `head`.
- `RemoteFeatures/Geogrids.py`: `material_id`, `tension_cutoff`, `compression_cutoff`.
- `RemoteFeatures/MeshFans.py`: `fan_angle`.
- `RemoteFeatures/MeshSizes.py`: `mesh_size`.
- `RemoteFeatures/NailRows.py`: `material_id`.
- `RemoteFeatures/PileRows.py`: `material_id`.
- `RemoteFeatures/PlateBcs.py`: `displacement_x`, `displacement_y`, `displacement_z`, `displacement_rotation`, `is_local_coord`, `csys_id`.
- `RemoteFeatures/Plates.py`: `material_id`.
- `RemoteFeatures/PointBcs.py`: `displacement_x`, `displacement_y`, `displacement_z`, `displacement_rotation_x`, `displacement_rotation_y`, `displacement_rotation_z`, `is_local_coord`, `csys_id`.
- `RemoteFeatures/Prestresses.py`: `force`.
- `RemoteFeatures/ReactionRelaxations.py`: `relaxation`.
- `RemoteFeatures/ResultPoints.py`: `is_control`.
- `RemoteFeatures/ShearJoints.py`: `material_id`.
- `RemoteFeatures/Solids.py`: `material_id`.

### Runtime docstring policy

The generator reads the configured stubs, but the material runtime loader only fills
empty docstrings and runs under `if __debug__`. FeatureAPI does not invoke it.
To provide the same text through `help()` without maintaining two sources,
choose build-time generation or consistent runtime loading, and validate it
against the packaged distribution. Do not delete runtime documentation until
that replacement is in place.

### Validation

```powershell
python -m unittest discover -s tests -p "test_gen_python_docs.py"
python optum-gx/scripts/gen_python_docs.py --dry-run --strict
```

Strict mode exits with status 1 while the remaining coverage warnings exist.
A normal second generation should write zero files. Deleted root-level pages are not recreated as forwarding pages. Concrete
feature pages stand alone; the internal `Feature` base and its references are
intentionally omitted. New public API types outside the configured mappings still need
an explicit documentation scope decision.
