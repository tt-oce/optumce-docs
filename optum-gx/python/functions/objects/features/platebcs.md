# PlateBcs

Boundary condition applied to a plate -- fixes or releases the plate's
displacement and rotation degrees of freedom.

## Examples

```python
feature = model.get_plate_bc(shapes)
feature.displacement_x = 0
feature.displacement_y = 0
feature.displacement_rotation = 0
```

## Properties

<dl>
<dt>displacement_x : object</dt>
<dt>displacement_y : object</dt>
<dt>displacement_z : object</dt>
<dt>displacement_rotation : object</dt>
<dt>is_local_coord : bool</dt>
<dt>csys_id : str</dt>
</dl>
