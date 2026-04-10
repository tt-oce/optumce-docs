# get_sub_shapes

Get subshapes in a model.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of shapes</dd>
<dt>sub_types : [Shapetype]</dt>
<dd>list of shapetypes. sub_types = ['face','edge','vertex']</dd>
</dl>

## See also

- [faces](/python/functions/model/faces)
- [edges](/python/functions/model/edges)
- [get_shapes](/python/functions/model/get_shapes)
- [vertices](/python/functions/model/vertices)
- [volumes](/python/functions/model/volumes)

## Examples

```python
model3d.add_prism(points=[[1,1,0],[2,1,0],[1,0,0]],height=3)
sel1=model3d.select([2,1,0],types='volume')
model3d.get_sub_shapes(shapes=sel1,sub_types=['face']).values
[face:id=19, face:id=15, face:id=18, face:id=16, face:id=17]
```
