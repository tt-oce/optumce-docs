# ModifiedCamClay

Define a Modified Cam Clay material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color=rgb(197,138,38)</dd>
<dt>drainage : str</dt>
<dd>Material drainage type. drainage = 'drained_undrained', 'always_drained', 'non_porous'</dd>
<dt>cavitation_cutoff : str</dt>
<dd>cavitation_cutoff = 'no' or 'yes'</dd>
<dt>pcav : float</dt>
<dd>Cavitation pressure in kPa.</dd>
<dt>parameter_set : str</dt>
<dd>Stiffnes parameters in v:ln(p') plane or v:log10(sigma'_v). parameter_set= 'A' or 'B'</dd>
<dt>mcc_kappa : float</dt>
<dd>Slope of unloading-reloading line.</dd>
<dt>mcc_lambda : float</dt>
<dd>Slope of normal compression line.</dd>
<dt>C_s : float</dt>
<dd>Swelling index.</dd>
<dt>C_c : float</dt>
<dd>Compression index.</dd>
<dt>nu : float</dt>
<dd>Poisson's ratio.</dd>
<dt>c : float</dt>
<dd>Cohesion in kPa</dd>
<dt>phi : float</dt>
<dd>Friction angle in degrees</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3</dd>
<dt>tension_cutoff : str</dt>
<dd>Apply tension cutoff. tension_cutoff = 'yes' or 'no'</dd>
<dt>sigma_t : str</dt>
<dd>Tensile cutoff stress, in kPa.</dd>
<dt>K0_option : str</dt>
<dd>Option to auto assign or user define Earth pressure coefficient at rest. K0_option= 'user' or 'auto'</dd>
<dt>K0_nc : float</dt>
<dd>Normally consolidated earth pressure coefficient at rest.</dd>
<dt>K0_oc : float</dt>
<dd>Over consolidated earth pressure coefficient at rest.</dd>
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
i = 9
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
MCCMaterial = prj.ModifiedCamClay(name='MCCMaterial',
color=rgb(197,138,38),
drainage = 'drained_undrained',
cavitation_cutoff=False,
pcav=100,
parameter_set= 'B',
mcc_kappa= 0.02,
mcc_lambda=0.1,
C_s=0.01,
C_c=0.1,
nu=0.25,
c=0,
phi=30,
tension_cutoff='yes',
sigma_t=0,
gamma_dry=18,
gamma_sat=20,
K0_option= 'user',
K0_nc= 0.6,
K0_oc= 0.4,
hydraulic_conductivity_option='anisotropic',
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
model2d.set_solid(shapes=Face,material=MCCMaterial)
```
