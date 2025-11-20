# add_vertex

Create a point in 2D or 3D.

## Parameters

<dl>
<dt>p0 : array</dt>
<dd>Point. p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dd>
</dl>

## See also

- [add_arc](/python/functions/model/add_arc)
- [add_box](/python/functions/model/add_box)
- [add_circle](/python/functions/model/add_circle)
- [add_line](/python/functions/model/add_line)
- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_rectangle](/python/functions/model/add_rectangle)

## Examples

```python
model2d.add_vertex([0,0])
model3d.add_vertex([2,2,2])
model3d.add_vertex([1,0,1])
```
