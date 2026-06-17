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
def run_simulation(tim_noise, mod_noise, title, Npulse, Nsubsteps=50, do_plot=True):
	# USER SETTINGS
	# Steel
	Es = 210000.0
	fy = 400.0
	fu = 520.0
	eu = 0.06
	# Rebars bond-slip
	fc = 25.0
	good_bond = True
	radius = 8.0
	# finite element length (just to test mesh-dependency)
	lch = 200.0
	# Integration
	implex = True
	auto_regularization = True
	bond_slip = True
	# Compute bond-slip
	alpha = 0.4
	s3 = max(25.4, 2.0*radius)
	if good_bond:
		beta = 2.5
		s1 = 1.0
		s2 = 2.0
	else:
		beta = 1.25
		s1 = 1.8
		s2 = 3.6
	tau_max = beta * math.sqrt(fc)
	tau_f = 0.4 * tau_max
	# compute slip values
	Te = np.concatenate((np.linspace(0.0, s1, 20), np.array([s2, s3])))
	# compute tau values
	def bond_fun(s):
		if s <= s1:
			return tau_max * (s / s1) ** alpha
		elif s <= s2:
			return tau_max
		elif s <= s3:
			return tau_max - (tau_max - tau_f) * (s - s2) / (s3 - s2)
		else:
			return tau_f
	
	Ts = [bond_fun(slip) for slip in Te]

	# damage
	Td = [0.2] * len(Te)
	# Initial stiffness of the bond-slip material
	bond_stiffness = Ts[1] / Te[1]
	# Just to define an almost zero plateau
	zero_tau = 1.0e-3
	zero_tau_slip = zero_tau / bond_stiffness
	Ne = [0.0, zero_tau_slip, zero_tau_slip * 2.0]
	Ns = [0.0, zero_tau, zero_tau ]
	Nd = [1.0, 1.0, 1.0]
	
	# the 1D model
	ops.wipe()
	ops.model('basic', '-ndm', 1, '-ndf', 1)
	
	# the bond material
	ops.uniaxialMaterial('ASDConcrete1D', 21, bond_stiffness, '-Te', *Te, '-Ts', *Ts, '-Td', *Td,
						'-Ce', *Ne, '-Cs', *Ns, '-Cd', *Nd, '-secant', '-implex', '-autoRegularization',1.0)
	ops.uniaxialMaterial('ASDConcrete1D', 22, bond_stiffness, '-Te', *Ne, '-Ts', *Ns, '-Td', *Nd,
						'-Ce', *Te, '-Cs', *Ts, '-Cd', *Td, '-secant', '-implex', '-autoRegularization', 1.0)
	ops.uniaxialMaterial('ASDConcrete1D', 23, bond_stiffness, '-Te', *Te, '-Ts', *Ts, '-Td', *Td,
						'-Ce', *Te, '-Cs', *Ts, '-Cd', *Td, '-secant', '-implex', '-autoRegularization', 1.0)
	
	stiff_c = bond_stiffness*100.0
	Te = [0.0, zero_tau/stiff_c, zero_tau/stiff_c * 2.0]
	Ts = [0.0, zero_tau, zero_tau ]
	Td = [1.0, 1.0, 1.0]
	Ce = [0.0, 1.0/stiff_c, 2.0/stiff_c]
	Cs = [0.0, 1.0, 2.0 ]
	ops.uniaxialMaterial('ASDConcrete1D', 41, stiff_c, '-Te', *Te, '-Ts', *Ts, '-Td', *Td,
						'-Ce', *Ce, '-Cs', *Cs, '-Cd', *Td, '-secant', '-implex')
	
	ops.uniaxialMaterial('Parallel', 2, 21, 22, 23, 41, '-factors', 0.5, 0.5, 0.5, 1.0)
	
	# the steel material
	# steel mandatory parameters
	steel_params = [Es, fy, fu, eu]
	if implex:
		steel_params.append('-implex')
	if auto_regularization:
		steel_params.append('-auto_regularization')
	if bond_slip:
		steel_params.extend(['-slip', 2, radius])
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
	SLIP = [0.0]
	BOND = [0.0]
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
	spec = plt.GridSpec(nrows=4, ncols=6,figure=fig)
	ax = [fig.add_subplot(spec[0,:]), fig.add_subplot(spec[1:,0:3]), fig.add_subplot(spec[1:,3:])]
	
	ax[0].grid(linestyle=':')
	ax[0].set_title('Strain history')
	ax[0].set_xlabel('Time')
	ax[0].set_ylabel('\N{GREEK SMALL LETTER EPSILON}')
	
	ax[1].grid(linestyle=':')
	ax[1].set_title('Stress-strain response')
	ax[1].set_xlabel('\N{GREEK SMALL LETTER EPSILON}')
	ax[1].set_ylabel('\N{GREEK SMALL LETTER SIGMA}')
	
	ax[2].grid(linestyle=':')
	ax[2].set_title('Bond-Slip')
	ax[2].set_xlabel('Slip') #Tau vs slip
	ax[2].set_ylabel('\N{GREEK SMALL LETTER TAU}')

	# the strain history
	the_line_hist_bg, = ax[0].plot(tim_noise, mod_noise, '--k', linewidth=1.0)
	the_line_hist,    = ax[0].plot(TIME, STRAIN, 'k', linewidth=1.0)
	the_tip_hist,     = ax[0].plot(TIME_TIP, STRAIN_TIP, 'or', fillstyle='full', markersize=8)
	
	# the composite response
	the_line, = ax[1].plot(STRAIN, STRESS, '-k', linewidth=1.0)
	the_tip,  = ax[1].plot(STRAIN_TIP, STRESS_TIP, 'or', fillstyle='full', markersize=8)
	
	# the slip response
	the_line_slip, = ax[2].plot(SLIP, BOND, '-r', linewidth=1.0)
	
	
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
				# bond-slip response
				try:
					bs = ops.eleResponse(1, 'material', 1, 'SlipResponse')
					SLIP.append(bs[0])
					BOND.append(bs[1])
				except:
					BOND.append(0.0)
				
			# update
				the_line_hist.set_xdata(TIME)
				the_line_hist.set_ydata(STRAIN)
				the_line.set_xdata(STRAIN)
				the_line.set_ydata(STRESS)
				the_line_slip.set_xdata(SLIP)
				the_line_slip.set_ydata(BOND)
			
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
	images[0].save('ASDSteel1D_Ex_Bond_Slip_Output.gif', format='GIF', save_all=True, append_images=images[1:], loop=0, duration=100, disposal=2)


# To generate load history
Npulse =  50
seed=2
max_scale=4.0
eu = 0.06
random.seed(seed)
np.random.seed(seed)

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


title = f'results__slip_run'
run_simulation(tim_noise, mod_noise, title, Npulse=Npulse)