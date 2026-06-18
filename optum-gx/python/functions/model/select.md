# select

Select geometric objects by point or bounding box.

## Parameters

<dl>
<dd>Selection by point:</dd>
<dt>p0 : array</dt>
<dt>Point : p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dt>
<dt>types : str | list[str]</dt>
<dd>One or more shape types:    types = 'edge' or ['vertex','edge', 'face', 'volume'] Selection by bounding box:</dd>
<dt>p0 : array</dt>
<dd>Starting point of bounding box: p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dd>
<dt>p1 : array</dt>
<dd>End point of bounding box:      p1 = [x1,y1] in 2D, p1 = [x1,y1,z1] in 3D</dd>
<dt>types : str | list[str]</dt>
<dd>One or more shape types:        types = ['vertex','edge', 'face', 'volume']</dd>
<dt>option : str</dt>
<dd>Bounding box type:              option = 'blue' or 'green' Multi-point selection (same type):</dd>
<dt>p0 : list[array]</dt>
<dd>List of points: p0 = [[x0,y0], [x1,y1], ...]</dd>
<dt>types : str</dt>
<dd>Shape type for all points:      types = 'face' Multi-point selection (mixed types):</dd>
<dt>p0 : list[list[array]]</dt>
<dd>Points grouped by type: p0 = [vertex_points, edge_points, ...] Each group is a list of points for the corresponding type.</dd>
<dt>types : list[str]</dt>
<dd>Shape types matching groups:    types = ['vertex', 'edge']</dd>
</dl>

## See also

- [edges](/python/functions/model/edges)
- [faces](/python/functions/model/faces)
- [vertices](/python/functions/model/vertices)
- [volumes](/python/functions/model/volumes)

## Notes

p0 and p1 define the bounding box and option defines bounding box type,
where "blue" and "green" refer to exclusive and inclusive select respectively
(refer to the colors of the bounding box for east/west selection in the GUI).

## Examples

```python
model2d.select([2,2], types='edge')                                             #Select edges at point
model2d.select([0,0], [3,3], types=['edge'], option='blue')                     #Bounding box select
model2d.select([[1,1], [3,3]], types='face')                                    #Multi-point, same type
model2d.select([                                                                #Multi-point, mixed types
    [[0,1], [2,3]],                                                             #  edges at these points
    [[0,0], [2,2]]                                                              #  vertices at these points
], types=['edge', 'vertex'])
model3d.select([1,1,1],types=['vertex','edge', 'face', 'volume'])               #List of every shape in point
model3d.select([0,0,0],[3,3,3],types=['edge'],option='blue')                    #Exclusive bounding box edge list
model3d.select([0,0,0],[3,3,3],types=['edge'],option='green')                   #Inclusive bounding box edge list
```
