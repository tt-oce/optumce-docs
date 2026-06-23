# GeneralPlate

General plate material -- configurable axial and bending stiffness for
modelling sheet piles, walls and other structural plates with custom
properties.

## Examples

```python
material = project.GeneralPlate(name='Plate', EA=4e6, EI=1e5)
material.EA
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
<dt>permeable : bool</dt>
<dd>Permeable flag.</dd>
<dt>weight : float | ParameterMap | Profile | Gradient</dt>
<dd>Weight per unit area.</dd>
<dt>model : int</dt>
<dd>Hydraulic conductivity model.</dd>
<dt>EA_x : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness in x-direction.</dd>
<dt>EA_y : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness in y-direction.</dd>
<dt>GA : float | ParameterMap | Profile | Gradient</dt>
<dd>Shear stiffness.</dd>
<dt>EI_x : float | ParameterMap | Profile | Gradient</dt>
<dd>Bending stiffness in x-direction.</dd>
<dt>EI_y : float | ParameterMap | Profile | Gradient</dt>
<dd>Bending stiffness in y-direction.</dd>
<dt>GI : float | ParameterMap | Profile | Gradient</dt>
<dd>Torsional stiffness.</dd>
<dt>n_px : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity in x-direction.</dd>
<dt>n_py : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity in y-direction.</dd>
<dt>n_pxy : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic shear capacity.</dd>
<dt>m_px : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic moment capacity in x-direction.</dd>
<dt>m_py : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic moment capacity in y-direction.</dd>
<dt>m_pxy : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic torsional capacity.</dd>
<dt>EA : float | ParameterMap | Profile | Gradient</dt>
<dd>Isotropic axial stiffness.</dd>
<dt>EI : float | ParameterMap | Profile | Gradient</dt>
<dd>Isotropic bending stiffness.</dd>
<dt>n_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Isotropic plastic axial capacity.</dd>
<dt>m_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Isotropic plastic moment capacity.</dd>
<dt>yield_condition : int</dt>
<dd>Yield condition type (square=0, diamond=1, iluyshin=2, none=3).</dd>
</dl>
