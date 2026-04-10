# set_hinge_2d

Set hinge in 2D.

## Parameters

<dl>
<dt>vertices : ShapeList</dt>
<dd>List of vertices</dd>
</dl>

## Notes

Vertices must be connected to atleast one plate, to which the hinge will be assigned.

## See also

- [set_hinge_3d](/python/functions/model/set_hinge_3d)

## Examples

```python
model2d.add_rectangle([0,0],[0,2])
edge = model2d.select(p0=[0,1],types='edge')
RigidPlateMaterial = prj.RigidPlate(name='RigidPlateMaterial',
color=rgb(128,156,180),
weight=0,
permeable='no',
)
model2d.set_plate(shapes=edge,material=RigidPlateMaterial)
model2d.add_vertex([0,1])
vertex = model2d.select(p0=[0,1],p1=[0,2],types=['vertex'])
model2d.set_hinge_2d(vertices=vertex)
```
