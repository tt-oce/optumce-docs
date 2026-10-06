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
<dt>roughness : float</dt>
<dd>Interface roughness. Reads the minus side; setting it applies to both sides.</dd>
<dt>strength_reduction_factor : float</dt>
<dd>Deprecated alias for ``roughness``.</dd>
<dt>tension_cutoff : bool</dt>
<dt>compression_cutoff : bool</dt>
<dt>interface_minus : _InterfaceSide</dt>
<dd>Interface minus side properties (material, roughness, tension_cutoff, compression_cutoff, fc, normal).</dd>
<dt>interface_plus : _InterfaceSide</dt>
<dd>Interface plus side properties (material, roughness, tension_cutoff, compression_cutoff, fc, normal).</dd>
</dl>
