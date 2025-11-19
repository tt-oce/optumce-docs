# create_csys_3d

Create three-dimensional coordinate system.

## Parameters

<dl>
<dt>origo : array</dt>
<dd>Origo of the coordinate system</dd>
<dt>direction_i : array</dt>
<dd>Point to define the basis vector from origo in direction i</dd>
<dt>direction_j : array</dt>
<dd>Point to define the basis vector from origo in direction j</dd>
<dt>name : str</dt>
<dd>String naming the coordinate system.</dd>
</dl>

## See also

*   [create_csys_2d](/optum-gx/python/functions/project/create_csys_2d)
*   [get_csys](/optum-gx/python/functions/project/get_csys)

## Notes

direction\_k is derived from direction\_i and direction\_j.

## Examples

```python
prj.create_csys_3d(origo = [0,0,0], direction_i= [0,np.sqrt(2)/2,np.sqrt(2)/2], direction_j=[1,0,0],name="csys_3D")
```