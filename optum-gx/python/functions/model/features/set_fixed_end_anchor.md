# set_fixed_end_anchor

Set fixed-end anchor from vertex.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'vertex'.</dd>
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
sel = model.select([5,5], types='vertex')
model.set_fixed_end_anchor(shapes=sel, length=3, angle=-30)
```
