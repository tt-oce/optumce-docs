# set_mesh_fan

Set mesh fan around vertex.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'vertex'.</dd>
<dt>fan_angle : float</dt>
<dd>Angle between fan blades in degrees.</dd>
</dl>

## Examples

```python
v = model.get_vertices([[4,8]])
model.set_mesh_fan(shapes=v, fan_angle=30)
```
