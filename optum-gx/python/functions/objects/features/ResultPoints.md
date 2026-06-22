# ResultPoints

Result point used for tracking output at a
specific location during analysis. Set ``is_control`` to mark the point
as the control point in a load-deformation analysis.

## Examples

```python
feature = model.get_resultpoint(shapes)
feature.is_control = True
```

## Properties

<dl>
<dt>is_control : bool</dt>
</dl>
