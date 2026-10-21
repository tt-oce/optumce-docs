# DesignApproaches

The project's design approaches keyed by name, as a read-only mapping.

Names match ignoring case, spaces and underscores: ``['uls']`` finds
"ULS", and ``['User 1']``, ``['user1']`` or ``['user_1']`` all find
"User 1". An unknown name raises KeyError. Iteration yields the names
in GUI order.

## Examples

```python
project.design_approach['ULS'].gamma_unfavorable_dead_load = 1.1
list(project.design_approach)
['Unity', 'SLS', 'ULS', 'ALS', 'User 1', 'User 2', 'User 3', 'User 4']
for name, approach in project.design_approach.items():
    print(name, approach.gamma_c)
```

## See also

- [DesignApproach](/python/functions/objects/settings/DesignApproach)
- [Project.design_approach](/python/functions/project/operations/design_approach)

## Methods

<a id="get"></a>
### get()

Get name of design approach

<a id="keys"></a>
### keys()

Get design approach keys

<a id="values"></a>
### values()

Get design approach values

<a id="items"></a>
### items()

Get design approach items
