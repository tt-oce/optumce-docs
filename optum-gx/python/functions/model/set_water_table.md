# set_water_table

Define watertable at shape.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'edge' in 2D and 'face' in 3D</dd>
</dl>

## See also

- [set_fixed_excess_pressure](/python/functions/model/set_fixed_excess_pressure)
- [set_fixed_head](/python/functions/model/set_fixed_head)
- [set_fixed_pressure](/python/functions/model/set_fixed_pressure)

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
model2d.set_water_table(model2d.select([0,2],types='edge'))
model3d.add_box([0,0,0],[1,1,3])
sel1 = model3d.select([0.5,0.5,3],types='face')
model3d.set_water_table(sel1)
```
