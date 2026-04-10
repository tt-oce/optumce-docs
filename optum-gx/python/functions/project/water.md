# Water

Define Water material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(59,172,195)</dd>
<dt>K : float</dt>
<dd>Bulk Modulus of water, in MPa.</dd>
<dt>gamma : float</dt>
<dd>Unit Weight, in kN/m^3.</dd>
</dl>

## Examples

```python
i = 13
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
WaterMaterial = prj.Water(name='WaterMaterial',
color=rgb(59,172,195),
K=2200,
gamma=9.8,
)
model2d.set_solid(shapes=Face,material=WaterMaterial)
```
