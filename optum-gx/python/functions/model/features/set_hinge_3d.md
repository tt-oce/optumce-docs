# set_hinge_3d

Set hinge in 3D.

## Parameters

<dl>
<dt>edges : ShapeList</dt>
<dd>List of edges</dd>
<dt>faces : ShapeList</dt>
<dd>List of faces</dd>
<dt>material : Hinge or str, optional</dt>
<dd>Hinge material (object, name or uuid). When omitted, the project's first hinge material is used (one is created if there is none).</dd>
</dl>

## Returns

<dl>
<dt>bool</dt>
<dd>True if at least one hinge was added.</dd>
</dl>

## Notes

Edges must be connected to at least one plate, to which the hinge will be assigned. If edges are connected to multiple plates,
hinges will all be set to all of them, unless faces are specified.

## See also

- [set_hinge_2d](/python/functions/model/features/set_hinge_2d)

## Examples

```python
edges = model.get_shapes(['edge'])
faces = model.get_shapes(['face'])
model.set_hinge_3d(edges, faces)
model.set_hinge_3d(edges, material=prj.Hinge(name='Hinge 50', moment=50))
```
