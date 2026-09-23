# StepOutput

Inherits from [StageResults](/python/functions/objects/results/StageResults) -- all of its properties and methods are available too.

Results of one analysis step: ``critical_results`` plus per-element
results through the result groups (``solid``, ``plate``, ...) inherited
from StageResults.

## Examples

```python
last = stage.output.step[-1]
last.critical_results.u_norm_max
last.plate[2].results.final_forces.M_y
```

## See also

- [StageOutput](/python/functions/objects/results/StageOutput)
- [StageResults](/python/functions/objects/results/StageResults)
- [CriticalResults](/python/functions/objects/results/CriticalResults)

## Properties

<dl>
<dt>critical_results : CriticalResults</dt>
<dd>Summary values of the step: load multiplier, factor of safety, extreme displacements, stresses and forces.</dd>
</dl>
