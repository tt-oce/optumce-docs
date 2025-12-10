"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
prj = gx.create_project('Slope fault')
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')
# Stage
stage1 = model2d.create_stage('stage 1')
stage2 = model2d.create_stage('stage 2')

"""Geometry"""
#Model outline
model2d.add_polygon(points=[[0,0],[20,0],[30,-13],[39,-13],[39,-17],[0,-17]])
#Fault line
top=[12.65,0]
bot=[28,-17]
model2d.add_line(p0=top,p1=bot)
a_fault = (top[1]-bot[1])/(top[0]-bot[0])
#Boundary
intersect = [20.01, -8.15]

#Boundary slope
bound =  np.array([[-6,16],[14.01,13.85]])
a = (bound[0][1]-bound[1][1])/(bound[0][0]-bound[1][0])
a = np.deg2rad(-6)
temp1=[22,-6+22*a]
model2d.add_line(p0=[0,-6],p1=temp1)
model2d.delete_shapes(model2d.select(p0=temp1,types='edge'))
left = [0+1,-8+1*a] 
right = [left[0]+40,left[1]+40*a]
model2d.add_line(p0=left,p1=right)
model2d.delete_shapes(model2d.select(p0=left,types=['edge']))
model2d.delete_shapes(model2d.select(p0=right,types='edge'))
# model2d.add_line(p0=[21.9503,-10.3],p1=[28.4617, -11.0002])
#Fault line
model2d.add_line(p0=[28,-17],p1=[12.65, 0])

"""Materials"""
#Soil domain (Upper)
MC_upper = prj.MohrCoulomb(
    name='MC upper',
    color=rgb(0,109,67),
    c = 30,
    phi= 30,
    gamma_dry=24,
    gamma_sat=20,
    Kx=1e-05,
    Ky=1e-05 
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[12.65,0],types='face')
model2d.set_solid(shapes=SoilFace,material=MC_upper)
#Soil domain (Lower)
MC_lower = prj.MohrCoulomb(
    name='MC lower',
    color=rgb(117,67,49),
    c = 40,
    phi= 30,
    gamma_dry=24,
    gamma_sat=20,
    Kx=1e-05,
    Ky=1e-05 
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[28,-17],types='face')
model2d.set_solid(shapes=SoilFace,material=MC_lower)
#Fault material
MC_Fault = prj.MohrCoulomb(
    name='MC Fault',
    color=rgb(245,222,10),
    E=20,
    nu=0.2,
    c = 0,
    phi = 20,
    drainage= 'always_drained'
    )
#Select fault lines
interface = model2d.select(p0=bot,p1=top,types='edge',option='blue').values[1:4]
interface = ShapeList(items=interface,stage=model2d)
model2d.set_interface(shapes=interface,material=MC_Fault)


"""Supports"""
#Set standard supports
model2d.set_standard_fixities()

"""Analysis"""
#Define analysis parameters (stage 1)
#Deactivate fault
stage1.toggle_features(model2d.get_features(interface),value='off')
stage1.set_analysis_properties(
                analysis_type= 'factor_of_safety',
                element_type='mixed',
                no_of_elements=5000,
                mesh_adaptivity='yes',
                adaptivity_iterations=3,
                )
#Define analysis parameters (stage 1)
stage2.set_analysis_properties(
                analysis_type= 'factor_of_safety',
                element_type='mixed',
                no_of_elements=5000,
                mesh_adaptivity='yes',
                adaptivity_iterations=3,
                )
#Begin analysis
prj.run_analysis()
"""Output"""
res = [stage1.output.global_results.factor_of_safety,
       stage2.output.global_results.factor_of_safety]
print("Factor of safety without fault:", round(res[0],ndigits=3))
print("Factor of safety with fault:", round(res[1],ndigits=3))
#Zoom and center model
model2d.zoom_all()