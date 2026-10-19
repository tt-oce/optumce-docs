# Hinge

Hinge -- hinge material for plates, assigned with set_hinge_2d /
set_hinge_3d: plastic moment m_p and an optional rotational stiffness k.

## Examples

```python
material = project.Hinge(name='Hinge 50', moment=50,
                         use_rotational_stiffness=True, k=1000)
model.set_hinge_2d(vertices, material=material)
```

## Properties

<dl>
<dt>name : str</dt>
<dd>Material name.</dd>
<dt>color : Color</dt>
<dd>Material color.</dd>
<dt>moment : float</dt>
<dd>Plastic moment per unit length, m_p (kNm/m).</dd>
<dt>use_rotational_stiffness : bool</dt>
<dd>Whether the rotational stiffness k is applied.</dd>
<dt>k : float</dt>
<dd>Rotational stiffness per unit length (kNm/m/rad); used when use_rotational_stiffness is set.</dd>
</dl>
