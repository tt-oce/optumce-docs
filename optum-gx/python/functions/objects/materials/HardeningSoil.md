# HardeningSoil

Hardening-Soil model -- work-hardening elastoplastic soil with separate
loading and unloading/reloading stiffnesses, suitable for staged
geotechnical analyses.

## Examples

```python
material = project.HardeningSoil(name='HS Sand', Eur_ref=90)
material.Eur_ref
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
<dt>E50_ref : float | ParameterMap | Profile | Gradient</dt>
<dd>Reference secant stiffness from drained triaxial test.</dd>
<dt>Eur_ref : float | ParameterMap | Profile | Gradient</dt>
<dd>Reference unloading/reloading stiffness.</dd>
<dt>pressure_dependence : int</dt>
<dd>Pressure dependence type.</dd>
<dt>pref : float | ParameterMap | Profile | Gradient</dt>
<dd>Reference pressure.</dd>
<dt>m : float | ParameterMap | Profile | Gradient</dt>
<dd>Power for stress-level dependency of stiffness.</dd>
<dt>Ru : float | ParameterMap | Profile | Gradient</dt>
<dd>Pore pressure ratio.</dd>
<dt>E0_ref : float | ParameterMap | Profile | Gradient</dt>
<dd>Reference initial stiffness (small-strain).</dd>
<dt>gamma_07 : float | ParameterMap | Profile | Gradient</dt>
<dd>Shear strain at which G_s = 0.7 G_0.</dd>
<dt>Eoed_ref : float | ParameterMap | Profile | Gradient</dt>
<dd>Reference oedometer stiffness.</dd>
<dt>c : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion.</dd>
<dt>phi : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle.</dd>
<dt>flow_rule : int</dt>
<dd>Flow rule type (Constant/Rowe/Taylor).</dd>
<dt>psi : float | ParameterMap | Profile | Gradient</dt>
<dd>Dilation angle.</dd>
<dt>ev_cr : float | ParameterMap | Profile | Gradient</dt>
<dd>Critical volumetric strain.</dd>
<dt>es_cr : float | ParameterMap | Profile | Gradient</dt>
<dd>Critical shear strain.</dd>
<dt>dilation_cap : int</dt>
<dd>Dilation cap type.</dd>
<dt>M : float | ParameterMap | Profile | Gradient</dt>
<dd>Stiffness parameter M (from IHardeningSoilA, different from m).</dd>
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
