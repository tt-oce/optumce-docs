# FlatPlateConcrete

Define a Flat Plate Concrete material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(241,131,53)</dd>
<dt>t : float</dt>
<dd>Thickness, in m.</dd>
<dt>E : float</dt>
<dd>Young's Modulus, in MPa.</dd>
<dt>nu : float</dt>
<dd>Poisson's ratio.</dd>
<dt>m_px : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>m_py : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>f_c : float</dt>
<dd>Compressive yield strength, in MPa.</dd>
<dt>f_t : float</dt>
<dd>Tensile yield strength, in MPa.</dd>
<dt>weight : float</dt>
<dd>Weight in kN/m^2.</dd>
<dt>permeable : float</dt>
<dd>Apply permability. permeable= 'yes' or 'no'</dd>
<dt>reducible_strength : str</dt>
<dd>Apply reducible strength. reducible_strength = 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 16
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
FlatPlateConcreteMaterial = prj.FlatPlateConcrete(name='FlatPlateConcreteMaterial',
color=rgb(241,131,53),
E=210000,
nu=0.3,
m_px=100,
m_py=100,
f_c=30,
f_t=1,
thickness=10,
weight=0,
permeable='no',
reducible_strength='yes',
)
model2d.set_solid(shapes=Face,material=FlatPlateConcreteMaterial)
```
