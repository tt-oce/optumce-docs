# MaterialPoint

A material point test: runs an analysis on a single material without any
geometry or stages.

Properties can be assigned directly (e.g. ``test.sx0 = -120``); each
assignment is sent to the application. ``run_analysis()`` runs the test and
blocks until it completes (the run log shows in the Analysis Progress
dialog); results are then available through ``output``.

## Examples

```python
mc = project.get_material('MC Basic')
test = gx.create_material_point(name='Triax 01', material=mc, sx0=-100)
test.run_analysis()
test.output.critical_results.deviatoric_stress
test.output.solid[0].results.final_stresses.total_stresses.q.value
```

## See also

- [create_material_point](/python/functions/application/operations/create_material_point)
- [get_material_point](/python/functions/application/operations/get_material_point)
- [MaterialPointOutput](/python/functions/objects/results/MaterialPointOutput)

## Properties

<dl>
<dt>name : str</dt>
<dd>Test name.</dd>
<dt>material : str</dt>
<dd>Identifier of the tested material. Can be set with a material object, uuid or name.</dd>
<dt>test_type : str</dt>
<dd>Test type ('triaxial').</dd>
<dt>cyclic : bool</dt>
<dd>Cyclic loading.</dd>
<dt>cycles : int</dt>
<dd>Number of cycles (cyclic tests).</dd>
<dt>steps : int</dt>
<dd>Number of load steps.</dd>
<dt>load_deformation_target : str</dt>
<dd>Load stepping target ('work', 'displacement', 'multiplier').</dd>
<dt>load_deformation_w : list of float</dt>
<dd>Target values per component.</dd>
<dt>drained_undrained : str</dt>
<dd>Drainage condition ('drained', 'undrained').</dd>
<dt>sx0, sy0, sz0, sxy0, syz0, szx0 : float</dt>
<dd>Initial stresses [kPa].</dd>
<dt>sx, sy, sz, sxy, syz, szx : float</dt>
<dd>Multiplier stresses [kPa].</dd>
<dt>supportSx, supportSy, supportSz, supportSxy, supportSyz, supportSzx : bool</dt>
<dd>Stress supports. The snake_case names (support_sx, ...) work too.</dd>
<dt>uuid : str</dt>
<dd>Unique identifier of this material point test (read-only).</dd>
<dt>output : MaterialPointOutput</dt>
<dd>Results of the material point test. Contains ``critical_results`` (e.g. deviatoric_stress and volumetric_strain), per-element results through ``solid``, and - when the test produced more than one step - ``step[i]`` with the same structure per step.</dd>
</dl>

## Methods

### run_analysis()

Run this material point test.

#### Examples

```python
test.run_analysis()
```

### delete()

Remove this material point test from the project.
