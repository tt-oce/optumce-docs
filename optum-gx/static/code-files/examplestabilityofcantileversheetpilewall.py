"""Initialization"""
from OptumGX import *

# Application
gx = GX()
# Project
project_name = "Example Cantilever Sheet Pile Wall"
prj = gx.create_project(project_name)
prj.get_current_model().delete()
# Model (2D)
model2d = prj.create_model('2D model', model_type='plane_strain')

"""Constants"""
# Soil-wall interface Reduction Factor r = tan(phi_i) / tan(phi)
r_values = [1.0, 0.5, 0.0]
# Two strength-reduction modes (matches Table 14.1 / Table 14.2 in the report)
modes = [('Solids', 'soil'), ('Plates', 'plates')]

"""Geometry"""
model2d.add_polygon(points=[
    [0, 0], [20, 0], [20, -6], [40, -6], [40, -20], [0, -20], [0, 0]
])
# Embedded part of the wall (interior line; plate assigned along it)
model2d.add_line(p0=[20, -6], p1=[20, -12])

"""Materials"""
# Soil (Mohr-Coulomb, purely frictional, always drained)
MC = prj.MohrCoulomb(
    name='MC',
    color=rgb(79, 180, 83),
    E=30,
    nu=0.25,
    c=0,
    phi=35,
    drainage='always_drained',
    gamma_dry=18,
    gamma_sat=20,
)
SoilFace = model2d.select(p0=[10, -10], types='face')
model2d.set_solid(shapes=SoilFace, material=MC)

# Cantilever Sheet pile
Plate = prj.GeneralPlate(
    name='Cantilever',
    color=rgb(241, 181, 13),
    EA=4e6,
    EI=1e5,
    n_p=5000,
    m_p=800,
    weight=0,
    permeable='no',
    reducible_strength='yes',
)

"""Supports"""
# Set standard supports
model2d.set_standard_fixities()

"""Analysis"""
# Lower and upper bound stages for Strength Reduction (Factor of Safety)
stage_lb = model2d.create_stage('LB')
stage_ub = model2d.create_stage('UB')

# Common analysis settings (2000 elements, no mesh adaptivity, long term)
for stg, etype in [(stage_lb, 'lower'), (stage_ub, 'upper')]:
    stg.set_analysis_properties(
        analysis_type='factor_of_safety',
        element_type=etype,
        no_of_elements=2000,
        time_scope='long_term',
        mesh_adaptivity='no',
    )

# Iterate over (mode, r) and print one table per mode
for table_label, mode in modes:
    print(f"\n=== Strength Reduction in {table_label} ===")
    header = f"{'r':>5} | {'Lower':>7} | {'Upper':>7} | {'Mean±Err':>14}"
    print(header)
    print("-" * len(header))

    for r in r_values:
        # (Re)apply the plate to the wall edges with the current reduction factor
        wall_exposed = model2d.select(p0=[20, -3], types='edge')
        wall_embedded = model2d.select(p0=[20, -9], types='edge')
        model2d.set_plate(shapes=wall_exposed, material=Plate,
                          strength_reduction_factor=r)
        model2d.set_plate(shapes=wall_embedded, material=Plate,
                          strength_reduction_factor=r)

        # Choose which set of strengths is reduced (Solids vs Structs/Plates)
        stage_lb.set_analysis_properties(reduce_strength_in=mode)
        stage_ub.set_analysis_properties(reduce_strength_in=mode)
        stage_lb.set_run_flag('run')
        stage_ub.set_run_flag('run')

        # Begin analysis
        prj.run_analysis()

        """Output"""
        lower = stage_lb.output.global_results.factor_of_safety
        upper = stage_ub.output.global_results.factor_of_safety
        mean = (lower + upper) / 2
        err = (upper - lower) / 2
        print(f"{r:>5.2f} | {lower:>7.2f} | {upper:>7.2f} | {mean:>5.2f} ± {err:>4.2f}")

# Zoom and center model
model2d.zoom_all()

if False:  # if True: Save GX file to current working directory
    current_path = os.getcwd()
    filename = project_name + ".gxx"
    gx.save_project(file_path=os.path.join(current_path, filename))
