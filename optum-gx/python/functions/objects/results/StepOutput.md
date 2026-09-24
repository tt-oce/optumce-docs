# StepOutput

Inherits from [StageResults](/python/functions/objects/results/StageResults) -- all of its properties and methods are available too.

Results of one analysis step: ``critical_results`` plus per-element
results through the result groups inherited from StageResults.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
last = stage.output.step[-1]
last.critical_results.u_norm_max
last.plate[2].results.final_forces.M_y
```

## See also

- [StageOutput](/python/functions/objects/results/StageOutput)
- [StageResults](/python/functions/objects/results/StageResults)
- [CriticalResults](/python/functions/objects/results/CriticalResults)

## Notes

In analysis with steps the StageResults are equivalent to the last step.

## Properties

<dl>
<dt>critical_results : CriticalResults</dt>
<dd>Critical values of the step: load multiplier, FoS, extreme displacements, stresses and forces.</dd>
</dl>
