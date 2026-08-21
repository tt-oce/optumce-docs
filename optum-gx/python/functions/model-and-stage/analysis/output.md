# output

Analysis output (results). Output always contains global_results and critical_results. These contain the often used results e.g. load_multiplier, consolidation_degree, u_norm_max etc.
Based on the present model all the output may be accessed through the objects, which is one or more of: 
solid, plate, geogrid, connector, nailrow, pilerow, interface, 
control_resulpoint, solid_resultpoint, plate_resultpoint, geogrid_resultpoint, connector_resultpoint, nail_row_resultpoint, pile_row_resultpoint, fixed_end_anchor_resultpoint, interface_resultpoint,
point_reaction, line_reaction, face_reaction

## Parameters

<dl>
<dd>None</dd>
</dl>

## Examples

```python
stage_lower = model.create_stage('lower bound')
stage_lower.set_analysis_properties(
        analysis_type='load_multiplier'
        )
prj.run_analysis()
stage_lower.output.global_results.load_multiplier
stage.output.plate[2].results.final_forces.M_y
stage.output.line_reaction[0].topology.nodes
stage.output.critical_results.fixed_end_anchor_force_max
```
