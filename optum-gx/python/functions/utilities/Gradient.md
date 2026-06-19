# Gradient

Gradient data (zref, zgrad, value).

## Parameters

<dl>
<dt>zref : float</dt>
<dd>Reference depth.</dd>
<dt>zgrad : float</dt>
<dd>Gradient.</dd>
<dt>value : float</dt>
<dd>Value at refrence.</dd>
</dl>

## See also

- [Map](/python/functions/utilities/Map)
- [Profile](/python/functions/utilities/Profile)

## Examples

```python
phi_gradient= Gradient(0,  1.2, 15)
prj.MohrCoulomb(
    name='MC phi_gradient',
    phi = phi_gradient)
```
