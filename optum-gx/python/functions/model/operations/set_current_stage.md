# set_current_stage

Sets the current stage.

## Parameters

<dl>
<dt>stage_name : str</dt>
<dd>sting containing the stage name or variable containg the stage</dd>
</dl>

## See also

- [create_stage](/python/functions/model-and-stage/operations/create_stage)
- [get_stage](/python/functions/model/operations/get_stage)
- [set_current_model](/python/functions/project/operations/set_current_model)

## Examples

```python
stage4 = model3d.create_stage("stage 4")
model3d.set_current_stage(stage_name="stage 4")
model3d.set_current_stage(stage_name= stage4)
```
