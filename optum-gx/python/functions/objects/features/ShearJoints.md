# ShearJoints

Shear joint / interface element between two solid domains -- typically
used to model reduced-strength contact surfaces such as soil-structure
interfaces.

## Examples

```python
feature = model.get_interface(shapes)
feature.material = 'MC Basic'
feature.strength_reduction_factor = 0.8
feature.tension_cutoff = False
```

## Properties

<dl>
<dt>material_id : str</dt>
<dt>material</dt>
<dd>Interface material (UUID string). Accepts a name, a material object or a UUID.</dd>
</dl>
