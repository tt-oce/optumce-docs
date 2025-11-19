# toggle_features

Toggle features for stage

## Parameters

<dl>
<dt>features : Features</dt>
<dd>List of features to toggle.</dd>
<dt>value : str</dt>
<dd>Toggle on or off. toggle_features = 'on' or 'off'</dd>
</dl>

## See also

*   [remove_features](/optum-gx/python/functions/stage/remove_features/)

## Examples

```py
model2d.add_line([0,0],[0,5])
sel = model2d.select(point1=[0,1],types=edge)
model2d.set_water_table(sel)
feat = model2d.get_features(sel)
stage1.toggle_features(features=feat,value='off')
stage1.toggle_features(features=feat,value='on')
```

