# set_analysis_properties

Define analysis properties

## Parameters

<dl>
<dt>analysis_type : str</dt>
<dd>analysis_type = 'mesh', 'initial_stress', 'load_multiplier', 'deformation','load_deformation', 'factor_of_safety', 'seepage'</dd>
<dt>no_of_elements : int</dt>
<dd>Number of elements.</dd>
<dt>element_type : str</dt>
<dd>Type of element. element_type= 'mixed', 'lower', 'upper', 'gauss'</dd>
<dt>mesh_adaptivity : int</dt>
<dd>Adaptive mesh. mesh_adapticity = 'yes' or 'no'</dd>
<dt>adaptivity_iterations : int</dt>
<dd>Number of iterations to adapt mesh.</dd>
<dt>start_elements : int</dt>
<dd>Starting number of elements in mesh adaptivity</dd>
<dt>adaptivity_control : str</dt>
<dd>Adaptivity control type. adaptivity_control = 'shear_disipation', total_disipation','strain'</dd>
<dt>time_scope : str</dt>
<dd>Time scope type. time_scope= 'long_term', 'short_term', 'variable'</dd>
<dt>from_model : str|object</dt>
<dd>From model. from_model = 'Model A'</dd>
<dt>from_stage : str|object</dt>
<dd>From stage. from_stage = 'stage 1'</dd>
<dt>seepage_time_settings : str</dt>
<dd>Time settings for seepage. seepage_time_settings = 'steady_state' or 'transient'</dd>
<dt>seepage_target_time : int</dt>
<dd>Target time for seepage analysis.</dd>
<dt>seepage_no_of_steps : int</dt>
<dd>Number of seepage steps.</dd>
<dt>seepage_time_step_variation : str</dt>
<dd>Time step variation. seepage_time_step_variation = 'constant' or 'linear'</dd>
<dt>load_multiplier_multiplier : str</dt>
<dd>Type of load multiplier. load_multiplier_multiplier = 'load' or 'gravity'</dd>
<dt>undrained_parameters : str</dt>
<dd>undrained_parameters = 'cu' or 'coupled'</dd>
<dt>initial_stresses : str</dt>
<dd>initial_stresses = 'automatic' or 'none'</dd>
<dt>reset_displacements : str</dt>
<dd>reset_displacements = 'yes' or 'no'</dd>
<dt>load_deformation_scheme : str</dt>
<dd>load_deformation_scheme = 'target' or 'auto'</dd>
<dt>load_deformation_target : str</dt>
<dd>load_deformation_target = 'displacement' or 'work'</dd>
<dt>load_deformation_u_target : float</dt>
<dd>Target displacement.</dd>
<dt>load_deformation_no_of_steps : int</dt>
<dd>Number of steps</dd>
<dt>load_deformation_step_variation : str</dt>
<dd>Step variation. load_deformation_step_variation = 'linear' or 'constant'</dd>
<dt>deformation_target : str</dt>
<dd>Target deformation. deformation_target = 'time' or 'consolidation_degree'</dd>
<dt>deformation_time : float</dt>
<dd>Deformation time in days.</dd>
<dt>target_consolidation_percent : float</dt>
<dd>Consolidation percentage target, as decimal</dd>
<dt>deformation_no_of_steps : int</dt>
<dd>Number of steps.</dd>
<dt>deformation_time_step_variation : str</dt>
<dd>Time step variation. deformation_time_step_variation = 'linear' or 'constant'</dd>
<dt>deformation_u_target : float</dt>
<dd>Target displacement.</dd>
<dt>design_approach : str</dt>
<dd>Design approach. design_approach = 'unity', 'sls', 'uls', 'als'</dd>
<dt>reduce_strength_in : str</dt>
<dd>Strength reduction. reduce_strength_in = 'solids', 'plates', 'anchors', 'plates_and_anchors'</dd>
<dt>davis_correction : str</dt>
<dd>Apply davis correction for MCE materials. davis_correction = 'yes' or 'no'</dd>
<dt>reduce_strength_in : str</dt>
<dd>Strength reduction. reduce_strength_in = 'soil', 'plates', 'anchors', 'plates_and_anchors'</dd>
</dl>

## See also

- [get_analysis_properties](/python/functions/stage/get_analysis_properties)

## Notes

Most analysis parameters only refer to specific analysis types. element_type = 'mixed' is not applicable for axisymmetry and will be reverted to gauss. time_scope = 'variable' is only applicable for defomation analysis.

## Examples

```python
stage1.set_analysis_properties(
analysis_type='mesh',
no_of_elements=1000,
)

stage2.set_analysis_properties(
analysis_type='initial_stress',
element_type='mixed',
no_of_elements=2000,
design_approach = 'unity'
)

stage3.set_analysis_properties(
analysis_type='load_multiplier',
element_type='lower',
no_of_elements=1000,
mesh_adaptivity='yes',
adaptivity_iterations=2,
start_elements=1000,
adaptivity_control= 'shear_disipation',
from_model = '2D model',
from_stage = 'stage 1',
design_approach= 'sls',
time_scope= 'short_term',
load_multiplier_multiplier = 'load',
undrained_parameters= 'cu',
)

stage4.set_analysis_properties(
analysis_type='deformation',
element_type='upper',
no_of_elements=1000,
mesh_adaptivity='no',
adaptivity_iterations=2,
adaptivity_control= 'total_disipation',
start_elements=1000,
from_model = '2D model',
from_stage = 'stage 2',
design_approach= 'uls',
time_scope= 'long_term',
initial_stresses= 'automatic',
reset_displacements= 'yes',
deformation_target= 'time',
deformation_time= 30,
deformation_no_of_steps= 3,
deformation_time_step_variation= 'linear',
deformation_u_target= 0.1,
)

stage5.set_analysis_properties(
analysis_type='load_deformation',
element_type='gauss',
no_of_elements=1000,
mesh_adaptivity='no',
adaptivity_iterations=2,
start_elements=1000,
adaptivity_control='strain',
from_model = '2D model',
from_stage = 'stage 2',
design_approach= 'als',
time_scope= 'variable',
initial_stresses= 'none',
reset_displacements = 'no',
load_deformation_scheme= 'target',
load_deformation_target= 'displacement',
load_deformation_u_target= 0.1,
load_deformation_no_of_steps= 10,
load_deformation_step_variation= 'constant',
)

stage6.set_analysis_properties(
analysis_type='factor_of_safety',
element_type='gauss',
no_of_elements=1000,
mesh_adaptivity='yes',
adaptivity_iterations=2,
start_elements=500,
adaptivity_control='strain',
from_model = '2D model',
from_stage = 'stage 2',
design_approach= 'sls',
time_scope='long_term'
reduce_strength_in= 'soil'
)

stage7.set_analysis_properties(
analysis_type='seepage',
element_type='gauss',
no_of_elements=1000,
mesh_adaptivity='yes',
adaptivity_iterations=2,
start_elements=500,
adaptivity_control='strain',
from_model = '2D model',
from_stage = 'stage 2',
seepage_time_settings = 'transient',
seepage_target_time= 120,
seepage_no_of_steps=10,
seepage_time_step_variation = 'linear',
)
```

