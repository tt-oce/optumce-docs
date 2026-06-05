"""Initialization"""
from OptumGX import *

# Application
gx = GX()
# Project
project_name = "Example Stem Wall"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('1000_Elements', model_type='plane_strain')

"""Constants"""
# Mesh convergence study: number of elements per analysis
element_counts = [1000, 2000, 4000, 8000, 16000]

"""Geometry"""
# Soil domain outline 
model2d.add_polygon(points=[
    [0, 0], [20, 0], [25, -1], [27, -1], [27.5, -1],
    [27.5, -11], [50, -11], [50, -25], [0, -25], [0, 0]
])

# Stem wall 
model2d.add_polygon(points=[
    [23, -13.5], [30, -13.5], [30, -13], [27.5, -13],
    [27.5, -1], [27, -1], [27, -13], [23, -13], [23, -13.5]
])

"""Materials"""
# Soil domain 
MC = prj.MohrCoulomb(
    name='MC',
    color=rgb(236, 198, 95),
    E=30,
    nu=0.33,
    c=0,
    phi=35,
    drainage='always_drained',
    gamma_dry=18,
    gamma_sat=20,
)
# Selecting soil domain and setting material
SoilFace = model2d.select(p0=[5, -5], types='face')
model2d.set_solid(shapes=SoilFace, material=MC)

# Rigid wall
Wall = prj.Rigid(
    name='RigidWall',
    color=rgb(108, 136, 160),
    gamma_dry=22,
)
# Selecting wall and setting material
WallFace = model2d.select(p0=[27.25, -7], types='face')
model2d.set_solid(shapes=WallFace, material=Wall)

# Mesh size on the wall to avoid too few elements
model2d.set_mesh_size(WallFace, 0.25)

"""Supports"""
# Set standard supports
model2d.set_standard_fixities()

"""Analysis"""
# Stages: one Lower bound, one Upper bound (Strength Reduction / Factor of Safety)

model2d.set_analysis_properties(
    analysis_type='factor_of_safety',
    element_type='mixed',
    time_scope='long_term',
    mesh_adaptivity='no',
)


# Print table header
header = f"{'No Elem':>8} | {'Mixed':>7}"
print(header)
print("-" * len(header))

# Iterate over element counts and re-run
for i, n in enumerate(element_counts):
    model2d.set_analysis_properties(no_of_elements=n)
    model2d.set_run_flag('run')

    # Begin analysis
    prj.run_analysis()

    """Output"""
    mixed = model2d.output.global_results.factor_of_safety
    print(f"{n:>8} | {mixed:>7.3f}")

    # Clone the model for the next element count (skip on the last iteration)
    if i < len(element_counts) - 1:
        model2d = model2d.clone(f"{element_counts[i+1]}_Elements")

# Zoom and center model
model2d.zoom_all()

if False:  # if True: Save GX file to current working directory
    current_path = os.getcwd()
    filename = project_name + ".gxx"
    gx.save_project(file_path=os.path.join(current_path, filename))
