# MultiMohrCoulomb

Multi-surface Mohr-Coulomb -- Mohr-Coulomb with multiple yield surfaces
for modelling cyclic loading or kinematic hardening.

## Examples

```python
material = project.MultiMohrCoulomb(name='Multi MC', no_surfaces=3)
material.no_surfaces
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
<dt>no_surfaces : float</dt>
<dd>Number of failure surfaces.</dd>
<dt>phi1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle for surface 1.</dd>
<dt>phi2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle for surface 2.</dd>
<dt>phi3 : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle for surface 3.</dd>
<dt>phi4 : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle for surface 4.</dd>
<dt>phi5 : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle for surface 5.</dd>
<dt>c1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion for surface 1.</dd>
<dt>c2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion for surface 2.</dd>
<dt>c3 : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion for surface 3.</dd>
<dt>c4 : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion for surface 4.</dd>
<dt>c5 : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion for surface 5.</dd>
<dt>tension_cutoff : bool</dt>
<dd>Tension cutoff enabled.</dd>
<dt>sigma_t : float | ParameterMap | Profile | Gradient</dt>
<dd>Tensile strength.</dd>
<dt>hydraulic_conductivity_option : int</dt>
<dd>Hydraulic conductivity option.</dd>
<dt>hydraulic_model : int</dt>
<dd>Hydraulic model type.</dd>
<dt>drainage : int</dt>
<dd>Drainage type.</dd>
<dt>excess_pore_pressure : float</dt>
<dd>Excess pore pressure.</dd>
<dt>K0 : float | ParameterMap | Profile | Gradient</dt>
<dd>Coefficient of earth pressure at rest.</dd>
<dt>K0_type : int</dt>
<dd>K0 type (auto or user).</dd>
<dt>cavitation_cutoff : bool</dt>
<dd>Cavitation cutoff enabled.</dd>
<dt>pcav : float | ParameterMap | Profile | Gradient</dt>
<dd>Cavitation pressure.</dd>
<dt>Kx : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity in x-direction.</dd>
<dt>Ky : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity in y-direction.</dd>
<dt>Kz : float | ParameterMap | Profile | Gradient</dt>
<dd>Hydraulic conductivity in z-direction.</dd>
<dt>K : float | ParameterMap | Profile | Gradient</dt>
<dd>Isotropic hydraulic conductivity.</dd>
<dt>e : int</dt>
<dd>Void ratio.</dd>
<dt>alpha : float | ParameterMap | Profile | Gradient</dt>
<dd>van Genuchten alpha parameter.</dd>
<dt>n : int</dt>
<dd>van Genuchten n parameter.</dd>
<dt>Sr : float | ParameterMap | Profile | Gradient</dt>
<dd>Residual saturation.</dd>
<dt>Ss : float | ParameterMap | Profile | Gradient</dt>
<dd>Saturated saturation.</dd>
</dl>
