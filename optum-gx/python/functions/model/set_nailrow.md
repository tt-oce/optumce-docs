# set_nailrow

Set shape as nail row.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes. ShapeType must be 'vertex'</dd>
<dt>material : NailRow</dt>
<dd>Material.</dd>
</dl>

## See also

- [set_fixedendanchor](/python/functions/model/set_fixedendanchor)
- [add_connector](/python/functions/model/add_connector)

## Examples

```python
model2d.add_line([7,3],[10,0])
NailMaterial = prj.NailRow(name="Nailrow1", color=Color(r=207,g=86,b=80),axial_strength=250,lateral_strength=10, diameter=0.4,young_modulus=200000)
sel = model2d.select([10,0],types='edge')
model2d.set_nailrow(shapes=sel,material=NailMaterial)
model3d.add_line(p0=[3,0,0],p1=[6,3,3])
sel =model3d.select([6,3,3],types='edge')
model3d.set_nailrow(shapes=sel,material=NailMaterial)
```
