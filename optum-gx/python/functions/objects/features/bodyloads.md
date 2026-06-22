# BodyLoads

Body load applied throughout a solid region -- distributed
force per unit volume across the selected face (2D) or volume (3D).

## Examples

```python
feature = model.get_body_load(shapes)
feature.load_direction = 'z'
feature.value = -20.0

# Apply multiple changes in a single network call:
with feature.batch():
    feature.load_direction = 'z'
    feature.value = -20.0
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
<dd>Body load value (unit weight).</dd>
<dt>value : float | Profile | Gradient</dt>
<dd>Alias for p.</dd>
</dl>
