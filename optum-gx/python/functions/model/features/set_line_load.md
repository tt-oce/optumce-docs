# set_line_load

Add line load.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Shapes to apply the load to.</dd>
<dt>value : float | ParameterMap | Gradient</dt>
<dd>Load magnitude in kN/m.</dd>
<dt>direction : str</dt>
<dd>Load direction. direction = 'x' or 'y' or 'z'.</dd>
<dt>option : str</dt>
<dd>Load option. option = 'fixed' or 'multiplier'.</dd>
<dt>coordinate_system : Csys or str</dt>
<dd>Coordinate system to define the load direction.</dd>
<dt>load_type : str</dt>
<dd>Load type. load_type = 'unfavourable' or 'favourable'.</dd>
<dt>load_category : str</dt>
<dd>Safety factor category.</dd>
<dt>load_variation : str</dt>
<dd>Load variation. load_variation = 'constant' or 'linear'.</dd>
<dt>magnitude : list[float]</dt>
<dd>Linear variation endpoint values [p1, p2].</dd>
<dt>location : list[list[float]]</dt>
<dd>Anchor point coordinates [[x1,y1,z1], [x2,y2,z2]].</dd>
<dt>p : float | ParameterMap | Gradient</dt>
<dd>Load magnitude; value is an alias and takes precedence when supplied.</dd>
<dt>csys : Csys</dt>
<dd>Coordinate system; coordinate_system is an alias and takes precedence when supplied.</dd>
</dl>

## Examples

```python
sel = model.select([3,3,0], types='edge')
feature = model.set_line_load(shapes=sel, value=-10, direction='z', option='multiplier')
```
