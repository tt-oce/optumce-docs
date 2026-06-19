# enable_transparency

Enable transparency on shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>Shapes to make transparent.</dd>
</dl>

## See also

- [disable_transparency](/python/functions/model/operations/disable_transparency)
- [disable_global_transparency](/python/functions/model/operations/disable_global_transparency)

## Examples

```python
model.add_rectangle([0.0, 0.0], [10.0, 10.0])
shapes = model.select([10.0, 10.0], types='face')
model.enable_transparency(shapes)
```
