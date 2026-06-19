# set_support

Set support conditions to shapes.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D and 'face' in 3D.</dd>
<dt>type : str</dt>
<dd>Support type. type = 'normal', 'tangential', 'full'.</dd>
<dt>is_local : bool</dt>
<dd>If True, displacement directions are in local face coordinates.</dd>
</dl>

## Examples

```python
sel = model.select([0,1], types='edge')
model.set_support(sel, type='full')
```
