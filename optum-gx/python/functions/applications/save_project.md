# save_project

Save current project

## Parameters

<dl>
<dt>file_path : str</dt>
<dd>path to desired save location.</dd>
</dl>

## Notes

If the specified file_path already exists the file will be overwritten without warning.

## Examples

```python
import os
current_path = os.getcwd()
filename ="slope_stability.gxx"
gx.save_project(file_path=os.path.join(current_path, filename))
```
