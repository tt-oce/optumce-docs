"""Preample"""
from OptumGX import *
gx = GX()

"""Project setup"""
project_name ="Stochastic analysis - Footing in clay"
project = gx.create_project(name=project_name)
model = project.get_current_model().delete()
model = project.create_model(name = 'Footing in clay')

"""Constants"""
width = 16; depth = 6; embedment = 1; B = 2

"""Model Setup"""
model.add_rectangle([-width/2,0], [width/2,-depth])
model.add_rectangle([-B/2,0], [B/2,-embedment])

shapes = model.select([0, -0.001], types='face')
material = project.get_material('Rigid')
solid = model.set_solid(shapes, material)

shapes = model.select([0, -embedment-0.001], types='face')
material = project.get_material('Tresca Basic')
profile = Profile([
    [0.0, 10.0],
    [-10.0, 40.0]
])
material.c_u = profile
# material.c_u = Gradient(zref=0.0, zgrad=-3.0, value=10.0)
solid = model.set_solid(shapes, material)



shapes = model.select([0.0, 0.0], types='edge')
load = model.set_surface_load(shapes, -1.0, direction='y', option='multiplier')

model.set_standard_fixities()

model.zoom_all()

"""Analysis and output"""
model.set_analysis_properties(
    analysis_type= 'load_multiplier',
    mesh_adaptivity= 'yes',
    adaptivity_iterations=3)

project.run_analysis()

print('Factor of safety: ', model.output.critical_results.load_multiplier)

current_path = os.getcwd()
filename =project_name+".gxx"
gx.save_project(file_path=os.path.join(current_path, filename))