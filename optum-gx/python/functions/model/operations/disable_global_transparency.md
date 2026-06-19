# disable_global_transparency

Disable transparency on all shapes.

## See also

- [enable_transparency](/python/functions/model/operations/enable_transparency)
- [disable_transparency](/python/functions/model/operations/disable_transparency)

## Examples

```python
model.add_rectangle([0.0, 0.0], [10.0, 10.0])
shapes = model.select([10.0, 10.0], types='face')
model.enable_transparency(shapes)
model.disable_global_transparency()
```
