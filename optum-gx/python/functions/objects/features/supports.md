# Supports

Support boundary condition feature.

Properties
----------
type : str
    Support type. One of:
    - ``'full'`` – fully fixed (no displacement in any direction)
    - ``'normal'`` – fixed in the normal direction only
    - ``'tangential'`` – fixed in the tangential direction only
    - ``'vertical_roller'`` – vertical roller (free vertical, fixed horizontal)
    - ``'horizontal_roller'`` – horizontal roller (free horizontal, fixed vertical)
is_local : bool
    If True, the support is defined in the local coordinate system
    of the shape. If False, it uses the global coordinate system.

## Examples

```python
edges = model.select([0, 2.5], types='edge')
model.set_support(shapes=edges, type='full')
support = model.get_support(edges)
support.type = 'normal'
support.is_local = False
```

## Properties

<dl>
<dt>type : str</dt>
<dd>Support type: 'full', 'normal', 'tangential', 'vertical_roller', 'horizontal_roller'.</dd>
<dt>is_local : bool</dt>
<dd>Whether the support uses local coordinate system.</dd>
</dl>
