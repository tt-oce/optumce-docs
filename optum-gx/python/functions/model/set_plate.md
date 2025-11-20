Set shape material as plate.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
<dt>material : material</dt>
<dd>Plate material</dd>
<dt>strength_reduction_factor : float</dt>
<dd>Strength reduction factor.</dd>
<dt>tension_cutoff : boolean</dt>
<dd>Tension cutoff. tension_cutoff = True or False</dd>
<dt>compression_cutoff : boolean</dt>
<dd>Compression cutoff. compression_cutoff = True or False</dd>
</dl>

## See also

- [set_solid](/python/functions/model/set_solid)

## Examples

```python
model2d.add_line(p0=[0,0],p1=[1,1])
Edge = model2d.select(p0=[0.5,0.5],types='edge')
RigidPlateMaterial = prj.RigidPlate(name='RigidPlateMaterial',
color=rgb(128,156,180),
weight=0,
permeable='no')                                    )
model2d.set_plate(shapes=Edge,
material=RigidPlateMaterial,
strength_reduction_factor=1,
tension_cutoff=True,
compression_cutoff=False)
model3d.add_box(p1=[0,0,0],p2=[1,1,1])
Face = model3d.select(p0=[1,0.5,0.5],types='face')
FlatPlateSteelMaterial = prj.FlatPlateSteel(name='FlatPlateSteelMaterial',
color=rgb(241,181,13),
t=10,
E=210000,
nu=0.3,
yield_condition='iluyshin',
parameter_set='A',
moment_resistance='elastic',
f_y=300,
m_p=5,
n_p = 3000,
weight=0,
permeable='no',
reducible_strength='yes',
)
model3d.set_plate(shapes=Face,
material=FlatPlateSteelMaterial,
strength_reduction_factor=1,
tension_cutoff=True,
compression_cutoff=False)
```
