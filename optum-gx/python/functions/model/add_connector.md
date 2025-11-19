# add_connector

add connector

## Parameters

<dl>
<dt>p0 : array</dt>
<dd>First point.        p0 = [x0,y0] in 2D, p0 = [x0,y0,z0] in 3D</dd>
<dt>p1 : array</dt>
<dd>Second point.       p1 = [x1,y1] in 2D, p1 = [x1,y1,z1] in 3D</dd>
<dt>material : Connector</dt>
<dd>Connector material</dd>
</dl>

## See also

*   [set_nailrow](/optum-gx/python/functions/model/set_nailrow)
*   [set_fixedendanchor](/optum-gx/python/functions/model/set_fixedendanchor)

## Examples

```python
ConnectorMaterial =prj.Connector(name='Connector1',
yield_force=300,
EA=210000,spacing=1,
color=Color(r=29,g=163,b=30),
)
model2d.add_connector(p0=[2,2],p1=[5,0],material=ConnectorMaterial)
model3d.add_connector(p0=[2,2,2],p1=[5,0,1],material=ConnectorMaterial)
```