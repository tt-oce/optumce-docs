# SixDofLoadings

Six-degree-of-freedom loading at a point -- combined force and moment
components (Fx, Fy, Fz, Mx, My, Mz) applied to the selected point(s).

## Examples

```python
feature = model.get_six_dof_load(shapes)
feature.Fx = 10.0
feature.Mz = 5.0

# Apply multiple changes in a single network call:

with feature.batch():
    feature.Fx = 10.0
    feature.Fy = 0.0
    feature.Fz = -20.0
    feature.Mx = 0.0
    feature.My = 0.0
    feature.Mz = 5.0
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
<dt>Fx : float</dt>
<dd>Force in X direction.</dd>
<dt>Fy : float</dt>
<dd>Force in Y direction.</dd>
<dt>Fz : float</dt>
<dd>Force in Z direction.</dd>
<dt>Mx : float</dt>
<dd>Moment about X axis.</dd>
<dt>My : float</dt>
<dd>Moment about Y axis.</dd>
<dt>Mz : float</dt>
<dd>Moment about Z axis.</dd>
</dl>
