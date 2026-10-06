# remove_features

Remove features by UUID or feature object.

## Parameters

<dl>
<dt>features : Feature | list[Feature] | None</dt>
<dd>Features to remove.</dd>
</dl>

## Raises

<dl>
<dt>TypeError</dt>
<dd>If features is not a Feature or a list/tuple of Features (e.g. a Shape or ShapeList). None is accepted and does nothing.</dd>
</dl>
