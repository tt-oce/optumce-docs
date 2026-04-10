# set_fixedendanchor

Set fixed-end anchor from vertex.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes. ShapeType must be 'vertex'</dd>
<dt>length : float</dt>
<dd>Equivalent length</dd>
<dt>angle : float</dt>
<dd>Inclination angle in 2D in degrees</dd>
<dt>direction : array</dt>
<dd>Anchor direction in 3D</dd>
<dt>material : str</dt>
<dd>Material. None = connector</dd>
</dl>

## See also

- [set_nailrow](/python/functions/model/set_nailrow)

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
sel = model2d.select([5,5],types='vertex')
model2d.set_fixedendanchor(shapes=sel,length=3, angle=-30)
model3d.add_box([0,0,0],[1,1,3])
sel = model3d.select([1,1,3],types='vertex')
model3d.set_fixedendanchor(shapes=sel,length=3, direction=[0,0,1])
```
