# ResultIndexer

The elements of one result group, e.g. all plate elements
(``stage.output.plate``) or all point reactions
(``stage.output.point_reaction``).

Supports ``len()``, indexing and iteration. Indexing returns an
ElementIndexer, or None when the index is out of range.

## Examples

```python
plates = stage.output.plate
len(plates)
plates[2].results.final_forces.M_y
for el in plates:
    print(el.general.material_name)
```

## Notes

A ResultIndexer is its own iterator, so it can be looped over only once.
To loop again, get the group from a new ``stage.output``.

## See also

- [StageResults](/python/functions/objects/results/StageResults)
- [ElementIndexer](/python/functions/objects/results/ElementIndexer)
