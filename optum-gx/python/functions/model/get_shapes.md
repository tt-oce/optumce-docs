# get_shapes

Get shapes in a model.

## Parameters

<dl>
<dt>types : list, optional</dt>
<dd>list of one or more ShapeType</dd>
</dl>

## See also

- [faces](/python/functions/model/faces/)
- [edges](/python/functions/model/edges/)
- [get_sub_shapes](/python/functions/model/get_sub_shapes/)
- [vertices](/python/functions/model/vertices/)
- [volumes](/python/functions/model/volumes/)

## Examples

```py
s = get_shapes()
s.values #display the list of shapes
vv = model3d.get_shapes(types=['vertex','volume'])
```
