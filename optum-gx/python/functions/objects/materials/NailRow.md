# NailRow

Soil-nail row material -- discrete row of grouted nails parameterised
by spacing, diameter and yield strength.

## Examples

```python
material = project.NailRow(name='Nail Row', young_modulus=200000)
material.young_modulus
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
<dt>young_modulus : float | ParameterMap | Profile | Gradient</dt>
<dd>Young's modulus of nail.</dd>
<dt>spacing : float</dt>
<dd>Spacing between nails.</dd>
<dt>axial_strength : float</dt>
<dd>Axial strength of nail.</dd>
<dt>lateral_strength : float</dt>
<dd>Lateral strength of nail.</dd>
<dt>diameter : float</dt>
<dd>Diameter of nail.</dd>
</dl>
