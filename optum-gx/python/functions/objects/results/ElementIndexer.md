# ElementIndexer

A single element of a result group, obtained by indexing a ResultIndexer.

The data is split into ``general``, ``topology``, ``material`` and
``results``.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
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
<dd>Material name, color, material model and shape ID of the element.</dd>
<dt>topology : Topology</dt>
<dd>Nodes of the element and their coordinates.</dd>
<dt>material : PropertyContainer</dt>
<dd>Parameters of the element's material as well as ``name`` and ``color``.</dd>
<dt>results : PropertyContainer</dt>
<dd>Result fields of the element as a nested PropertyContainer.</dd>
</dl>
