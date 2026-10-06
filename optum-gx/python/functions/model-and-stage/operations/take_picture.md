# take_picture

Save a plot of a result field of this model or stage to an image file.

## Parameters

<dl>
<dt>result_path : str</dt>
<dd>Identity path of the result field as shown in the Results tree, segments separated by "/", matched case-insensitively. Greek letters are spelled out, with subscripts appended after "_": "solid/stresses/total/sigma_x" addresses Solid > Stresses > Total > sigma-x. The raw field name is accepted too (e.g. "solid/stresses/total/sx"), as is the spelling without the subscript separator ("sigmax", or "my" for the plate moment shown as My). The sub-group segment ("total") may be omitted when the field name is unambiguous without it. get_plots lists the valid paths.</dd>
<dt>file_path : str</dt>
<dd>Path of the image file to write. The format follows the extension (PNG when there is none); missing folders are created, and an existing file is overwritten without warning.</dd>
<dt>options : dict, optional</dt>
<dd>Capture settings. Unset options fall back to the report display settings. Supported keys: - width, height : int, image size in pixels (default 2000 x 1500) - grid, mesh_overlay, model_outline, average_vertex_values : bool - colorbar_min, colorbar_max : float, pin the colorbar range; a side left out keeps the current range of the plot - colorbar_height, colorbar_width, colorbar_value_count : int - colorbar_text_scale : float - medium : display profile, "report" (default), "screen" or "screenshot" (see gx.settings.report/screen/screenshot) Result toolbar settings (unset = as currently shown in the Results tab): - step : int, step number as the toolbar shows it ("Step 1" is 1; results that start at "Step 0" count from 0); negative numbers count from the end, -1 being the last step - displacement : "total" or "incremental" - deformation_scale : float >= 0, the deformation scale factor - deformation_percent : float 0-100, the deformation animation slider; 0 plots the undeformed shape, 100 the full scale</dd>
</dl>

## Notes

The stage must have up-to-date results (run the analysis first).
The Results tab is left as it was after the picture is taken.

## Examples

```python
stage1.take_picture('solid/stresses/total/sigma_x', 'sigma_x.png')
model2d.take_picture('solid/displacements/|u|', 'u.png',
                     options={'width': 1200, 'height': 900, 'mesh_overlay': True})
stage1.take_picture('solid/displacements/|u|', 'u_step1.png',
                    options={'step': 1, 'deformation_scale': 50,
                             'deformation_percent': 100})
```
