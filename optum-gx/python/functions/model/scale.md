# scale

Scale shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
<dt>base_point : array</dt>
<dt>Point : base_point = [x0,y0] in 2D, base_point = [x0,y0,z0] in 3D</dt>
<dt>value : float</dt>
<dd>Scaling factor</dd>
</dl>

## See also

- [extrude](/python/functions/model/extrude)
- [revolve](/python/functions/model/revolve)
- [rotate](/python/functions/model/rotate)

## Examples

```python
model2d.add_polygons([[[2,0],[5,0],[5,5],[3,5]]])                       #Add polygon
a = model2d.select([0,0],[3,3],types=['edge'],option='green')           #Select edges
model2d.scale(shapes=a,base_point=[2,0],value=2)                        #Scale edges
model3d.add_rectangle([0,0,0],[3,3,0])                                  #Add rectangle
a = model3d.select([0,0,0],[5,5,5],types=['face'],option='green')       #Select face
model3d.scale(shapes=a,base_point=[0,0,0],value=1/2)                    #Scale face
model3d.add_box([0,0,0],[-1,-1,1])                                      #Add box
a = model3d.select([0,0,0],[-2,-2,2],types=['volume'],option='blue')    #Select volume
model3d.scale(shapes=a,base_point=[0,0,0],value=3)                      #Scale volume
```
