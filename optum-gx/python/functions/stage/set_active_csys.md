# set_active_csys

Set the active coordinate system.

## Parameters

<dl>
<dt>csys : Csys</dt>
<dd>Coordinate system</dd>
</dl>

## See also

- [get_active_csys](/python/functions/model/get_active_csys)
- [get_csys](/python/functions/project/get_csys)
- [prj.create_csys_2d](/python/functions/model/prj.create_csys_2d)
- [prj.create_csys_3d](/python/functions/model/prj.create_csys_3d)

## Examples

```python
model2d.set_active_csys(csys= prj.create_csys_2d(origo = [0,0], direction_i= [1,1],name= "csys_2D"))
model3d.set_active_csys(csys=prj.create_csys_3d(origo = [0,0,0], direction_i= [0,np.sqrt(2)/2,np.sqrt(2)/2], direction_j=[1,0,0],name="csys_3D"))
```
