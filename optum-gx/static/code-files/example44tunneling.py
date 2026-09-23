"""Preample"""
from OptumGX import *
import matplotlib.pyplot as plt
gx = GX()
# Project
project_name = "Tunneling using convergence-confinement method"
project = gx.create_project(project_name)
model = project.get_current_model()
model.name = "Convergence-confinement"

"""Geometry"""
###Domain
d_depth = 36
d_width = 120
model.add_rectangle([0.0, 0.0], [d_width, -d_depth])
##tunnel
t_radius = 4
t_depth = 16
model.add_circle([d_width/2, -t_depth-t_radius], t_radius, 48)

"""Materials"""
domain = model.select([
	[0,0],
	], types='face')
shapes = model.select([
	[d_width/2, -t_depth-t_radius],
	], types='face')
material = project.get_material('MC Basic')
model.set_solid(domain, material)
model.set_solid(shapes, material)
Tunnel_domain = model.get_solid(shapes)
"""Tunnel"""
Tunnel_wall =   model.select([
	[60.77869, -16.085259],
	[56.99908, -17.368264],
	[63.57981, -18.234633],
	[56.220389, -21.283005],
	[63.00092, -17.368264],
	[63.98289, -19.738948],
	[59.22131, -23.914741],
	[62.217523, -16.681243],
	[60.261052, -16.01711],
	[59.738948, -16.01711],
	[56.681243, -17.782477],
	[63.914741, -19.22131],
	[58.234633, -16.42019],
	[58.716995, -16.220389],
	[59.22131, -16.085259],
	[63.779611, -18.716995],
	[63.318757, -17.782477],
	[62.631736, -16.99908],
	[61.765367, -16.42019],
	[61.283005, -16.220389],
	[57.782477, -16.681243],
	[57.368264, -16.99908],
	[56.42019, -18.234633],
	[61.283005, -23.779611],
	[56.220389, -18.716995],
	[56.085259, -19.22131],
	[56.01711, -19.738948],
	[56.01711, -20.261052],
	[56.085259, -20.77869],
	[56.42019, -21.765367],
	[56.681243, -22.217523],
	[56.99908, -22.631736],
	[57.368264, -23.00092],
	[57.782477, -23.318757],
	[58.234633, -23.57981],
	[58.716995, -23.779611],
	[59.738948, -23.98289],
	[60.261052, -23.98289],
	[60.77869, -23.914741],
	[61.765367, -23.57981],
	[62.217523, -23.318757],
	[62.631736, -23.00092],
	[63.00092, -22.631736],
	[63.57981, -21.765367],
	[63.318757, -22.217523],
	[63.779611, -21.283005],
	[63.914741, -20.77869],
	[63.98289, -20.261052]
	], types='edge')
plate_mat = project.GeneralPlate(
    name = 'Tunnel wall',
    EA= 6e6,
    EI= 45e3,
    n_p= 10000,
    m_p= 1000,
    weight=6.472389,
)
plate = model.set_plate(Tunnel_wall, plate_mat)
support = model.set_support(shapes=Tunnel_wall, type='full')
relaxation_factors = np.linspace(0,1,11)
relax = model.set_reaction_relaxation(Tunnel_wall, relaxation=0.3)

model.set_standard_fixities()

"""Stages"""
model.zoom_all() #Zoom and center model.
stage1 = model.create_stage('Initial')
stage2 = model.create_stage('Relaxation')
stage3 = model.create_stage('Lining')

stage1.toggle_features(plate, 'off')
stage1.toggle_features(support, 'off')
stage1.toggle_features(relax, 'off')

stage2.toggle_features(Tunnel_domain,'off')
stage2.toggle_features(support,'on')
stage2.toggle_features(plate, 'off')

stage3.toggle_features(Tunnel_domain, 'off')
stage3.toggle_features(plate,'on')
stage3.toggle_features(support, 'off')

stage1.set_analysis_properties(
    analysis_type="initial_stress")
stage2.set_analysis_properties(
    analysis_type="deformation",
    from_stage=stage1)
stage3.set_analysis_properties(
    analysis_type="deformation",
    from_stage=stage2)

models = [model]
if True: #Run the whole investigation or just a single model.
	for i in range(len(relaxation_factors)):
		m_new = model.clone(name=f'λ = {relaxation_factors[i]:.1f}')
		m_new.get_reaction_relaxation(Tunnel_wall).relaxation = relaxation_factors[i]
		models.append(m_new)

else:
	relaxation_factors = [0.3]

project.run_analysis()
u1 = []
Mb = []
valid_relaxation_factors = []

for model in models:
	u1_val = None
	Mb_val = None
	relax_factor = None

	try:
		relax_factor = float(model.name.split('λ = ')[1]) if 'λ = ' in model.name else None
	except (ValueError, IndexError):
		pass

	for stage in model._Model__stages():
		if stage.name == 'Relaxation':
			try:
				results = stage.output
				if results and hasattr(results, 'critical_results'):
					u1_val = results.critical_results.u_solid_z_max
					if u1_val is not None and not np.isfinite(u1_val):
						u1_val = None
			except (IndexError, Exception):
				pass

		if stage.name == 'Lining':
			try:
				results = stage.output
				if results and hasattr(results, 'critical_results'):
					Mb_val = results.critical_results.moment_plate2d_max
					if Mb_val is not None and not np.isfinite(Mb_val):
						Mb_val = None
			except (IndexError, Exception):
				pass

	if u1_val is not None and Mb_val is not None and relax_factor is not None:
		u1.append(u1_val)
		Mb.append(Mb_val)
		valid_relaxation_factors.append(relax_factor)

if u1 and valid_relaxation_factors:
	plt.plot(u1, valid_relaxation_factors)
	plt.xlabel("settlement (mm)")
	plt.ylabel("Relaxation Factor, λ")
	plt.show()
if Mb and valid_relaxation_factors:
	plt.plot(Mb, valid_relaxation_factors)
	plt.xlabel("Moment (kNm/m)")
	plt.ylabel("Relaxation Factor, λ")
	plt.show()