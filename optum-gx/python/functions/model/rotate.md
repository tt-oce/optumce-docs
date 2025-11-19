# rotate

rotate shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
<dt>base_point : array</dt>
<dd>point to rotate around:   base_point = [x0,y0] in 2D, base_point = [x0,y0,z0] in 3D</dd>
<dt>angle : float</dt>
<dd>Rotation angle in degrees</dd>
<dt>direction : array, optional</dt>
<dd>Point defining direction, from origo, to rotate around in 3D</dd>
</dl>

## See also

*   [extrude](/optum-gx/python/functions/model/extrude)
*   [revolve](/optum-gx/python/functions/model/revolve)
*   [scale](/optum-gx/python/functions/model/scale)

## Examples

```python
model2d.add_polygons([[[2,0],[5,0],[5,5],[3,5]]])                       #Add polygon
a = model2d.select([0,0],[3,3],types=['face'],option='green')           #Select face
model2d.rotate(shapes=a,base_point=[2,0],angle=45)                      #Rotate polygon
model3d.add_rectangle([0,0,0],[3,3,0])                                  #Add rectangle
a = model3d.select([1,1,0],types=['face'])                              #Select face
model3d.rotate(shapes=a,base_point=[0,0,0],angle=45,direction=[1,0,0])  #Rotate face
model3d.add_prism(points=[[-1,-1,0],[-3,-3,0],[-3,0,0]],height=3)
a = model3d.select([-2,-2,1],types=['volume'])
model3d.rotate(shapes=a,base_point=[-3,-3,3],angle=90,direction=[1,1,0])
```