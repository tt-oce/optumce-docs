# rectangular_array

Generate rectangular array of shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes Nx, Ny, Nz : int Number of copies in x, y, z directions dx, dy, dz : float Spacing in x, y, z directions</dd>
</dl>

## Examples

```python
model2d.add_rectangle([0,0],[2,2])
f = model2d.select([1,1], types='face')
model2d.rectangular_array(f, Nx=3, Ny=2, dx=4, dy=4)
```
