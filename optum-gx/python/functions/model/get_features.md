# get_features

Obtain features associated with shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
</dl>

## See also

*   [get_selected_shapes](/optum-gx/python/functions/model/get_selected_shapes)

## Examples

```python
model3d.add_rectangle([0,0,0],[3,3,0])
sel = model3d.select([2,0,0],types='edge')
model3d.set_line_load(shapes=sel,value=-10,direction='z',option='fixed')
model3d.get_features(sel)
Size: 1
[
{
Type: LOAD
Name: Load
attributes:
Load_Kind: Line
Load_Option: Fixed
Load_Type: LOAD
Load_SafetyType: Unity
Load_Value: -10.0
},
]
```