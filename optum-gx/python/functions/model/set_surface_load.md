# set_surface_load

Add surface load.

## See also

*   [set_body_load](/optum-gx/python/functions/model/set_body_load)
*   [set_line_load](/optum-gx/python/functions/model/set_line_load)
*   [set_point_load](/optum-gx/python/functions/model/set_point_load)

## Examples

```python
model3d.add_rectangle([0,0,0],[3,3,0])
sel = model3d.select([3,3,0],types='face')
model3d.set_surface_load(shapes=sel,value=-10,direction='z',option='multiplier')
model3d.add_box([0,-5,0],[3,5,3])
sel = model3d.select(point1=[1,0,3],types='face')
Pmap = ParameterMap(data=[[0,-5,3,-10],[3,-5,3,-5],[0,5,3,-10],[3,5,3,-20],[0,0,3,-40]])
model3d.set_surface_load(shapes=sel,value=Pmap,direction='z',coordinate_type='local')
```