# Beam

Define a beam material

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color=rgb(169,179,193)</dd>
<dt>envelope : str</dt>
<dd>Type of yield envelope. envelope= 'none', 'square', 'diamond', 'iluyshin'</dd>
<dt>m_py : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>m_pz : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>n_p : float</dt>
<dd>Yield force, in kN.</dd>
<dt>t_p : float</dt>
<dd>Torsional capacity, in kNm.</dd>
<dt>EI_y : float</dt>
<dd>Bending stifness in y, in kNm^2.</dd>
<dt>EI_z : float</dt>
<dd>Bending stifness in z, in kNm^2.</dd>
<dt>EA : float</dt>
<dd>Normal Stiffness, in kN.</dd>
<dt>GJ : float</dt>
<dd>Torsional stifness, in kN/m^2.</dd>
<dt>gamma : float</dt>
<dd>Unit weight, in kN/m.</dd>
</dl>

## Examples

```python
i = 22
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
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
model2d.set_solid(shapes=Face,material=BeamMaterial)
```
