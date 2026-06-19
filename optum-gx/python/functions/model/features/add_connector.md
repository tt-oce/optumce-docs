# add_connector

Add a connector between two points.

## Parameters

<dl>
<dt>p0 : list[float]</dt>
<dd>Start point [x, y] or [x, y, z].</dd>
<dt>p1 : list[float]</dt>
<dd>End point [x, y] or [x, y, z].</dd>
<dt>material : ConnectorMaterial</dt>
<dd>Connector material.</dd>
</dl>

## Examples

```python
model.add_connector(p0=[2,0], p1=[5,3], material=conn_mat)
```
