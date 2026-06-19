# polar_array

Generate polar array of shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
<dt>axis_origo : array</dt>
<dd>Origin of rotation axis</dd>
<dt>axis_dir : array</dt>
<dd>Direction of rotation axis</dd>
<dt>angle : float</dt>
<dd>Total angle in degrees</dd>
<dt>N : int</dt>
<dd>Number of copies</dd>
</dl>

## Examples

```python
model2d.add_rectangle([2,0],[4,2])
f = model2d.select([3,1], types='face')
model2d.polar_array(f, axis_origo=[0,0], axis_dir=[0,0,1], angle=360, N=6)
```
