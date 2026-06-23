# Beam

Beam element -- beam material with axial and bending stiffness in two
directions, for modelling secondary structural members.

## Examples

```python
material = project.Beam(name='Steel Beam', E=210000)
material.E
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
<dt>E : float | ParameterMap | Profile | Gradient</dt>
<dd>Young's modulus.</dd>
<dt>nu : float | ParameterMap | Profile | Gradient</dt>
<dd>Poisson's ratio.</dd>
<dt>envelope : int</dt>
<dd>Yield envelope type (square=0, diamond=1, iluyshin=2, none=3).</dd>
<dt>m_py : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic moment capacity about y-axis.</dd>
<dt>m_pz : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic moment capacity about z-axis.</dd>
<dt>n_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity.</dd>
<dt>t_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic torsional capacity.</dd>
<dt>EI_y : float | ParameterMap | Profile | Gradient</dt>
<dd>Bending stiffness about y-axis.</dd>
<dt>EI_z : float | ParameterMap | Profile | Gradient</dt>
<dd>Bending stiffness about z-axis.</dd>
<dt>EA : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness.</dd>
<dt>GJ : float | ParameterMap | Profile | Gradient</dt>
<dd>Torsional stiffness.</dd>
<dt>gamma : float | ParameterMap | Profile | Gradient</dt>
<dd>Weight per unit length.</dd>
</dl>
