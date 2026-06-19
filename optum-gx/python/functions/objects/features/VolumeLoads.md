# VolumeLoads

Volume (body) load feature with remote API synchronization via IFeature.

Usage:
    feature = model.get_volume_load(shapes)
    feature.direction = 'z'
    feature.value = -20.0

Batch updates:
    with feature.batch():
        feature.direction = 'z'
        feature.value = -20.0

## Properties

<dl>
<dt>option : int</dt>
<dd>Load option (fixed/multiplier).</dd>
<dt>load_direction : int</dt>
<dd>Load direction (x/y/z).</dd>
<dt>coordinate : int</dt>
<dd>Coordinate system type.</dd>
<dt>coordinate_system : str</dt>
<dd>Coordinate system (local/global_2d/global_3d or csys UUID).</dd>
<dt>load_category : int</dt>
<dd>Load category.</dd>
<dt>load_type : int</dt>
<dd>Load type (unfavourable/favourable).</dd>
<dt>load_variation : int</dt>
<dd>Load variation (constant/linear).</dd>
<dt>p : float | Profile | Gradient</dt>
<dd>Volume load value (unit weight).</dd>
<dt>value : float | Profile | Gradient</dt>
<dd>Alias for p.</dd>
</dl>
