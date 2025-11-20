# set_body_load

Add body load.

## See also

- [set_surface_load](/python/functions/model/set_surface_load)
- [set_line_load](/python/functions/model/set_line_load)
- [set_point_load](/python/functions/model/set_point_load)

```python
# NEEDS VALIDATION!
model3d.add_prism(
        points=[[1, 1, 0], [3, 3, 0], [3, 0, 0]],
        height=3
    )

sel = model3d.select([3, 0], types='volume')

model3d.set_body_load(
        shapes=sel,
        value=-10,
        direction='z',
        option='fixed'
    )

```

