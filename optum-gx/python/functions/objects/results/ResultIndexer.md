# ResultIndexer

The elements of one result group, e.g. all plate elements
(``stage.output.plate``) or all point reactions
(``stage.output.point_reaction``).

Supports ``len()``, indexing and iteration. Indexing returns an
ElementIndexer, or None when the index is out of range.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
plates = stage.output.plate
len(plates)
plates[2].results.final_forces.M_y
for el in plates:
    print(el.general.material_name)
```

## See also

- [StageResults](/python/functions/objects/results/StageResults)
- [ElementIndexer](/python/functions/objects/results/ElementIndexer)
