# StageOutput

Inherits from [StepOutput](/python/functions/objects/results/StepOutput) -- all of its properties and methods are available too.

Output of a stage, returned by ``stage.output``.

Holds the results of the final step (``critical_results`` and the result
groups ``solid``, ``plate``, ...), the stage's ``global_results`` and -
when the analysis has more than one step - the output of each step in
``step``.

## Examples

```python
project.run_analysis()
out = stage.output
out.global_results.load_multiplier
out.critical_results.u_norm_max
out.plate[2].results.final_forces.M_y
u_norm_max = [step.critical_results.u_norm_max for step in out.step]
```

## See also

- [output](/python/functions/model-and-stage/analysis/output)
- [StepOutput](/python/functions/objects/results/StepOutput)
- [StageResults](/python/functions/objects/results/StageResults)
- [Result](/python/functions/objects/results/Result)

## Properties

<dl>
<dt>global_results : Result</dt>
<dd>Global results of the stage: factor_of_safety, load_multiplier and max_displacement.</dd>
<dt>step : List[StepOutput]</dt>
<dd>Output of each step, in order. Only present when the analysis has more than one step.</dd>
</dl>
