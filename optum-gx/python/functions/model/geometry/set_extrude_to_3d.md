# set_extrude_to_3d

Set extrude-to-3D settings on shapes.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to assign extrusion settings to.</dd>
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

## Examples

```python
sel = model.select([2,4], types='edge')
model.set_extrude_to_3d(shapes=sel, depth_in=3, depth_out=7)
```
