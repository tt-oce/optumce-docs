# LinearElastic

Linear-elastic material -- Hooke's law without yielding, used where
deformation is small or stiffness is the only quantity of interest.

## Examples

```python
material = project.LinearElastic(name='Elastic', E=30, nu=0.3)
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
