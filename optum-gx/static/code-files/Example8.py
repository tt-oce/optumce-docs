"""Preample"""
from OptumGX import *
import matplotlib.pyplot as plt
gx = GX()
# Project
project_name = "Example 8 Slope seepage"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model',model_type='plane_strain')

"""Geometry"""
depth = 12
#Model outline
model2d.add_polygon(points=[[0,0],[15,0],[25,-7],[32,-7],[32,-depth],[0,-depth]])
#Layer boundary (lower)
model2d.add_line(p0=[0,-5],p1=[32,-5])
#Select and remove the part of the line outside of model outline
sel = model2d.select(p0=[30,-5],types="edge")
model2d.delete_shapes(sel)
#Layer boundary (upper)
model2d.add_line(p0=[0,-1],p1=[32,-1])
#Select and remove the part of the line outside of model outline
sel = model2d.select(p0=[30,-1],types="edge")
model2d.delete_shapes(sel)

"""Materials"""
#Soil domain (Upper)
Soft_Clay = prj.MohrCoulomb(
    name='Soft Clay',
    color=rgb(185,137,129),
    c = 5,
    phi= 25,
    gamma_dry=19,
    gamma_sat=19,
    K0=0.69, 
    drainage='drained_undrained'
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[1,-0.5],types='face')
model2d.set_solid(shapes=SoilFace,material=Soft_Clay)
#Soil domain (middle)
Firm_Clay = prj.MohrCoulomb(
    name='Firm Clay',
    color=rgb(119,67,56),
    c = 10,
    phi= 20,
    gamma_dry=20,
    gamma_sat=20,
    K0=0.66,
    drainage='drained_undrained'                     
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[1,-2],types='face')
model2d.set_solid(shapes=SoilFace,material=Firm_Clay)
#Soil domain (Lower)
Stiff_Clay = prj.MohrCoulomb(
    name='Stiff Clay',
    color=rgb(84,47,38),
    c = 20,
    phi= 22,
    gamma_dry=21,
    gamma_sat=21,
    K0=0.63, 
    drainage='drained_undrained',
    )
#Selecting soil domain and setting material
SoilFace = model2d.select(p0=[1,-7],types='face')
model2d.set_solid(shapes=SoilFace,material=Stiff_Clay)

"""Supports"""
#Set standard supports
model2d.set_standard_fixities()
"""Groundwater"""
#Select and set groundwater level at toe
sel = model2d.select(p0=[30,-7],types='edge')
model2d.set_water_table(sel)
#Select left boundary up to the soft clay layer
sel = model2d.select(p0=[0,-1],p1=[0,-depth],types='edge',option='blue')
#Set fixed head
model2d.set_fixed_head(sel,head=-1) #Head y-coordinate

"""Stages"""
stage1 = model2d.create_stage('Seepage')
stage2 = model2d.create_stage('Fos')

"""Analysis"""
#Define analysis parameters
stage1.set_analysis_properties(
                analysis_type= 'seepage',
                element_type='mixed',
                no_of_elements=2000,
                mesh_adaptivity='yes',
                adaptivity_iterations=3,
                time_scope= 'long_term'
                )
stage2.set_analysis_properties(
                analysis_type= 'factor_of_safety',
                element_type='mixed',
                no_of_elements=2000,
                time_scope= 'long_term',
                from_stage=stage1
                )
#Begin analysis
prj.run_analysis()

"""Output"""
res = [stage2.output.global_results.factor_of_safety]
print("Factor of safety:", round(res[0],ndigits=3))
#Zoom and center model
model2d.zoom_all()

#If desired, save the GX file produced by the script by setting: save = True  
save = False
if save: #Save GX file to current working directory 
       current_path = os.getcwd()
       filename =project_name+".gxx"
       gx.save_project(file_path=os.path.join(current_path, filename))
