# RigidPlate

Rigid plate -- plate element with no deformation, used for sheet piles
or walls whose stiffness dominates the analysis.

## Examples

```python
material = project.RigidPlate(name='Rigid Wall', weight=0)
material.weight
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
<dt>permeable : bool</dt>
<dd>Permeable flag.</dd>
<dt>weight : float | ParameterMap | Profile | Gradient</dt>
<dd>Weight per unit area.</dd>
</dl>
