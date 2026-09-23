# screenshot

Save an image of the current view to a PNG file.

Captures whichever view is showing, model or result, without the
canvas quick-access toolbar.

## Parameters

<dl>
<dt>file_path : str</dt>
<dd>Path to the PNG file to write. Missing folders are created, and an existing file is overwritten without warning.</dd>
</dl>

## Examples

```python
import os
gx.screenshot(file_path=os.path.join(os.getcwd(), "model.png"))
```
