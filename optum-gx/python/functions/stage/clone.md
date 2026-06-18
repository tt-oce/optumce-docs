# clone

Clones the selected model.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String nameing the clone.</dd>
</dl>

## Returns

<dl>
<dt>GX model identical to the selected</dt>
</dl>

## See also

- [set_current_model](/python/functions/project/set_current_model)
- [get_current_model](/python/functions/project/get_current_model)

## Examples

```python
model2d.clone()
model2d.clone("Cloned 2D model")
model3d.clone("Cloned 3D model")
```
