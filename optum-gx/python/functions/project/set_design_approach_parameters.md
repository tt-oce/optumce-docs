# set_design_approach_parameters

Set the factors of a design approach from a positional list (legacy
form). Prefer ``project.design_approach[name].<factor> = value``.

## Parameters

<dl>
<dt>name : str</dt>
<dd>Design approach name ("SLS", "ULS", ...; case-insensitive).</dd>
<dt>parameters : list of float</dt>
<dd>Values in the order of ``DesignApproach.FIELDS``; a short list leaves the trailing factors unchanged.</dd>
</dl>

## See also

- [design_approach](/python/functions/project/design_approach)
- [DesignApproach.update](/python/functions/project/DesignApproach.update)
