# set_geogrid

Set shape as geogrid

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
<dt>material : material</dt>
<dd>Geogrid material</dd>
<dt>strength_reduction_factor : float</dt>
<dd>Strength reduction factor.</dd>
<dt>tension_cutoff : boolean</dt>
<dd>Tension cutoff. tension_cutoff = True or False</dd>
<dt>compression_cutoff : boolean</dt>
<dd>Compression cutoff. compression_cutoff = True or False</dd>
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