# set_interface

Define interface (shear joint).

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge' in 2D and 'face' in 3D.</dd>
<dt>material : Material</dt>
<dd>Interface material (MohrCoulomb or Tresca).</dd>
</dl>

## Examples

```python
sel = model.select([10,5], types='edge')
model.set_interface(shapes=sel, material=MC)
```
