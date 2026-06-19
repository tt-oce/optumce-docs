# set_body_load

Add body load.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to apply the load to.</dd>
<dt>value : float | ParameterMap | Gradient</dt>
<dd>Load magnitude in kN/m^3.</dd>
</dl>

## Examples

```python
sel = model.select([3,3,0], types='volume')
model.set_body_load(shapes=sel, value=-10, direction='z', option='fixed')
```
