# set_line_load

Add line load.

## See also

- [set_body_load](/python/functions/model/set_body_load)
- [set_point_load](/python/functions/model/set_point_load)
- [set_surface_load](/python/functions/model/set_surface_load)

## Examples

```python
model3d.add_rectangle([0,0,0],[3,3,0])
sel = model3d.select([3,3,0],types='edge')
model3d.set_line_load(shapes=sel,value=-10,direction='z',option='multiplier')
```
