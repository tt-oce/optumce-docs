# revolve

Revolve shape around axis.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
<dt>axis_origo : array</dt>
<dd>point to define origo</dd>
<dt>axis_dir : array</dt>
<dd>point to define axis direction</dd>
<dt>angle : float</dt>
<dd>angle in degrees</dd>
<dt>N : int</dt>
<dd>Number of linearly spaced segments.</dd>
</dl>

## See also

*   [create_3d_from_2d_model](/optum-gx/python/functions/model/create_3d_from_2d_model)
*   [extrude](/optum-gx/python/functions/model/extrude)
*   [rotate](/optum-gx/python/functions/model/rotate)
*   [revolve_2d_to_3d](/optum-gx/python/functions/model/revolve_2d_to_3d)
*   [scale](/optum-gx/python/functions/model/scale)

## Examples

```python
model3d.add_rectangle([0,0,0],[3,3,0])                                      #Create rectangle
a = model3d.select([0,0,0],[5,5,5],types=['face'],option='green')           #Select shape
model3d.revolve(shapes=a,axis_origo=[0,0,0],axis_dir=[1,0,0],angle=90,N=12) #Revolve
```