# add_polygons

Add a list of polygons defined by an array of two-dimensional arrays of vertex points for each polygon.

## Parameters

<dl>
<dt>points : list of polygons defined by an array of two-dimensional arrays of vertex points for each polygon</dt>
</dl>

## See also

- [add_arc](/python/functions/model/add_arc)
- [add_box](/python/functions/model/add_box)
- [add_circle](/python/functions/model/add_circle)
- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_rectangle](/python/functions/model/add_rectangle)
- [add_vertex](/python/functions/model/add_vertex)

## Notes

add_polygons is faster than using add_polygon sequentially

## Examples

```python
model2d.add_polygons([[[0,0],[1,0],[1,1]],[[2,0],[3,0],[4,5]]])
model3d.add_polygons([[[0,0,0],[1,0,0],[1,1,2]],[[2,0,4],[3,0,1],[4,5,3]]])
```
