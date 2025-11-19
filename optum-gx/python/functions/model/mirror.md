# mirror

Mirror shapes.

## Parameters

<dl>
<dt>point1 : array</dt>
<dd>Start point of vector defining mirroring axis. point1 = [x0,y0] in 2D, point1 = [x0,y0,z0] in 3D</dd>
<dt>point2 : array</dt>
<dd>End point of vector defining mirroring axis. point2 = [x0,y0] in 2D, point2 = [x0,y0,z0] in 3D</dd>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
</dl>

## See also

*   [move](/optum-gx/python/functions/model/move)
*   [rotate](/optum-gx/python/functions/model/rotate)

## Examples

```python
model2d.add_rectangle(p1=[0,0],p2=[1,2])                                #Add rectangle
f = model2d.select([0.5,1],types='face')                                #Select rectangle face
model2d.mirror(point1=[0,0], point2=[1,-1],shapes=f)                    #Mirror rectangle
model3d.add_prism(points=[[-1,-1,0],[-3,-3,0],[-3,0,0]],height=3)       #Add prism
v = model3d.select([0,0,0],[-3,-3,3],types=['volume'],option='blue')    #Select prism volume
model3d.mirror(point1=[0,0,0],point2=[0,0,1],shapes=v)                  #Mirror prism
```