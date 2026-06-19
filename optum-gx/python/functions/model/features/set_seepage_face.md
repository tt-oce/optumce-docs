# set_seepage_face

Set shape to allow seepage.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D, 'face' in 3D.</dd>
</dl>

## Examples

```python
sel = model.select([1,5], types='edge')
model.set_seepage_face(sel)
```
