# add_arc

Draw an arc in 2D, using N line segments between two points and a midpoint.

## Parameters

<dl>
<dt>p0 : array</dt>
<dd>First point:   p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dd>
<dt>p1 : array</dt>
<dd>Mid point:     p1 = [x1,y1] in 2D, p1 = [x1,y1,z1] in 3D</dd>
<dt>p2 : array</dt>
<dd>Second point:  p2 = [x2,y2] in 2D, p2 = [x2,y2,z2] in 3D</dd>
<dt>N : int</dt>
<dd>Number of linearly spaced line segments.</dd>
</dl>

## See also

- [add_circle](/python/functions/model/add_circle)
- [add_line](/python/functions/model/add_line)
- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_rectangle](/python/functions/model/add_rectangle)
- [add_vertex](/python/functions/model/add_vertex)

## Examples

```python
model2d.add_arc([0,0], [1,0], [1,1], N=12)
model3d.add_arc([0,0,0], [1,0,0], [1,1,0], N=20)
model3d.add_arc([0,0,0], [np.sqrt(2)/2,1-np.sqrt(2)/2,0], [1,1,0], N=20)
```

