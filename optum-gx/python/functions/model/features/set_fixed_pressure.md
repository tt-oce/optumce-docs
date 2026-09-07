# set_fixed_pressure

Set fixed pressure boundary condition.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D, 'face' in 3D.</dd>
<dt>pressure : float</dt>
<dd>Pressure in kPa.</dd>
<dt>minus_plus : str</dt>
<dd>Side of the boundary the condition acts on: 'minus' (default) or 'plus'.</dd>
<dt>variation : str</dt>
<dd>Pressure variation over the shape: 'constant' or 'linear' (default).</dd>
<dt>p1 : float</dt>
<dd>Linear variation value in kPa at anchor point 1.</dd>
<dt>p2 : float</dt>
<dd>Linear variation value in kPa at anchor point 2.</dd>
<dt>p3 : float</dt>
<dd>Linear variation value in kPa at anchor point 3 (3D only).</dd>
<dt>p1_location : list[float]</dt>
<dd>Anchor point 1.</dd>
<dt>p2_location : list[float]</dt>
<dd>Anchor point 2.</dd>
<dt>p3_location : list[float]</dt>
<dd>Anchor point 3 (3D only).</dd>
</dl>

## Examples

```python
sel = model.select([1,5], types='edge')
model.set_fixed_pressure(sel, pressure=100)
model.set_fixed_pressure(sel, pressure=100, minus_plus='plus')
model.set_fixed_pressure(sel, variation='linear', p1=50, p2=100,
    p1_location=[0,0,0], p2_location=[0,5,0])
```
