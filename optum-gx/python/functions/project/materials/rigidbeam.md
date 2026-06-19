# RigidBeam

Define a rigid beam material

## Parameters

<dl>
<dt>name : str</dt>
<dd>String naming the material.</dd>
<dt>color : Color</dt>
<dd>Material appearance. color=rgb(169,179,193)</dd>
<dt>gamma : float</dt>
<dd>Weight per unit length.</dd>
</dl>

## Examples

```python
RigidBeamMaterial = prj.RigidBeam(name='Rigid Beam',
                        color=rgb(0,44,99),
                        gamma=0,
                        )
```
