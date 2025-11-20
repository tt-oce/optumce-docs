# create_model

Create model in project

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the model.</dd>
<dt>model_type : str</dt>
<dd>Type of model. model_type = 'plane_strain', 'axisymmetric', 'three_dimensional'</dd>
</dl>

## Examples

```python
model2d = prj.create_model('2D model',model_type='plane_strain')
modelAs = prj.create_model('As',model_type='axisymmetric')
model3d = prj.create_model('New 3D model',model_type='three_dimensional')
```
