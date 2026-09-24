# StageResults

Results of one analysis step, grouped by element type.

Each property returns a ResultIndexer over the elements of that group.
StepOutput and StageOutput extend this class, so the groups are available on ``stage.output`` and on each
``stage.output.step[i]``.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
out = stage.output
out
out.plate[2].results.final_forces.M_y
out.line_reaction[0].topology.nodes
out.plate_resultpoint[0].results.displacements.total_displacements.u_x.value
```

## See also

- [StageOutput](/python/functions/objects/results/StageOutput)
- [StepOutput](/python/functions/objects/results/StepOutput)
- [ResultIndexer](/python/functions/objects/results/ResultIndexer)

## Properties

<dl>
<dt>solid : ResultIndexer | None</dt>
<dd>Solid elements (surfaces in 2D, volumes in 3D). None if the model has none.</dd>
<dt>plate : ResultIndexer | None</dt>
<dd>Plate elements. None if the model has none.</dd>
<dt>geogrid : ResultIndexer | None</dt>
<dd>Geogrid elements. None if the model has none.</dd>
<dt>connector : ResultIndexer | None</dt>
<dd>Connector elements. None if the model has none.</dd>
<dt>nailrow : ResultIndexer | None</dt>
<dd>Nail row elements. None if the model has none.</dd>
<dt>pilerow : ResultIndexer | None</dt>
<dd>Pile row elements. None if the model has none.</dd>
<dt>interface : ResultIndexer | None</dt>
<dd>Interface elements. None if the model has none.</dd>
<dt>control_resultpoint : ResultIndexer | None</dt>
<dd>Control result point. None if the model has none.</dd>
<dt>solid_resultpoint : ResultIndexer | None</dt>
<dd>Result points on solids. None if the model has none.</dd>
<dt>plate_resultpoint : ResultIndexer | None</dt>
<dd>Result points on plates. None if the model has none.</dd>
<dt>geogrid_resultpoint : ResultIndexer | None</dt>
<dd>Result points on geogrids. None if the model has none.</dd>
<dt>connector_resultpoint : ResultIndexer | None</dt>
<dd>Result points on connectors. None if the model has none.</dd>
<dt>nail_row_resultpoint : ResultIndexer | None</dt>
<dd>Result points on nail rows. None if the model has none.</dd>
<dt>pile_row_resultpoint : ResultIndexer | None</dt>
<dd>Result points on pile rows. None if the model has none.</dd>
<dt>fixed_end_anchor_resultpoint : ResultIndexer | None</dt>
<dd>Result points on fixed end anchors. None if the model has none.</dd>
<dt>interface_resultpoint : ResultIndexer | None</dt>
<dd>Result points on interfaces. None if the model has none.</dd>
<dt>point_reaction : ResultIndexer | None</dt>
<dd>Point reactions. None if the model has none.</dd>
<dt>line_reaction : ResultIndexer | None</dt>
<dd>Line reactions. None if the model has none.</dd>
<dt>face_reaction : ResultIndexer | None</dt>
<dd>Face reactions. None if the model has none.</dd>
</dl>
