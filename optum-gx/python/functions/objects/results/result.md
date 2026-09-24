# Result

Global results of a calculation stage.

Each property is read from OptumGX when it is accessed.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
stage.output.global_results.factor_of_safety
stage.output.global_results.load_multiplier
stage.output.global_results.max_displacement
```

## See also

- [StageOutput](/python/functions/objects/results/StageOutput)
- [CriticalResults](/python/functions/objects/results/CriticalResults)

## Properties

<dl>
<dt>factor_of_safety : float | None</dt>
<dd>Factor of safety of the stage, or None if not available.</dd>
<dt>load_multiplier : float | None</dt>
<dd>Load multiplier of the stage, or None if not available.</dd>
<dt>max_displacement : float | None</dt>
<dd>Maximum displacement of the stage, or None if not available.</dd>
</dl>
