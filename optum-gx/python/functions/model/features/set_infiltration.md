# set_infiltration

Set a uniform infiltration boundary condition on the selected shapes.

## Parameters

<dl>
<dt>shapes : Shape | ShapeList</dt>
<dd>Boundary shapes on which to prescribe infiltration.</dd>
<dt>infiltration : float</dt>
<dd>Flux per unit boundary area, positive into the domain and negative out of it. Uses the feature's own unit: mm/day for SI projects, in/day for US projects.</dd>
</dl>

## Returns

<dl>
<dt>Infiltrations</dt>
<dd>The created infiltration features.</dd>
</dl>

## See also

- [get_infiltration](/python/functions/model/features/get_infiltration)
- [Infiltrations](/python/functions/objects/features/Infiltrations)
