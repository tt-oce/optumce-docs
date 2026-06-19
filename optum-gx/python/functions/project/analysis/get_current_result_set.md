# get_current_result_set

Get data of the currently plotted result.

## Returns

<dl>
<dt>PlottedResult or None</dt>
<dd>Object with: - name: short name (last segment of the property path) - navigation_property: path e.g. ``output.solid[].results.stresses.total_stresses.sigma_x`` - indexer: ``result[i]`` returns ElementResult for element i, ``len(result)`` for count Returns None if no result is currently plotted.</dd>
</dl>

## Examples

```python
project.get_current_result_set()
```
