# HMC

Define a Hardening Mohr-Coulomb material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= Color(r=79,g=180,b=63)</dd>
<dt>drainage : str</dt>
<dd>Material drainage type. drainage = 'drained_undrained', 'always_drained', 'non_porous'</dd>
<dt>cavitation_cutoff : str</dt>
<dd>cavitation_cutoff = 'no' or 'yes'</dd>
<dt>pcav : float</dt>
<dd>Cavitation pressure in kPa</dd>
<dt>E50_ref : float</dt>
<dd>Reference secant modulus based on triaxial failure, in MPa</dd>
<dt>Eur_ref : float</dt>
<dd>Unloading/reloading reference modulus, in MPa.</dd>
<dt>nu_ref : float</dt>
<dd>Reference Poisson's ratio.</dd>
<dt>c : float</dt>
<dd>Cohesion in kPa.</dd>
<dt>phi : float</dt>
<dd>Friction angle in degrees</dd>
<dt>flow_rule : str</dt>
<dd>flow_rule = 'associated' or 'nonassociated'</dd>
<dt>psi : float</dt>
<dd>Dilation angle</dd>
<dt>dilation_cap : str</dt>
<dd>dilation_cap = 'no', 'volumetric', 'deviatoric'</dd>
<dt>ev_cr : float</dt>
<dd>Critical volumetric strain</dd>
<dt>es_cr : float</dt>
<dd>Critical shear strain</dd>
<dt>pressure_dependence : str</dt>
<dd>Type of pressure dependence. pressure_dependence = 'sigma3', 'p', 'p_minus_q3'</dd>
<dt>pref : float</dt>
<dd>Reference pressure in kPa. Commonly pref = 100</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3</dd>
<dt>tension_cutoff : boolean</dt>
<dd>Apply tension cutoff. tension_cutoff = 'yes' or 'no'</dd>
<dt>sigma_t : float</dt>
<dd>Tensile cutoff stress.</dd>
<dt>softening : str</dt>
<dd>Apply softening. softening = 'yes' or 'no'</dd>
<dt>phi_residual : float</dt>
<dd>Residual shear strength.</dd>
<dt>e_cr1 : float</dt>
<dd>Critical plastic strain peak.</dd>
<dt>e_cr2 : float</dt>
<dd>Critical plastic strain residual.</dd>
<dt>K0 : float</dt>
<dd>Earth pressure coefficient at rest.</dd>
<dt>hydraulic_conductivity_option : str</dt>
<dd>hydraulic_conductivity_option = 'isotropic' or 'anisotropic'</dd>
<dt>K : float</dt>
<dd>Hydraulic conductivity, in m/day.</dd>
<dt>Kx : float</dt>
<dd>Hydraulic conductivity in x, in m/day.</dd>
<dt>Ky : float</dt>
<dd>Hydraulic conductivity in y, in m/day.</dd>
<dt>Kz : float</dt>
<dd>Hydraulic conductivity in z, in m/day.</dd>
<dt>hydraulic_model : str</dt>
<dd>hydraulic_model = 'basic' or 'van_genuchten'</dd>
<dt>e : float</dt>
<dd>Void ratio.</dd>
<dt>alpha : float</dt>
<dd>Model parameter related to the air entry pressure.</dd>
<dt>n : float</dt>
<dd>Model parameter related to the rate at which water is extracted from the soil once the air entry pressure has been exceeded.</dd>
<dt>Sr : float</dt>
<dd>Residual degree of saturation (may be slightly greater than 0).</dd>
<dt>Ss : float</dt>
<dd>Fraction of water filled pores at full saturation (may be slightly less than 1).</dd>
<dt>reducible_strength : str</dt>
<dd>Apply reducible strength. reducible_strength = 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 4
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
HMCMaterial = prj.HMC(name='HMCMaterial',
color= Color(r=27,g=152,b=86),
drainage = 'drained_undrained',
cavitation_cutoff = 'yes',
pcav = 100,
E50_ref = 30,
Eur_ref= 100,
nu_ref = 0.25,
c = 0,
phi = 35,
flow_rule= 'taylor',
psi=5,
dilation_cap= 'volumetric',
ev_cr= 0.01,
es_cr= 0.01,
pressure_dependence='sigma3',
pref=100,
m = 0.5,
tension_cutoff= 'yes',
sigma_t = 0,
softening= 'yes',
phi_residual=20,
e_cr1=0.01,
e_cr2=0.012,
gamma_dry= 18,
gamma_sat= 20,
K0=0.58,
hydraulic_conductivity_option= 'anisotropic',
K=0.001,
Kx=0.001,
Ky=0.001,
Kz=0.001,
hydraulic_model='van_genuchten',
e=1,
alpha=2,
n=2,
Sr=0,
Ss=1,
reducible_strength='yes',
)
model2d.set_solid(shapes=Face,material=HMCMaterial)
```
