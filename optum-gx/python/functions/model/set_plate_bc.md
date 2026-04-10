# set_plate_bc

Set plate boundary condition.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'vertex' in 2D and 'edge' in 3D</dd>
<dt>displacement_x : DisplacementType|float</dt>
<dd>Displacement in x. DisplacementType = 'free' or 'fixed'</dd>
<dt>displacement_y : DisplacementType|float</dt>
<dd>Displacement in y. DisplacementType = 'free' or 'fixed'</dd>
<dt>displacement_z : DisplacementType|float</dt>
<dd>Displacement in z. DisplacementType = 'free' or 'fixed' displacement_rotation DisplacementType|float Rotational displacement. DisplacementType = 'free' or 'fixed'</dd>
<dt>csys : Csys</dt>
<dd>Coordinate system</dd>
<dt>use_local_coord : boolean</dt>
<dd>Apply local coordinate system.</dd>
</dl>

## See also

- [set_point_bc](/python/functions/model/set_point_bc)
- [set_standard_fixities](/python/functions/model/set_standard_fixities)

## Examples

```python
model2d.add_line([0,0],[0,5])
RigidWall = prj.RigidPlate(name="RigidWall",gamma_dry=24,color=Color(r=108,g=136,b=160))
sel = model2d.select([0,1],types='edge')
model2d.set_plate(shapes=sel,
material=RigidWall,
strength_reduction_factor=1,
tension_cutoff=5,
compression_cutoff=False,
)
v = model2d.get_vertices([[0,0]])
model2d.set_plate_bc(shapes=v,
displacement_x='fixed',
displacement_y='fixed',
displacement_z='free',
displacement_rotation='free',
csys=project.get_csys('Global 2D'),
use_local_coord= False
)
```
