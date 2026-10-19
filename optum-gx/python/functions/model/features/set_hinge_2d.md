# set_hinge_2d

Set hinge in 2D.

## Parameters

<dl>
<dt>vertices : ShapeList</dt>
<dd>List of vertices</dd>
<dt>edges : ShapeList</dt>
<dd>List of edges</dd>
<dt>material : Hinge or str, optional</dt>
<dd>Hinge material (object, name or uuid). When omitted, the project's first hinge material is used (one is created if there is none).</dd>
</dl>

## Returns

<dl>
<dt>bool</dt>
<dd>True if at least one hinge was added.</dd>
</dl>

## Notes

Vertices must be connected to at least one plate, to which the hinge will be assigned. If vertices are connected to multiple plates,
hinges will all be set to all of them, unless edges are specified.

## See also

- [set_hinge_3d](/python/functions/model/features/set_hinge_3d)

## Examples

```python
vertices = model.get_shapes(['vertex'])
edges = model.get_shapes(['edge'])
model.set_hinge_2d(vertices, edges)
model.set_hinge_2d(vertices, material=prj.Hinge(name='Hinge 50', moment=50))
```
