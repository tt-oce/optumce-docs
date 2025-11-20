# NGIADP

Define a NGI-ADP material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(129,114,132)</dd>
<dt>s_uA : float</dt>
<dd>Active undrained shear strength.</dd>
<dt>ratio_su_PA : float</dt>
<dd>Ratio of passive undrained shear strength over active undrained shear strength.</dd>
<dt>ratio_su_DSSA : float</dt>
<dd>Ratio of direct simple shear strength over active undrained shear strength.</dd>
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
i = 10
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
NGIADPMaterial = prj.NGIADP(name='NGIADP',
color=rgb(129,114,132),
s_uA=30,
ratio_su_PA=0.25,
ratio_su_DSSA=5,
tension_cutoff='yes',
sigma_t=0,
gamma_dry=18,
gamma_sat=20,
K0=0.58,
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
model2d.set_solid(shapes=Face,material=NGIADPMaterial)
```
