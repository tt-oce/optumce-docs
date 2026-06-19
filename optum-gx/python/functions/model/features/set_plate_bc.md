# set_plate_bc

Set plate boundary condition.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'vertex' in 2D and 'edge' in 3D.</dd>
<dt>displacement_x : str | float</dt>
<dd>Displacement in x. 'free', 'fixed', or float value.</dd>
<dt>displacement_y : str | float</dt>
<dd>Displacement in y. 'free', 'fixed', or float value.</dd>
<dt>displacement_z : str | float</dt>
<dd>Displacement in z. 'free', 'fixed', or float value.</dd>
<dt>displacement_rotation : str | float</dt>
<dd>Rotational displacement. 'free', 'fixed', or float value.</dd>
<dt>coordinate_system : Csys | str</dt>
<dd>Coordinate system.</dd>
<dt>csys : Csys | str</dt>
<dd>Alias for coordinate_system (backward compat).</dd>
</dl>

## Examples

```python
v = model.select([0,0], types='vertex')
model.set_plate_bc(v, displacement_x='fixed', displacement_y='fixed',
                   displacement_rotation='free')
```
