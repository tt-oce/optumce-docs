# Regional

Regional (units) settings of the project.

Exposes the project's unit systems as read/write properties.

## Examples

```python
prj.regional.unit = UnitSystem.us_customary
prj.regional.result_unit
<UnitSystem.si: 0>
```

## See also

- [regional](/python/functions/project/operations/regional)

## Properties

<dl>
<dt>unit : UnitSystem</dt>
<dd>The project editing/grid unit system (``UnitSystem.si`` or ``UnitSystem.us_customary``).</dd>
<dt>result_unit : UnitSystem</dt>
<dd>The result viewer display unit system (the "Result units" setting).</dd>
</dl>
