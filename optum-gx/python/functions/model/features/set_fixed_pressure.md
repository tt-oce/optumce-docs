# set_fixed_pressure

Set fixed pressure boundary condition.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D, 'face' in 3D.</dd>
<dt>pressure : float</dt>
<dd>Pressure in kPa.</dd>
</dl>

## Examples

```python
sel = model.select([1,5], types='edge')
model.set_fixed_pressure(sel, pressure=100)
```
