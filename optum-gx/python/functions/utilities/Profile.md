# Profile

Profile data (depth, value).

## Parameters

<dl>
<dt>data : List[List[float]]</dt>
<dd>List of depth and corresponding parameter value.</dd>
</dl>

## See also

- [ParameterMap](/python/functions/utilities/ParameterMap)
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

## Properties

<dl>
<dt>unit</dt>
<dd>Unit the values are expressed in (e.g. 'MPa'), or None if unknown.</dd>
</dl>
