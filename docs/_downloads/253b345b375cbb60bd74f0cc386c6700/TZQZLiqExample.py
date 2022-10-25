#################################################################################
# Modeling of axial load behaviour of a pile in liquefiable soil
# Sumeet Kumar Sinha, UC Davis
#################################################################################

#####################################################
# Import all the libraries
import math;
import numpy as np;
import matplotlib.pyplot as plt
import opensees as op;

###########################################################
# Starting a new model
###########################################################

Analysis_Name                = "TZQZLiq_Example"

###### Pile Properties #######
E                   = 69e6; # in kPa
Diameter            = 0.635; # outer diameter [m]
Thickness           = 0.039; # thickness [m]
Inner_Diameter      = Diameter - 2*Thickness;
A                   = math.pi*(Diameter**2-Inner_Diameter**2)/4.0;
Iz                  = math.pi/4*(Diameter**4-Inner_Diameter**4);
Iy                  = Iz;
G                   = 26e6; # in kPa
J                   = Iz+Iy;

# wipe the model
op.wipe()
# spring nodes created with 2 dim, 3 dof
op.model('basic', '-ndm', 2, '-ndf', 3) 

# create nodes
#---- Pile Node 
op.node(1,0.0,0.0);
op.node(2,0.0,0.5);
op.node(3,0.0,1.0);
#---- Soil Node 
op.node(4,0.0,0.5);
op.node(5,0.0,0);

# fix the soil nodes 
op.fix(4,1,1,1);
op.fix(5,1,1,1);

# fix x dof of the pile nodes 
op.fix(1,1,0,0);
op.fix(2,1,0,0);
op.fix(3,1,0,0);

#---------------------------------------------------------------------------
# define QZLiq and TZLiq material model for shaft and tip interafce elements
#---------------------------------------------------------------------------

# define mean stress as a time series data 
MeanStress=np.array([1.000,0.990,0.980,0.970,0.960,0.950,0.940,0.931,0.921,0.911,0.902,0.892,0.882,0.873,0.864,0.854,0.845,0.836,0.826,0.817,0.808,0.799,0.790,0.781,0.772,0.763,0.755,0.746,0.737,0.729,0.720,0.711,0.703,0.694,0.686,0.678,0.669,0.661,0.653,0.645,0.637,0.629,0.621,0.613,0.605,0.597,0.589,0.582,0.574,0.566,0.559,0.551,0.544,0.536,0.529,0.522,0.514,0.507,0.500,0.493,0.486,0.479,0.472,0.465,0.458,0.451,0.444,0.438,0.431,0.424,0.418,0.357,0.394,0.411,0.400,0.359,0.352,0.386,0.388,0.359,0.301,0.354,0.371,0.356,0.304,0.311,0.349,0.348,0.311,0.256,0.317,0.335,0.313,0.249,0.276,0.314,0.310,0.264,0.221,0.285,0.300,0.273,0.196,0.245,0.283,0.274,0.218,0.192,0.257,0.269,0.233,0.143,0.219,0.255,0.240,0.173,0.168,0.231,0.239,0.195,0.104,0.196,0.229,0.208,0.130,0.148,0.209,0.212,0.159,0.082,0.177,0.206,0.177,0.087,0.132,0.189,0.186,0.124,0.069,0.161,0.185,0.149,0.047,0.120,0.172,0.163,0.090,0.061,0.148,0.166,0.122,0.008,0.111,0.158,0.141,0.059,0.057,0.138,0.149,0.097,0.000,0.105,0.146,0.122,0.029,0.055,0.130,0.135,0.073,0.000,0.101,0.136,0.104,0.004,0.057,0.125,0.122,0.052,0.003,0.101,0.128,0.089,0.000,0.062,0.122,0.112,0.033,0.005,0.102,0.123,0.075,0.000,0.068,0.121,0.104,0.016,0.018,0.106,0.119,0.064])
MNS_TZ   = MeanStress
MNS_QZ   = 0.8*MeanStress+0.2
MNS_Time = 1.0+np.linspace(0,30.0,len(MNS_TZ));

seriesTag = 1; op.timeSeries('Path', seriesTag, '-time', *MNS_Time, '-values', *MNS_QZ, '-factor', 1.0);
seriesTag = 2; op.timeSeries('Path', seriesTag, '-time', *MNS_Time, '-values', *MNS_TZ, '-factor', 1.0);

# q-z liq
matTag =1;
qzType =1;      #qzType = 1 Backbone of q-z curve approximates Reese and O'Neill's (1987) relation for drilled shafts in clay. qzType = 2 Backbone of q-z curve approximates Vijayvergiya's (1977) relation for piles in sand.
qult   =1000.0; #Ultimate capacity of the q-z material. (kN)
qzz50  =0.02;   #Displacement at which 50% of qult is mobilized in monotonic loading. (m)
suction= 0.0;   #Uplift resistance is equal to suction*qult. Default = 0.0.
c      = 0.0;   #The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
alpha  =0.55;   #The exponent defining the decreae in the tip capacity qult,ru = qult*(1-ru)^alpha where alpha=3sin(phi')/(1-3*sin(phi')) where phi'=effective friction angle of the soil. 
op.uniaxialMaterial('QzLiq1', matTag, qzType, qult, qzz50, suction, c, alpha, '-timeSeries', 1);

# t-z liq
matTag   = 2;
soilType = 2;    #soilType = 1 Backbone of t-z curve approximates Reese and O’Neill (1987). soilType = 2 Backbone of t-z curve approximates Mosher (1984) relation.
tult     = 50;   #Ultimate capacity of the t-z material. (kN)
tzz50    = 0.001;#Displacement at which 50% of tult is mobilized in monotonic loading. (mm)
c        = 0.0;  #The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity).
op.uniaxialMaterial('TzLiq1', matTag, soilType, tult, tzz50, c,'-timeSeries', 2);

#----------------------------------------------------------
# zero-length interfac elements
#----------------------------------------------------------
eleTag = 1; node1=5; node2=1;
op.element('zeroLength', eleTag, node1, node2, '-mat', 1,  '-dir', 2);
eleTag = 2; node1=4; node2=2;
op.element('zeroLength', eleTag, node1, node2, '-mat', 2,  '-dir', 2);

#----------------------------------------------------------
# create pile elements
#----------------------------------------------------------
transfTag=1; op.geomTransf('Linear', transfTag);       #geometry transformation
eleTag = 3; node1=1; node2=2;
op.element('elasticBeamColumn', eleTag, node1, node2, A, E, Iz, transfTag);
eleTag = 4; node1=2; node2=3;
op.element('elasticBeamColumn', eleTag, node1, node2, A, E, Iz, transfTag);

#####################################
# Stage 1 : Apply Axial Load on Pile
#####################################
P          = -200;
Total_Time = 1.0;
timeStep   = 0.01; NumSteps = int(Total_Time/timeStep);

#----------------------------------------------------------
# record element forces and node displacements  
#----------------------------------------------------------
op.recorder('Element', '-file', 'QZ_Forces_Liq.txt',  '-time','-ele', 1, 'force')
op.recorder('Element', '-file', 'TZ_Forces_Liq.txt',  '-time','-ele', 2, 'force')
op.recorder('Element', '-file', 'Pile_Forces_Liq.txt','-time','-ele', 3,4, 'force')
op.recorder('Node',    '-file', 'Pile_Disp_Liq.txt',  '-time','-node', 1,2,3, '-dof',2, 'disp')

# create time series
seriesTag = seriesTag + 1;
op.timeSeries("Linear", seriesTag);

# create a plain load pattern
patternTag = 1;
op.pattern("Plain", patternTag,seriesTag)

# add load at the pile head load
loadValues = [0, P, 0.0];
op.load(3, *loadValues)

# ------------------------------
# Start of analysis generation
# ------------------------------
# create SOE
op.system('UmfPack')
# create DOF number
op.numberer('RCM')
# create constraint handler
op.constraints('Transformation')
# create integrator
op.integrator('LoadControl',timeStep,NumSteps)
# create algorithm
op.algorithm('Newton')
# create test
op.test('NormUnbalance', 1, 1000, 1)
# create analysis object
op.analysis('Static')
# perform the analysis
op.analyze(NumSteps)
op.loadConst('-time',1.00);
op.wipeAnalysis();

#----------------------------------------------------------------------------------
###################################################################################
# Stage 2 : Perform Dynamic analysis with excess pore pressure generation in soil 
###################################################################################

Total_Time= 30;                #total time of simulation
dt = 0.01;                     #time step increment
numIncr = int(Total_Time/dt)-1; #number of analysis steps to perform

#create time series
seriesTag = seriesTag + 1;
op.timeSeries('Constant',seriesTag)

#----------------------------------------------------------
# update the TZLiq and QZLiq materials
#----------------------------------------------------------
op.updateMaterialStage('-material',1,'-stage',1);
op.updateMaterialStage('-material',2,'-stage',1);

#----------------------------------------------------------
# create a plain load pattern
#----------------------------------------------------------
patternTag = patternTag+1;
op.pattern("Plain", patternTag,seriesTag)

# ------------------------------
# Start of analysis generation
# ------------------------------
# create SOE
op.system('UmfPack'); 
# create DOF number
op.numberer('RCM'); 
# create constraint handler
alpha = 1e18; op.constraints('Penalty',alpha,alpha); 
# create integrator
gamma = 0.6; beta  = 0.3; op.integrator('Newmark',gamma,beta) 
# create algorithm
op.algorithm('Newton'); 
# create test
op.test('NormUnbalance', 1e-3, 1000, 1)
# create analysis object
op.analysis('VariableTransient')
dtMin = dt/100; #Minimum time steps. (required for VariableTransient analysis)
dtMax = dt; #Maximum time steps (required for VariableTransient analysis)
Jd = 1000; #Number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge (required for VariableTransient analysis)
op.analyze(numIncr,dt,dtMin,dtMax,Jd);
op.wipe()

#################################################################
# Plot the results 
#################################################################
Pile_Disp_Liq   = np.loadtxt('Pile_Disp_Liq.txt', delimiter=' '); 
QZ_Forces_Liq   = np.loadtxt('QZ_Forces_Liq.txt', delimiter=' '); 
TZ_Forces_Liq   = np.loadtxt('TZ_Forces_Liq.txt', delimiter=' '); 
Pile_Forces_Liq = np.loadtxt('Pile_Forces_Liq.txt', delimiter=' '); 

Pile_Disp_Liq[:,1:]=Pile_Disp_Liq[:,1:]*1000;

Time = Pile_Disp_Liq[:,0];

Figure          = plt.figure(figsize=(10,8))
ru_Axis         = Figure.add_subplot(411);
Disp_Axis       = Figure.add_subplot(412);
TZQZForce_Axis  = Figure.add_subplot(413);
TZQZ_Axis       = Figure.add_subplot(414);

ru_Axis.plot(MNS_Time,1-MNS_TZ,'-b',linewidth=2, label="TZLiq");
ru_Axis.plot(MNS_Time,1-MNS_QZ,'-r',linewidth=2, label="QZLiq");
ru_Axis.set_ylabel('$r_u $');
ru_Axis.set_xlabel('Time (s)');
ru_Axis.set_xlim([0,31]);

Disp_Axis.plot(Time,-Pile_Disp_Liq[:,3],'-b',linewidth=2);
Disp_Axis.set_ylabel('Pile Disp (mm)');
Disp_Axis.set_xlabel('Time (s)');
Disp_Axis.set_xlim([0,31]);

TZQZForce_Axis.plot(Time,TZ_Forces_Liq[:,2],'-b',linewidth=2, label="TZLiq");
TZQZForce_Axis.plot(Time,QZ_Forces_Liq[:,2],'-r',linewidth=2, label="QZLiq");
TZQZForce_Axis.set_ylabel('$Force (kN)$ ');
TZQZForce_Axis.set_xlabel('Time (s)');
TZQZForce_Axis.set_xlim([0,31]);

TZQZ_Axis.plot(-Pile_Disp_Liq[:,2],TZ_Forces_Liq[:,2]/tult,'-b',linewidth=2, label="TZLiq");
TZQZ_Axis.plot(-Pile_Disp_Liq[:,1],QZ_Forces_Liq[:,2]/qult,'-r',linewidth=2, label="QZLiq");
TZQZ_Axis.set_ylabel('$t/t_{ult}, q/q_{ult}$ ');
TZQZ_Axis.set_xlabel('$z/z_{50}$');
TZQZ_Axis.set_xlim([0,25]);

handles, labels = TZQZ_Axis.get_legend_handles_labels()
Figure.legend(handles,labels, loc='upper center',ncol=2)


plt.grid(True);
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.minorticks_on();
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.tight_layout();
plt.savefig('Pile_Response_'+Analysis_Name+'.png', bbox_inches = 'tight', dpi = 800);
plt.show()
plt.close()

