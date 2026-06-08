"""Initialization"""
from OptumGX import *
import numpy as np
# Application
gx = GX()
# Project
project_name = "Example Retaining Wall"
prj = gx.create_project(project_name)
model2d = prj.get_current_model()
# Model (2D)
model2d.name = "Embankment outline"

"""Constants"""
S_v = 2         #Vertical soil nail spacing
S_h = 1.5       #Horizontal soil nail spacing
H = 10          #Slope height
H_base = 5      #Model base height
L = 10          #Soil nail length
L_emb = 20      #Embankment length
L_base = 15     #Model base length
L_plate = 0.547 #Nail head plate length
W_foot = 30     #Embankment width at foot level
D = 30e-3       #Nail diameter

cover_h = 1     #Nail soil cover horizontal (m)
cover_v = 1     #Nail soil cover vertical (m)
alpha = 5  #Nail angle (deg)

c = 10
phi = 18
gamma = 15

y = 5
"""Geometry"""
# Soil domain outline 
model2d.add_polygon(points=[
    [0,H_base],[1/3*W_foot,H_base+H],[2/3*W_foot,H_base+H],
    [W_foot,H_base],[0,H_base]
])
model2d.add_polygon(points=[
    [0,H_base],[0,0],[30,0],[30,H_base]
])
nail_coords = []
N_vNails = int(np.ceil((H-cover_v)/S_v))
for i in range(N_vNails):
    H_nail_row = cover_v + i * S_v
    z = H_base + H_nail_row
    # At this height the embankment spans x = [H_nail_row, W_foot - H_nail_row]
    # (1:1 slopes). Subtract cover_h on each side to get the nailable width.
    curr_width = (W_foot - 2*H_nail_row) - 2*cover_h
    if curr_width < 0:
        continue
    N_hNails = int(np.floor(curr_width / S_h)) + 1
    # Center the row symmetrically: split the leftover evenly between both sides
    span = (N_hNails - 1) * S_h
    x_start = H_nail_row + cover_h + (curr_width - span) / 2
    for j in range(N_hNails):
        nail_coords.append([x_start + S_h*j, z])

"""Materials"""
# Soil domain 
soilFaces = model2d.select([1,5], types='face')
MCBasic = prj.get_material('MC Basic')
MCBasic.c = c
MCBasic.phi = phi
MCBasic.gamma_dry = gamma
model2d.set_solid(soilFaces, MCBasic)

NRmat = prj.NailRow(
    name= 'NRmat',
    diameter=30e-3,
    E= 200e3, #MPa
)
NHmat = prj.FlatPlateSteel(
    name='NHmat',
    t = 20 #mm
)

"""Extruding"""
soilFace1 = model2d.select([1,H_base-0.1], types='face')
soilFace2 = model2d.select([1,H_base+0.1], types='face')
soilFace1.settings_3d.depth_out = 0
soilFace1.settings_3d.depth_in = L_emb
soilFace2.settings_3d.depth_out = -y
soilFace2.settings_3d.depth_in = L_emb

model2d.extrude_2d_to_3d_model()
model3d = prj.get_current_model()
model3d.name = "3D Emb"

model3dReinf = model3d.clone("3D Emb reinforced")
csys = prj.create_csys_3d(origo=[0,y,0], direction_i=[1, 0.0, 0], direction_j=[0, 0.0, 1], name='CSYS 1')
for x, z in nail_coords:
    model3dReinf.add_line([x,y,z],[x, y+L*np.cos(alpha*np.pi/180),z-L*np.sin(alpha*np.pi/180)])
    sel = model3dReinf.select([x,y,z],types=['edge'])
    model3dReinf.set_connector(sel,NRmat)
    
    model3dReinf.set_active_csys(csys=csys)
    model3dReinf.add_rectangle([x-L_plate/2,z-L_plate/2],[x+L_plate/2,z+L_plate/2])
    model3dReinf.set_active_csys(csys='Global 3D')
    sel = model3dReinf.select([x,y,z],types=['face'])
    model3dReinf.set_plate(sel, NHmat)
"""Supports"""
# Set standard supports
model3d.set_standard_fixities()
model3dReinf.set_standard_fixities()

"""Analysis"""
model2d.set_run_flag(False)
model3d.set_analysis_properties(
    analysis_type='factor_of_safety',
)
model3dReinf.set_analysis_properties(
    analysis_type='factor_of_safety',
)
prj.run_analysis()

model2d.zoom_all()