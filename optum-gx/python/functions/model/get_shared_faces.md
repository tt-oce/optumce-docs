# get_shared_faces

Obtain the shared faces between two lists of shapes.

## Parameters

<dl>
<dt>shapeList0 : ShapeList</dt>
<dd>list of shapes</dd>
<dt>shapeList1 : ShapeList</dt>
<dd>list of shapes</dd>
</dl>

## See also

- [get_shared_edges](/python/functions/model/get_shared_edges)

## Examples

```py
model3d.add_prism(points=[[1,1,0],[2,1,0],[1,0,0]],height=3)
model3d.add_box([0,0,0],[1,1,3])
sel1 = model3d.select([2,1,0],types='volume')
sel2 = model3d.select([0.5,0.5,0.5],types='volume')
model3d.get_shared_faces(sel1,sel2).values
[face:id=16]
```
