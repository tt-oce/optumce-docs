# get_shared_edges

Obtain the shared edges between two lists of shapes.

## Parameters

<dl>
<dt>shapeList0 : ShapeList</dt>
<dd>list of shapes</dd>
<dt>shapeList1 : ShapeList</dt>
<dd>list of shapes</dd>
</dl>

## See also

- [get_shared_faces](/python/functions/model/get_shared_faces)

## Examples

```python
model2d.add_rectangle([0,0],[1,1])
model2d.add_rectangle([1,0],[2,1])
sel1 = model2d.select([0,0],types='face')
sel2 = model2d.select([2,0],types='face')
model2d.get_shared_edges(sel1,sel2)
[edge:id=5]
model3d.add_prism(points=[[1,1,0],[2,1,0],[1,0,0]],height=3)
model3d.add_box([0,0,0],[1,1,3])
sel1 = model3d.select([2,1,0],types='volume')
sel2 = model3d.select([0.5,0.5,0.5],types='volume')
model3d.get_shared_edges(sel1,sel2).values
[edge:id=9, edge:id=12, edge:id=13, edge:id=14]
```
