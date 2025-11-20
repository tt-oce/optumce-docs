# set_mesh_fan

Set mesh fan around vertex

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'vertex'</dd>
<dt>fan_angle : float</dt>
<dd>Angle between fan blads in degrees</dd>
</dl>

## See also

- [set_analysis_properties](/python/functions/stage/set_analysis_properties)
- [set_mesh_size](/python/functions/model/set_mesh_size)

## Examples

```python
model2d.add_rectangle([0,0],[10,10])
model2d.add_rectangle([4,8],[6,11])
v = model2d.get_vertices([[4,8]])
model2d.set_mesh_fan(shapes=v,fan_angle=30)
```

