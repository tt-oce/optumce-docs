# set_solver_settings

Define solver settings.

## Parameters

<dl>
<dt>solver_type : str</dt>
<dd>Type of solver. solver_type = 'Mosek' or 'Clarabel'</dd>
<dt>solver_method : str</dt>
<dd>Applied solver method. solver_method = 'QDLDL', 'FAER', 'MKL', 'Panua'</dd>
<dt>equilibrate : bool</dt>
<dd>equilibrate = True or False</dd>
</dl>

## Examples

```python
model2d.set_solver_settings(
solver_method=SolverMethod.FAER,
solver_type=SolverType.Mosek,
equilibrate=True
)
```