# MultiMohrCoulomb

Define a Multi Mohr-Coulomb material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(27,152,86)</dd>
<dt>drainage : str</dt>
<dd>Material drainage type. drainage = 'drained_undrained', 'always_drained', 'non_porous'</dd>
<dt>cavitation_cutoff : str</dt>
<dd>cavitation_cutoff = 'no' or 'yes'</dd>
<dt>pcav : float</dt>
<dd>Cavitation pressure in kPa.</dd>
<dt>E : float</dt>
<dd>Young's Modulus, in MPa.</dd>
<dt>nu : float</dt>
<dd>Poisson's ratio.</dd>
<dt>no_surfaces : int</dt>
<dd>Number of surfaces up to 5.</dd>
<dt>c1 : float</dt>
<dd>Cohesion for the first surface.</dd>
<dt>phi1 : float</dt>
<dd>Friction angle in degrees for the first surface.</dd>
<dt>c2 : float</dt>
<dd>Cohesion for the second surface.</dd>
<dt>phi2 : float</dt>
<dd>Friction angle in degrees for the second surface.</dd>
<dt>c3 : float</dt>
<dd>Cohesion for the third surface.</dd>
<dt>phi3 : float</dt>
<dd>Friction angle in degrees for the third surface.</dd>
<dt>c4 : float</dt>
<dd>Cohesion for the fourth surface.</dd>
<dt>phi4 : float</dt>
<dd>Friction angle in degrees for the fourth surface.</dd>
<dt>c5 : float</dt>
<dd>Cohesion for the fifth surface.</dd>
<dt>phi5 : float</dt>
<dd>Friction angle in degrees for the fifth surface.</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3</dd>
<dt>tension_cutoff : str</dt>
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
<dt>reducible_strength : str</dt>
<dd>Apply reducible strength. reducible_strength = 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 11
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
MMCMaterial = prj.MultiMohrCoulomb(name='MMCMaterial',
color= rgb(27,152,86),
drainage = 'drained_undrained',
cavitation_cutoff = True,
pcav = 100,
E= 30,
nu= 0.25,
no_surfaces=2,
c1= 5,
phi1= 35,
c2= 15,
phi2=25,
c3=25,
phi3=20,
c4=40,
phi4=15,
c5=60,
phi5=10,
gamma_dry= 18,
gamma_sat= 20,
tension_cutoff= True,
sigma_t=0,
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
reducible_strength='yes',
)
model2d.set_solid(shapes=Face,material=MMCMaterial)
```
