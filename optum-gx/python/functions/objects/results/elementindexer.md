# ElementIndexer

A single element of a result group, obtained by indexing a ResultIndexer
(e.g. ``stage.output.plate[2]``).

Its data is split into ``general``, ``topology``, ``material`` and
``results``; ``repr()`` lists these.

## Examples

```python
el = stage.output.plate[2]
el.general.material_name
el.topology.nodes
el.results.final_forces.M_y
el.material
```

## See also

- [ResultIndexer](/python/functions/objects/results/ResultIndexer)
- [GeneralProperties](/python/functions/objects/results/GeneralProperties)
- [Topology](/python/functions/objects/results/Topology)
- [PropertyContainer](/python/functions/objects/results/PropertyContainer)

## Properties

<dl>
<dt>general : GeneralProperties</dt>
<dd>Material name, colour, material model and shape ID of the element.</dd>
<dt>topology : Topology</dt>
<dd>Nodes of the element and their coordinates.</dd>
<dt>material : PropertyContainer</dt>
<dd>Parameters of the element's material, plus the material's ``name`` and ``color``.</dd>
<dt>results : PropertyContainer</dt>
<dd>Result fields of the element as a nested PropertyContainer whose leaves are ElementResult objects (e.g. ``results.final_forces.M_y``).</dd>
</dl>
