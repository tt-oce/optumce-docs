# add_circle

Draw a circle in 2D, from center point and radius, using N line segments.

## Parameters

<dl>
<dt>center : array</dt>
<dd>Center point:       center = [x0,y0] in 2D, center = [x0,y0,z0] in 3D</dd>
<dt>radius : float</dt>
<dd>Radius.</dd>
<dt>N : int</dt>
<dd>Number of linearly spaced line segments</dd>
</dl>

## See also

- [add_arc](/python/functions/model/add_arc)
- [add_line](/python/functions/model/add_line)
- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_rectangle](/python/functions/model/add_rectangle)
- [add_sphere](/python/functions/model/add_sphere)

## Examples

```python
model2d.add_circle([0,0], radius=2, N=12)
model3d.add_circle([0,0,0], radius=4, N=16)
```
