# Connector

Connector material -- axial-only element for trusses, struts and
similar line members.

## Examples

```python
material = project.Connector(name='Tie', EA=210000, yield_force=300)
material.yield_force
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
<dt>yield_force : float | ParameterMap | Profile | Gradient</dt>
<dd>Yield force.</dd>
<dt>EA : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness.</dd>
<dt>spacing : float</dt>
<dd>Spacing between bars.</dd>
<dt>yield_strength : float | ParameterMap | Profile | Gradient</dt>
<dd>Yield strength (parameter set B).</dd>
<dt>diameter : float</dt>
<dd>Bar diameter (parameter set B).</dd>
<dt>parameter_set : str</dt>
<dd>Parameter set: 'A' or 'B'.</dd>
</dl>
