# FixedHeads

Prescribed hydraulic head boundary condition -- fixes the head value
at the selected shapes.

## Examples

```python
feature = model.get_fixed_head(shapes)
feature.head = -2.0
feature.minus_plus = 'plus'
```

## Properties

<dl>
<dt>head : float</dt>
<dt>minus_plus : str</dt>
<dd>Side of the boundary the condition acts on: 'minus' (default) or 'plus'.</dd>
</dl>
