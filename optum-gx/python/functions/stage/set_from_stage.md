# set_from_stage

Set stage from another stage in the same model.

## Parameters

<dl>
<dt>from_stage : str|Stage</dt>
<dd>Stage origin.</dd>
</dl>

## See also

- [set_from_model](/python/functions/model/set_from_model/)

## Examples

```py
stage1 = model2d.create_stage(name='stage 1')
stage2.set_from_stage(from_stage='stage 1')
stage2.set_from_stage(from_stage= stage1)
```

