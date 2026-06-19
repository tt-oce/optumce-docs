# add_ncone

Draw a cone (or truncated cone) in 3D.

## Parameters

<dl>
<dt>center : array</dt>
<dd>Center point: center = [x0,y0,z0]</dd>
<dt>N : int</dt>
<dd>Number of linearly spaced faces.</dd>
<dt>radius0 : float</dt>
<dd>Bottom radius.</dd>
<dt>radius1 : float</dt>
<dd>Top radius (0 for a pointed cone).</dd>
<dt>height : float</dt>
<dd>Height of cone.</dd>
</dl>

## Examples

```python
model3d.add_cone([0,0,0], N=12, radius0=3, radius1=0, height=5)
model3d.add_cone([5,0,0], N=6, radius0=2, radius1=1, height=4)
```
