# DesignApproach

One design approach (a column of the GUI's Design Approaches table): the
partial factors applied to loads, soil strength and structural strength
by every stage that uses it (``stage.design_approach = 'ULS'``).

Reading a factor queries the running application; assigning one updates
it immediately and the GUI table follows. "Unity" is read-only.

## Examples

```python
uls = project.design_approach['ULS']
uls.gamma_unfavorable_dead_load = 1.1
uls.gamma_unfavorable_live_load
1.65
uls.update(gamma_c=1.25, gamma_phi=1.25)   # several factors, one call
uls.to_dict()
{'gamma_unfavorable_dead_load': 1.1, ...}
```

## See also

- [DesignApproaches](/python/functions/objects/settings/DesignApproaches)
- [Project.design_approach](/python/functions/project/operations/design_approach)

## Properties

<dl>
<dt>name : str</dt>
<dd>The name as shown in the GUI ("SLS", "ULS", "ALS", "User 1", ...). gamma_unfavorable_dead_load, gamma_unfavorable_live_load,</dd>
<dt>gamma_unfavorable_user1_load, gamma_unfavorable_user2_load : float</dt>
<dd>Load factors for unfavourable dead, live, user 1 and user 2 loads. gamma_favorable_dead_load, gamma_favorable_live_load,</dd>
<dt>gamma_favorable_user1_load, gamma_favorable_user2_load : float</dt>
<dd>Load factors for favourable loads.</dd>
<dt>gamma_c, gamma_phi, gamma_cu : float</dt>
<dd>Soil strength factors on c', phi' and cu. gamma_anchor, gamma_general_plate, gamma_flat_plate_steel, gamma_sheet_pile, gamma_flat_plate_concrete_m, gamma_flat_plate_concrete_fc,</dd>
<dt>gamma_flat_plate_concrete_ft, gamma_geogrid : float</dt>
<dd>Structural strength factors.</dd>
<dt>parameters : List[float]</dt>
<dd>All factors as a list in the positional order of ``FIELDS`` (the legacy ``set_design_approach_parameters`` form).</dd>
<dt>gamma_unfavorable_dead_load : float</dt>
<dd>Load factor for unfavourable dead loads.</dd>
<dt>gamma_unfavorable_live_load : float</dt>
<dd>Load factor for unfavourable live loads.</dd>
<dt>gamma_unfavorable_user1_load : float</dt>
<dd>Load factor for unfavourable loads of safety type "user 1".</dd>
<dt>gamma_unfavorable_user2_load : float</dt>
<dd>Load factor for unfavourable loads of safety type "user 2".</dd>
<dt>gamma_favorable_dead_load : float</dt>
<dd>Load factor for favourable dead loads.</dd>
<dt>gamma_favorable_live_load : float</dt>
<dd>Load factor for favourable live loads.</dd>
<dt>gamma_favorable_user1_load : float</dt>
<dd>Load factor for favourable loads of safety type "user 1".</dd>
<dt>gamma_favorable_user2_load : float</dt>
<dd>Load factor for favourable loads of safety type "user 2".</dd>
<dt>gamma_c : float</dt>
<dd>Soil strength factor on the effective cohesion c'.</dd>
<dt>gamma_phi : float</dt>
<dd>Soil strength factor on the effective friction angle phi' (applied to tan phi').</dd>
<dt>gamma_cu : float</dt>
<dd>Soil strength factor on the undrained shear strength cu.</dd>
<dt>gamma_anchor : float</dt>
<dd>Structural strength factor for anchors (steel).</dd>
<dt>gamma_general_plate : float</dt>
<dd>Structural strength factor for General Plate materials.</dd>
<dt>gamma_flat_plate_steel : float</dt>
<dd>Structural strength factor for Flat Plate (steel) materials.</dd>
<dt>gamma_sheet_pile : float</dt>
<dd>Structural strength factor for Sheet Pile materials.</dd>
<dt>gamma_flat_plate_concrete_m : float</dt>
<dd>Flat Plate (concrete) factor on the moment capacity (gamma_m).</dd>
<dt>gamma_flat_plate_concrete_fc : float</dt>
<dd>Flat Plate (concrete) factor on the compressive strength (gamma_fc).</dd>
<dt>gamma_flat_plate_concrete_ft : float</dt>
<dd>Flat Plate (concrete) factor on the tensile strength (gamma_ft).</dd>
<dt>gamma_geogrid : float</dt>
<dd>Structural strength factor for Geogrid materials (gamma_np).</dd>
</dl>

## Methods

<a id="update"></a>
### update()

Set several factors in one call.

#### Parameters

<dl>
<dd>**factors : float Keyword arguments named as in ``FIELDS``; a ``None`` value is skipped. Unknown names raise AttributeError.</dd>
</dl>

#### Examples

```python
project.design_approach['ULS'].update(gamma_c=1.25, gamma_phi=1.25)
```

<a id="to_dict"></a>
### to_dict()

All factors as ``{field: value}`` (one round trip). Feed the result
to ``update(**d)`` to restore or copy them.
