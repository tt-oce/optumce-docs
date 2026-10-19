# Infiltrations

Prescribed infiltration boundary condition -- a uniform inflow normal
to the selected boundary shapes, entering the domain. The value is in
the feature's own unit (mm/day for SI projects, in/day for US).

## Examples

```python
feature = model.get_infiltration(shapes)
feature.infiltration = 25.0
```

## Properties

<dl>
<dt>infiltration : float</dt>
<dd>Flux per unit boundary area, positive into the domain, negative out of it.</dd>
</dl>
