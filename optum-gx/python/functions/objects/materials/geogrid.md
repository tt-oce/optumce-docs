# Geogrid

Geogrid reinforcement material -- thin tensile reinforcement for
modelling geogrids and reinforcement layers in soils.

## Examples

```python
material = project.Geogrid(name='Geogrid', E=210000)
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
<dt>permeable : bool</dt>
<dd>Permeable flag.</dd>
<dt>n_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity.</dd>
<dt>EA : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness.</dd>
<dt>EA_x : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness in x-direction (anisotropic mode).</dd>
<dt>EA_y : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness in y-direction (anisotropic mode).</dd>
<dt>n_px : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity in x-direction (anisotropic mode).</dd>
<dt>n_py : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity in y-direction (anisotropic mode).</dd>
</dl>
