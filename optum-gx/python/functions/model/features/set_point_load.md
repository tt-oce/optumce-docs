# set_point_load

Add point load.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to apply the load to.</dd>
<dt>value : float</dt>
<dd>Load magnitude in kN.</dd>
<dt>direction : str</dt>
<dd>Load direction. direction = 'x' or 'y' or 'z'.</dd>
<dt>option : str</dt>
<dd>Load option. option = 'fixed' or 'multiplier'.</dd>
<dt>p : float</dt>
<dd>Load magnitude; value is an alias and takes precedence when supplied.</dd>
<dt>csys : Csys</dt>
<dd>Coordinate system; coordinate_system is an alias and takes precedence when supplied.</dd>
</dl>

## Examples

```python
sel = model.select([3,3,0], types='vertex')
model.set_point_load(shapes=sel, value=-10, direction='z', option='fixed')
```
