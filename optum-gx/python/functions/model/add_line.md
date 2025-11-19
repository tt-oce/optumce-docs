# add_line

Add a line defined by two points.

## Parameters

<dl>
<dt>p0 : array</dt>
<dd>first point: p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dd>
<dt>p1 : array</dt>
<dd>second point: p1 = [x1,y1] in 2D, p1 = [x1,y1,z1] in 3D</dd>
</dl>

## See also

*   [add_arc](/optum-gx/python/functions/model/add_arc)
*   [add_circle](/optum-gx/python/functions/model/add_circle)
*   [add_polygon](/optum-gx/python/functions/model/add_polygon)
*   [add_polygons](/optum-gx/python/functions/model/add_polygons)
*   [add_rectangle](/optum-gx/python/functions/model/add_rectangle)
*   [add_vertex](/optum-gx/python/functions/model/add_vertex)

## Examples

```python
model2d.add_line([0,0], [1,2])
model3d.add_line([0,0,0], [1,2,3])
```