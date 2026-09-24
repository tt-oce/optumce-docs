# MaterialPointOutput

Inherits from [StepOutput](/python/functions/objects/results/StepOutput) -- all of its properties and methods are available too.

Output of a material point test: the last step's results plus per-step
access. Returned by ``MaterialPoint.output``.

## Examples

```python
test = gx.get_material_point()
test.output.critical_results.s
test.output.solid[0].results.final_stresses.total_stresses.q.value
p = [step.solid[0].results.final_stresses.total_stresses.p.value[0] for step in test.output.step]
```

## See also

- [MaterialPoint](/python/functions/objects/analysis/MaterialPoint)
- [StepOutput](/python/functions/objects/results/StepOutput)

## Notes

In analysis with steps the StageResults are equivalent to the last step.
Material points have uncommon critical results relevant only for this analysis type.

## Properties

<dl>
<dt>step : List[StepOutput]</dt>
<dd>Output of each step, in order. Only present when the test has more than one step.</dd>
</dl>
