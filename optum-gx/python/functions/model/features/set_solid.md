# set_solid

Set shape material as solid.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to assign material to.</dd>
<dt>material : Material</dt>
<dd>Solid material (MohrCoulomb, Tresca, Rigid, etc.).</dd>
</dl>

## Examples

```python
sel = model.select([1,1], types='face')
model.set_solid(shapes=sel, material=soil)
```
