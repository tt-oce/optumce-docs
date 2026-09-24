# CriticalResults

Summary values of one analysis step: load multiplier, factor of safety
and the extreme (min/max) displacements, stresses and sectional forces.

The attributes are sent by OptumGX and depend on the analysis and the
model. ``repr()`` lists the ones present, and accessing one that was not
sent raises AttributeError. Values are floats, or lists of floats for
array-valued fields. The properties below are the common ones.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
cr = stage.output.critical_results
cr
cr.u_norm_max
u_norm_max = [step.critical_results.u_norm_max for step in stage.output.step]
```

## See also

- [StepOutput](/python/functions/objects/results/StepOutput)
- [Result](/python/functions/objects/results/Result)

## Properties

<dl>
<dt>load_multiplier : float</dt>
<dt>factor_of_safety : float</dt>
<dt>consolidation_degree : float</dt>
<dt>time_days : float</dt>
<dt>u_norm_max : float</dt>
<dt>u_x_max : float</dt>
<dt>u_y_max : float</dt>
<dt>u_z_max : float</dt>
<dt>u_result_point_norm : float</dt>
<dt>u_solid_norm_max : float</dt>
<dt>u_solid_x_max : float</dt>
<dt>u_solid_y_max : float</dt>
<dt>u_solid_z_max : float</dt>
<dt>u_solid_x_min : float</dt>
<dt>u_solid_y_min : float</dt>
<dt>u_solid_Z_min : float</dt>
<dt>du_solid_norm_max : float</dt>
<dt>du_solid_x_max : float</dt>
<dt>du_solid_y_max : float</dt>
<dt>du_solid_z_max : float</dt>
<dt>du_solid_x_min : float</dt>
<dt>du_solid_y_min : float</dt>
<dt>du_solid_z_min : float</dt>
<dt>sx_total_min : float</dt>
<dt>sy_total_min : float</dt>
<dt>sz_total_min : float</dt>
<dt>txy_total_min : float</dt>
<dt>tyz_total_min : float</dt>
<dt>tzx_total_min : float</dt>
<dt>sx_total_max : float</dt>
<dt>sy_total_max : float</dt>
<dt>sz_total_max : float</dt>
<dt>txy_total_max : float</dt>
<dt>tyz_total_max : float</dt>
<dt>tzx_total_max : float</dt>
<dt>sx_effective_min : float</dt>
<dt>sy_effective_min : float</dt>
<dt>sz_effective_min : float</dt>
<dt>txy_effective_min : float</dt>
<dt>tyz_effective_min : float</dt>
<dt>tzx_effective_min : float</dt>
<dt>sx_effective_max : float</dt>
<dt>sy_effective_max : float</dt>
<dt>sz_effective_max : float</dt>
<dt>txy_effective_max : float</dt>
<dt>tyz_effective_max : float</dt>
<dt>tzx_effective_max : float</dt>
<dt>u_plate_norm_max : float</dt>
<dt>u_plate_x_max : float</dt>
<dt>u_plate_y_max : float</dt>
<dt>u_plate_z_max : float</dt>
<dt>u_plate_x_min : float</dt>
<dt>u_plate_y_min : float</dt>
<dt>u_plate_Z_min : float</dt>
<dt>du_plate_norm_max : float</dt>
<dt>du_plate_x_max : float</dt>
<dt>du_plate_y_max : float</dt>
<dt>du_plate_z_max : float</dt>
<dt>du_plate_x_min : float</dt>
<dt>du_plate_y_min : float</dt>
<dt>connector_force_min : float</dt>
<dt>connector_force_max : float</dt>
<dt>fixed_end_anchor_force_min : float</dt>
<dt>fixed_end_anchor_force_max : float</dt>
<dt>moment_plate2d_min : float</dt>
<dt>moment_plate2d_max : float</dt>
<dt>normal_force_plate2d_min : float</dt>
<dt>normal_force_plate2d_max : float</dt>
<dt>shear_force_plate2d_min : float</dt>
<dt>shear_force_plate2d_max : float</dt>
<dt>mx_plate3d_min : float</dt>
<dt>mx_plate3d_max : float</dt>
<dt>my_plate3d_min : float</dt>
<dt>my_plate3d_max : float</dt>
<dt>mxy_plate3d_min : float</dt>
<dt>mxy_plate3d_max : float</dt>
<dt>sx_plate3d_min : float</dt>
<dt>sx_plate3d_max : float</dt>
<dt>sy_plate3d_min : float</dt>
<dt>sy_plate3d_max : float</dt>
<dt>txy_plate3d_min : float</dt>
<dt>txyx_plate3d_max : float</dt>
</dl>
