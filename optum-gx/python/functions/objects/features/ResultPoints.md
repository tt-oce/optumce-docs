# ResultPoints

Result point used for tracking output at a
specific location during analysis. Set ``is_control`` to mark the point
as the control point in a load-deformation analysis. ``name`` and
``index`` come from Feature: the name is unique within a model (a
clashing name gets a numeric suffix) and the index is assigned by the
model and cannot be changed from a script.

## Examples

```python
feature = model.get_result_point(shapes)
feature.is_control = True
feature.name = 'Crest'
print(feature.index)
```

## Properties

<dl>
<dt>is_control : bool</dt>
</dl>
