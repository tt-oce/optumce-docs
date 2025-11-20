# add_prism

Draw a prism in 3D.

## Parameters

<dl>
<dt>points : array</dt>
<dd>List of points:    points = [[x0,y0,z0],[x1,y1,z1],...,[xN,yN,zN]]</dd>
<dt>height : float</dt>
<dd>Height of prism normal to the active coordinate system.</dd>
</dl>

## See also

- [add_ncone] missing
- [add_nprism](/python/functions/model/add_nprism)
- [create_csys_2d](/python/functions/project/create_csys_2d)
- [create_csys_3d](/python/functions/project/create_csys_3d)
- [set_active_csys](/python/functions/model/set_active_csys)

## Notes

To create a solid prism all points must be on the same plane.

## Examples

```python
model3d.add_prism([[0,0,0],[1,0,0],[0,1,0]], height = 4)
model3d.add_prism([[4,-2,0],[2,2,0],[0,2,0],[3,-2,0]], height = 1)
```

