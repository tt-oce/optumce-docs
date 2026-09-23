# Geogrids

Geogrid reinforcement assigned to an edge (2D) or face (3D).

## Examples

```python
feature = model.get_geogrid(shapes)
feature.material_id
```

## Properties

<dl>
<dt>material_id : str</dt>
<dt>strength_reduction_factor : float</dt>
<dt>tension_cutoff : bool</dt>
<dt>compression_cutoff : bool</dt>
<dt>interface_minus : _InterfaceSide</dt>
<dd>Interface minus side properties (material, strength_reduction_factor, tension_cutoff, compression_cutoff, fc, normal).</dd>
<dt>interface_plus : _InterfaceSide</dt>
<dd>Interface plus side properties (material, strength_reduction_factor, tension_cutoff, compression_cutoff, fc, normal).</dd>
</dl>
