# Profile

Profile data (depth, value).

## Parameters

<dl>
<dd>List[List[float]] List of depth and corresponding parameter value.</dd>
</dl>

## See also

- [Map](/python/functions/utilities/Map)
- [Gradient](/python/functions/utilities/Gradient)

## Examples

```python
gamma_profile= Profile([
    [0, 15],
    [-3, 18],
    [-5, 20],
 ])
prj.MohrCoulomb(
    name='MC gamma_profile',
    gamma_dry = gamma_profile,
    )
```
