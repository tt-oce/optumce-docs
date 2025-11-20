# set_current_model

Sets the current model.

## Parameters

<dl>
<dt>model_name : str|Model</dt>
<dd>String containing the model name or variable containg the Model</dd>
</dl>

## See also

- [create_model](/python/functions/project/create_model)
- [get_model](/python/functions/project/get_model)
- [set_current_stage](/python/functions/model/set_current_stage)

## Examples

```python
prj.set_current_model(model_name='2D model')
prj.set_current_model(model_name=model3d)
```

