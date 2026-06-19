# add_lines

Add line segments between consecutive points.

## Parameters

<dl>
<dt>points : list</dt>
<dd>List of points. Lines are created between consecutive points: p0-p1, p1-p2, p2-p3, etc. Each point is [x,y] in 2D or [x,y,z] in 3D.</dd>
</dl>

## See also

- [add_line](/python/functions/model/geometry/add_line)
- [add_polygon](/python/functions/model/geometry/add_polygon)
- [add_polyline](/python/functions/model/geometry/add_polyline)

## Examples

```python
model2d.add_lines([[0,0],[1,0],[1,1],[0,1]])
model3d.add_lines([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
```
