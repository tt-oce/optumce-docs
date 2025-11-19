# delete_interior

Delete shapes and leave voids in their place.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
</dl>

## See also

*   [select](/optum-gx/python/functions/model/select)
*   [del_shapes](/optum-gx/python/functions/model/del_shapes)

## Examples

```python
model2d.add_polygons([[[0,0],[2,0],[2,2]],[[2,0],[5,0],[5,5],[3,5]]])       #Add two polygons
f = model2d.select([1,1],[2,2],types=['face'],option='green')           #Select the face of first polygon
model2d.delete_interior(f)                                              #Delete the face
model2d.add_polygons([[[0,0],[2,0],[2,2]],[[2,0],[5,0],[5,5],[3,5]]])       #Add two polygons
v = model2d.select([2,2],types=['vertex'])                              #Select vertex
model2d.delete_interior(v)                                              #Delete vertex
model3d.add_box([0,0,0],[5,5,5])                                        #Add box
v = model3d.select([1,1,1],types=['volume'])                            #Select volume of box
model3d.delete_interior(v)                                                              #Delete box
```