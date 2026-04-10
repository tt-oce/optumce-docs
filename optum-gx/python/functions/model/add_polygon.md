# add_polygon

Add a polygon defined by a two-dimensional array of vertex points.

## Parameters

<dl>
<dd>list : list of vertex points</dd>
</dl>

## See also

- [add_polygons](/python/functions/model/add_polygons)
- [add_sphere](/python/functions/model/add_sphere)
- [add_vertex](/python/functions/model/add_vertex)

## Notes

In 3D all vertex points must be on the same plane.

## Examples

```python
model2d.add_polygon([[0,0],[1,0],[1,1]])
model3d.add_polygon([[0,0,0],[1,0,0],[1,1,2]])
```
