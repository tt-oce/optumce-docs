# toggle_features

Toggle features on/off.

This toggles between activated and deactivated status for features on
a stage.

## Parameters

<dl>
<dt>features : Feature | list[Feature] | None</dt>
<dd>Features to toggle.</dd>
<dt>value : bool | str</dt>
<dd>True/'on' to enable, False/'off' to disable.</dd>
</dl>

## Raises

<dl>
<dt>TypeError</dt>
<dd>If features is not a Feature or a list/tuple of Features (e.g. a Shape or ShapeList). None is accepted and does nothing.</dd>
</dl>
