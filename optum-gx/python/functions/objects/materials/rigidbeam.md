# RigidBeam

Rigid beam -- beam element with no deformation, used for stiff
secondary structural members.

## Examples

```python
material = project.RigidBeam(name='Rigid Strut', gamma=0)
material.gamma
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
<dt>gamma : float | ParameterMap | Profile | Gradient</dt>
<dd>Weight per unit length.</dd>
</dl>
