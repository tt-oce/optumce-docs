# set_six_dof_load

Add six degree of freedom load.

## Parameters

<dl>
<dd>fx, fy, fz : float Forces in kN. mx, my, mz : float Moments in kNm.</dd>
</dl>

## Examples

```python
sel = model.select([0.5,0.5,1], types='face')
model.set_six_dof_load(shapes=sel, fx=-10, fz=-30, option='multiplier')
```
