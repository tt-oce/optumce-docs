# extrude

Extrude a shape.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
<dt>vector : array</dt>
<dd>point to define vector from origo</dd>
</dl>

## See also

- [create_3d_from_2d_model](/python/functions/model/create_3d_from_2d_model)
- [revolve](/python/functions/model/revolve)
- [revolve_2d_to_3d](/python/functions/model/revolve_2d_to_3d)
- [scale](/python/functions/model/scale)

## Examples

```python
model2d.add_line([0,1],[0,3])                                           #Create line
a = model2d.select([0,0],[3,3],types=['edge'],option='green')           #Select line shapes
model2d.extrude(a,vector=[5,0])                                         #Extrude to face
model3d.add_line(p0=[2,0,0],p1=[2,0,3])                                 #Create line
a = model3d.select([0,0,0],[5,5,5],types=['edge'],option='green')       #Select line
model3d.extrude(a,vector=[2,0,0])                                       #Extrude to face
a = model3d.select([0,0,0],[5,5,5],types=['face'],option='green')       #Select face
model3d.extrude(a,vector=[5,3,0])                                                       #Extrude to volume
```
