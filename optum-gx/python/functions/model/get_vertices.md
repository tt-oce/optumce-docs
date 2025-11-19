# get_vertices

Get vertex from their coordinates.

## Parameters

<dl>
<dt>points : list</dt>
<dd>point or list of points. points = [x0,y0] or points=[[x0,y0],[x1,y1],[x2,y2]] in 2D</dd>
</dl>

## See also

*   [select](/optum-gx/python/functions/model/select)
*   [vertices](/optum-gx/python/functions/model/vertices)

## Examples

```python
model2d.get_vertices_by_coordinates(points = [x0,y0])
model2d.get_vertices_by_coordinates(points = [[x0,y0],[x1,y1],[x2,y2]])
model3d.get_vertices_by_coordinates(points = [[x0,y0,z0],[x1,y1,z1]])
```