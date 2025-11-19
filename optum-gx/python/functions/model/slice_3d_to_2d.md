# slice_3d_to_2d

Slide a 3D model to 2D.

## Parameters

<dl>
<dt>point1 : array</dt>
<dd>Starting point of basis vector: point1 = [x0,y0,z0] in 3D</dd>
<dt>point2 : array</dt>
<dd>End point of basis vector: point2 = [x0,y0,z0] in 3D</dd>
</dl>

## See also

*   [extrude](/optum-gx/python/functions/model/extrude)
*   [revolve_2d_to_3d](/optum-gx/python/functions/model/revolve_2d_to_3d)

## Examples

```python
model3d.slice_3d_to_2d([0,0,0],[1,0,0])
model3d.slice_3d_to_2d([2,0,0],[3,1,1])
```