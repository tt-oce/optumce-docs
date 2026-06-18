# add_polyline

Add a polyline defined by a list of points.

## Parameters

<dl>
<dt>points : list</dt>
<dd>List of points defining the polyline. Each point is [x,y] in 2D or [x,y,z] in 3D.</dd>
</dl>

## See also

- [add_line](/python/functions/model/add_line)
- [add_lines](/python/functions/model/add_lines)
- [add_polygon](/python/functions/model/add_polygon)

## Examples

```python
model2d.add_polyline([[0,0],[1,0],[1,1],[0,1]])
model3d.add_polyline([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
```
