# set_water_table

Define water table at shape.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D, 'face' in 3D.</dd>
</dl>

## Examples

```python
sel = model.select([0,2], types='edge')
model.set_water_table(sel)
```
