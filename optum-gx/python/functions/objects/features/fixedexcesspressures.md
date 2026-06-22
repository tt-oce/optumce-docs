# FixedExcessPressures

Prescribed excess pore pressure boundary condition -- fixes the
excess pressure above the steady-state value at the selected shapes.

## Examples

```python
feature = model.get_fixed_excess_pressure(shapes)
feature.pressure = 50.0
```

## Properties

<dl>
<dt>pressure : float</dt>
</dl>
