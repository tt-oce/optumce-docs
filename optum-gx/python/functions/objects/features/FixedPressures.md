# FixedPressures

Prescribed pore pressure boundary condition -- fixes the
total pore pressure value at the selected shapes.

## Examples

```python
feature = model.get_fixed_pressure(shapes)
feature.pressure = 100.0
feature.minus_plus = 'plus'
```

## Properties

<dl>
<dt>pressure : float</dt>
<dt>minus_plus : str</dt>
<dd>Side of the boundary the condition acts on: 'minus' (default) or 'plus'.</dd>
</dl>
