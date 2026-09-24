# Results

After an analysis you read results through `stage.output`. A stage in this context is a so-called calculation stage, which can be both a stage and a model without stages. As long as it it calculated and carries results it considered a calculation stage. Results follow a fixed hierarchy: from the stage down to a single value on one element.

```text
Calculation stage
  └── output                                  StageOutput
        ├── global_results                    Result
        ├── critical_results                  CriticalResults
        ├── solid, plate, ..., line_reaction  ResultIndexer
        │     └── [i]                         ElementIndexer
        │           ├── general               GeneralProperties
        │           ├── topology              Topology
        │           ├── material              PropertyContainer
        │           └── results               PropertyContainer
        │                 └── ... .<field>    ElementResult (unit, value)
        └── step[i]                           StepOutput
              ├── critical_results            CriticalResults
              └── solid, plate, ...           ResultIndexer
```
All these object are further described on their own page in this section.
Each level is reached with an attribute or an index, so a single value is one expression:

```python
project = gx.get_current_project()
project.run_analysis()
stage = project.get_models_and_stages()[0]
out = stage.output

out.global_results.factor_of_safety                 # stage Factor of Safety
out.critical_results.u_norm_max                     # maximum normalized displacement
out.plate[2].results.final_forces.M_y.value         # values on plate element 2
out.plate[2].topology.X                             # node X coordinates
[s.critical_results.u_norm_max for s in out.step]   # per-step max normalized displacement
```

## Levels

| Object | Reached by | Holds |
| --- | --- | --- |
| [StageOutput](/python/functions/objects/results/StageOutput) | `stage.output` | Everything below; the final step's results |
| [Result](/python/functions/objects/results/Result) | `.global_results` | Factor of safety, load multiplier, max displacement |
| [CriticalResults](/python/functions/objects/results/CriticalResults) | `.critical_results` | Min/max displacements, stresses and forces of a step |
| [StageResults](/python/functions/objects/results/StageResults) | *(base class)* | The result groups `solid`, `plate`, `point_reaction`, ... |
| [ResultIndexer](/python/functions/objects/results/ResultIndexer) | `.plate`, `.solid`, ... | All elements of one group; supports `len()`, `[i]` and iteration |
| [ElementIndexer](/python/functions/objects/results/ElementIndexer) | `.plate[i]` | One element: `general`, `topology`, `material`, `results` |
| [GeneralProperties](/python/functions/objects/results/GeneralProperties) | `.general` | Material name, material model and shape ID |
| [Topology](/python/functions/objects/results/Topology) | `.topology` | Node indices and X, Y, Z coordinates |
| [PropertyContainer](/python/functions/objects/results/PropertyContainer) | `.results`, `.material` | Nested result fields or material parameters |
| [ElementResult](/python/functions/objects/results/ElementResult) | `.results. ... .<field>` | `unit` and `value` (one entry per element point) |
| [StepOutput](/python/functions/objects/results/StepOutput) | `.step[i]` | The same groups and critical results for one step |
| [MaterialPointOutput](/python/functions/objects/results/MaterialPointOutput) | `test.output` | Material point test output; same structure, no `global_results` |

## Good to know
- **Repeated extraction of results from GX** is cumbersome for the program and will slow down scripts. It is preferable to extract the output to Python once and only interacting with the object from there e.g. 
```python
#Bad practice
[stage.output.critical_results.u_norm_max for s in out.step] #Interacts with GX API at every step.
#Preferable
out = stage.output
[s.critical_results.u_norm_max for s in out.step] #Only interacts with the Python object.
```
- **Explore with `repr()`.** The fields in `CriticalResults` and `PropertyContainer` depend on the analysis type and element type. Print the object to list what is available at that level.
- **Steps.** `step` exists only when the analysis has more than one step. The top-level results of `stage.output` are the results of the last step.
