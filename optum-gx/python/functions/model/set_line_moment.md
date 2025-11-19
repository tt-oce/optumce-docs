# set_line_moment

Add line moment.

## See also

*   [set_body_load](/optum-gx/python/functions/model/set_body_load)
*   [set_surface_load](/optum-gx/python/functions/model/set_surface_load)
*   [set_line_load](/optum-gx/python/functions/model/set_line_load)
*   [set_point_load](/optum-gx/python/functions/model/set_point_load)


```python
# NEEDS VALIDATION!
model3d.add_prism(
        points=[[1, 1, 0], [3, 3, 0], [3, 0, 0]],
        height=3
    )

sel = model3d.select([3, 3, 0], types='edge')

model3d.set_line_moment(
        shapes=sel,
        value=-10,
        option='multiplier',
        load_type='unfavourable'
    )

```