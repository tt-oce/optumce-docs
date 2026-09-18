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
"""Screenshot model"""
# Zoom and center model
model2d.zoom_all()
gx.screenshot(file_path='Geometry.png') #Screenshot settings: Application settings->Display->Screenshot
"""Analysis"""
#Define analysis parameters

model2d.set_analysis_properties(
                analysis_type= 'factor_of_safety',
                element_type='mixed',
                no_of_elements=2000,
                mesh_adaptivity= True,
                adaptivity_iterations=3,
                time_scope= 'long_term',
                )
#Begin analysis
prj.run_analysis()

"""Post processing"""
###Save results in object to avoid excessive interaction with GX API.
res = model2d.output
###Output
FoS = res.critical_results.factor_of_safety
print("Factor of safety:", round(FoS,ndigits=3))

###Pictures
model2d.take_picture(
       result_path='Solid/Seepage/Saturation/S',
       file_path='Saturation.png',
       options={
            'width': 2000,
            'height': 1500,
            'mesh_overlay': True,
            'medium':"print",
            'grid':False,
            'colorbar_min':0,
            'colorbar_max':1,
            'colorbar_text_scale':1.5,
            })
#Obtain the maximum shear dissipation
smax = np.max([res.solid[i].results.plasticity.shear_dissipation.value for i in range(len(res.solid))])

model2d.take_picture(
        result_path='Solid/Plasticity/Shear dissipation',
        file_path='SlipSurface.png',
        options={
            'width': 2000,
            'height': 1500,
            'mesh_overlay': True,
            'medium':"print",
            'grid':False,
            'colorbar_min':0,
            'colorbar_max':smax*0.9,
            'colorbar_text_scale':1.5,
            
            }
)



#If desired, save the GX file produced by the script by setting: save = True  
save = False
if save: #Save GX file to current working directory 
       current_path = os.getcwd()
       filename =project_name+".gxx"
       gx.save_project(file_path=os.path.join(current_path, filename))

