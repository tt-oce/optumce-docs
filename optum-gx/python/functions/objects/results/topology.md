# Topology

Mesh topology of a single element: its nodes and their coordinates.

## Examples

```python
topo = stage.output.line_reaction[0].topology
topo.nodes
list(zip(topo.X, topo.Y))
```

## See also

- [ElementIndexer](/python/functions/objects/results/ElementIndexer)

## Properties

<dl>
<dt>mesh_id : int</dt>
<dd>ID of the mesh part the element belongs to.</dd>
<dt>nodes : list[int]</dt>
<dd>Indices of the element's nodes.</dd>
<dt>X : list[float]</dt>
<dd>x-coordinates of the element's nodes, in the order of ``nodes``.</dd>
<dt>Y : list[float]</dt>
<dd>y-coordinates of the element's nodes, in the order of ``nodes``.</dd>
<dt>Z : list[float]</dt>
<dd>z-coordinates of the element's nodes, in the order of ``nodes``.</dd>
</dl>
