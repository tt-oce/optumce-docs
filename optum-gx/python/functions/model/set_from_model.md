# set_from_model

Set model from another model.

## Parameters

<dl>
<dt>from_model : str|Model</dt>
<dd>Model name. str = 'Model A'</dd>
</dl>

## Examples

```python
model2d.set_from_model('Model A')
model1 = prj.create_model(name='model1',model_type='plane_strain')
model1.set_from_model(model2d)
```