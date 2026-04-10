# set_fixed_pressure

Set shape to fixed pressure.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'edge' in 2D and 'face' in 3D</dd>
<dt>pressure : float</dt>
<dd>Pressure in kPa</dd>
</dl>

## See also

- [set_fixed_excess_pressure](/python/functions/model/set_fixed_excess_pressure)
- [set_fixed_head](/python/functions/model/set_fixed_head)

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
sel = model2d.select([1,5],types='edge')
model2d.set_fixed_pressure(sel,pressure=100)
model3d.add_box([0,0,0],[1,1,3])
sel = model3d.select([0.5,0,1],types='face')
model3d.set_fixed_pressure(sel,pressure=10)
```
