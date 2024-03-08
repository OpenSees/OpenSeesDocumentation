from openseespy import opensees as ops
from ASDConcrete3D_MakeLaws import make as make_concrete
from matplotlib import pyplot as plt
import numpy as np

# the 2D model
ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 2)

# the material (units = N, mm)
E = 30000.0
v = 0.2
fc = 30.0
ft = fc/10.0
ec = 2.0*fc/E
Gt = 0.073*fc**0.18
Gc = 2.0*Gt*(fc/ft)**2
Te, Ts, Td, Ce, Cs, Cd, lch_ref = make_concrete(E, ft, fc, ec, Gt, Gc)
ops.nDMaterial('ASDConcrete3D', 1,
	E, v, # elasticity
	'-Te', *Te, '-Ts', *Ts, '-Td', *Td, # tensile law
	'-Ce', *Ce, '-Cs', *Cs, '-Cd', *Cd, # compressive law
	'-autoRegularization', lch_ref # use auto regularization: the input Gt and Gc are NOT specific fracture energies
	)

# the plane stress
ops.nDMaterial('PlaneStress', 2, 1)

# a triangle with lch = 250
lch = 250.0
ops.node(1, 0, 0)
ops.node(2, lch, 0)
ops.node(3, 0, lch)
ops.element('tri31', 1,   1, 2, 3,   1.0, 'PlaneStress', 2)

# fixity
ops.fix(1,   1, 1)
ops.fix(2,   0, 1)
ops.fix(3,   1, 0)

# a simple ramp
ops.timeSeries('Linear', 1)

# imposed  strain
emax = 0.01
cycles = np.linspace(0.0, emax, 10)

# begin plot
SX = [0.0]
SY = [0.0]
PX = [0.0]
PY = [0.0]
plt.ion()
fig, ax = plt.subplots(1,1)
ax.grid(linestyle=':')
ax.set(xlim=[-emax*1.1, emax*0.1],ylim=[-fc*1.2, fc*0.1])
ax.set_title('Cyclic uniaxial compression')
ax.set_xlabel('\N{GREEK SMALL LETTER EPSILON}\N{SUBSCRIPT ONE}\N{SUBSCRIPT ONE}')
ax.set_ylabel('\N{GREEK SMALL LETTER SIGMA}\N{SUBSCRIPT ONE}\N{SUBSCRIPT ONE}')
the_line, = ax.plot(SX, SY, '-k', linewidth=2.0)
the_tip, = ax.plot(PX, PY, 'or', fillstyle='full', markersize=8)

# some default analysis settings
ops.constraints('Transformation')
ops.numberer('Plain')
ops.system('FullGeneral')
ops.test('NormDispIncr', 1.0e-8, 10, 0)
ops.algorithm('Newton')

for icycle in range(1, len(cycles)):
	# get current plastic strain (if any)
	ep = -ops.nodeDisp(2)[0]/lch
	# impose strain
	current_strain = cycles[icycle]
	ops.pattern('Plain', 1, 1)
	ops.sp(2, 1, -current_strain*lch)
	# load
	# start from a percentage = ep/current_strain
	time_start = ep/current_strain
	ops.setTime(time_start)
	num_incr = max(1, int((current_strain-ep)/emax*100.0))
	time_incr = (1.0-time_start)/float(num_incr) 
	ops.integrator('LoadControl', time_incr)
	ops.analysis('Static')
	for i in range(num_incr):
		ok = ops.analyze(1)
		if ok == 0:
			strain = ops.eleResponse(1, 'material', 1, 'strain')
			stress = ops.eleResponse(1, 'material', 1, 'stress')
			SX.append(strain[0])
			SY.append(stress[0])
			the_line.set_xdata(SX)
			the_line.set_ydata(SY)
			PX = [SX[-1]]
			PY = [SY[-1]]
			the_tip.set_xdata(PX)
			the_tip.set_ydata(PY)
			fig.canvas.draw()
			fig.canvas.flush_events()
		else:
			break
	if ok != 0:
		break
	# unload
	ops.remove('pattern', 1)
	ops.setTime(0.0)
	ops.integrator('LoadControl', 1.0)
	ops.analysis('Static')
	ok = ops.analyze(1)
	# plot the unload point
	strain = ops.eleResponse(1, 'material', 1, 'strain')
	stress = ops.eleResponse(1, 'material', 1, 'stress')
	SX.append(strain[0])
	SY.append(stress[0])
	the_line.set_xdata(SX)
	the_line.set_ydata(SY)
	PX = [SX[-1]]
	PY = [SY[-1]]
	the_tip.set_xdata(PX)
	the_tip.set_ydata(PY)
	fig.canvas.draw()
	fig.canvas.flush_events()

plt.ioff()
plt.show()