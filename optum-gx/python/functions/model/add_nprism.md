# add_nprism

Draw a Nprism in 3D.

## Parameters

<dl>
<dt>center : array</dt>
<dd>Center point: center = [x0,y0,z0]</dd>
<dt>radius : float</dt>
<dd>Radius.</dd>
<dt>height : float</dt>
<dd>Height of prism normal to the active coordinate system.</dd>
<dt>N : int</dt>
<dd>Number of linearly spaced faces.</dd>
</dl>

## See also

- [add_circle](/python/functions/model/add_circle)
- [add_polygon](/python/functions/model/add_polygon)
- [add_polygons](/python/functions/model/add_polygons)
- [add_prism](/python/functions/model/add_prism)
- [add_sphere](/python/functions/model/add_sphere)
- [add_vertex](/python/functions/model/add_vertex)

## Notes

This function is designed for use in 3D, refer to add_circle in 2D.

## Examples

```python
model3d.add_nprism([0,0,0], radius=2.2, height=4.3, N=50)
```
