# SurfaceLoads

Surface load applied to a face -- distributed pressure on
the selected face(s). Supports constant or linearly-varying
distributions.

## Examples

```python
feature = model.get_surface_load(shapes)
feature.load_direction = 'z'
feature.load_type = 'unfavourable'
feature.value = 10.0

# Apply multiple changes in a single network call:

with feature.batch():
    feature.load_direction = 'z'
    feature.load_type = 'unfavourable'
    feature.value = 10.0
```

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
<dd>Surface load value.</dd>
<dt>value : float | Profile | Gradient</dt>
<dd>Alias for p.</dd>
<dt>p1 : float | Profile | Gradient</dt>
<dd>Linear variation endpoint 1.</dd>
<dt>p2 : float | Profile | Gradient</dt>
<dd>Linear variation endpoint 2.</dd>
<dt>p3 : float | Profile | Gradient</dt>
<dd>Linear variation endpoint 3.</dd>
<dt>p1_location : object</dt>
<dd>Anchor point 1.</dd>
<dt>p2_location : object</dt>
<dd>Anchor point 2.</dd>
<dt>p3_location : object</dt>
<dd>Anchor point 3.</dd>
</dl>
