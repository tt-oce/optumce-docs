# Plates

Plate element assigned to an edge (2D) or face (3D).

## Examples

```python
feature = model.get_plate(shapes)
feature.material_id
feature.use_beam_coordinate_system = True
feature.strong_axis = [0, 1, 0]
```

## Properties

<dl>
<dt>material_id : str</dt>
<dt>use_beam_coordinate_system : bool</dt>
<dd>Use a custom beam coordinate system (3D beam plates only). Setting strong_axis enables this automatically.</dd>
<dt>strong_axis : List[float]</dt>
<dd>Strong axis (Y / J) of the beam coordinate system as [x, y, z]. Setting this enables ``use_beam_coordinate_system``.</dd>
<dt>interface_minus : _InterfaceSide</dt>
<dd>Interface minus side properties (material, strength_reduction_factor, tension_cutoff, compression_cutoff, fc, normal).</dd>
<dt>interface_plus : _InterfaceSide</dt>
<dd>Interface plus side properties (material, strength_reduction_factor, tension_cutoff, compression_cutoff, fc, normal).</dd>
<dt>coordinate_system : str</dt>
<dd>Beam internal coordinate system: ``'default'`` or ``'custom'`` (alias for use_beam_coordinate_system).</dd>
</dl>
