"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
project_name = 'Example 1 Shallow foundation'
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')
# Stage
stage1 = model2d.create_stage('stage 1')

"""Geometry"""
model2d.add_line(p0=[0,0],p1=[20,0])
model2d.add_line(p0=[20,0],p1=[20,7])
model2d.add_line(p0=[20,7],p1=[10,7])
model2d.add_line(p0=[10,8],p1=[10,6])
model2d.add_line(p0=[10,6],p1=[11,6])
model2d.add_line(p0=[11,6],p1=[11,5])
model2d.add_line(p0=[11,5],p1=[8,5])
model2d.add_line(p0=[8,5],p1=[8,6])
model2d.add_line(p0=[8,6],p1=[9,6])
model2d.add_line(p0=[9,6],p1=[9,8])
model2d.add_line(p0=[9,8],p1=[9.7,8])
model2d.add_line(p0=[9.7,8],p1=[10,8])
model2d.add_line(p0=[9,7],p1=[0,7])
model2d.add_line(p0=[0,7],p1=[0,0])

"""Materials"""
#Soil domain
Tresca1 = prj.Tresca(name='Tresca1',
       color= rgb(195,105,54),
       Eu = 40,
       cu = 30,
       gamma_dry= 20,
       gamma_sat= 20,
       tension_cutoff= 'yes',
       sigma_t = 0,
       K0=0.5,
       hydraulic_conductivity_option= 'anisotropic',
       Kx=0.01,
       Ky=0.01,
       Kz=0.01,
       alpha=0.5,
       )
#Selecting soil domain
SoilFace = model2d.select(p0=[1,1],types='face')
#Setting 
model2d.set_solid(shapes=SoilFace,material=Tresca1)
#Rigid footing
RigidMaterial = prj.Rigid(name="Rigid1",
       color=rgb(r=108,g=136,b=160),
       gamma_dry=24)
f = model2d.select(p0=[9.5,7],types=['face'])
model2d.set_solid(shapes=f,material=RigidMaterial)
"""Loads"""
#Surcharge
model2d.set_surface_load(shapes=model2d.select(p0=[9.5,8],types='edge'),
                         value=-1,
                         direction='y',
                         coordinate_type= 'local',
                         option='multiplier')

"""Supports"""
#Set standard supports
model2d.set_standard_fixities()

"""Analysis"""
#Define analysis parameters
stage1.set_analysis_properties(
                analysis_type='load_multiplier',
                element_type='mixed',
                no_of_elements=1000,
                )
#Begin analysis
prj.run_analysis()

"""Output"""
res = [stage1.output.global_results.load_multiplier]
print("Capacity:", round(res[0],ndigits=1),"kN/m^2")
#Zoom and center model
model2d.zoom_all()

#If desired, save the GX file produced by the script by setting: save = True  
save = False
if save: #Save GX file to current working directory 
       current_path = os.getcwd()
       filename =project_name+".gxx"
       gx.save_project(file_path=os.path.join(current_path, filename))