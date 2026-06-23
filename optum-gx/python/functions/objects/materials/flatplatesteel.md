# FlatPlateSteel

Flat plate (steel) -- steel plate element parameterised by thickness
and yield strength, with optional yield-condition cutoff.

## Examples

```python
material = project.FlatPlateSteel(name='Steel Plate', t=0.01, f_y=355)
material.t
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
<dt>t : float | ParameterMap | Profile | Gradient</dt>
<dd>Thickness.</dd>
<dt>permeable : bool</dt>
<dd>Permeable flag.</dd>
<dt>weight : float | ParameterMap | Profile | Gradient</dt>
<dd>Weight per unit area.</dd>
<dt>yield_condition : int</dt>
<dd>Yield condition type (square=0, diamond=1, iluyshin=2, none=3).</dd>
<dt>parameter_set : int</dt>
<dd>Parameter set (A=0, B=1).</dd>
<dt>moment_resistance : int</dt>
<dd>Moment resistance type (elastic=0, plastic=1, hardening=2).</dd>
<dt>f_y : float | ParameterMap | Profile | Gradient</dt>
<dd>Yield strength.</dd>
<dt>m_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic moment capacity.</dd>
<dt>n_p : float | ParameterMap | Profile | Gradient</dt>
<dd>Plastic axial capacity.</dd>
</dl>
