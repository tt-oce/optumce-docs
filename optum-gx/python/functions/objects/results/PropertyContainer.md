# PropertyContainer

Nested namespace of named values for one element containing result fields or
material parameters.

The attribute names come from the element's result definitions, so they
depend on the type of analysis and the element type.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
res = stage.output
r = res.plate[2].results
r
r.final_forces.M_y
res.solid[0].results.final_stresses.total_stresses.q.value
```

## See also

- [ElementIndexer](/python/functions/objects/results/ElementIndexer)
- [ElementResult](/python/functions/objects/results/ElementResult)
