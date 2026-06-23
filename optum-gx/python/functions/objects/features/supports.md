# Supports

Support boundary condition -- fixes displacement in specified
directions on the selected edges or faces.

## Examples

```python
feature = model.get_support(shapes)
feature.type = 'normal'
feature.is_local = False
```

## Properties

<dl>
<dt>type : str</dt>
<dd>Support type: 'full', 'normal', 'tangential'.</dd>
<dt>is_local : bool</dt>
<dd>Whether the support uses local coordinate system.</dd>
</dl>
