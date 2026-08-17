"""Preample"""
from OptumGX import *
gx = GX()

"""Project setup"""
project_name ="Stochastic analyisis - Introductory example"
project = gx.create_project(name=project_name)
model = project.get_current_model().delete()

"""Constants"""
B = [0.5, 1, 2, 4, 8, 16]
cu = 80

"""Model setup"""
for i in range(len(B)):
    soil_width = 8*B[i]
    soil_depth = 3*B[i]
    footing_height = 0.5
    model = project.create_model(name = "Footing B = %.1f m" % (B[i]))
    model.add_rectangle([-soil_width/2, 0.0], [soil_width/2, -soil_depth])
    model.add_rectangle([-B[i]/2, 0.0], [B[i]/2, footing_height])
    
    shapes = model.select([0, -0.001], types='face')
    material = project.get_material('Tresca Basic')
    material.cu = cu
    solid = model.set_solid(shapes, material)
    
    shapes = model.select([0, 0.001], types='face')
    material = project.get_material('Rigid')
    solid = model.set_solid(shapes, material)
    
    shapes = model.select([0.0, footing_height], types='edge')
    load = model.set_surface_load(shapes, -1.0, direction='y', option='fixed',value=-249)
    
    model.set_standard_fixities()
    
    model.set_analysis_properties(
        analysis_type= 'factor_of_safety',
        mesh_adaptivity= 'yes',
        adaptivity_iterations=3)
    
"""Analysis and output"""
model.zoom_all()
project.run_analysis()

current_path = os.getcwd()
filename =project_name+".gxx"
gx.save_project(file_path=os.path.join(current_path, filename))
