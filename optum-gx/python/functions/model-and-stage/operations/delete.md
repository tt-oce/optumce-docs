# delete

Delete model or stage.

## Parameters

<dl>
<dd>None</dd>
</dl>

## See also

- [delete_interior](/python/functions/model/geometry/delete_interior)
- [delete_shapes](/python/functions/model/geometry/delete_shapes)
- [delete_features](/python/functions/model-and-stage/delete_features)

## Examples

```python
model2d.delete()                            #Delete model
stage1 = model2d.create_stage('stage 1')    #Create stage
stage1.delete()                             #Delete stage
```
