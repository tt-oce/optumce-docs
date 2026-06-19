# set_plate

Set shape material as plate.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to assign plate to.</dd>
<dt>material : Material</dt>
<dd>Plate material (RigidPlate, FlatPlateSteel, etc.).</dd>
<dt>strength_reduction_factor : float</dt>
<dd>Strength reduction factor.</dd>
<dt>tension_cutoff : bool</dt>
<dd>Enable tension cutoff.</dd>
<dt>compression_cutoff : bool</dt>
<dd>Enable compression cutoff.</dd>
</dl>

## Examples

```python
sel = model.select([0.5,0.5], types='edge')
model.set_plate(shapes=sel, material=plate_mat)
```
