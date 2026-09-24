# create_material_point

Create a material point test. The test runs on a single material - no
geometry, model or stage is involved.

## Parameters

<dl>
<dt>name : str</dt>
<dd>Test name.</dd>
<dt>test_type : str</dt>
<dd>Test type ('triaxial').</dd>
<dt>cyclic : bool|str</dt>
<dd>Cyclic loading ('true'/'false').</dd>
<dt>cycles : int</dt>
<dd>Number of cycles (cyclic tests).</dd>
<dt>material : RemoteMaterial|str</dt>
<dd>The material to test (material object, uuid or name).</dd>
<dt>load_deformation_target : str</dt>
<dd>Load stepping target ('work', 'displacement', 'multiplier').</dd>
<dt>load_deformation_w : list of float</dt>
<dd>Target values per component.</dd>
<dt>steps : int</dt>
<dd>Number of load steps.</dd>
<dt>drained_undrained : str</dt>
<dd>Drainage condition ('drained', 'undrained').</dd>
<dt>sx0, sy0, sz0, sxy0, syz0, szx0 : float</dt>
<dd>Initial stresses [kPa].</dd>
<dt>sx, sy, sz, sxy, syz, szx : float</dt>
<dd>Multiplier stresses [kPa].</dd>
<dt>supportSx, supportSy, supportSz, supportSxy, supportSyz, supportSzx : bool|str</dt>
<dd>Stress supports ('true'/'false').</dd>
</dl>

## Examples

```python
mc = project.get_material('MC Basic')
test = gx.create_material_point(
    name='Triaxial 01', test_type='triaxial', material=mc,
    load_deformation_target='work', load_deformation_w=[0, 0, 0.1],
    steps=10, drained_undrained='drained',
    sx0=-100, sy0=-100, sz0=-100, sx=0, sy=0, sz=-1)
test.run_analysis()
test.output.critical_results.deviatoric_stress
```

## See also

- [MaterialPoint](/python/functions/objects/analysis/MaterialPoint)
- [get_material_point](/python/functions/application/operations/get_material_point)
