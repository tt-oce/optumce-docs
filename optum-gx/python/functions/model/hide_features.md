# hide_features

Hide the visual of features.

Only the drawing is affected: the shapes the features sit on stay
visible and the features keep their effect in the analysis. Visibility
is model-wide, so it applies to every stage of the model.

## Parameters

<dl>
<dt>features : Feature | list[Feature] | None</dt>
<dd>Features to hide.</dd>
</dl>

## Raises

<dl>
<dt>TypeError</dt>
<dd>If features is not a Feature or a list/tuple of Features (e.g. a Shape or ShapeList). None is accepted and does nothing.</dd>
</dl>

## See also

- [unhide_features](/python/functions/model/unhide_features)
- [unhide_all_features](/python/functions/model/unhide_all_features)
- [Feature.hidden](/python/functions/model/Feature.hidden)

## Examples

```python
load = model.get_surface_load(model.select([2, 4], types='edge'))
model.hide_features(load)
load.hidden
True
```
