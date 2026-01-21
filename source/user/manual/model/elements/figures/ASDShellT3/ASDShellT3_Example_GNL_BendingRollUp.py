from openseespy import opensees as ops
import opsvis as opsv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# model and section
ops.model('basic', '-ndm', 3, '-ndf', 6)
E = 1e4
h = 1.0
ops.section('ElasticMembranePlateSection', 1, E, 0.0, h)

# mesh
Lx = 20.0
Ly = 1.0
Nx = 20
Ny = 1
dLx = Lx/Nx
dLy = Ly/Ny
for j in range(Ny+1):
	offset = j*(Nx+1)
	jY = j*dLy
	for i in range(Nx+1):
		iX = i*dLx
		ops.node(offset+i+1, iX, jY, 0.0)
a1 = (0,1,3)
a2 = (1,2,3)
b1 = (0,1,2)
b2 = (0,2,3)
ele_id = 1
for j in range(Ny):
	for i in range(Nx):
		qids = (j*(Nx+1)+i+1, j*(Nx+1)+i+2, (j+1)*(Nx+1)+i+2, (j+1)*(Nx+1)+i+1)
		t1,t2 = a1,a2
		if (i+j) % 2 != 1:
			t1,t2 = b1,b2
		ops.element('ASDShellT3', ele_id, *[qids[k] for k in t1], 1, '-corotational')
		ops.element('ASDShellT3', ele_id+1, *[qids[k] for k in t2], 1, '-corotational')
		ele_id += 2

# fix
for j in range(Ny+1):
	ops.fix(j*(Nx+1)+1, 1,1,1,1,1,1)

# load
Nrolls = 2
M = (Nrolls*2.0*math.pi*E*h**3/12/Lx)
dM = M/Ny/2
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)
for j in range(Ny):
	i = Nx-1
	n1 = j*(Nx+1)+i+2
	n2 = (j+1)*(Nx+1)+i+2
	ops.load(n1, 0,0,0,0,-dM,0)
	ops.load(n2, 0,0,0,0,-dM,0)

# analysis
duration = 1.0
nsteps = 40
dt = duration/nsteps
dt_record = 0.2
ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('UmfPack')
ops.test('NormDispIncr', 1.0e-5, 100, 0)
ops.algorithm('Newton')
ops.integrator('LoadControl', dt)
ops.analysis('Static')
fig = plt.figure()
ax1 = fig.add_subplot(121, projection=Axes3D.name)
ax2 = fig.add_subplot(122)
ctime = 0.0
time = [0.0]*(nsteps+1)
Uz = [0.0]*(nsteps+1)
Ry = [0.0]*(nsteps+1)
CNode = (Nx+1)*(Ny+1)
for i in range(nsteps):
	print('step {} of {}'.format(i+1, nsteps))
	if ops.analyze(1) != 0:
		break
	ctime += dt
	if ctime > dt_record:
		ctime = 0.0
		opsv.plot_defo(sfac=1.0, node_supports=False, ax=ax1,
			unDefoFlag=0)
	time[i+1] = ops.getTime()
	Uz[i+1] = ops.nodeDisp(CNode, 3)
	Ry[i+1] = -ops.nodeDisp(CNode, 5)
ax1.axis('off')
ax2.plot(time, Uz, '-xk', label='Uz')
ax2.plot(time, Ry, '-xr', label='Ry')
ax2.set_xlabel('Load factor')
ax2.set_ylabel('Uz(displacement)-Ry(rotation)')
ax2.legend()
ax2.grid(True)

# compute exact solution at Nrolls number of rotations
ref_Uz = 0.0
ref_Ry = Nrolls*2*math.pi
num_Uz = Uz[-1]
num_Ry = Ry[-1]
fmt_str = ' | '.join(['{:>12s}']*4)
fmt_num = ' | '.join(['{:>12s}'] + ['{:12.3g}']*3)
print('Summary')
print(fmt_str.format('Value', 'Exact', 'Numerical', 'Error'))
print(fmt_num.format('Uz', ref_Uz, num_Uz, abs(num_Uz-ref_Uz)))
print(fmt_num.format('Ry', ref_Ry, num_Ry, abs(num_Ry-ref_Ry)))

# show plot
plt.show()