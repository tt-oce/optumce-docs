# set_point_bc

Set point boundary condition.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'vertex' in 2D and 'edge' in 3D</dd>
<dt>displacement_x : DisplacementType|float</dt>
<dd>Displacement in x. DisplacementType = 'free' or 'fixed'</dd>
<dt>displacement_y : DisplacementType|float</dt>
<dd>Displacement in y. DisplacementType = 'free' or 'fixed'</dd>
<dt>displacement_z : DisplacementType|float</dt>
<dd>Displacement in z. DisplacementType = 'free' or 'fixed' displacement_rotation_x DisplacementType|float Rotational displacement in x. DisplacementType = 'free' or 'fixed' displacement_rotation_y DisplacementType|float Rotational displacement in y. DisplacementType = 'free' or 'fixed' displacement_rotation_z DisplacementType|float Rotational displacement in z. DisplacementType = 'free' or 'fixed'</dd>
<dt>csys : Csys</dt>
<dd>Coordinate system</dd>
<dt>use_local_coord : boolean</dt>
<dd>Apply local coordinate system.</dd>
</dl>

## See also

- [set_plate_bc](/python/functions/model/set_plate_bc)
- [set_standard_fixities](/python/functions/model/set_standard_fixities)

## Examples

```python
model3d.add_line([0,0,0],[0,5,0])
Edge = model3d.select(point1=[0,2,0],types='edge')
print(Edge.values)
BeamMaterial = prj.Beam(name='BeamMaterial',
color=rgb(0,84,166),
envelope='diamond',
m_py=800,
m_pz=800,
n_p=5000,
t_p=500,
EI_y=100000,
EI_z=100000,
EA=4e6,
GJ=100000,
gamma=0,
)
model3d.set_plate(shapes=Edge,material=BeamMaterial)
RigidWall = prj.RigidPlate(name="RigidWall",gamma_dry=24,color=rgb(r=108,g=136,b=160))
sel = model3d.select([0,0,0],types='vertex')
model3d.set_point_bc(shapes=sel,
displacement_x='fixed',
displacement_y='fixed',
displacement_z='free',
displacement_rotation_x = 'free',
displacement_rotation_y= 'fixed',
displacement_rotation_z = 'free',
csys=model3d.get_csys('Global 3D'),
use_local_coord= False
)
```
