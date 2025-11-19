# set_no_flow

Set shape to disallow flow

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes. ShapeType must be 'edge' in 2D and 'face' in 3D</dd>
</dl>

## See also

*   [set_fixed_pressure](/knowledge-base/gx/set_fixed_pressure)
*   [set_fixed_head](/knowledge-base/gx/set_fixed_head)
*   [set_fixed_excess_pressure](/knowledge-base/gx/set_fixed_excess_pressure)

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
sel = model2d.select([1,5],types='edge')
model2d.set_no_flow(sel)
model3d.add_box([0,0,0],[1,1,3])
sel = model3d.select([0.5,0,1],types='face')
model3d.set_no_flow(sel)
```