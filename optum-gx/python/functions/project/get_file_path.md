# get_file_path

Get the full path of the currently opened project file.

## Returns

<dl>
<dt>str or None</dt>
<dd>The absolute path of the open project file, or None if no file is currently open (e.g. an unsaved/untitled or recovery session).</dd>
</dl>

## Examples

```python
gx.get_current_project().get_file_path()
'C:\\Users\\me\\Documents\\MyProject.gxx'
```
