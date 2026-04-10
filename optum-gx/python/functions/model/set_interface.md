# set_interface

Define interface.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'edge' in 2D and 'face' in 3D.</dd>
<dt>material : Material</dt>
<dd>Interface material.</dd>
</dl>

## See also

- [set_no_flow](/python/functions/model/set_no_flow)

## Examples

```python
MC = prj.MohrCoulomb(name='MC Soil',color= Color(r=79,g=180,b=63))
model2d.add_polygon(points=[[0,0],[15,0],[15,5],[8,5],[11,5],[0,5]])
sel = model2d.select(point1=[10,5],types='edge')
model2d.set_interface(shapes=sel, material=MC)
model3d.add_box([0,0,0],[2,2,2])
sel = model3d.select(point1=[1,0,1],types='face')
model3d.set_interface(shapes=sel, material=MC)
```
