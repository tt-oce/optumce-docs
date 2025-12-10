"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
project_name = "Example 3 Strip footing"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')
# Stage
stage1 = model2d.create_stage('stage 1')

"""Constants"""
B = 2 #m
E = 30 #MPa
nu = 0.2 # [-]
q = 150 #kN/m^2
factor = q*B/(E*10**3) #m
"""Geometry"""

model2d.add_rectangle(p0=[0,0],p1=[7,4])
model2d.add_rectangle(p0=[0,4],p1=[B/2,4+1/4])


"""Materials"""
#Soil domain
LinearElasticMaterial = prj.LinearElastic(name='LinearElasticMaterial',
                            color=rgb(0,56,122),
                            E=E,
                            nu=nu,                        
                            )
#Selecting soil domain
SoilFace = model2d.select(p0=[1,1],types='face')
#Setting 
model2d.set_solid(shapes=SoilFace,material=LinearElasticMaterial)
#Rigid footing
RigidMaterial = prj.Rigid(name="Rigid1",
       color=rgb(r=108,g=136,b=160),
       )
f = model2d.select(p0=[0,4.1],types=['face'])
model2d.set_solid(shapes=f,material=RigidMaterial)

#Surcharge
model2d.set_surface_load(shapes=model2d.select(p0=[0.01,4+1/4],types='edge'),
                         value=-150,
                         direction='y',
                         coordinate_type= 'local',
                         option='fixed')
"""Supports"""
#Set standard supports
model2d.set_standard_fixities()

"""Analysis"""
#Define analysis parameters
stage1.set_analysis_properties(
                analysis_type='deformation',
                element_type='mixed',
                no_of_elements=10000,
                )
#Begin analysis
prj.run_analysis()

"""Output"""
res = [stage1.output.global_results.max_displacement]
print("Max displacement:", round(res[0],ndigits=5),"m")
print(f"Constant factor q*B/E = {factor}\nbeta = {round(res[0]/factor,3)} for nu = {nu}")
#Zoom and center model
model2d.zoom_all()

#If desired, save the GX file produced by the script by setting: save = True  
save = False
if save: #Save GX file to current working directory 
       current_path = os.getcwd()
       filename =project_name+".gxx"
       gx.save_project(file_path=os.path.join(current_path, filename))