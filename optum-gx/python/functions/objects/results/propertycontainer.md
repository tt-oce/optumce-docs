# PropertyContainer

Nested namespace of named values for one element - its result fields or
material parameters.

The attribute names come from the element's result definitions, so they
depend on the analysis and the element type. Nested groups are themselves
PropertyContainers; the leaves are ElementResult objects (plus plain values
such as a material's ``name`` and ``color``). ``repr()`` lists the names
available at that level, which is the easiest way to explore the tree.

## Examples

```python
r = stage.output.plate[2].results
r
r.final_forces.M_y
test.output.solid[0].results.final_stresses.total_stresses.q.value
```

## See also

- [ElementIndexer](/python/functions/objects/results/ElementIndexer)
- [ElementResult](/python/functions/objects/results/ElementResult)
