# set_six_dof_load

Add six degree of freedom load.

## Parameters

<dl>
<dt>fx, fy, fz : float</dt>
<dd>Forces in kN.</dd>
<dt>mx, my, mz : float</dt>
<dd>Moments in kNm.</dd>
</dl>

## Examples

```python
sel = model.select([0.5,0.5,1], types='face')
model.set_six_dof_load(shapes=sel, fx=-10, fz=-30, option='multiplier')
```
