# Water

Water material -- assigned to fluid regions to represent free water
(e.g. lakes, reservoirs, fluid-filled cavities).

## Examples

```python
material = project.Water(name='Water', gamma=9.81)
material.gamma
```

## Properties

<dl>
<dt>name : str</dt>
<dd>Material name.</dd>
<dt>color : Color</dt>
<dd>Material color.</dd>
<dt>K : float | ParameterMap | Profile | Gradient</dt>
<dd>Bulk modulus of water.</dd>
<dt>gamma : float | ParameterMap | Profile | Gradient</dt>
<dd>Unit weight of water.</dd>
</dl>
