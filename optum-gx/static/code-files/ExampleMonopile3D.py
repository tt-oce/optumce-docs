"""Preample"""
from OptumGX import *
import matplotlib.pyplot as plt
gx = GX()
# Project
project_name = "Monopile lateral load and result extraction"
project = gx.create_project(project_name)
model = project.get_current_model()
model.name = "Monopile 2D"

"""Geometry"""
pile_embedment = 10
pile_height = 30
pile_diam = 5
model.add_rectangle([0,0], [5*pile_diam, -30.0])
model.add_lines([
	[pile_diam/2, -pile_embedment],
	[pile_diam/2, pile_height],
    [0, pile_height]
	])

model.zoom_all()

"""Materials"""
material = project.FlatPlateSteel(
    name='Tower_plate',
    color=rgb(247, 147, 30),
    E=210e3,
    nu=0.3,
    t=80,
    gamma_dry=77
    )

shapes = model.select([[pile_diam/2, -pile_embedment],[pile_diam/2, pile_height]], types='edge', option='blue')
shapes.merge(model.select([0,pile_height],types='edge'))

plate = model.set_plate(shapes, material)

HS = project.HardeningSoil(
    name="HS Sand",
    color="#b4b55c",
    E50_ref= 55,
    Eur_ref= 164,
    Eoed_ref= 55,
    nu= 0.2,
    c= 0,
    phi= 40,
    gamma_dry= 18.5,
    gamma_sat= 20.5,
    flow_rule= "rowe",
    psi=10,
    pref=100,
    m = 0.5,
)
shapes = model.select([0,0],types='face')
soil = model.set_solid(shapes, HS)

model.set_standard_fixities()

###Result point
model.set_resultpoint(shapes)
"""2D to 3D"""
model3d = model.revolve_2d_to_3d(angle_deg=180,N=8,name='Monopile 3D')

model3d.delete_interior(model3d.select([0,0,1],types='face')) #remove the autodetected enclosed face created by revolving  the pile.
"""Load"""
shapes = model.select([0, pile_height], types='point')
load = model.set_line_load(
    shapes,
    option='multiplier',
    coordinate_system = 'local',
    direction = 'x',
    value = 1.0
    )
shapes = model3d.select([0, 0, pile_height], types='point')
load = model3d.set_point_load(
    shapes,
    option='multiplier',
    coordinate_system = 'local',
    direction = 'x',
    value = 1.0
    )

"""Analysis"""
model.set_analysis_properties(
    analysis_type='load_multiplier'
    )

model3d.set_analysis_properties(
    analysis_type='load_multiplier'
    )
project.run_analysis()

"""Elements to extract results from"""


"""Function to extract results along pile"""
def extract(element_start, element_end, CalculationStage, Output):
    if len(element_start) != len(element_end):
        raise ValueError("Element start and end points must be of same dimension.")
    stage = CalculationStage
    model = stage if hasattr(stage, "model_type") else stage.model #Determine model or stage
    is_3d = model.model_type == ModelType.three_dimensional #Determine model type
    vertical_axis = 2 if is_3d else 1

    shapes = stage.select( #Select shapes
        element_start,
        element_end,
        types="face" if is_3d else "edge",
        option="blue",
    )
    print(shapes)
    shape_ids = {shape.id for shape in shapes}  #Get shape ids

    plate_res = Output.plate
    
    elements = [
        plate_res[i] for i in range(len(plate_res))
        if plate_res[i].general.shape_id in shape_ids
    ]
    print(elements)
    points = []
    
    for element in elements:
        ux = element.results.displacements.total_displacements.u_x.value if is_3d else element.results.collapse_mechanism.u_x.value
        mesh = element.mesh
        start = element.element_index * mesh.element_size
        node_ids = mesh.indices[start:start + mesh.element_size]
    
        for node_id, value in zip(node_ids, ux):
            if node_id != 0xFFFFFFFF:
                elevation = Output.vertices[3 * node_id + vertical_axis]
                points.append((elevation, value))
    depth, displacement = zip(*sorted(points))
    
    return depth, displacement


"""Extract results"""
model_res = model.output
depth, displacement = extract([2.5, -10],[2.5, 30],model,model_res)
plt.plot(displacement, depth, ".-")
depth, displacement = extract([2.5, 0, -10],[2.3097, 0.956709, 30],model,model_res)
plt.plot(displacement, depth, ".-")
plt.xlabel("Total horizontal displacement, $u_x$")
plt.ylabel("Elevation")
plt.grid()


plt.show()
