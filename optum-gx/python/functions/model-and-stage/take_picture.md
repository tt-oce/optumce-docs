# take_picture

Save a plot of a result field of this model or stage to an image file.

## Parameters

<dl>
<dt>result_path : str</dt>
<dd>Identity path of the result field as shown in the Results tree, segments separated by "/", matched case-insensitively. Greek letters are spelled out, with subscripts appended after "_": "solid/stresses/total/sigma_x" addresses Solid > Stresses > Total > sigma-x. The raw field name is accepted too (e.g. "solid/stresses/total/sx"), as is the spelling without the subscript separator ("sigmax", or "my" for the plate moment shown as My). The sub-group segment ("total") may be omitted when the field name is unambiguous without it. get_plots lists the valid paths.</dd>
<dt>file_path : str</dt>
<dd>Path of the image file to write. The format follows the extension (PNG when there is none); missing folders are created, and an existing file is overwritten without warning.</dd>
<dt>options : dict, optional</dt>
<dd>Capture settings. Unset options fall back to the report display settings. Supported keys: - width, height : int, image size in pixels (default 2000 x 1500) - grid, mesh_overlay, model_outline, average_vertex_values : bool - colorbar_min, colorbar_max : float, pin the colorbar range - colorbar_height, colorbar_width, colorbar_value_count : int - colorbar_text_scale : float - medium : "print" (default, report style) or "screen"</dd>
</dl>

## Notes

The stage must have up-to-date results (run the analysis first).

## Examples

```python
stage1.take_picture('solid/stresses/total/sigma_x', 'sigma_x.png')
model2d.take_picture('solid/displacements/|u|', 'u.png',
                     options={'width': 1200, 'height': 900, 'mesh_overlay': True})
```
