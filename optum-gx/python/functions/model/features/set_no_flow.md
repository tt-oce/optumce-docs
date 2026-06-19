# set_no_flow

Set shape to disallow flow.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D, 'face' in 3D.</dd>
</dl>

## Examples

```python
sel = model.select([1,5], types='edge')
model.set_no_flow(sel)
```
