"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
prj = gx.create_project('Basic slope stability')
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')
# Stage
stage1 = model2d.create_stage('stage 1')

"""Geometry"""
#Model outline
model2d.add_polygon(points=[[0,0],[8,0],[16,-7],[21,-7],[21,-9],[0,-9]])
#Layer boundary
model2d.add_line(p0=[0,-5],p1=[21,-5])
#Select and remove the part of the line outside of model outline
sel = model2d.select(p0=[20,-5],types="edge")
model2d.delete_shapes(sel)

"""Materials"""
#Soil domain (Upper)
Firm_Clay = prj.MohrCoulomb(
    name='Firm Clay',
    color=rgb(119,67,56),
    E = 25,
    nu=0.3,
    c = 10,
    phi= 20,
    gamma_dry=20,
    gamma_sat=20,                  
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[1,-1],types='face')
model2d.set_solid(shapes=SoilFace,material=Firm_Clay)
#Soil domain (Lower)
Stiff_Clay = prj.MohrCoulomb(
    name='Stiff Clay',
    color=rgb(84,47,38),
    E = 50,
    nu=0.25,
    c = 20,
    phi= 22,
    gamma_dry=21,
    gamma_sat=21,                  
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[1,-6],types='face')
model2d.set_solid(shapes=SoilFace,material=Stiff_Clay)

"""Supports"""
#Set standard supports
model2d.set_standard_fixities()

"""Analysis"""
#Define analysis parameters
stage1.set_analysis_properties(
                analysis_type= 'factor_of_safety',
                element_type='mixed',
                no_of_elements=1000,
                mesh_adaptivity='yes',
                adaptivity_iterations=3,
                )
#Begin analysis
prj.run_analysis()

"""Output"""
res = [stage1.output.global_results.factor_of_safety]
print("Factor of safety:", round(res[0],ndigits=3))
#Zoom and center model
model2d.zoom_all()