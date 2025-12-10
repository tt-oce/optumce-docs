"""Initialization"""
from OptumGX import *
import numpy as np
import os
# Application
gx = GX()
# Project
project_name = "Example 4 Gibson soil"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')
# Stage
stage1 = model2d.create_stage('stage 1')

"""Constants"""
depth = 35
nu = 0.5 # [-]
q = 10 #kN/m^2
#Soil profile with Gibson
E = Profile([[0,0],[-depth,depth*0.3]]) #MPa
"""Geometry"""
model2d.add_rectangle(p0=[0,0],p1=[depth,-depth])
model2d.add_line(p0=[0,0],p1=[1,0])

"""Materials"""
#Soil domain
LinearElasticMaterial = prj.LinearElastic(name='LinearElasticMaterial',
                            color=rgb(0,56,122),
                            E=E,
                            nu=nu,                        
                            )
#Selecting soil domain
SoilFace = model2d.select(p0=[1,-1],types='face')
#Setting 
model2d.set_solid(shapes=SoilFace,material=LinearElasticMaterial)

"""Loads"""
#Surcharge
model2d.set_surface_load(shapes=model2d.select(p0=[0.01,0],types='edge'),
                         value=-q,
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
uy = [stage1.output.critical_results.u_solid_y_min,stage1.output.critical_results.u_solid_y_max]
uy = [x if x>=0 else -x for x in uy]
uy_max = max(uy)
print("Max vertical displacement:", round(uy_max,ndigits=5),"m")
print(f"Deviation from theoretical: {round((uy_max-0.05)/0.05*100,2)}%")
#Zoom and center model
model2d.zoom_all()

#If desired, save the GX file produced by the script by setting: save = True  
save = False
if save: #Save GX file to current working directory 
       current_path = os.getcwd()
       filename =project_name+".gxx"
       gx.save_project(file_path=os.path.join(current_path, filename))