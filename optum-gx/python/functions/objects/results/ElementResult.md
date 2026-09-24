# ElementResult

A result field or material parameter of a single element containing its unit and
values.

Printing an ElementResult shows the unit as text (e.g. ``kN/m2``)
together with the values.

## Examples

```python
stage = gx.get_current_project().get_models_and_stages()[0]
m = stage.output.plate[2].results.final_forces.M_y
m
m.value
```

## See also

- [PropertyContainer](/python/functions/objects/results/PropertyContainer)

## Properties

<dl>
<dt>unit : Unit</dt>
<dd>Unit of the values.</dd>
<dt>value : array of float</dt>
<dd>Values of the field for this element, one entry per element point.</dd>
</dl>
