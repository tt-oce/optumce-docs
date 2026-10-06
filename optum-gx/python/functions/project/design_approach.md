# design_approach

The project's design approaches (partial factors), keyed by name.

## Returns

<dl>
<dt>DesignApproaches</dt>
<dd>Mapping of name -> DesignApproach; each factor is a read/write property that talks to the running application.</dd>
</dl>

## Examples

```python
project.design_approach['ULS'].gamma_unfavorable_dead_load = 1.1
project.design_approach['SLS'].gamma_favorable_user2_load
1.0
project.design_approach['ULS'].update(gamma_c=1.25, gamma_phi=1.25)
project.design_approach['User 1'].gamma_cu = 1.4    # also 'user1'
```

## See also

- [DesignApproaches](/python/functions/project/DesignApproaches)
- [DesignApproach](/python/functions/project/DesignApproach)
- [set_design_approach_parameters](/python/functions/project/set_design_approach_parameters)
