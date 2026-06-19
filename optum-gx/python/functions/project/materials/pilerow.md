# PileRow

Define a Pile Row material.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color=rgb(169,179,193)</dd>
<dt>pile_type : PileType</dt>
<dd>Pile type: "massive_circular", "circular_tube", "massive_square", "user_defined" (or int: 0-3)</dd>
<dt>diameter : float</dt>
<dd>Pile diameter (for MassiveCircular and CircularTube), in m.</dd>
<dt>wall_thickness : float</dt>
<dd>Wall thickness (for CircularTube), in m.</dd>
<dt>width : float</dt>
<dd>Pile width (for MassiveSquare), in m.</dd>
<dt>sectional_area : float</dt>
<dd>Sectional area (for UserDefined), in m^2.</dd>
<dt>moment_of_inertia : float</dt>
<dd>Moment of inertia (for UserDefined), in m^4.</dd>
<dt>user_defined_deq : bool</dt>
<dd>Flag for user-defined equivalent diameter.</dd>
<dt>deq : float</dt>
<dd>Equivalent diameter, in m.</dd>
<dt>young_modulus : float|ParameterMap|Profile|Gradient</dt>
<dd>Young's modulus of pile material, in kPa.</dd>
<dt>spacing : float</dt>
<dd>Spacing between piles, in m.</dd>
<dt>axial_strength : float|ParameterMap|Profile|Gradient</dt>
<dd>Axial strength per unit length, in kN/m.</dd>
<dt>lateral_strength : float|ParameterMap|Profile|Gradient</dt>
<dd>Lateral strength per unit length, in kN/m.</dd>
<dt>base_strength : float|ParameterMap|Profile|Gradient</dt>
<dd>Base strength, in kN.</dd>
<dt>soil_pile_stiffness : SoilPileStiffness</dt>
<dd>Soil-pile stiffness mode: "default_stiffness", "interaction_factors", "spring_stiffness" (or int: 0-2)</dd>
<dt>IFSa : float</dt>
<dd>Interaction factor for axial stiffness.</dd>
<dt>IFSl : float</dt>
<dd>Interaction factor for lateral stiffness.</dd>
<dt>IFSb : float</dt>
<dd>Interaction factor for base stiffness.</dd>
<dt>axial_stiffness : float|ParameterMap|Profile|Gradient</dt>
<dd>Axial stiffness, in kN/m^2.</dd>
<dt>lateral_stiffness : float|ParameterMap|Profile|Gradient</dt>
<dd>Lateral stiffness, in kN/m^2.</dd>
<dt>base_stiffness : float|ParameterMap|Profile|Gradient</dt>
<dd>Base stiffness, in kN/m.</dd>
<dt>elastic_zone : ElasticZone</dt>
<dd>Elastic zone type: "use_deq", "none" (or int: 0-1)</dd>
</dl>

## Examples

```python
PileRowMaterial = prj.PileRow(name='Concrete Piles',
                              color=rgb(169,179,193),
                              pile_type='massive_circular',
                              diameter=0.5,
                              young_modulus=2e7,
                              spacing=1.0,
                              axial_strength=100.0,
                              lateral_strength=1000.0,
                              base_strength=500.0,
                              soil_pile_stiffness='default_stiffness',
                              IFSa=0.5,
                              IFSl=0.5,
                              IFSb=5.0,
                              axial_stiffness=1000.0,
                              lateral_stiffness=1000.0,
                              base_stiffness=2000.0,
                              elastic_zone='use_deq'
                              )
```
