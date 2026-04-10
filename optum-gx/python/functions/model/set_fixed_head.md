# set_fixed_head

Set shape to fixed head.

## See also

- [set_fixed_excess_pressure](/python/functions/model/set_fixed_excess_pressure)
- [set_fixed_pressure](/python/functions/model/set_fixed_pressure)

## Examples

```python
model2d.add_rectangle([0,0],[5,5])
sel = model2d.select([0,5],types='edge')
model2d.set_fixed_head(sel,head=10)
model3d.add_box([0,0,0],[1,1,3])
sel = model3d.select([1,0.5,1],types='face')
model3d.set_fixed_head(sel,head=10)
```
