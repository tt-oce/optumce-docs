# move

Move shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
<dt>vector : array</dt>
<dd>Vector defining the movement.</dd>
</dl>

## See also

- [rotate](/python/functions/model/rotate)
- [mirror](/python/functions/model/mirror)

## Examples

```python
model2d.add_rectangle(p1=[0,0],p2=[1,2])
f = model2d.select([0.5,1],types='face')
model2d.move(shapes=f,vector=[3,2])
model3d.add_prism(points=[[-1,-1,0],[-3,-3,0],[-3,0,0]],height=3)
v  = model3d.select([0,0,0],[-3,-3,3],types=['volume'],option='blue')
model3d.move(shapes=v,vector=[3,0,-3])
```
