# set_prestress

Set prestress.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes. Must be 'edge'.</dd>
<dt>force : float</dt>
<dd>Prestressing force in kN.</dd>
</dl>

## Examples

```python
sel = model.select([0,3], types='edge')
model.set_prestress(shapes=sel, force=50)
```
