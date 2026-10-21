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

- [ParameterMap](/python/functions/utilities/ParameterMap)
- [Profile](/python/functions/utilities/Profile)

## Examples

```python
phi_gradient= Gradient(0,  1.2, 15)
prj.MohrCoulomb(
    name='MC phi_gradient',
    phi = phi_gradient)
```

## Properties

<dl>
<dt>unit</dt>
<dd>Unit the values are expressed in (e.g. 'MPa'), or None if unknown.</dd>
</dl>
