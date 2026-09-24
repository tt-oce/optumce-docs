# GeneralProperties

General information about a single element: its material and the shape
it belongs to.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
g = stage.output.solid[0].general
g.material_name, g.material_model, g.shape_id
```

## See also

- [ElementIndexer](/python/functions/objects/results/ElementIndexer)

## Properties

<dl>
<dt>material_name : str</dt>
<dd>Name of the element's material (empty string when there is none).</dd>
<dt>color</dt>
<dd>Display colour of the element's material (empty string when there is none).</dd>
<dt>shape_id : int</dt>
<dd>ID of the shape the element belongs to, or None if not available.</dd>
<dt>material_model : str</dt>
<dd>Name of the material model of the element's material, or None if not available.</dd>
<dt>result_point_name : str</dt>
<dd>Result point name (result point meshes only, else None).</dd>
<dt>result_point_index : int</dt>
<dd>Result point index (result point meshes only, else None).</dd>
</dl>
