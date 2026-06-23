# MohrCoulombEngineering

Mohr-Coulomb Engineering -- Mohr-Coulomb variant parameterised with
engineering-style strength quantities for design-code workflows.

## Examples

```python
material = project.MohrCoulombEngineering(name='MCE Clay', phi=25, c=20)
material.phi
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
<dd>Young's modulus (parameter set A).</dd>
<dt>nu : float | ParameterMap | Profile | Gradient</dt>
<dd>Poisson's ratio (parameter sets A and B).</dd>
<dt>K : float | ParameterMap | Profile | Gradient</dt>
<dd>Bulk modulus (parameter sets B and C).</dd>
<dt>G : float | ParameterMap | Profile | Gradient</dt>
<dd>Shear modulus (parameter set C).</dd>
<dt>parameter_set : str</dt>
<dd>Elastic parameter set: 'A' (E, nu), 'B' (K, nu), or 'C' (K, G).</dd>
<dt>phi : float | ParameterMap | Profile | Gradient</dt>
<dd>Friction angle.</dd>
<dt>c : float | ParameterMap | Profile | Gradient</dt>
<dd>Cohesion.</dd>
<dt>flow_rule : int</dt>
<dd>Flow rule type.</dd>
<dt>psi : float | ParameterMap | Profile | Gradient</dt>
<dd>Dilation angle.</dd>
<dt>dilation_cap : int</dt>
<dd>Dilation cap type.</dd>
<dt>ev_cr : float | ParameterMap | Profile | Gradient</dt>
<dd>Critical volumetric strain.</dd>
<dt>es_cr : float | ParameterMap | Profile | Gradient</dt>
<dd>Critical shear strain.</dd>
<dt>compression_cap : bool</dt>
<dd>Compression cap enabled.</dd>
<dt>compression_strength : float | ParameterMap | Profile | Gradient</dt>
<dd>Compression strength.</dd>
<dt>softening : bool</dt>
<dd>Softening enabled.</dd>
<dt>phi_residual : float | ParameterMap | Profile | Gradient</dt>
<dd>Residual friction angle.</dd>
<dt>e_cr1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Critical strain 1.</dd>
<dt>e_cr2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Critical strain 2.</dd>
<dt>phi_2d : float | ParameterMap | Profile | Gradient</dt>
<dd>2D friction angle.</dd>
<dt>phi_3d : float | ParameterMap | Profile | Gradient</dt>
<dd>3D friction angle.</dd>
<dt>cu : float | ParameterMap | Profile | Gradient</dt>
<dd>Undrained shear strength.</dd>
<dt>c_2d_davis : float | ParameterMap | Profile | Gradient</dt>
<dd>2D Davis cohesion.</dd>
<dt>c_3d_davis : float | ParameterMap | Profile | Gradient</dt>
<dd>3D Davis cohesion.</dd>
<dt>phi_2d_davis : float | ParameterMap | Profile | Gradient</dt>
<dd>2D Davis friction angle.</dd>
<dt>phi_3d_davis : float | ParameterMap | Profile | Gradient</dt>
<dd>3D Davis friction angle.</dd>
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
