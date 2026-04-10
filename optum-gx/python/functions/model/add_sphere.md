# add_sphere

Add a sphere from center point and radius, using N line segments.

## Parameters

<dl>
<dt>center : array</dt>
<dd>Center point: center = [x0,y0,z0]</dd>
<dt>radius : float</dt>
<dd>Radius.</dd>
<dt>N : int</dt>
<dd>Number of linearly spaced line segments in the arc spanning each quarter sphere.</dd>
</dl>

## See also

- [add_arc](/python/functions/model/add_arc)
- [add_box](/python/functions/model/add_box)
- [add_circle](/python/functions/model/add_circle)
- [add_line](/python/functions/model/add_line)
- [add_nprism](/python/functions/model/add_nprism)
- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_rectangle](/python/functions/model/add_rectangle)

## Examples

```python
model3d.add_sphere(center = [0,0,3],radius = 3, N = 6)
```
