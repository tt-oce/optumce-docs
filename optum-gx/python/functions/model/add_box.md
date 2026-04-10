# add_box

Create a solid box in 3D between a start and end point.

## Parameters

<dl>
<dt>p0 : array</dt>
<dd>Start point:        p0 = [x0,y0,z0]</dd>
<dt>p1 : array</dt>
<dd>End point:  p1 = [x0,y0,z0]</dd>
</dl>

## Notes

This function is designed for use in 3D, refer to [add_rectangle](/python/functions/model/add_rectangle) in 2D.

## See also

- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_rectangle](/python/functions/model/add_rectangle)

## Examples

```python
model3d.add_box([0,0,0],[1,2,5])
```
