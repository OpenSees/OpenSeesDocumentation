from opensees import *
from math import sqrt

wipe()

# define a 3D model
model("basic","-ndm",3,"-ndf",6)

# the response spectrum function
timeSeries(
	"Path",1,"-time",
	0.0,0.06,0.1,0.12,0.18,0.24,0.3,0.36,0.4,0.42,
	0.48,0.54,0.6,0.66,0.72,0.78,0.84,0.9,0.96,1.02,
	1.08,1.14,1.2,1.26,1.32,1.38,1.44,1.5,1.56,1.62,
	1.68,1.74,1.8,1.86,1.92,1.98,2.04,2.1,2.16,2.22,
	2.28,2.34,2.4,2.46,2.52,2.58,2.64,2.7,2.76,2.82,
	2.88,2.94,3.0,3.06,3.12,3.18,3.24,3.3,3.36,3.42,
	3.48,3.54,3.6,3.66,3.72,3.78,3.84,3.9,3.96,4.02,
	4.08,4.14,4.2,4.26,4.32,4.38,4.44,4.5,4.56,4.62,
	4.68,4.74,4.8,4.86,4.92,4.98,5.04,5.1,5.16,5.22,
	5.28,5.34,5.4,5.46,5.52,5.58,5.64,5.7,5.76,5.82,
	5.88,5.94,6.0,
	"-values",
	0.2,0.38,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4762,
	0.4167,0.3704,0.3333,0.303,0.2778,0.2564,0.2381,0.2222,0.2083,0.1961,
	0.1852,0.1754,0.1667,0.1587,0.1515,0.1449,0.1389,0.1333,0.1282,0.1235,
	0.119,0.1149,0.1111,0.1075,0.1042,0.101,0.098,0.0952,0.0926,0.0901,
	0.0877,0.0855,0.0833,0.0813,0.0794,0.0775,0.0758,0.0741,0.0725,0.0709,
	0.0694,0.068,0.0667,0.0641,0.0616,0.0593,0.0572,0.0551,0.0531,0.0513,
	0.0495,0.0479,0.0463,0.0448,0.0434,0.042,0.0407,0.0394,0.0383,0.0371,
	0.036,0.035,0.034,0.0331,0.0322,0.0313,0.0304,0.0296,0.0289,0.0281,
	0.0274,0.0267,0.026,0.0254,0.0248,0.0242,0.0236,0.0231,0.0225,0.022,
	0.0215,0.021,0.0206,0.0201,0.0197,0.0193,0.0189,0.0185,0.0181,0.0177,
	0.0174,0.017,0.0167,
	"-factor",9.806)

# a uniaxial material for transverse shear
uniaxialMaterial("Elastic",2,938000000.0)

# the elastic beam section and aggregator
section("Elastic",1,30000000000.0,0.09,0.0006749999999999999,0.0006749999999999999,12500000000.0,0.0011407499999999994)
section("Aggregator",3,2,"Vy",2,"Vz","-section",1)

# nodes and masses
node(1,0,0,0)
node(2,0,0,3,"-mass",200,200,200,0,0,0)
node(3,4,0,3,"-mass",200,200,200,0,0,0)
node(4,4,0,0)
node(5,0,0,6,"-mass",200,200,200,0,0,0)
node(6,4,0,6,"-mass",200,200,200,0,0,0)
node(7,4,3,6,"-mass",200,200,200,0,0,0)
node(8,0,3,6,"-mass",200,200,200,0,0,0)
node(9,0,3,3,"-mass",200,200,200,0,0,0)
node(10,0,3,0)
node(11,4,3,3,"-mass",200,200,200,0,0,0)
node(12,4,3,0)
node(13,2,1.5,6)
node(14,2,1.5,3)

# beam elements
beamIntegration("Lobatto", 1, 3, 5)
# beam_column_elements forceBeamColumn
# Geometric transformation command
geomTransf("Linear", 1, 1.0, 0.0, -0.0)
element("forceBeamColumn", 1, 1, 2, 1, 1)
# Geometric transformation command
geomTransf("Linear", 2, 0.0, 0.0, 1.0)
element("forceBeamColumn", 2, 2, 3, 2, 1)
# Geometric transformation command
geomTransf("Linear", 3, 1.0, 0.0, -0.0)
element("forceBeamColumn", 3, 4, 3, 3, 1)
# Geometric transformation command
geomTransf("Linear", 4, 1.0, 0.0, -0.0)
element("forceBeamColumn", 4, 2, 5, 4, 1)
# Geometric transformation command
geomTransf("Linear", 5, 0.0, 0.0, 1.0)
element("forceBeamColumn", 5, 5, 6, 5, 1)
# Geometric transformation command
geomTransf("Linear", 6, 0.0, 0.0, 1.0)
element("forceBeamColumn", 6, 7, 6, 6, 1)
# Geometric transformation command
geomTransf("Linear", 7, 0.0, 0.0, 1.0)
element("forceBeamColumn", 7, 8, 7, 7, 1)
# Geometric transformation command
geomTransf("Linear", 8, 0.0, 0.0, 1.0)
element("forceBeamColumn", 8, 9, 2, 8, 1)
# Geometric transformation command
geomTransf("Linear", 9, 0.0, 0.0, 1.0)
element("forceBeamColumn", 9, 8, 5, 9, 1)
# Geometric transformation command
geomTransf("Linear", 10, 1.0, 0.0, -0.0)
element("forceBeamColumn", 10, 10, 9, 10, 1)
# Geometric transformation command
geomTransf("Linear", 11, 1.0, 0.0, -0.0)
element("forceBeamColumn", 11, 3, 6, 11, 1)
# Geometric transformation command
geomTransf("Linear", 12, 1.0, 0.0, -0.0)
element("forceBeamColumn", 12, 11, 7, 12, 1)
# Geometric transformation command
geomTransf("Linear", 13, 0.0, 0.0, 1.0)
element("forceBeamColumn", 13, 11, 3, 13, 1)
# Geometric transformation command
geomTransf("Linear", 14, 0.0, 0.0, 1.0)
element("forceBeamColumn", 14, 9, 11, 14, 1)
# Geometric transformation command
geomTransf("Linear", 15, 1.0, 0.0, -0.0)
element("forceBeamColumn", 15, 12, 11, 15, 1)
# Geometric transformation command
geomTransf("Linear", 16, 1.0, 0.0, -0.0)
element("forceBeamColumn", 16, 9, 8, 16, 1)

# Constraints.sp fix
fix(1, 1, 1, 1, 1, 1, 1)
fix(10, 1, 1, 1, 1, 1, 1)
fix(4, 1, 1, 1, 1, 1, 1)
fix(12, 1, 1, 1, 1, 1, 1)
fix(13, 0, 0, 1, 1, 1, 0)
fix(14, 0, 0, 1, 1, 1, 0)

# Constraints.mp rigidDiaphragm
rigidDiaphragm(3, 14, 2, 3, 9, 11)
rigidDiaphragm(3, 13, 5, 6, 7, 8)

# define some analysis settings
constraints("Transformation")
numberer("RCM")
system("UmfPack")
test("NormUnbalance", 0.0001, 10)
algorithm("Linear")
integrator("LoadControl", 0.0)
analysis("Static")

# run the eigenvalue analysis with 7 modes
# and obtain the eigenvalues
eigs = eigen("-genBandArpack", 7)

# compute the modal properties
modalProperties("-print", "-file", "ModalReport.txt", "-unorm")

# define a recorder for the (use a higher precision otherwise the results
# won't match with those obtained from eleResponse)
filename = 'ele_1_sec_1.txt'
recorder('Element', '-file', filename, '-closeOnWrite', '-precision', 16, '-ele', 1, 'section', '1', 'force')

# some settings for the response spectrum analysis
tsTag = 1 # use the timeSeries 1 as response spectrum function
direction = 1 # excited DOF = Ux

# currently we use same damping for each mode
dmp = [0.05]*len(eigs)
# we don't want to scale some modes...
scalf = [1.0]*len(eigs)
# CQC function
def CQC(mu, lambdas, dmp, scalf):
	u = 0.0
	ne = len(lambdas)
	for i in range(ne):
		for j in range(ne):
			di = dmp[i]
			dj = dmp[j]
			bij = lambdas[i]/lambdas[j]
			rho = ((8.0*sqrt(di*dj)*(di+bij*dj)*(bij**(3.0/2.0))) /
				((1.0-bij**2.0)**2.0 + 4.0*di*dj*bij*(1.0+bij**2.0) + 
				4.0*(di**2.0 + dj**2.0)*bij**2.0))
			u += scalf[i]*mu[i] * scalf[j]*mu[j] * rho;
	return sqrt(u)

# ========================================================================
# TEST 01
# run a response spectrum analysis for each mode.
# then do modal combination in post-processing.
# ========================================================================
responseSpectrum(tsTag, direction)

# read the My values [3rd column] for each step 
# (1 for each mode, they are section forces associated to each modal displacement)
My = []
with open(filename, 'r') as f:
	lines = f.read().split('\n')
	for line in lines:
		if len(line) > 0:
			tokens = line.split(' ')
			My.append(float(tokens[2]))

# post process the results doing the CQC modal combination for the My response (3rd column in section forces)
MyCQC = CQC(My, eigs, dmp, scalf)

print('\n\nTEST 01:\nRun a Response Spectrum Analysis for each mode.\nDo CQC combination in post processing.\n')
print('{0: >10}{1: >15}'.format('Mode', 'My'))
for i in range(len(eigs)):
	print('{0: >10}{1: >15f}'.format(i+1, My[i]))
print('{0: >10}{1: >15f}'.format('CQC', MyCQC))

# ========================================================================
# TEST 02
# run a response spectrum analysis mode-by-mode.
# grab results during the loop, not using the recorder
# then do modal combination in post-processing.
# ========================================================================
remove('recorder', 0)
My = []
for i in range(len(eigs)):
	responseSpectrum(tsTag, direction, '-mode', i+1)
	force = eleResponse(1, 'section', '1', 'force')
	My.append(force[2])

# post process the results doing the CQC modal combination for the My response (3rd column in section forces)
MyCQC = CQC(My, eigs, dmp, scalf)

print('\n\nTEST 01:\nRun a Response Spectrum Analysis mode-by-mode.\nGrab results during the loop.\nDo CQC combination in post processing.\n')
print('{0: >10}{1: >15}'.format('Mode', 'My'))
for i in range(len(eigs)):
	print('{0: >10}{1: >15f}'.format(i+1, My[i]))
print('{0: >10}{1: >15f}'.format('CQC', MyCQC))

# done
wipe()
