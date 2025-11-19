# remove_features

Remove features

## Parameters

<dl>
<dt>features : Feature|list[Feature]</dt>
<dd>Feature or list of features</dd>
</dl>

## See also

*   [del_shapes](/optum-gx/python/functions/model/del_shapes)
*   [delete_interior](/optum-gx/python/functions/model/delete_interior)
*   [get_features](/optum-gx/python/functions/model/get_features)
*   [remove](/optum-gx/python/functions/model/remove)

## Examples

```python
model2d.add_rectangle([0,0],[10,10])
model2d.set_surface_load(shapes=sel,value=-10,direction='y',option='fixed')
sel = model2d.select([1,10],types='edge')
f=model2d.get_features(sel)
model2d.remove_features(f)
```