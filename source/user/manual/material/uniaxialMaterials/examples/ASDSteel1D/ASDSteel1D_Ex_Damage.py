import numpy as np
import math
import random
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.stats import norm
import time
import openseespy.opensees as ops
from PIL import Image

#Function for single run
def run_simulation(tim_noise, mod_noise, max_scale, title, Npulse=100, Nsubsteps=300, do_plot=True):
	# USER SETTINGS
	# Steel
	Es = 210000.0
	fy = 400.0
	fu = 520.0
	eu = 0.06
	# fracture
	radius = 8.0
	# finite element length (just to test mesh-dependency)
	lch = 100.0
	# Integration
	implex = True
	auto_regularization = True
	fracture = True
	
	# the 1D model
	ops.wipe()
	ops.model('basic', '-ndm', 1, '-ndf', 1)
	
	# the steel material
	# steel mandatory parameters
	steel_params = [Es, fy, fu, eu]
	if implex:
		steel_params.append('-implex')
	if auto_regularization:
		steel_params.append('-auto_regularization')
	if fracture:
		steel_params.extend(['-fracture', radius])
	ops.uniaxialMaterial('ASDSteel1D', 1, *steel_params)

	# a truss
	ops.node(1, 0)
	ops.node(2, lch)
	ops.element('truss', 1, 1, 2, 1.0, 1)
	# fixity
	ops.fix(1, 1)
	
	# a simple ramp
	ops.timeSeries('Path', 1, '-time', *tim_noise , '-values', *mod_noise )
	ops.pattern('Plain', 1, 1)
	ops.sp(2, 1, lch)
	
	# some default analysis settings
	ops.constraints('Transformation')
	ops.numberer('Plain')
	ops.system('UmfPack')
	ops.test('NormDispIncr', 1.0e-8, 10, 0)
	ops.algorithm('Newton')
	time_incr = 1.0 / (Npulse * Nsubsteps)
	ops.integrator('LoadControl', time_incr)
	ops.analysis('Static')
	
	# begin plot
	STRAIN = [0.0]
	STRESS = [0.0]
	DAMAGE = [0.0]
	RVE = [0.0]
	EQP = [0.0]
	TIME = [0.0]
	STRAIN_TIP = [0.0]
	STRESS_TIP = [0.0]
	TIME_TIP = [0.0]
	
	# plot settings
	SMALL_SIZE = 8
	MEDIUM_SIZE = 10
	LARGE_SIZE = 12
	plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
	plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
	plt.rc('figure', titlesize=LARGE_SIZE)  # fontsize of the figure title
	plt.ion()
 
	# figure and axes
	fig = plt.figure(figsize=(12, 6), dpi=100)
	spec = plt.GridSpec(nrows=5, ncols=7,figure=fig)
	ax = [fig.add_subplot(spec[0,:]), fig.add_subplot(spec[1:,0:3]), fig.add_subplot(spec[1:3,5:]), fig.add_subplot(spec[3:5,5:]), fig.add_subplot(spec[1:,3:5])]
	
	ax[0].grid(linestyle=':')
	ax[0].set_title('Strain history')
	ax[0].set_xlabel('Time')
	ax[0].set_ylabel('\N{GREEK SMALL LETTER EPSILON}')
	
	ax[1].grid(linestyle=':')
	ax[1].set_title('Stress-strain response')
	ax[1].set_xlabel('\N{GREEK SMALL LETTER EPSILON}')
	ax[1].set_ylabel('\N{GREEK SMALL LETTER SIGMA}')
	
	ax[2].grid(linestyle=':')
	ax[2].set_title('Damage')
	ax[2].set_xlabel('Time')
	ax[2].set_ylabel('D')
	
	ax[3].grid(linestyle=':')
	ax[3].set_title('Equivalent plastic strain')
	ax[3].set_xlabel('Time')   #Equivalent plastic strain vs time
	ax[3].set_ylabel('\N{GREEK SMALL LETTER EPSILON}\u209A\u2097')
	
	strain = STRAIN[-1]
	l_eff = lch * (1 + strain)
	ax[4].grid(linestyle=':')
	ax[4].set_title('RVE')
	ax[4].set_xlabel('Lateral Displacement')   #Lateral vs vertical displacement
	ax[4].set_ylabel('Vertical Displacement')
	ax[4].axvline(x=0, color='gray', linestyle = '--', linewidth=0.8)
	ax[4].set_xlim(-lch,lch)
	ax[4].set_ylim(-lch/20, lch+ max_scale*eu* lch + lch/20)

	# the strain history
	the_line_hist_bg, = ax[0].plot(tim_noise, mod_noise, '--k', linewidth=1.0)
	the_line_hist,    = ax[0].plot(TIME, STRAIN, 'k', linewidth=1.0)
	the_tip_hist,     = ax[0].plot(TIME_TIP, STRAIN_TIP, 'or', fillstyle='full', markersize=8)
	
	# the composite response
	the_line, = ax[1].plot(STRAIN, STRESS, '-k', linewidth=1.0)
	the_tip,  = ax[1].plot(STRAIN_TIP, STRESS_TIP, 'or', fillstyle='full', markersize=8)
	
	# the fracture
	the_line_damage, = ax[2].plot(TIME, DAMAGE, '-b', linewidth=1.0)
	
	#equivalent plastic strain
	the_line_eqp, = ax[3].plot(TIME, EQP, '-b', linewidth=1.0)
	
	#rve
	y_shape = np.linspace(0,lch,100)
	x_shape = np.zeros_like(y_shape)
	points = np.array([x_shape, y_shape]).T.reshape(-1, 1, 2)
	segments = np.concatenate([points[:-1], points[1:]], axis=1)
	
	# Initial uniform linewidth
	linewidths = np.full(len(segments), radius*2.0)
	
	# Create LineCollection
	the_line_rve = LineCollection(segments, colors='k', linewidths=linewidths)
	ax[4].add_collection(the_line_rve)
	# done
	fig.tight_layout(pad=2.0)



	# process each step
	time_start = time.time()
	frames = []
	for i in range(Npulse):
		failed = False
		for j in range(Nsubsteps):
			ok = ops.analyze(1)
			if not do_plot:
				if ok != 0:
					failed = True
					break
				continue
			if ok == 0:
				# time
				TIME.append(ops.getTime())
				# composite response
				STRAIN.append(ops.eleResponse(1, 'material', 1, 'strain')[0])
				STRESS.append(ops.eleResponse(1, 'material', 1, 'stress')[0])
				# damage response
				try:
					DAMAGE.append(ops.eleResponse(1, 'material', 1, 'Damage')[0])
				except:
					DAMAGE.append(0.0)
				# equivalent plastic strain response
				try:
					EQP.append(ops.eleResponse(1, 'material', 1, 'EquivalentPlasticStrain')[0])
				except:
					EQP.append(0.0)
				# RVE response
				try:
					RVE.append(ops.eleResponse(1, 'material', 1, 'BucklingIndicator')[0])
				except:
					RVE.append(0.0)
			# update
				the_line_hist.set_xdata(TIME)
				the_line_hist.set_ydata(STRAIN)
				the_line.set_xdata(STRAIN)
				the_line.set_ydata(STRESS)
				the_line_damage.set_xdata(TIME)
				the_line_damage.set_ydata(DAMAGE)
				the_line_eqp.set_xdata(TIME)
				the_line_eqp.set_ydata(EQP)
				A = RVE[-1] 
				strain = STRAIN[-1]
				l_eff = lch * (1 + strain)
				y_half = np.linspace(0, l_eff/2, 100)
				x_half = np.zeros_like(y_half)
				y_shape = np.concatenate([y_half, l_eff - y_half[::-1]])
				x_shape = np.concatenate([x_half, +x_half[::-1]])
				points = np.array([x_shape, y_shape]).T.reshape(-1, 1, 2)
				segments = np.concatenate([points[:-1], points[1:]], axis=1)
				
				# Update the line collection
				the_line_rve.set_segments(segments)
				
				n_segments = len(segments)
				mid = n_segments // 2
				
				sigma = n_segments / 20  
				
				# smooth profile (Maximum at the center and gradually decreases toward the sides)
				x = np.arange(n_segments)
				gaussian_profile = np.exp(-((x - mid) ** 2) / (2 * sigma ** 2))
				gaussian_profile = gaussian_profile / gaussian_profile.max()
				linewidth_min = radius*2.0
				linewidth_max = max(radius*2.0 * (1.0 - DAMAGE[-1]), 0.5)
				linewidths = linewidth_min + (linewidth_max - linewidth_min) * gaussian_profile
				
				the_line_rve.set_linewidths(linewidths)
			else:
				failed = True
				break
		if failed:
			break
		STRAIN_TIP = [STRAIN[-1]]
		STRESS_TIP = [STRESS[-1]]
		TIME_TIP = [TIME[-1]]
		if i == Npulse-1:
			the_tip.remove()
			the_tip_hist.remove()
		else:
			the_tip.set_xdata(STRAIN_TIP)
			the_tip.set_ydata(STRESS_TIP)
			the_tip_hist.set_xdata(TIME_TIP)
			the_tip_hist.set_ydata(STRAIN_TIP)
		for iax in ax:
			iax.relim()
			iax.autoscale_view()

		fig.canvas.draw()
		fig.canvas.flush_events()
		plt.pause(0.001)
		# store frame
		w, h = fig.canvas.get_width_height()
		buf = np.frombuffer(fig.canvas.buffer_rgba(), dtype=np.uint8)
		buf.shape = (h, w, 4)
		frame = buf[:, :, :3].copy()
	
		frames.append(frame)
	time_end = time.time()

	plt.ioff()
	plt.close(fig)
	ops.wipe()

	print(f'Saving GIF animation {title}.gif...')
	images = [Image.fromarray(frame) for frame in frames]
	images[0].save('ASDSteel1D_Ex_Damage_Output.gif', format='GIF', save_all=True, append_images=images[1:], loop=0, duration=100, disposal=2)


# To generate load history
Npulse =  50

max_scale= 4.0
eu = 0.06

mod_noise = np.linspace(0, eu * max_scale, Npulse)
mod_noise = list(mod_noise)

tim_noise = [0.0] * Npulse
for i in range(1, Npulse):
	dy = abs(mod_noise[i] - mod_noise[i-1])
	tim_noise[i] = tim_noise[i-1] + dy

tim_noise_max = tim_noise[-1]
if tim_noise_max == 0.0:
	tim_noise_max = 1.0
tim_noise = [t / tim_noise_max for t in tim_noise] 


title = f'results__damage_run'
run_simulation(tim_noise, mod_noise, max_scale, title, Npulse=Npulse)