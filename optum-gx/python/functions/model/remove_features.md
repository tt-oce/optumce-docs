# remove_features

Remove features

## Parameters

<dl>
<dt>features : Feature|list[Feature]</dt>
<dd>Feature or list of features</dd>
</dl>

## See also

- [del_shapes](/python/functions/model/del_shapes)
- [delete_interior](/python/functions/model/delete_interior)
- [get_features](/python/functions/model/get_features)
- [remove]missing

## Examples

```python
model2d.add_rectangle([0,0],[10,10])
model2d.set_surface_load(shapes=sel,value=-10,direction='y',option='fixed')
sel = model2d.select([1,10],types='edge')
f=model2d.get_features(sel)
model2d.remove_features(f)
```

