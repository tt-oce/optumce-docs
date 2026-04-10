# Geogrid

Define a Geogrid material

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color=rgb(177,140,6)</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3</dd>
<dt>nu : float</dt>
<dd>Poisson's ratio.</dd>
<dt>permeable : str</dt>
<dd>Apply permability. permeable= 'yes' or 'no'</dd>
<dt>n_p : float</dt>
<dd>Yield force, in kN/m.</dd>
<dt>EA : float</dt>
<dd>Normal Stiffness, in kN/m.</dd>
</dl>

## Examples

```python
i = 23
model2d.add_rectangle([i,0],[i+1,2])
Edge = model2d.select(p0=[i,1],types='edge')
GeoGridMaterial = prj.Geogrid(name='Geogrid Material',
color=rgb(177,140,6),
gamma_dry= 17,
gamma_sat= 19,
nu = 0.3,
permeable= 'yes',
n_p = 45,
EA = 500)
model2d.set_geogrid(shapes=Edge,
material=GeoGridMaterial,
strength_reduction_factor=1,
tension_cutoff= False,
compression_cutoff= False)
```
