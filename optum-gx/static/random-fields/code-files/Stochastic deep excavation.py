"""Preample"""
from OptumGX import *
gx = GX()

"""Project setup"""
project_name='Stochastic Analysis of deep excavation'
project = gx.create_project(project_name)
model = project.get_model('Model A')
model.name = 'Deep excavation'

"""Constants"""
phi = [30, 35, 40, 45]

"""Model Setup"""
model.add_rectangle([0.0, 0.0], [22.0, -15.0])
model.add_line([17, 0.0], [17.0, -13.0])
model.add_line([17.0, -3.0], [22.0, -3.0])
model.add_line([17.0, -6.0], [22.0, -6.0])


shapes = model.select([
	[18.666667, -5.0],
	[11.333333, -11.333333],
	[20.333333, -1.0]
	], types='face')
MCSand = project.MohrCoulomb(
    name='MC Sand',
    color=rgb(236, 198, 95),
    phi = 35,
    c = 0
    )
solid = model.set_solid(shapes, MCSand)


shapes = model.select([
	[17.0, -9.5],
	[17.0, -4.5],
	[17.0, -1.5]
	], types='edge')
material = project.GeneralPlate(
    name = 'Sheet Pile PU12',
    color = rgb(241, 71, 133),
    EA = 2.94e06,
    EI = 4.536e04,
    n_p=3780,
    m_p=393.4,
    weight= 110,
    )
plate = model.set_plate(shapes, material)

shapes = model.select([17.0, 0.0], types='vertex')
result_point = model.set_resultpoint(shapes=shapes)

model.set_standard_fixities()
model.mesh_adaptivity = 'yes'
IS = model.create_stage('Initial stress')
IS.analysis_type = 'initial_stress'

Ex1 = IS.create_stage('Excavation 1')
shapes = Ex1.select([20.333333, -1.0], types='face')
solid = model.get_solid(shapes)
Ex1.toggle_features(solid, "off")
Ex1.analysis_type = 'deformation'
Ex1.from_stage = IS

Ex2 = Ex1.create_stage('Excavation 2')
Ex2.analysis_type = 'deformation'
Ex2.from_stage = Ex1
shapes = Ex2.select([18.666667, -3.0], types='face')
solid = model.get_solid(shapes)
Ex2.toggle_features(solid, "off")

FoS = Ex2.create_stage('Factor of Safety')
FoS.analysis_type = 'factor_of_safety'
FoS.from_stage = Ex2

stage_names = model.get_stage()
model.zoom_all() 

print("Friction angle \phi (deg), Displacement (mm), Factor of safety" )
for i in range(len(phi)):
    MCSand.phi = phi[i]
    for j in range(len(stage_names)):
        stage = model.get_stage(name="%s" % (stage_names[j]))
        stage.set_run_flag('run')
    project.run_analysis()
    u_norm = Ex2.output.critical_results.u_norm_max
    u_x = Ex2.output.plate_resultpoint[0].results.displacements.total_displacements.u_x.value[0]
    FS = FoS.output.critical_results.factor_of_safety
    print("%.2f                      %.2f             %.2f" % (phi[i],u_x,FS) )


current_path = os.getcwd()
filename =project_name+".gxx"
gx.save_project(file_path=os.path.join(current_path, filename))


