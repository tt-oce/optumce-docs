# ExtrudeTo3dSettings

2D-to-3D extrusion settings attached to a 2D feature -- controls
extrusion depths, repetition, end-cap fills, and whether the resulting shape
is a face or a volume.

## Examples

```python
extrudeSettings = model.get_extrude_to_3d(shapes)
extrudeSettings.depth_in = 5.0
extrudeSettings.depth_out = 5.0
extrudeSettings.as_face = True
```

## Properties

<dl>
<dt>depth_in : float</dt>
<dd>Extrusion depth inward.</dd>
<dt>depth_out : float</dt>
<dd>Extrusion depth outward.</dd>
<dt>repetition : bool</dt>
<dd>Enable repetition.</dd>
<dt>repetition_spacing : float</dt>
<dd>Spacing between repetitions.</dd>
<dt>repetition_out : int</dt>
<dd>Number of repetitions outward.</dd>
<dt>repetition_in : int</dt>
<dd>Number of repetitions inward.</dd>
<dt>fill : bool</dt>
<dd>Enable fill.</dd>
<dt>fill_in : float</dt>
<dd>Fill depth inward.</dd>
<dt>fill_out : float</dt>
<dd>Fill depth outward.</dd>
<dt>as_face : bool</dt>
<dd>Treat as face.</dd>
</dl>
