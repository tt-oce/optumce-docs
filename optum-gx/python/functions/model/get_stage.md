# get_stage

Obtain a list of stages.

## Parameters

<dl>
<dt>name : str</dt>
</dl>

## See also

*   [create_stage](/optum-gx/python/functions/model/create_stage)
*   [set_current_stage](/optum-gx/python/functions/model/set_current_stage)

## Examples

```python
stage_init = model2d.create_stage(name='init')
stage_def = model2d.create_stage(name='def')
model2d.get_stage()                                 #Obtain stage list
model2d.set_current_stage(model2d.get_stage()[0])   #Set first stage as the current
```