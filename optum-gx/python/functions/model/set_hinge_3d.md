# set_hinge_3d

Set hinge in 3D.

## Parameters

<dl>
<dt>vertices : Shapelist</dt>
<dd>List of edges</dd>
</dl>

## Notes

Edges must be connected to atleast one plate, to which the hinge will be assigned.

## See also

- [set_hinge_2d](/python/functions/model/set_hinge_2d)

## Examples

```python
e = model3d.select(
p0=[0,0,0],
p1=[0,0,1],
types=['edge'],
option='blue')
model3d.set_hinge_3d(edges=e)
```
