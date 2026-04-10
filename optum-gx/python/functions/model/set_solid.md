# set_solid

Set shape material as solid.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
<dt>material : material</dt>
<dd>Solid material</dd>
</dl>

## See also

- [set_plate](/python/functions/model/set_plate)

## Examples

```python
model2d.add_rectangle([0,0],[4,4])
SoilMaterial = prj.MohrCoulomb(name="Soil",c=10, phi=20, gamma_dry=20, color=Color(r=79,g=180,b=83))
SoilFace = model2d.select(point1=[1,1],types=[ShapeType.face])
model2d.set_solid(shapes=SoilFace,material=SoilMaterial)
model3d.add_box([1,1,1],[3,3,3])
SoilVol = model3d.select(point1=[2,2,1],types='volume')
model3d.set_solid(shapes=SoilVol,material=SoilMaterial)
```
