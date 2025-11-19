# get_shapes_by_vertices

Get shapes bounded by vertices.

## Parameters

<dl>
<dt>shapeType : ShapeType</dt>
<dd>One of the following shapes: 'vertex','edge', 'face', 'volume'</dd>
<dt>vertices : ShapeList</dt>
<dd>ShapeList of vertex points</dd>
</dl>

## See also

*   [get_shapes](/optum-gx/python/functions/model/get_shapes/)
*   [select](/optum-gx/python/functions/model/select/)

## Examples

```py
model2d.add_rectangle([0,0],[2,2])                                      #Add rectangle
v = model2d.get_shapes(types=['vertex'])                                #Get all vertex
f = model2d.get_shapes_by_vertices(shapeType='face',vertices=v)         #Get face bounded by vertices
f.values                                                                #Output values
[face:id=8]
model3d.add_prism(points=[[-1,-1,0],[-3,-3,0],[-3,0,0]],height=3)       #Add prism
v  = model3d.select([-1,-1,0],[-2,-2,3],types=['vertex'],option='blue') #Select two vertex
e = model3d.get_shapes_by_vertices(shapeType='edge',vertices=v)         #Get edge bounded by vertex
e.values                                                                #Output values
[edge:id=13]
```