# RigidPlate

Define a Rigid Plate material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(128,156,180)</dd>
<dt>weight : float</dt>
<dd>Weight in kN/m^2</dd>
<dt>permeable : str</dt>
<dd>Apply permability. permeable= 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 14
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
RigidPlateMaterial = prj.RigidPlate(name='RigidPlateMaterial',
color=rgb(128,156,180),
weight=0,
permeable='no',
)
model2d.set_solid(shapes=Face,material=RigidPlateMaterial)
```
