# ReinforcedConcrete

Reinforced concrete -- composite solid material combining a concrete
matrix with discrete reinforcement, for slab and wall analyses.

## Examples

```python
material = project.ReinforcedConcrete(name='RC Slab', compression=30)
material.compression
```

## Properties

<dl>
<dt>name : str</dt>
<dd>Material name.</dd>
<dt>color : Color</dt>
<dd>Material color.</dd>
<dt>gamma_dry : float | ParameterMap | Profile | Gradient</dt>
<dd>Dry unit weight.</dd>
<dt>gamma_sat : float | ParameterMap | Profile | Gradient</dt>
<dd>Saturated unit weight.</dd>
<dt>reducible_strength : bool</dt>
<dd>Reducible strength flag.</dd>
<dt>E : float | ParameterMap | Profile | Gradient</dt>
<dd>Young's modulus.</dd>
<dt>nu : float | ParameterMap | Profile | Gradient</dt>
<dd>Poisson's ratio.</dd>
<dt>compression : float | ParameterMap | Profile | Gradient</dt>
<dd>Compression strength.</dd>
<dt>tension : float | ParameterMap | Profile | Gradient</dt>
<dd>Tension strength.</dd>
<dt>effectiveness_factor : float | ParameterMap | Profile | Gradient</dt>
<dd>Effectiveness factor.</dd>
<dt>cracked_stiffness : bool</dt>
<dd>Use cracked stiffness.</dd>
<dt>reinforcement_type : int</dt>
<dd>Reinforcement type (Cartesian=0, Polar=1).</dd>
<dt>mesh_x_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh X yield strength.</dd>
<dt>mesh_x_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh X bar diameter.</dd>
<dt>mesh_x_spacing1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh X spacing 1.</dd>
<dt>mesh_x_spacing2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh X spacing 2.</dd>
<dt>mesh_x_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh X anchorage length.</dd>
<dt>mesh_y_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Y yield strength.</dd>
<dt>mesh_y_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Y bar diameter.</dd>
<dt>mesh_y_spacing1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Y spacing 1.</dd>
<dt>mesh_y_spacing2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Y spacing 2.</dd>
<dt>mesh_y_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Y anchorage length.</dd>
<dt>mesh_z_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Z yield strength.</dd>
<dt>mesh_z_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Z bar diameter.</dd>
<dt>mesh_z_spacing1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Z spacing 1.</dd>
<dt>mesh_z_spacing2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Z spacing 2.</dd>
<dt>mesh_z_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Mesh Z anchorage length.</dd>
<dt>mesh_x_polar_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh X yield strength.</dd>
<dt>mesh_x_polar_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh X bar diameter.</dd>
<dt>mesh_x_polar_number_bars : int</dt>
<dd>Polar mesh X number of bars.</dd>
<dt>mesh_x_polar_spacing : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh X spacing.</dd>
<dt>mesh_x_polar_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh X anchorage length.</dd>
<dt>mesh_y_polar_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y yield strength.</dd>
<dt>mesh_y_polar_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y bar diameter.</dd>
<dt>mesh_y_polar_spacing1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y spacing 1.</dd>
<dt>mesh_y_polar_spacing2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y spacing 2.</dd>
<dt>mesh_y_polar_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y anchorage length.</dd>
<dt>mesh_y_polar_b_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y-B yield strength.</dd>
<dt>mesh_y_polar_b_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y-B bar diameter.</dd>
<dt>mesh_y_polar_b_number_bars : int</dt>
<dd>Polar mesh Y-B number of bars.</dd>
<dt>mesh_y_polar_b_spacing : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y-B spacing.</dd>
<dt>mesh_y_polar_b_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Y-B anchorage length.</dd>
<dt>mesh_z_polar_yield : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Z yield strength.</dd>
<dt>mesh_z_polar_diameter : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Z bar diameter.</dd>
<dt>mesh_z_polar_spacing1 : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Z spacing 1.</dd>
<dt>mesh_z_polar_spacing2 : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Z spacing 2.</dd>
<dt>mesh_z_polar_anchorage : float | ParameterMap | Profile | Gradient</dt>
<dd>Polar mesh Z anchorage length.</dd>
<dt>parameter_mesh_y_polar : int</dt>
<dd>Parameter set for polar mesh Y (A=0, B=1).</dd>
</dl>
