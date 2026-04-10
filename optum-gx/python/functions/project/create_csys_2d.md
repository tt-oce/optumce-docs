# create_csys_2d

Create two-dimensional coordinate system.

## Parameters

<dl>
<dt>origo : array</dt>
<dd>Origo of the coordinate system</dd>
<dt>direction_i : array</dt>
<dd>Point to define the basis vector from origo in direction i</dd>
<dt>name : str</dt>
<dd>String naming the coordinate system.</dd>
</dl>

## See also

- [create_csys_3d](/python/functions/project/create_csys_3d)
- [get_csys](/python/functions/project/get_csys)

## Notes

direction_j is derived from direction_i.

## Examples

```python
prj.create_csys_2d(origo = [0,0], direction_i= [1,1],name="csys_2D_45")
```
