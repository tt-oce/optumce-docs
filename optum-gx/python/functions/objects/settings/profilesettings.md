# ProfileSettings

Attribute-style access to one display profile's settings.

Reading an attribute returns the setting's current value as text
(colors as hex); assigning stores it. Colors accept hex ("#ff0000")
or SVG color names ("white", "red"); numbers can be given as numbers
or text. Unknown setting names raise an error from the server.

## Examples

```python
gx.settings.screen.background_color = "white"
gx.settings.report.background_color = "red"
gx.settings.screenshot.vertex_color
```

## Properties

<dl>
<dt>background_color : str</dt>
<dd>Background color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>default_text_color : str</dt>
<dd>Default text color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>mesh_edge_color : str</dt>
<dd>Mesh edge color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>background_mesh_face_color : str</dt>
<dd>Background mesh face color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>background_mesh_edge_color : str</dt>
<dd>Background mesh edge color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>model_see_through_color : str</dt>
<dd>Model see-through color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>grayout_color : str</dt>
<dd>Grayout color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>vertex_color : str</dt>
<dd>Vertex color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>vertex_selected_color : str</dt>
<dd>Vertex selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>edge_color : str</dt>
<dd>Edge color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>edge_selected_color : str</dt>
<dd>Edge/node selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>face_selected_color : str</dt>
<dd>Face selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>specular_color : str</dt>
<dd>Specular color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>load_fixed_color : str</dt>
<dd>Fixed load color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>load_multiplier_color : str</dt>
<dd>Multiplier load color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>load_selected_color : str</dt>
<dd>Selected load color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>plate_bc_color : str</dt>
<dd>PlateBC color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>point_bc_color : str</dt>
<dd>PointBC color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>noflow_color : str</dt>
<dd>NoFlow color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>noflow_selected_color : str</dt>
<dd>NoFlow selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>flow_color : str</dt>
<dd>Flow color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>structural_color : str</dt>
<dd>Structural color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>connector_connected_color : str</dt>
<dd>Connector connected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>connector_unconnected_color : str</dt>
<dd>Connector unconnected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>support_color : str</dt>
<dd>Support color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>support_selected_color : str</dt>
<dd>Support selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>water_table_color : str</dt>
<dd>Water table color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>water_table_selected_color : str</dt>
<dd>Water table selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>fixed_pressure_color : str</dt>
<dd>Fixed pressure color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>fixed_pressure_selected_color : str</dt>
<dd>Fixed pressure selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>fixed_head_color : str</dt>
<dd>Fixed head color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>fixed_head_selected_color : str</dt>
<dd>Fixed head selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>infiltration_color : str</dt>
<dd>Infiltration color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>infiltration_selected_color : str</dt>
<dd>Infiltration selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>fixed_excess_pressure_color : str</dt>
<dd>Fixed excess pressure color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>fixed_excess_pressure_selected_color : str</dt>
<dd>Fixed excess pressure selected color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>grid_default_color : str</dt>
<dd>Grid default color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>grid_mod_five_color : str</dt>
<dd>Grid 5th line color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>grid_x_zero_line_color : str</dt>
<dd>Grid x zero line color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>grid_y_zero_line_color : str</dt>
<dd>Grid y zero line color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>axi_symmetry_color : str</dt>
<dd>Axi symmetry color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>axi_symmetry_linewidth : str</dt>
<dd>Axi-symmetry line thickness (number, returned as text).</dd>
<dt>specular_2d_strength : str</dt>
<dd>Specular 2d strength (number, returned as text).</dd>
<dt>specular_3d_strength : str</dt>
<dd>Specular 3d strength (number, returned as text).</dd>
<dt>specular_exponent : str</dt>
<dd>Specular exponent (number, returned as text).</dd>
<dt>anti_aliasing : str</dt>
<dd>Anti-aliasing sample count (0 = off) (integer, returned as text).</dd>
<dt>face_highlight_factor : str</dt>
<dd>Face highlight factor (number, returned as text).</dd>
<dt>line_thickness : str</dt>
<dd>Line thickness (number, returned as text).</dd>
<dt>point_radius : str</dt>
<dd>Point radius (number, returned as text).</dd>
<dt>highlight_text_color : str</dt>
<dd>Highlight text color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>connection_color : str</dt>
<dd>Connected point color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>rubber_color : str</dt>
<dd>Rubber color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>prestress_color : str</dt>
<dd>Prestress color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>reaction_relaxation_color : str</dt>
<dd>Reaction relaxation color. Returned as "#RRGGBBAA" hex; set accepts SVG color names, "#RRGGBB" or Qt's "#AARRGGBB".</dd>
<dt>mesh_overlay_thickness : str</dt>
<dd>Mesh overlay line thickness (number, returned as text).</dd>
<dt>min_curve_width : str</dt>
<dd>2D min curve width (pixels) (number, returned as text).</dd>
<dt>max_relative_curve_width : str</dt>
<dd>2D max curve width (pixels per 1000 vertical resolution) (number, returned as text).</dd>
<dt>max_curve_width_3d : str</dt>
<dd>3D max curve width (distance) (number, returned as text).</dd>
<dt>transparency : str</dt>
<dd>Transparency (number, returned as text).</dd>
<dt>result_light_mode : str</dt>
<dd>Result view light mode: 0 = Ambient, 1 = Diffuse, 2 = Specular (integer, returned as text).</dd>
<dt>model_light_mode : str</dt>
<dd>Model view light mode: 0 = Ambient, 1 = Diffuse, 2 = Specular (integer, returned as text).</dd>
<dt>screenshot_folder : str</dt>
<dd>Folder gx toolbar screenshots are saved into; empty = the Windows Pictures folder.</dd>
<dt>show_grid : str</dt>
<dd>Render the grid in the output ("true"/"false"). Report: the shared report grid default (per-figure overrides win); Screenshot: follows the live view's grid until customized; Screen: the live grid toggle.</dd>
</dl>

## Methods

<a id="reset"></a>
### reset()

Reset this display profile: "screen" restores the factory display
defaults (and repaints the views); "report"/"screenshot" drop every
override so the profile follows the screen values again.

#### Examples

```python
gx.settings.report.reset()
```
