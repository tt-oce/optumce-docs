# get_shapes

Get shapes in a model.

## Parameters

<dl>
<dt>types : list, optional</dt>
<dd>list of one or more ShapeType</dd>
</dl>

## See also

- [faces](/python/functions/model-and-stage/geometry/faces)
- [edges](/python/functions/model-and-stage/geometry/edges)
- [get_sub_shapes](/python/functions/model-and-stage/geometry/get_sub_shapes)
- [vertices](/python/functions/model-and-stage/geometry/vertices)
- [volumes](/python/functions/model-and-stage/geometry/volumes)

## Examples

```python
s = get_shapes()
s.values #display the list of shapes
vv = model3d.get_shapes(types=['vertex','volume'])
```
