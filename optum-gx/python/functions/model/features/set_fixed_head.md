# set_fixed_head

Set fixed head boundary condition.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D, 'face' in 3D.</dd>
<dt>head : float</dt>
<dd>Head in m.</dd>
<dt>minus_plus : str</dt>
<dd>Side of the boundary the condition acts on: 'minus' (default) or 'plus'.</dd>
</dl>

## Examples

```python
sel = model.select([0,5], types='edge')
model.set_fixed_head(sel, head=10)
model.set_fixed_head(sel, head=10, minus_plus='plus')
```
