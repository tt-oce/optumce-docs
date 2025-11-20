# set_point_load

Add point load.

## See also

- [set_body_load](/python/functions/model/set_body_load)
- [set_line_load](/python/functions/model/set_line_load)
- [set_surface_load](/python/functions/model/set_surface_load)

## Examples

```python
model3d.add_rectangle([0,0,0],[3,3,0])
sel = model3d.select([3,3,0],types='vertex')
model3d.set_point_load(shapes=sel,value=-10,direction='z',option='fixed')
sel = model3d.select([3,0,0],types='vertex')
model3d.set_point_load(shapes=sel,value=-10,direction='z',coordinate_type='Global',option='fixed')
```
