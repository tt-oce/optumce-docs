# PointBcs

Boundary condition applied at a point -- fixes or releases the point's
displacement and rotation degrees of freedom.

## Examples

```python
feature = model.get_point_bc(shapes)
feature.displacement_x = 0
feature.displacement_y = 0
feature.displacement_z = 0
```

## Properties

<dl>
<dt>displacement_x : object</dt>
<dt>displacement_y : object</dt>
<dt>displacement_z : object</dt>
<dt>displacement_rotation_x : object</dt>
<dt>displacement_rotation_y : object</dt>
<dt>displacement_rotation_z : object</dt>
<dt>is_local_coord : bool</dt>
<dt>csys_id : str</dt>
</dl>
