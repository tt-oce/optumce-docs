"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
project_name = "Example Retaining Wall"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')

"""Constants"""
phi = [35, 25, 15, 0]


"""Geometry"""
# Model outline
model2d.add_polygon(points=[[0, 0], [0,-15], [28, -15], [28, 8], [15, 7], [15, -3], [13, -3], [13, 0], [0, 0]])
# Retaining wall
model2d.add_polygon(points=[[13, 0], [14, 7], [15, 7],[15, -3], [13, -3], [13, 0]])

"""Materials"""
#Soil domain
MC = prj.MohrCoulomb(
    name='MC',
    color = rgb(79,180,63),
    E = 30,
    nu = 0.33,
    c = 0,
    phi= 35,
    drainage= 'always_drained',
    gamma_dry= 16,
    gamma_sat= 18,
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[0,-1],types='face')
model2d.set_solid(shapes=SoilFace,material=MC)

# Rigid wall
RWall = prj.Rigid(
       name= 'Retaining Wall',
       gamma_dry= 22,
)
#Selecting wall and setting material
WallFace = model2d.select(p0=[14,0],types='face')
model2d.set_solid(shapes=WallFace,material=RWall)

#Selecting and setting interfaces
interface_mat = prj.MohrCoulomb(
    name='MC Interface',
    color = rgb(79,180,63),
    E = 30,
    nu = 0.33,
    c = 0,
    drainage= 'always_drained',
    gamma_dry= 16,
    gamma_sat= 18,
    )
shapes = model2d.select([15.0, 2.0], types='edge')
model2d.set_interface(shapes, interface_mat)

shapes = model2d.select([14.0, -3.0], types='edge')
model2d.set_interface(shapes, interface_mat)

shapes = model2d.select([13.0, -1.5], types='edge')
model2d.set_interface(shapes, interface_mat)

"""Supports"""
#Set standard supports
model2d.set_standard_fixities()

"""Analysis and output"""
# Stages
stage1 = model2d.create_stage('Lower')
# Define analysis parameters

stage1.set_analysis_properties(
        analysis_type='factor_of_safety',
        element_type='mixed',
        no_of_elements=2000,
        time_scope='long_term'
)

# Clone stages
stage2 = model2d.create_stage('Upper')
stage3 = model2d.create_stage('Mixed')

stage2.set_analysis_properties(
        analysis_type='factor_of_safety',
        element_type='upper',
        no_of_elements=2000,
        time_scope='long_term'
)
stage3.set_analysis_properties(
        analysis_type='factor_of_safety',
        element_type='mixed',
        no_of_elements=2000,
        time_scope='long_term', 
)

#Print table header
header = f"{'ϕ (°)':>6} | {'Lower':>7} | {'Upper':>7} | {'Mixed':>7} | {'Stability':>10}"
print(header)
print("-" * len(header))

#Iterate over the friction angles
for i in range(len(phi)):
    interface_mat.phi = phi[i]
    stage1.set_run_flag('run')
    stage2.set_run_flag('run')
    stage3.set_run_flag('run')
    #Begin analysis
    prj.run_analysis()

    res = [
        stage1.output.global_results.factor_of_safety,
        stage2.output.global_results.factor_of_safety,
        stage3.output.global_results.factor_of_safety
        ]
    stability = "Stable" if res[2] >= 1 else "Unstable"
    print(f"{interface_mat.phi:>6.0f} | {res[0]:>7.2f} | {res[1]:>7.2f} | {res[2]:>7.2f} | {stability:>10}")

#Zoom and center model
model2d.zoom_all()

if False: #if True: Save GX file to current working directory 
       current_path = os.getcwd()
       filename =project_name+".gxx"
       gx.save_project(file_path=os.path.join(current_path, filename))
