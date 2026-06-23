# PileRow

Pile row material -- row of equally-spaced piles parameterised by
diameter, spacing and pile type (driven, bored, etc.).

## Examples

```python
material = project.PileRow(name='Pile Row', diameter=0.5)
material.diameter
```

## Properties

<dl>
<dt>name : str</dt>
<dd>Material name.</dd>
<dt>color : Color</dt>
<dd>Material color.</dd>
<dt>gamma : float | ParameterMap | Profile | Gradient</dt>
<dd>Unit weight.</dd>
<dt>reducible_strength : bool</dt>
<dd>Reducible strength flag.</dd>
<dt>E : float | ParameterMap | Profile | Gradient</dt>
<dd>Young's modulus.</dd>
<dt>nu : float | ParameterMap | Profile | Gradient</dt>
<dd>Poisson's ratio.</dd>
<dt>pile_type : int</dt>
<dd>Pile type: massive_circular=0, circular_tube=1, massive_square=2, user_defined=3.</dd>
<dt>diameter : float</dt>
<dd>Pile diameter (for MassiveCircular and CircularTube).</dd>
<dt>wall_thickness : float</dt>
<dd>Wall thickness (for CircularTube).</dd>
<dt>width : float</dt>
<dd>Pile width (for MassiveSquare).</dd>
<dt>sectional_area : float</dt>
<dd>Sectional area (for UserDefined).</dd>
<dt>moment_of_inertia : float</dt>
<dd>Moment of inertia (for UserDefined).</dd>
<dt>user_defined_deq : bool</dt>
<dd>Flag for user-defined equivalent diameter.</dd>
<dt>deq : float</dt>
<dd>Equivalent diameter.</dd>
<dt>young_modulus : float | ParameterMap | Profile | Gradient</dt>
<dd>Young's modulus of pile material.</dd>
<dt>spacing : float</dt>
<dd>Spacing between piles.</dd>
<dt>axial_strength : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial strength per unit length.</dd>
<dt>lateral_strength : float | ParameterMap | Profile | Gradient</dt>
<dd>Lateral strength per unit length.</dd>
<dt>base_strength : float | ParameterMap | Profile | Gradient</dt>
<dd>Base strength.</dd>
<dt>soil_pile_stiffness : int</dt>
<dd>Soil-pile stiffness mode: default_stiffness=0, interaction_factors=1, spring_stiffness=2.</dd>
<dt>IFSa : float</dt>
<dd>Interaction factor for axial stiffness.</dd>
<dt>IFSl : float</dt>
<dd>Interaction factor for lateral stiffness.</dd>
<dt>IFSb : float</dt>
<dd>Interaction factor for base stiffness.</dd>
<dt>axial_stiffness : float | ParameterMap | Profile | Gradient</dt>
<dd>Axial stiffness.</dd>
<dt>lateral_stiffness : float | ParameterMap | Profile | Gradient</dt>
<dd>Lateral stiffness.</dd>
<dt>base_stiffness : float | ParameterMap | Profile | Gradient</dt>
<dd>Base stiffness.</dd>
<dt>elastic_zone : int</dt>
<dd>Elastic zone type: use_deq=0, none=1.</dd>
</dl>
