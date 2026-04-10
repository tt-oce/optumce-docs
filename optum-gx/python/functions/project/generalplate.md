# GeneralPlate

Define a General Plate material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(241,101,93)</dd>
<dt>model : str</dt>
<dd>model= 'isotropic' or 'anisotropic'.</dd>
<dt>EA : float</dt>
<dd>Normal stifness, in kN/m.</dd>
<dt>EI : float</dt>
<dd>Bending stifness, in kNm.</dd>
<dt>n_p : float</dt>
<dd>Yield force, in kN/m.</dd>
<dt>m_p : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>EA_x : float</dt>
<dd>In-plane stifness, in kN/m.</dd>
<dt>EA_y : float</dt>
<dd>In-plane stifness, in kN/m.</dd>
<dt>GA : float</dt>
<dd>In-plane shear stiffness, in kN/m.</dd>
<dt>EI_x : float</dt>
<dd>Bending stifness in x, in kNm.</dd>
<dt>EI_y : float</dt>
<dd>Bending stifness in y, in kNm.</dd>
<dt>GI : float</dt>
<dd>Torsional stifness, in kN/m</dd>
<dt>yield_condition : str</dt>
<dd>Type of yield surface. yield_condition= 'none', 'square', 'diamond', 'iluyshin'</dd>
<dt>n_px : float</dt>
<dd>Anisotropic shell strength parameter, in kN/m.</dd>
<dt>n_py : float</dt>
<dd>Anisotropic shell strength parameter, in kN/m.</dd>
<dt>n_pxy : float</dt>
<dd>Anisotropic shell strength parameter, in kN/m.</dd>
<dt>m_px : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>m_py : float</dt>
<dd>Bending moment capacity, in kNm/m.</dd>
<dt>m_pxy : float</dt>
<dd>Torsional moment capacity, in kNm/m.</dd>
<dt>weight : float</dt>
<dd>Weight in kN/m^2.</dd>
<dt>permeable : float</dt>
<dd>Apply permability. permeable= 'yes' or 'no'</dd>
<dt>reducible_strength : str</dt>
<dd>Apply reducible strength. reducible_strength = 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 17
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
GeneralPlateMaterial = prj.GeneralPlate(name='GeneralPlateMaterial',
color=rgb(241,101,93),
# model='anisotropic',
EA= 4e6,
EI=1e5,
n_p=5000,
m_p=800,
EA_x=210000,
EA_y=0.3,
GA=100,
EI_x=100,
EI_y=30,
GI=1,
yield_condition='square',
n_px=4.4e6,
n_py=2400,
n_pxy=51000,
m_px=124000,
m_py=40,
m_pxy=1100,
weight=0,
permeable='no',
reducible_strength='yes',
)
model2d.set_solid(shapes=Face,material=GeneralPlateMaterial)
```
