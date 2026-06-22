# ParameterMap

Map data (x, y, z, value).

## Parameters

<dl>
<dt>data : List[List[float]]</dt>
<dd>List of coordinates and corresponding parameter value.</dd>
</dl>

## See also

- [Profile](/python/functions/utilities/Profile)
- [Gradient](/python/functions/utilities/Gradient)

## Examples

```python
c_map = ParameterMap([
    [      2,    0,       1,  50.548 ],
    [  1.785,    0,   0.783,  47.444 ],
    [      2,    0,   0.667,  55.074 ],
    [ 1.6667,    0,       1,  47.398 ],
    [      2,    0,   0.333,  59.481 ],
    [  1.785,    0,   0.217,  56.275 ],
    [      2,    0,       0,  62.736 ],
    [ 1.6667,    0,       0,  56.639 ],
    [ 0.3333,    0,       0,  34.833 ],
    [ 0.2151,    0,   0.217,  39.318 ],
    [      0,    0,       0,  37.735 ],
    [      0,    0,   0.333,  49.557 ],
    [      0,    0,   0.667,  62.669 ],
    [  0.215,    0,   0.783,  59.746 ],
    [      0,    0,       1,  74.451 ],
    ])
prj.MohrCoulomb(
    name='MC c_map',
    c = c_map
    )
```
