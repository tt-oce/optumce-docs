# set_point_bc

Set point boundary condition.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'vertex'.</dd>
<dt>displacement_x : str | float</dt>
<dd>Displacement in x. 'free', 'fixed', or float value.</dd>
<dt>displacement_y : str | float</dt>
<dd>Displacement in y. 'free', 'fixed', or float value.</dd>
<dt>displacement_z : str | float</dt>
<dd>Displacement in z. 'free', 'fixed', or float value.</dd>
<dt>displacement_rotation_x : str | float</dt>
<dd>Rotational displacement in x. 'free', 'fixed', or float value.</dd>
<dt>displacement_rotation_y : str | float</dt>
<dd>Rotational displacement in y. 'free', 'fixed', or float value.</dd>
<dt>displacement_rotation_z : str | float</dt>
<dd>Rotational displacement in z. 'free', 'fixed', or float value.</dd>
<dt>coordinate_system : Csys | str</dt>
<dd>Coordinate system.</dd>
<dt>csys : Csys | str</dt>
<dd>Alias for coordinate_system (backward compat).</dd>
</dl>

## Examples

```python
sel = model.select([0,0,0], types='vertex')
model.set_point_bc(sel, displacement_x='fixed', displacement_y='fixed',
                   displacement_z='free', displacement_rotation_x='free',
                   displacement_rotation_y='fixed', displacement_rotation_z='free')
```
