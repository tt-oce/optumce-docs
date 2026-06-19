# model

Stage origin model property.

## Parameters

<dl>
<dd>None</dd>
</dl>

## Examples

```python
model2d = prj.create_model('2D model',model_type='plane_strain')
stage2 = model2d.create_stage(name='stage 2')
stage2.model
stage2.model.name
2D model
```
