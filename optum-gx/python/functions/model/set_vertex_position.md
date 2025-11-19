# set_vertex_position

Set new postion of vertex.

## Parameters

<dl>
<dt>vertices : ShapeList</dt>
<dd>List of shapes</dd>
<dt>pos : array</dt>
<dd>Position of vertex</dd>
</dl>

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
sel = model2d.select([5,5],types='vertex')
model2d.set_vertex_position(vertices=sel,pos=[1,1,0])
```