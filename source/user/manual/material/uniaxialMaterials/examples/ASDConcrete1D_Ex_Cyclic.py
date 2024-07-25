from openseespy import opensees as ops
from ASDConcrete1D_MakeLaws import make as make_concrete
from matplotlib import pyplot as plt
#from matplotlib.animation import PillowWriter
import numpy as np
import random
from scipy.stats import norm

class _pd_settings:
	PLASTIC_DAMAGE = 0
	PURE_DAMAGE = 1
	PURE_PLASTICITY = 2

material_tag = 1
def run_sample(
		# to save the GIF animation
		title:str = 'No Title',
		# if eta = 0.0 we have the rate-independent (inviscid) model, otherwise we have the rate-dependent (viscous) model
		eta:float = 0.0,
		# tensile plastic-damage override type
		pd_pos_override:int = _pd_settings.PLASTIC_DAMAGE,
		# compressive plastic-damage override type
		pd_neg_override:int = _pd_settings.PLASTIC_DAMAGE,
	) -> None:
	
	global material_tag
	print('Running Sample: "{}"'.format(title))
	
	# define a random input
	# adapted from: https://portwooddigital.com/2024/04/21/material-testing-with-white-noise/
	seed = 2
	random.seed(seed)
	Npulse = 150 # Number of pulses
	Nsubsteps = 50
	noise = [norm.ppf(random.random()) for i in range(Npulse)]
	mod_noise = [noise[i]*i/Npulse for i in range(Npulse)]
	max_noise = max(abs(max(mod_noise)),abs(min(mod_noise)))
	max_ref_value = 0.0005
	min_ref_value = 0.004
	mod_noise = [mod_noise[i]/max_noise*(max_ref_value if mod_noise[i] > 0.0 else min_ref_value) for i in range(Npulse)]
	tim_noise = [0.0]*Npulse
	for i in range(1, Npulse):
		dy = abs(mod_noise[i] - mod_noise[i-1])
		tim_noise[i] = tim_noise[i-1]+dy
	tim_noise_max = tim_noise[-1]
	tim_noise = [i/tim_noise_max for i in tim_noise]
	
	# the 1D model
	ops.wipe()
	ops.model('basic', '-ndm', 1, '-ndf', 1)
	
	# the material (units = N, mm)
	E = 30000.0
	v = 0.2
	fc = 30.0
	ft = fc/10.0
	ec = 2.0*fc/E
	Gt = 0.073*fc**0.18 # warning: this equation assumed fc in MPa!
	Gc = 2.0*Gt*(fc/ft)**2
	# create tensile and uniaxial laws from the make_concrete function.
	Te, Ts, Td, Ce, Cs, Cd, lch_ref = make_concrete(E, ft, fc, ec, Gt, Gc)
	# damage variables are computed for normal strength concrete.
	# however you can change them to see their effect on the cyclic response
	# damage variables range from 0 (pure plasticity) to 1 (pure damage)
	if pd_pos_override == _pd_settings.PURE_DAMAGE:
		Td = [1.0]*len(Td)
	elif pd_pos_override == _pd_settings.PURE_PLASTICITY:
		Td = [0.0]*len(Td)
	if pd_neg_override == _pd_settings.PURE_DAMAGE:
		Cd = [1.0]*len(Cd)
	elif pd_neg_override == _pd_settings.PURE_PLASTICITY:
		Cd = [0.0]*len(Cd)
	# create the material
	ops.uniaxialMaterial('ASDConcrete1D', material_tag,
		E, # elasticity
		'-Te', *Te, '-Ts', *Ts, '-Td', *Td, # tensile law
		'-Ce', *Ce, '-Cs', *Cs, '-Cd', *Cd, # compressive law
		'-autoRegularization', lch_ref, # use auto regularization: the input Gt and Gc are NOT specific fracture energies
		'-eta', eta
		)
	
	# a truss with lch = 250 mm
	lch = 250.0
	ops.node(1, 0)
	ops.node(2, lch)
	ops.element('truss', 1,   1, 2,   1.0, material_tag)
	material_tag += 1
	
	# fixity
	ops.fix(1, 1)
	
	# a simple ramp
	ops.timeSeries('Path',1,'-time',*tim_noise+[2.0],'-values',*mod_noise+[mod_noise[-1]])
	
	# begin plot
	SX = [0.0]
	SY = [0.0]
	PX = [0.0]
	PY = [0.0]
	DAMP = [0.0]
	DAMN = [0.0]
	EPLP = [0.0]
	EPLN = [0.0]
	TIM = [0.0]
	HY_PX = [0.0]
	HY_PY = [0.0]
	
	SMALL_SIZE = 8
	MEDIUM_SIZE = 10
	LARGE_SIZE = 12
	plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
	plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
	plt.rc('figure', titlesize=LARGE_SIZE)  # fontsize of the figure title
	plt.ion()
	
	fig = plt.figure(figsize=(6, 5), dpi=100)
	fig.suptitle(title)
	spec = plt.GridSpec(nrows=3, ncols=2, width_ratios=[1.5,1], figure=fig)
	ax = [fig.add_subplot(spec[0,:]), fig.add_subplot(spec[1:,0]), fig.add_subplot(spec[1,1]), fig.add_subplot(spec[2,1])]
	
	ax[0].grid(linestyle=':')
	ax[0].set_title('Strain history')
	ax[0].set_xlabel('Time')
	ax[0].set_ylabel('\N{GREEK SMALL LETTER EPSILON}\N{SUBSCRIPT ONE}\N{SUBSCRIPT ONE}')
	ax[1].grid(linestyle=':')
	ax[1].set_title('Stress-strain response')
	ax[1].set_xlabel('\N{GREEK SMALL LETTER EPSILON}\N{SUBSCRIPT ONE}\N{SUBSCRIPT ONE}')
	ax[1].set_ylabel('\N{GREEK SMALL LETTER SIGMA}\N{SUBSCRIPT ONE}\N{SUBSCRIPT ONE}')
	ax[2].grid(linestyle=':')
	ax[2].set_title('Damage')
	ax[2].set_xlabel('Time')
	ax[2].set_ylabel('Damage')
	ax[3].grid(linestyle=':')
	ax[3].set_title('Equivalent Plastic Strain')
	ax[3].set_xlabel('Time')
	ax[3].set_ylabel('Eq. Plastic Strain')
	the_line_hist_bg, = ax[0].plot(tim_noise, mod_noise, '--k', linewidth=1.0)
	the_line_hist, = ax[0].plot(TIM, SX, 'k', linewidth=1.0)
	the_tip_hist, = ax[0].plot(HY_PX, HY_PY, 'or', fillstyle='full', markersize=8)
	the_line, = ax[1].plot(SX, SY, '-k', linewidth=1.0)
	the_tip, = ax[1].plot(PX, PY, 'or', fillstyle='full', markersize=8)
	the_line_dam_pos, = ax[2].plot(TIM, DAMP, '-b', linewidth=1.0, label='D+')
	the_line_dam_neg, = ax[2].plot(TIM, DAMN, '-r', linewidth=1.0, label='D-')
	the_line_epl_pos, = ax[3].plot(TIM, EPLP, '-b', linewidth=1.0, label='Epl+')
	the_line_epl_neg, = ax[3].plot(TIM, EPLN, '-r', linewidth=1.0, label='Epl-')
	ax[2].legend()
	ax[3].legend()
	fig.tight_layout()
	
	# load
	ops.pattern('Plain', 1, 1)
	ops.sp(2, 1, lch)
	
	# some default analysis settings
	ops.constraints('Transformation')
	ops.numberer('Plain')
	ops.system('UmfPack')
	ops.test('NormDispIncr', 1.0e-8, 10, 0)
	ops.algorithm('Newton')
	time_incr = 1.0/(Npulse*Nsubsteps)
	ops.integrator('LoadControl', time_incr)
	ops.analysis('Static')
	
	# Initialize a list to store the frames
	frames = []
	
	# process each step
	for i in range(Npulse):
		failed = False
		for j in range(Nsubsteps):
			ok = ops.analyze(1)
			if ok == 0:
				TIM.append(ops.getTime())
				strain = ops.eleResponse(1, 'material', 1, 'strain')
				stress = ops.eleResponse(1, 'material', 1, 'stress')
				damage = ops.eleResponse(1, 'material', 1, 'damage')
				eqplst = ops.eleResponse(1, 'material', 1, 'equivalentPlasticStrain')
				pos_damage = damage[0]
				neg_damage = damage[1]
				pos_eqplst = eqplst[0]
				neg_eqplst = eqplst[1]
				SX.append(strain[0])
				SY.append(stress[0])
				DAMP.append(pos_damage if pos_damage > 1.0e-8 else 0.0)
				DAMN.append(neg_damage if neg_damage > 1.0e-8 else 0.0)
				EPLP.append(pos_eqplst if pos_eqplst > 1.0e-8 else 0.0)
				EPLN.append(neg_eqplst if neg_eqplst > 1.0e-8 else 0.0)
				the_line_hist.set_xdata(TIM)
				the_line_hist.set_ydata(SX)
				the_line.set_xdata(SX)
				the_line.set_ydata(SY)
				the_line_dam_pos.set_xdata(TIM)
				the_line_dam_pos.set_ydata(DAMP)
				the_line_dam_neg.set_xdata(TIM)
				the_line_dam_neg.set_ydata(DAMN)
				the_line_epl_pos.set_xdata(TIM)
				the_line_epl_pos.set_ydata(EPLP)
				the_line_epl_neg.set_xdata(TIM)
				the_line_epl_neg.set_ydata(EPLN)
			else:
				failed = True
				break
		if failed:
			break
		PX = [SX[-1]]
		PY = [SY[-1]]
		HY_PX = [TIM[-1]]
		HY_PY = [SX[-1]]
		if i == Npulse-1:
			the_tip.remove()
			the_tip_hist.remove()
		else:
			the_tip.set_xdata(PX)
			the_tip.set_ydata(PY)
			the_tip_hist.set_xdata(HY_PX)
			the_tip_hist.set_ydata(HY_PY)
		for iax in ax:
			iax.relim()
			iax.autoscale_view()
		fig.canvas.draw()
		fig.canvas.flush_events()
		# store frame
		frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
		frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
		frames.append(frame)
	
	# done
	plt.ioff()
	ops.wipe()
	
	print('Saving GIF animation...')
	from PIL import Image
	images = [Image.fromarray(frame) for frame in frames]
	images[0].save('{}.gif'.format(title), save_all=True, append_images=images[1:], loop=0, duration=100)
	images[-1].save('{}-still.png'.format(title))

run_sample(title = 'Mixed-Plastic-Damage(rate-independent)',
		eta = 0.0,
		pd_pos_override = _pd_settings.PLASTIC_DAMAGE,
		pd_neg_override = _pd_settings.PLASTIC_DAMAGE
	)
run_sample(title = 'Mixed-Plastic-Damage(rate-dependent)',
		eta = 0.001,
		pd_pos_override = _pd_settings.PLASTIC_DAMAGE,
		pd_neg_override = _pd_settings.PLASTIC_DAMAGE
	)
run_sample(title = 'Pure-Damage',
		eta = 0.0,
		pd_pos_override = _pd_settings.PURE_DAMAGE,
		pd_neg_override = _pd_settings.PURE_DAMAGE
	)
run_sample(title = 'Pure-Plasticity',
		eta = 0.0,
		pd_pos_override = _pd_settings.PURE_PLASTICITY,
		pd_neg_override = _pd_settings.PURE_PLASTICITY
	)
run_sample(title = 'Mixed-Plastic-Damage(compression)-Pure-Damage(tension)',
		eta = 0.0,
		pd_pos_override = _pd_settings.PURE_DAMAGE,
		pd_neg_override = _pd_settings.PLASTIC_DAMAGE
	)