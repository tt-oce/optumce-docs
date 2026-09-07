# get_plots

List all result field plots available for this model or stage.

## Parameters

<dl>
<dd>None</dd>
</dl>

## Returns

<dl>
<dt>list[str]</dt>
<dd>The identity path of every plottable result field, one per leaf of the Results tree, e.g. "Solid/Stresses/Total/sigma_x". Each entry can be passed directly to take_picture.</dd>
</dl>

## See also

- [take_picture](/python/functions/model-and-stage/take_picture)

## Notes

The stage must have up-to-date results (run the analysis first).

## Examples

```python
for path in stage1.get_plots():
    print(path)
stage1.take_picture(stage1.get_plots()[0], 'plot.png')
```
