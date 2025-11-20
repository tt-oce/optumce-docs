# select

Select geometric objects by point or bounding box.

## Parameters

<dl>
<dd>Selection by point:</dd>
<dt>p0 : array</dt>
<dt>Point : p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dt>
<dt>types : str</dt>
<dd>One or more shape types:    types = ['vertex','edge', 'face', 'volume'] Selection by bounding box:</dd>
<dt>p0 : array</dt>
<dd>Starting point of bounding box: p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dd>
<dt>p1 : array</dt>
<dd>End point of bounding box:      p1 = [x1,y1] in 2D, p1 = [x1,y1,z1] in 3D</dd>
<dt>types : str</dt>
<dd>One or more shape types:        types = ['vertex','edge', 'face', 'volume']</dd>
<dt>option : str</dt>
<dd>Bounding box type:              option = 'blue' or 'green'</dd>
</dl>

## See also

- [edges](/python/functions/model/edges)
- [faces](/python/functions/model/faces)
- [vertices](/python/functions/model/vertices)
- [volumes](/python/functions/model/volumes)

## Notes

p0 and p1 define the bounding box and option defines bounding box type, where "blue" and "green" refer to exclusive and inclusive select respectively (refer to the colors of the bounding box for east/west selection in the GUI).

## Examples

```python
model2d.add_polygons([[[0,0],[2,0],[2,2]],[[2,0],[5,0],[5,5],[3,5]]])           #Add two polygons
model2d.select([2,2],types=['edge'])                                            #Select edges at point
model2d.select([2,2],types=['edge']).values                                     #List of edges at point
[edge:id=7, edge:id=8]
model2d.select([2,0],types=['vertex','edge', 'face']).values                    #List of vertex, edges and faces
[vertex:id=1, edge:id=6, edge:id=7, edge:id=9, edge:id=12, face:id=13, face:id=14]
model2d.select([0,0],[3,3],types=['edge'],option='blue').values                 #Exclusive bounding box edge list
[edge:id=6, edge:id=7, edge:id=8]
model2d.select([0,0],[3,3],types=['edge'],option='green').values                #Inclusive bounding box edge list
[edge:id=6, edge:id=7, edge:id=8, edge:id=9, edge:id=12]
sel = model2d.select([0,0],[10,10],ShapeType.vertex,SelectOption.green)              #Select all four vertices
model3d.add_box([0,0,0],[5,5,5])                                                #Add box
model3d.select([1,1,1],types=['vertex','edge', 'face', 'volume']).values        #List of every shape in point
[volume:id=26]
model3d.select([0,0,0],[3,3,3],types=['edge'],option='blue').values             #Exclusive bounding box edge list
[]
model3d.select([0,0,0],[3,3,3],types=['edge'],option='green').values            #Inclusive bounding box edge list
[edge:id=8, edge:id=11, edge:id=14]
```
