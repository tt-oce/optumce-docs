# set_resultpoint

Set points to record results.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes. ShapeType must be 'vertex'</dd>
</dl>

## Examples

```python
model2d.add_polygon(points=[[0,0],[15,0],[15,5],[8,5],[11,5],[0,5]])
sel = model2d.get_vertices(points=[[8,5],[11,5]])
model2d.set_resultpoint(sel)
```