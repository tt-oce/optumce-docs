# FixedPressures

Prescribed pore pressure boundary condition -- fixes the
total pore pressure value at the selected shapes. Supports
constant or linearly-varying distributions.

## Examples

```python
feature = model.get_fixed_pressure(shapes)
feature.pressure = 100.0
feature.minus_plus = 'plus'

# Linear variation defined by values at anchor points:

feature.variation = 'linear'
feature.p1 = 50.0
feature.p2 = 100.0
feature.p1_location = [0, 0, 0]
feature.p2_location = [0, 5, 0]
```

## Properties

<dl>
<dt>pressure : float</dt>
<dd>Pressure value: the constant value ('constant' variation) or p1 ('linear' variation).</dd>
<dt>minus_plus : str</dt>
<dd>Side of the boundary the condition acts on: 'minus' (default) or 'plus'.</dd>
<dt>variation : str</dt>
<dd>Pressure variation over the shape: 'constant' or 'linear' (default).</dd>
<dt>p1 : float</dt>
<dd>Linear variation value at anchor point 1.</dd>
<dt>p2 : float</dt>
<dd>Linear variation value at anchor point 2.</dd>
<dt>p3 : float</dt>
<dd>Linear variation value at anchor point 3 (3D only).</dd>
<dt>p1_location : object</dt>
<dd>Anchor point 1.</dd>
<dt>p2_location : object</dt>
<dd>Anchor point 2.</dd>
<dt>p3_location : object</dt>
<dd>Anchor point 3 (3D only).</dd>
</dl>
