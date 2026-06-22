# Connectors

Connector element linking two points.

## Examples

```python
feature = model.get_connector(shapes)
feature.material_id
feature.corrosion_loss = 0.10
```

## Properties

<dl>
<dt>p0 : List[float]</dt>
<dt>p1 : List[float]</dt>
<dt>material_id : str</dt>
<dt>corrosion_loss : float</dt>
<dd>Corrosion loss (mm).</dd>
</dl>

## Methods

### set_prestress()

Apply a prestress to this connector's edge.
