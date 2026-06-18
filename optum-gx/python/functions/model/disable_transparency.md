# disable_transparency

Disable transparency on shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>Shapes to make opaque.</dd>
</dl>

## See also

- [enable_transparency](/python/functions/model/enable_transparency)
- [disable_global_transparency](/python/functions/model/disable_global_transparency)

## Examples

```python
model.add_rectangle([0.0, 0.0], [10.0, 10.0])
shapes = model.select([10.0, 10.0], types='face')
model.enable_transparency(shapes)
model.disable_transparency(shapes)
```
