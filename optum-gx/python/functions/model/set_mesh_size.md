# set_mesh_size

Set mesh size to shape

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'vertex'</dd>
<dt>mesh_size : float</dt>
<dd>Maximum mesh size</dd>
</dl>

## See also

*   [set_analysis_properties](/optum-gx/python/functions/model/set_analysis_properties)
*   [set_mesh_fan](/optum-gx/python/functions/model/set_mesh_fan)

## Examples

```python
model2d.add_rectangle([0,0],[10,10])
model2d.add_rectangle([4,8],[6,11])
f = model2d.select([5,9],types='face')
model2d.set_mesh_size(shapes=f,mesh_size=0.1)
model3d.add_box([0,0,0],[10,10,10])
e = model3d.select([5,0,10],types='edge')
model3d.set_mesh_size(shapes=e,mesh_size=0.2)
```