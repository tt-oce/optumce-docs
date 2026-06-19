# output

Analysis output.

## Parameters

<dl>
<dd>None</dd>
</dl>

## Examples

```python
stage_lower = model2d.create_stage('lower bound')
stage_lower.set_analysis_properties(
        analysis_type='load_multiplier',
        element_type='lower',
        no_of_elements=1000,
        )
prj.run_analysis()
stage_lower.output.global_results.load_multiplier
```
