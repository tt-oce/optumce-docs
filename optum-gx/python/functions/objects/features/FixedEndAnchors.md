# FixedEndAnchors

Fixed-end anchor connecting a point in the model to a fictitious fixed
support at the far end of the anchor.

## Examples

```python
feature = model.get_fixed_end_anchor(shapes)
feature.material_id
feature.length = 6.0
feature.inclination_angle = 30
feature.corrosion_loss = 0.10
```

## Properties

<dl>
<dt>length : float</dt>
<dt>inclination_angle : float</dt>
<dt>direction : List[float]</dt>
<dt>material_id : str</dt>
<dt>point : List[float]</dt>
<dt>corrosion_loss : float</dt>
<dd>Corrosion loss (mm).</dd>
</dl>

## Methods

### set_prestress()

Apply a prestress to this fixed-end anchor's vertex.
