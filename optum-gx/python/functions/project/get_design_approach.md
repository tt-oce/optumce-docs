# get_design_approach

The raw IDesignApproach message of one design approach: ``name``,
the positional ``parameters`` list and one field per factor. Prefer
``project.design_approach[name]``. An unknown name raises
grpc.RpcError (INVALID_ARGUMENT).

## See also

- [design_approach](/python/functions/project/design_approach)
