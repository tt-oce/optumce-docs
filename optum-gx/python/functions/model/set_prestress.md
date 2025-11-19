# set_prestress

Set prestress.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes. ShapeType must be 'edge'</dd>
<dt>force : float</dt>
<dd>Prestressing force, in kPa</dd>
</dl>

## Examples

```python
model2d.add_rectangle(p1=[0,0],p2=[3,3])
sel = model2d.select(point1=[0,3],types='edge')
model2d.set_prestress(shapes=sel, force=50)
model3d = model2d.create_3d_from_2d_model('Model 3D')
sel = model3d.select(point1=[3,-5,0],types='edge')
model3d.set_prestress(shapes=sel,force=30)
```