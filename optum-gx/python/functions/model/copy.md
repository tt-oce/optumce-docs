# copy

Copy shapes.

## Parameters

<dl>
<dt>shapes : ShapeList</dt>
<dd>List of shapes</dd>
<dt>vector : array</dt>
<dd>Vector defining the copy offset.</dd>
</dl>

## See also

- [move](/python/functions/model/move)
- [rotate](/python/functions/model/rotate)
- [mirror](/python/functions/model/mirror)

## Examples

```python
model2d.add_rectangle(p1=[0,0],p2=[1,2])
f = model2d.select([0.5,1],types='face')
model2d.copy(shapes=f,vector=[3,2])
```
