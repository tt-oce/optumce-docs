# ReinforcedConcrete

Creates a ReinforcedConcrete material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance.</dd>
<dt>E : float</dt>
<dd>Young's Modulus, in MPa.</dd>
<dt>nu : float</dt>
<dd>Poisson's ratio.</dd>
<dt>gamma_dry : float</dt>
<dd>Dry unit weight in kN/m^3.</dd>
<dt>gamma_sat : float</dt>
<dd>Saturated unit weight in kN/m^3.</dd>
<dt>compression : float</dt>
<dd>Compressive strength, in MPa.</dd>
<dt>tension : float</dt>
<dd>Tensile strength, in MPa.</dd>
<dt>effectiveness_factor : float</dt>
<dd>Effectiveness factor for concrete strength.</dd>
<dt>cracked_stiffness : boolean</dt>
<dd>Use cracked stiffness. cracked_stiffness = 'yes' or 'no'</dd>
<dt>reinforcement_type : str</dt>
<dd>Reinforcement layout type. reinforcement_type = 'Cartesian' or 'Polar'</dd>
<dt>mesh_x_yield : float</dt>
<dd>Yield strength of x-direction reinforcement, in MPa.</dd>
<dt>mesh_x_diameter : float</dt>
<dd>Diameter of x-direction reinforcement, in mm.</dd>
<dt>mesh_x_spacing1 : float</dt>
<dd>Spacing 1 of x-direction reinforcement, in mm.</dd>
<dt>mesh_x_spacing2 : float</dt>
<dd>Spacing 2 of x-direction reinforcement, in mm.</dd>
<dt>mesh_x_anchorage : float</dt>
<dd>Anchorage length of x-direction reinforcement, in mm.</dd>
<dt>mesh_y_yield : float</dt>
<dd>Yield strength of y-direction reinforcement, in MPa.</dd>
<dt>mesh_y_diameter : float</dt>
<dd>Diameter of y-direction reinforcement, in mm.</dd>
<dt>mesh_y_spacing1 : float</dt>
<dd>Spacing 1 of y-direction reinforcement, in mm.</dd>
<dt>mesh_y_spacing2 : float</dt>
<dd>Spacing 2 of y-direction reinforcement, in mm.</dd>
<dt>mesh_y_anchorage : float</dt>
<dd>Anchorage length of y-direction reinforcement, in mm.</dd>
<dt>mesh_z_yield : float</dt>
<dd>Yield strength of z-direction reinforcement, in MPa.</dd>
<dt>mesh_z_diameter : float</dt>
<dd>Diameter of z-direction reinforcement, in mm.</dd>
<dt>mesh_z_spacing1 : float</dt>
<dd>Spacing 1 of z-direction reinforcement, in mm.</dd>
<dt>mesh_z_spacing2 : float</dt>
<dd>Spacing 2 of z-direction reinforcement, in mm.</dd>
<dt>mesh_z_anchorage : float</dt>
<dd>Anchorage length of z-direction reinforcement, in mm. Example: >>> rc = prj.ReinforcedConcrete(name='RC Wall', gamma_dry=25.0, gamma_sat=25.0, E=30000.0, nu=0.2, compression=25.0, tension=2.5, effectiveness_factor=0.5, cracked_stiffness=True, reinforcement_type=0, mesh_x_yield=500.0, mesh_x_diameter=12.0, mesh_x_spacing1=150.0, mesh_x_spacing2=150.0, mesh_x_anchorage=240.0, ) >>> model2d.set_solid(shapes=Face,material=rc)</dd>
</dl>
