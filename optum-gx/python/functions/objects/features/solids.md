# Solids

Solid material assignment on a face (2D) or volume (3D) of the model.

## Examples

```python
feature = model.get_solid(shapes)
feature.material_id
```

## Properties

<dl>
<dt>material_id : str</dt>
<dt>coordinate_system : _CoordinateSystem</dt>
<dd>Reinforcement coordinate system (origo, direction_i, direction_j, direction_k). Only meaningful for solids with a ReinforcedConcrete material.</dd>
</dl>
