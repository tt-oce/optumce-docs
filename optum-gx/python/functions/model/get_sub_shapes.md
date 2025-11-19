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

*   [faces](/optum-gx/python/functions/model/faces)
*   [edges](/optum-gx/python/functions/model/edges)
*   [get\_shapes](/optum-gx/python/functions/model/get_shapes)
*   [vertices](/optum-gx/python/functions/model/vertices)
*   [volumes](/optum-gx/python/functions/model/volumes)

## Examples

```python
model3d.add_prism(points=[[1,1,0],[2,1,0],[1,0,0]],height=3)
sel1=model3d.select([2,1,0],types='volume')
model3d.get_sub_shapes(shapes=sel1,sub_types=['face']).values
[face:id=19, face:id=15, face:id=18, face:id=16, face:id=17]
```