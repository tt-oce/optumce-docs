# SheetPile

Sheet pile profile -- standard steel sheet pile sections (Az, Larssen,
etc.) with built-in section properties and yield strength.

## Examples

```python
material = project.SheetPile(name='AZ Profile', profile='AZ_17_700')
material.profile
```

## Properties

<dl>
<dt>name : str</dt>
<dd>Material name.</dd>
<dt>color : Color</dt>
<dd>Material color.</dd>
<dt>gamma_dry : float | ParameterMap | Profile | Gradient</dt>
<dd>Dry unit weight.</dd>
<dt>gamma_sat : float | ParameterMap | Profile | Gradient</dt>
<dd>Saturated unit weight.</dd>
<dt>reducible_strength : bool</dt>
<dd>Reducible strength flag.</dd>
<dt>profile_type : int</dt>
<dd>Profile type (AZ=0).</dd>
<dt>profile : str</dt>
<dd>Profile name.</dd>
<dt>parameter_set : int</dt>
<dd>Parameter set (A=0, B=1).</dd>
<dt>E : float</dt>
<dd>Young's modulus of sheet pile.</dd>
<dt>f_y : float</dt>
<dd>Yield strength.</dd>
<dt>yield_condition : int</dt>
<dd>Yield condition type (square=0, diamond=1, iluyshin=2, none=3).</dd>
<dt>moment_resistance : int</dt>
<dd>Moment resistance type (elastic=0, plastic=1, hardening=2).</dd>
<dt>EA_y : float</dt>
<dd>Axial stiffness in y-direction.</dd>
<dt>EI_y : float</dt>
<dd>Bending stiffness in y-direction.</dd>
<dt>GA : float</dt>
<dd>Shear stiffness.</dd>
<dt>GI : float</dt>
<dd>Torsional stiffness.</dd>
<dt>n_py : float</dt>
<dd>Plastic axial capacity in y-direction.</dd>
<dt>m_py : float</dt>
<dd>Plastic moment capacity in y-direction.</dd>
<dt>n_pxy : float</dt>
<dd>Plastic shear capacity.</dd>
<dt>m_pxy : float</dt>
<dd>Plastic torsional capacity.</dd>
<dt>weight : float | ParameterMap | Profile | Gradient</dt>
<dd>Unit weight.</dd>
</dl>
