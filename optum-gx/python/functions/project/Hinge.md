# Hinge

Define a Hinge material, assigned to plate hinges with set_hinge_2d / set_hinge_3d.

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color=rgb(96,96,96)</dd>
<dt>moment : float</dt>
<dd>Plastic moment m_p, in kNm/m.</dd>
<dt>use_rotational_stiffness : str</dt>
<dd>Apply the rotational stiffness k. use_rotational_stiffness= 'yes' or 'no'</dd>
<dt>k : float</dt>
<dd>Rotational stiffness, in kNm/m/rad. Used when use_rotational_stiffness is 'yes'.</dd>
</dl>

## Examples

```python
model2d.add_rectangle([0,0],[2,2])
model2d.add_line([1,0],[1,2])
model2d.set_plate(model2d.select([1,1],types='edge'), prj.RigidPlate(name='Plate'))
HingeMaterial = prj.Hinge(name='Hinge Material',
                              color=rgb(96,96,96),
                              moment=50,
                              use_rotational_stiffness='yes',
                              k=1000)
model2d.set_hinge_2d(model2d.select([1,2],types='vertex'),
                         material=HingeMaterial)
```
