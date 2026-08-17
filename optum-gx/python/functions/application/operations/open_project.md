# open_project

Open GX project.

## Parameters

<dl>
<dt>file_path : str</dt>
<dd>path to file</dd>
<dt>convert_units : bool, optional</dt>
<dd>When True (default), a file saved in a different unit system than the active session is rescaled and its materials/loads rebased to the session units on open. Set to False to load the file as-is.</dd>
</dl>

## Examples

```python
current_path = os.getcwd()
filename ="slope_stability.gxx"
gx.open_project(file_path=os.path.join(current_path, filename))
```
