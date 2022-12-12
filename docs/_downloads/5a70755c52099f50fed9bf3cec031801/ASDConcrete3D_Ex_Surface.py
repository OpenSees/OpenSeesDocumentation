from openseespy import opensees as ops
from math import pi, sin, cos
from matplotlib import pyplot as plt

def analyze_dir (dX, dY):
	
	# info
	print("Analyze direction ({:8.3g}, {:8.3g})".format(dX, dY))
	
	# the 2D model
	ops.wipe()
	ops.model('basic', '-ndm', 2, '-ndf', 2)
	
	# the isotropic material
	E = 30000.0
	v = 0.2
	sig0 = 30.0
	# define a perfect bilinear behavior in tension and compression to record the failure surface
	fc = sig0
	ec = fc/E
	ft = fc/10.0
	et = ft/E
	ops.nDMaterial('ASDConcrete3D', 1, E, v,
		'-Ce', 0.0, ec, ec+1,
		'-Cs', 0.0, fc, fc,
		'-Cd', 0.0, 0.0, 0.0,
		'-Te', 0.0, et, et+1,
		'-Ts', 0.0, ft, ft,
		'-Td', 0.0, 0.0, 0.0)
	
	# the plane stress
	ops.nDMaterial('PlaneStress', 2, 1)
	
	# a triangle
	ops.node(1, 0, 0)
	ops.node(2, 1, 0)
	ops.node(3, 0, 1)
	ops.element('tri31', 1,   1, 2, 3,   1.0, 'PlaneStress', 2)
	
	# fixity
	ops.fix(1,   1, 1)
	ops.fix(2,   0, 1)
	ops.fix(3,   1, 0)
	
	# a simple ramp
	ops.timeSeries('Linear', 1, '-factor', 2.0*sig0)
	
	# imposed stresses in the current direction
	ops.pattern('Plain', 1, 1)
	ops.load(2,  dX, 0.0)
	ops.load(3, 0.0,  dY)

	# analyze
	ops.constraints('Transformation')
	ops.numberer('Plain')
	ops.system('FullGeneral')
	ops.test('NormDispIncr', 1.0e-6, 10, 0)
	ops.algorithm('Newton')
	
	dLambda = 0.1
	dLambdaMin = 0.0001
	Lambda = 0.0
	sX = 0.0
	sY = 0.0
	while True:
		ops.integrator('LoadControl', dLambda)
		ops.analysis('Static')
		ok = ops.analyze(1)
		if ok == 0:
			stress = ops.eleResponse(1, 'material', 1, 'stress')
			sX = stress[0]
			sY = stress[1]
			Lambda += dLambda
			if Lambda > 0.9999:
				break
		else:
			dLambda /= 2.0
			if dLambda < dLambdaMin:
				break
	
	# done
	return (sX, sY)

# number of subdivisions
NDiv = 80
NP = NDiv+1
dAngle = 2.0*pi/NDiv
SX = [0.0]*NP
SY = [0.0]*NP

plt.ion()
fig, ax = plt.subplots(1,1)
ax.set(xlim=[-45, 10],ylim=[-45, 10])
ax.plot([-1000,1000],[0,0],color='black',linewidth=0.5) # S1
ax.plot([0,0],[-1000,1000],color='black',linewidth=0.5) # S2
ax.grid(linestyle=':')
ax.set_aspect('equal', 'box')

the_line, = ax.plot(SX, SY, '-k', linewidth=2.0)
for i in range(NP):
	angle = float(i)*dAngle
	dX = cos(angle)
	dY = sin(angle)
	a,b = analyze_dir(dX, dY)
	SX[i] = a
	SY[i] = b
	the_line.set_xdata(SX)
	the_line.set_ydata(SY)
	fig.canvas.draw()
	fig.canvas.flush_events()

plt.ioff()
plt.show()