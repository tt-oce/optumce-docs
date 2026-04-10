# add_rectangle

Create a rectangle in 2D between a start and end point.

## Parameters

<dl>
<dt>p0 : array</dt>
<dd>Start point.        p0 = [x0,y0]</dd>
<dt>p1 : array</dt>
<dd>End point.      p1 = [x1,y1]</dd>
</dl>

## See also

- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_box](/python/functions/model/add_box)

## Examples

```python
model2d.add_rectangle([0,0],[1,1])
model3d.add_rectangle([0,0,0],[1,1,0])
```
