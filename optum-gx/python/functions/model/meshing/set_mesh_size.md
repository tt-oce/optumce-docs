# set_mesh_size

Set mesh size to shape.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to set mesh size on.</dd>
<dt>mesh_size : float</dt>
<dd>Maximum mesh size.</dd>
</dl>

## Examples

```python
f = model.select([5,9], types='face')
model.set_mesh_size(shapes=f, mesh_size=0.1)
```
