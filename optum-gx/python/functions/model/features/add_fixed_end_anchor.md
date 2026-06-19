# add_fixed_end_anchor

Add fixed-end anchor at a point (without shape selection).

## Parameters

<dl>
<dt>point : list[float]</dt>
<dd>Anchor location [x, y] or [x, y, z].</dd>
<dt>length : float</dt>
<dd>Equivalent length.</dd>
<dt>angle : float</dt>
<dd>Inclination angle in 2D (degrees).</dd>
<dt>direction : list[float]</dt>
<dd>Anchor direction in 3D [x, y, z].</dd>
<dt>material : ConnectorMaterial</dt>
<dd>Connector material. None = default.</dd>
</dl>

## Examples

```python
model.add_fixed_end_anchor(point=[5,3], length=3, angle=-30)
```
