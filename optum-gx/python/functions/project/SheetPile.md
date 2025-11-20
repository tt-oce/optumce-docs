# SheetPile

Define a Sheet Pile material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(241,71,133)</dd>
<dt>profile_type : str</dt>
<dd>Profile type.</dd>
<dt>profile : str</dt>
<dd>Name of profile. ex. profile='AZ_17_700'</dd>
<dt>parameter_set : str</dt>
<dd>parameter_set= 'A' or 'B'</dd>
<dt>E : float</dt>
<dd>Young's Modulus, in MPa.</dd>
<dt>f_y : float</dt>
<dd>Yield strength, in MPa.</dd>
<dt>moment_resistance : str</dt>
<dd>Type of moment resistance. moment_resistance='elastic' or 'plastic'</dd>
<dt>yield_condition : str</dt>
<dd>Type of yield surface. yield_condition= 'none', 'square', 'diamond', 'iluyshin'</dd>
<dt>EA_y : float</dt>
<dd>In-plane stiffness, in N/m.</dd>
<dt>EI_y : float</dt>
<dd>Bending stifness in y, in Nm^2/m.</dd>
<dt>GA : float</dt>
<dd>In-plane shear stifness, in kN/m.</dd>
<dt>GI : float</dt>
<dd>Torsional stifness, in Nm^2/m</dd>
<dt>n_py : float</dt>
<dd>Anisotropic shell strength parameter, in N/m.</dd>
<dt>n_pxy : float</dt>
<dd>Anisotropic shell strength parameter, in N/m.</dd>
<dt>m_py : float</dt>
<dd>Bending moment capacity, in Nm/m.</dd>
<dt>m_pxy : float</dt>
<dd>Torsional moment capacity, in Nm/m.</dd>
<dt>reducible_strength : str</dt>
<dd>Apply reducible strength. reducible_strength = 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 18
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
SheetPileMaterial = prj.SheetPile(name='SheetPileMaterial',
color=rgb(241,71,133),
profile_type='AZ',
profile='AZ_17_700',
parameter_set='B',
E =210000,
f_y=350,
yield_condition='diamond',
moment_resistance='plastic',
EA_y= 644,
EI_y=10.7,
GA=21219,
GI=452,
n_py=2400,
n_pxy=51000,
m_py=40,
m_pxy=1100,
reducible_strength='yes',
)
model2d.set_solid(shapes=Face,material=SheetPileMaterial)
```
