# get_shape_by_id

Get shape by id.

## Parameters

<dl>
<dt>id : int or List[int]</dt>
<dd>Shape id or list of shape ids</dd>
</dl>

## Returns

<dl>
<dt>Shape or ShapeList</dt>
<dd>Single shape if id is int, ShapeList if id is List[int]</dd>
</dl>

## See also

- [select](/python/functions/model/select)
- [get_shapes](/python/functions/model/get_shapes)

## Examples

```python
model2d.add_rectangle([0,0],[2,2])
model2d.get_shape_by_id(id=8)
face:id=8
model2d.get_shape_by_id(id=[8, 9, 10])
ShapeList with 3 shapes
```
