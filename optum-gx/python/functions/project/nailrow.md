# NailRow

Define a Nail Row material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(218,28,92)</dd>
<dt>diameter : float</dt>
<dd>Diameter, in m.</dd>
<dt>youngs_modulus : float</dt>
<dd>Young's modulus, in MPa.</dd>
<dt>spacing : float</dt>
<dd>Spacing, in m.</dd>
<dt>axial_strength : float</dt>
<dd>Axial strength, in kN/m.</dd>
<dt>lateral_strength : float</dt>
<dd>Lateral strength, kN/m.</dd>
</dl>

## Examples

```python
i = 21
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
NailRowMat = prj.NailRow(name='NailRowMat',
color=rgb(218,28,92),
diameter=0.05,
young_modulus=200000,
spacing=1,
axial_strength=250,
lateral_strength=10,
)
model2d.set_solid(shapes=Face,material=NailRowMat)
```
