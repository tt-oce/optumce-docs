# set_support

Set support conditions to shapes

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'edge' in 2D and 'face' in 3D</dd>
<dt>type : str</dt>
<dd>Type of support. type='normal', 'tangential', 'full'</dd>
</dl>

## See also

- [set_standard_fixities](/python/functions/model/set_standard_fixities)
- [set_plate_bc](/python/functions/model/set_plate_bc)
- [set_point_bc](/python/functions/model/set_point_bc)

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
sel = model2d.select([0,1],types='edge')
model2d.set_support(sel,type='normal')
sel = model2d.select([1,0],types='edge')
model2d.set_support(sel,type='tangential')
sel = model2d.select([1,5],types='edge')
model2d.set_support(sel,type='full')
model3d.add_box([0,0,0],[5,5,5])
sel = model3d.select([3,0,1],types='face')
model3d.set_support(sel,type='full')
```
