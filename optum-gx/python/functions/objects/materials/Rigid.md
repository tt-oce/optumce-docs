# Rigid

Rigid material -- no deformation, used to model bodies whose stiffness
dominates the solution (e.g. retaining walls, footings).

## Examples

```python
material = project.Rigid(name='Wall', gamma_dry=22)
material.gamma_dry
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
<dt>tension_cutoff : bool</dt>
<dd>Tension cutoff flag.</dd>
<dt>sigma_t : float | ParameterMap | Profile | Gradient</dt>
<dd>Tensile strength.</dd>
<dt>hydraulic_conductivity_option : int</dt>
<dd>Hydraulic conductivity option (isotropic/anisotropic).</dd>
<dt>hydraulic_model : int</dt>
<dd>Hydraulic model type.</dd>
<dt>drainage : int</dt>
<dd>Drainage type.</dd>
<dt>K0 : float | ParameterMap | Profile | Gradient</dt>
<dd>Coefficient of earth pressure at rest.</dd>
<dt>K0_type : int</dt>
<dd>K0 type (auto or user).</dd>
<dt>cavitation_cutoff : bool</dt>
<dd>Cavitation cutoff flag.</dd>
<dt>pcav : float | ParameterMap | Profile | Gradient</dt>
<dd>Cavitation pressure.</dd>
<dt>Kx : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity in x direction.</dd>
<dt>Ky : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity in y direction.</dd>
<dt>Kz : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity in z direction.</dd>
<dt>K : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity (isotropic).</dd>
<dt>e : float | ParameterMap | Profile | Gradient</dt>
<dd>Void ratio.</dd>
<dt>alpha : float | ParameterMap | Profile | Gradient</dt>
<dd>Van Genuchten alpha parameter.</dd>
<dt>n : float | ParameterMap | Profile | Gradient</dt>
<dd>Van Genuchten n parameter.</dd>
<dt>Sr : float | ParameterMap | Profile | Gradient</dt>
<dd>Residual saturation.</dd>
<dt>Ss : float | ParameterMap | Profile | Gradient</dt>
<dd>Saturated saturation.</dd>
</dl>
