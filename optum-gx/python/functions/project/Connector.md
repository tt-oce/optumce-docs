# Connector

Define a Connector material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color= rgb(29,163,30)</dd>
<dt>yield_force : float</dt>
<dd>Yield force, in kN.</dd>
<dt>EA : float</dt>
<dd>Normal stifness, in kN.</dd>
<dt>spacing : float</dt>
<dd>Spacing, in m.</dd>
<dt>reducible_strength : str</dt>
<dd>Apply reducible strength. reducible_strength = 'yes' or 'no'</dd>
</dl>

## Examples

```python
i = 19
model2d.add_rectangle([i,0],[i+1,2])
Face = model2d.select(p0=[i+0.5,1],types='face')
ConnectorMaterial = prj.Connector(name='ConnectorMaterial',
color=rgb(29,163,30),
yield_force=300,
EA=200000,
spacing= 2,
reducible_strength='yes',
)
model2d.set_solid(shapes=Face,material=ConnectorMaterial)
```
