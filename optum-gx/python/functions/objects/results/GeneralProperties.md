# GeneralProperties

General information about a single element: its material and the shape
it belongs to.

## Examples

```python
g = stage.output.solid[0].general
g.material_name, g.material_model, g.shape_id
```

## See also

- [ElementIndexer](/python/functions/objects/results/ElementIndexer)

## Properties

<dl>
<dt>material_name : str</dt>
<dd>Name of the element's material ('' if it has none).</dd>
<dt>color</dt>
<dd>Display colour of the element's material ('' if it has none).</dd>
<dt>shape_id : int</dt>
<dd>ID of the shape the element belongs to, or None if not available.</dd>
<dt>material_model : str</dt>
<dd>Name of the material model of the element's material, or None if not available.</dd>
</dl>
