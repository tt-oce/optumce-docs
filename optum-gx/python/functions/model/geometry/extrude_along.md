# extrude_along

Extrude faces along a path defined by a list of points.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>list of face shapes to extrude</dd>
<dt>path : list of arrays</dt>
<dd>list of points defining the extrusion path</dd>
</dl>

## Examples

```python
faces = model3d.select([1,1,0], types='face')
model3d.extrude_along(faces, [[0,0,0], [0,0,2], [2,0,4]])
```
