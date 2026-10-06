# set_plate

Set shape material as plate.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to assign plate to.</dd>
<dt>material : Material</dt>
<dd>Plate material (RigidPlate, FlatPlateSteel, etc.).</dd>
<dt>roughness : float</dt>
<dd>Interface roughness (strength reduction factor) applied to both sides.</dd>
<dt>tension_cutoff : bool</dt>
<dd>Enable tension cutoff.</dd>
<dt>compression_cutoff : bool</dt>
<dd>Enable compression cutoff.</dd>
<dt>interface_material : Material | str</dt>
<dd>Interface material applied to both sides ('adjacent_solid', a material or None).</dd>
<dt>roughness_minus, roughness_plus : float</dt>
<dd>Per-side roughness overrides.</dd>
<dt>tension_cut_off_minus, tension_cut_off_plus : bool</dt>
<dd>Per-side tension cutoff overrides.</dd>
<dt>compression_cut_off_minus, compression_cut_off_plus : bool</dt>
<dd>Per-side compression cutoff overrides.</dd>
<dt>interface_material_minus, interface_material_plus : Material | str</dt>
<dd>Per-side interface material overrides.</dd>
<dt>strength_reduction_factor, strength_reduction_factor_minus, strength_reduction_factor_plus : float</dt>
<dd>Deprecated aliases for roughness, roughness_minus and roughness_plus.</dd>
</dl>

## Examples

```python
sel = model.select([0.5,0.5], types='edge')
model.set_plate(shapes=sel, material=plate_mat)
```
