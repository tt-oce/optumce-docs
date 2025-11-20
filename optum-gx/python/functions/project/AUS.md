# AUS

Define an AUS material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= Color(r=139,g=131,b=166)</dd>
<dt>Eu : float</dt>
<dd>Undrained Young's modulus, in MPa.</dd>
<dt>ec50 : float</dt>
<dd>Axial strain halfway to failure in compression.</dd>
<dt>ee50 : float</dt>
<dd>Axial strain halfway to failure in extension.</dd>
<dt>suc : float</dt>
<dd>Undrained shear strength in compression.</dd>
<dt>sue : float</dt>
<dd>Undrained shear strength in extension.</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3</dd>
<dt>tension_cutoff : str</dt>
<dd>Apply tension cutoff. tension_cutoff = 'yes' or 'no'</dd>
<dt>sigma_t : str</dt>
<dd>Tensile cutoff stress, in kPa.</dd>
<dt>softening : str</dt>
<dd>Apply softening. softening = 'yes' or 'no'</dd>
<dt>suc_residual : float</dt>
<dd>Residual undrained shear strength in compression, in kPa.</dd>
<dt>e_suc_cr1 : float</dt>
<dd>Critical plastic strain at undrained shear peak strength in compression.</dd>
<dt>e_suc_cr2 : float</dt>
<dd>Critical plastic strain at undrained shear residual strength in compression.</dd>
<dt>sue_residual : float</dt>
<dd>Residual undrained shear strength in extension, in kPa.</dd>
<dt>e_sue_cr1 : float</dt>
<dd>Critical plastic strain at undrained shear peak strength in extension.</dd>
<dt>e_sue_cr2 : float</dt>
<dd>Critical plastic strain at undrained shear residual strength in compression.</dd>
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
i = 6
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
AUSMaterial = prj.AUS(name='AUSMaterial',
color=Color(r=187,g=132,b=78),
Eu=30,
ec50=0.005,
ee50=0.02,
suc=30,
sue=18,
tension_cutoff='no',
sigma_t=0,
softening='yes',
suc_residual= 25,
e_suc_cr1=0.01,
e_suc_cr2=0.012,
sue_residual=15,
e_sue_cr1=0.04,
e_sue_cr2=0.05,
gamma_dry=18,
gamma_sat=20,
K0=0.58,
sigma_0= 0,
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
model2d.set_solid(shapes=Face,material=AUSMaterial)
```

