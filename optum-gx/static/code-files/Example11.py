"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
project_name = "Example 11 Loukidis_seismic"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')
# Stage
stage1 = model2d.create_stage('stage 1')

"""Constants"""
a = 20
b = 50


"""Geometry"""
#Model outline
model2d.add_polygon(points=[[0, 0], [b, 0], [b, -25-a], [-99, -25-a], [-99, -25], [-75, -25]])

"""Materials"""
#Soil domain
MC = prj.MohrCoulomb(
    name='MC',
    color = rgb(79,180,63),
    c = 20,
    phi= 30,
    gamma_dry=20,
    gamma_sat=20,
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[0,-1],types='face')
model2d.set_solid(shapes=SoilFace,material=MC)

"""Loads"""
#Surcharge
model2d.set_body_load(
    shapes=SoilFace,
    value= -1,
    direction= 'x',
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
                mesh_adaptivity= 'yes',
                adaptivity_iterations=3,
                start_elements= 1000,
                time_scope='long_term'
                )
#Begin analysis
prj.run_analysis()

"""Output"""
res = [stage1.output.global_results.load_multiplier]
print("k_c =", round(9.8/res[0],ndigits=3))
#Zoom and center model
model2d.zoom_all()