# open_project

Open GX project.

## Parameters

<dl>
<dt>file_path : str</dt>
<dd>path to file</dd>
</dl>

## Examples

```python
current_path = os.getcwd()
filename ="slope_stability.gxx"
gx.open_project(file_path=os.path.join(current_path, filename))
```
