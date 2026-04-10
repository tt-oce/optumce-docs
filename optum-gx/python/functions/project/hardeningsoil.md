# HardeningSoil

Define a Hardeing Soil material.

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
<dd>Cavitation pressure in kPa.</dd>
<dt>E50_ref : float</dt>
<dd>Reference secant modulus based on triaxial failure, in MPa.</dd>
<dt>Eur_ref : float</dt>
<dd>Reference unloading-reloading modulus, in MPa.</dd>
<dt>nu : float</dt>
<dd>Poisson's ratio.</dd>
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
<dd>Reference pressure in kPa</dd>
<dt>m : float</dt>
<dd>Model fitting parameter. Generally: 0.5 < m < 1</dd>
<dt>Ru : float</dt>
<dd>Failure ratio.</dd>
<dt>E0_ref : float</dt>
<dd>Small strain reference modulus, in MPa.</dd>
<dt>gamma_07 : float</dt>
<dd>Shear strain relating small strain modulus and secant modulus.</dd>
<dt>Eoed_ref : float</dt>
<dd>Reference oedometer modulus.</dd>
<dt>M : float</dt>
<dd>Internal material parameter for cap.</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3</dd>
<dt>tension_cutoff : boolean</dt>
<dd>Apply tension cutoff. tension_cutoff = 'yes' or 'no'</dd>
<dt>sigma_t : float</dt>
<dd>Tensile cutoff stress, in kPa.</dd>
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
</dl>

## Examples

```python
i = 3
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
HardeningSoilMaterial = prj.HardeningSoil(name='HardeningSoilMaterial',
color= Color(r=180,g=181,b=92),
drainage = 'drained_undrained',
cavitation_cutoff = 'yes',
pcav = 100,
e50_ref = 30,
eur_ref= 100,
nu = 0.2,
c = 0,
phi = 35,
flow_rule= 'rowe',
psi=35,
dilation_cap= 'volumetric',
ev_cr= 0.01,
es_cr= 0.01,
pressure_dependence='sigma3',
pref=100,
m = 0.5,
Ru=0.9,
E0_ref= 250,
gamma_07= 0.0001,
Eoed_ref=30,
M=1.5,
gamma_dry= 18,
gamma_sat= 20,
tension_cutoff= 'yes',
sigma_t = 0,
K0=0.001,
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
)
model2d.set_solid(shapes=Face,material=HardeningSoilMaterial)
```
