"""Preample"""
from OptumGX import *
gx = GX()

"""Project setup"""
project_name="Stochastic slope in clay"
project = gx.create_project(project_name)
model = project.get_model('Model A')
model.name = 'Clay slope'

"""Constants"""
cu = 70

"""Model Setup"""
model.add_polygon([[35,15], [-30,15], [-30,-15], [80,-15], [80,0], [56.42,0], [35,15]])

shapes = model.select([0, -0.001], types='face')
material = project.get_material('Tresca Basic')
material.cu = cu
solid = model.set_solid(shapes, material)

model.set_standard_fixities()

model.zoom_all()

"""Analysis and output"""
model.set_analysis_properties(
    analysis_type= 'factor_of_safety',
    # load_multiplier_multiplier = 'gravity',
    mesh_adaptivity= 'yes',
    adaptivity_iterations=3)

project.run_analysis()

print('Factor of safety: ', model.output.critical_results.factor_of_safety)

current_path = os.getcwd()
filename =project_name+".gxx"
gx.save_project(file_path=os.path.join(current_path, filename))