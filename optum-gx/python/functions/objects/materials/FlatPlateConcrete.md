# FlatPlateConcrete

Flat plate (concrete) -- concrete plate element parameterised by
thickness and concrete grade for slab and wall modelling.

## Examples

```python
material = project.FlatPlateConcrete(name='Concrete Slab', t=0.3)
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
<dt>m_px_plus : float | ParameterMap | Profile | Gradient</dt>
<dd>Positive plastic moment capacity in x-direction.</dd>
<dt>m_py_plus : float | ParameterMap | Profile | Gradient</dt>
<dd>Positive plastic moment capacity in y-direction.</dd>
<dt>f_c : float | ParameterMap | Profile | Gradient</dt>
<dd>Compressive strength of concrete.</dd>
<dt>f_t : float | ParameterMap | Profile | Gradient</dt>
<dd>Tensile strength of concrete.</dd>
<dt>m_px_minus : float | ParameterMap | Profile | Gradient</dt>
<dd>Negative plastic moment capacity in x-direction.</dd>
<dt>m_py_minus : float | ParameterMap | Profile | Gradient</dt>
<dd>Negative plastic moment capacity in y-direction.</dd>
</dl>
