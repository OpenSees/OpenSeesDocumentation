#Created by Zhaohui Yang (zhyang@ucsd.edu)
#elastic pressure independent material
#plane strain,  single element,  dynamic analysis (input motion: sinusoidal acceleration at base)  
#SI units (m, s, KN, ton)
#
#         4     3
#         ------- 
#         |     |
#         |     |
#         |     |
#        1-------2   (nodes 1 and 2 fixed)
#         ^     ^
#          <--> input motion: sinusoidal acceleration at base
wipe
#
#some user defined variables
# 
set accMul   9.81     ;
set massDen  2.000      ;# solid mass density
set fluidDen 1.0        ;# fluid mass density
set massProportionalDamping   0.0 ;
set stiffnessProportionalDamping 0.001 ;
set cohesion 30 ;
set peakShearStrain 0.1 ;
set E1      90000.0      ;#Young's modulus
set poisson1 0.40 ;
set G [expr $E1/(2*(1+$poisson1))] ;
set B [expr $E1/(3*(1-2*$poisson1))] ;
set press    0        ;# isotropic consolidation pressure on quad element(s)
set period   1        ;# Period of applied sinusoidal load
set deltaT   0.01     ;# time step for analysis
set numSteps 2000     ;# Number of analysis steps
set gamma    0.5      ;# Newmark integration parameter
set pi 3.1415926535     ;
set inclination 0       ;
set unitWeightX [expr  ($massDen-$fluidDen)*9.81*sin($inclination/180.0*$pi)] ;# buoyant unit weight in X direction
set unitWeightY [expr -($massDen-$fluidDen)*9.81*cos($inclination/180.0*$pi)] ;# buoyant unit weight in Y direction
#############################################################

#create the ModelBuilder
model basic -ndm 2 -ndf 2

# define material and properties
nDMaterial PressureIndependMultiYield 2 2 $massDen $G $B  $cohesion $peakShearStrain
nDMaterial FluidSolidPorous 1 2 2 2.2e6

    
# define the nodes
node 1   0.0 0.0 
node 2   1.0 0.0 
node 3   1.0 1.0 
node 4   0.0 1.0

# define the element      thick  material      maTag   press  density  gravity 
element quad  1  1 2 3 4  1.0   "PlaneStrain"     2   $press  0.0    $unitWeightX  $unitWeightY  

updateMaterialStage -material 2 -stage 0

# fix the base in vertical direction
fix 1 1 1 
fix 2 1 1

#############################################################
# GRAVITY APPLICATION (elastic behavior)
# create the SOE, ConstraintHandler, Integrator, Algorithm and Numberer
system ProfileSPD
test NormDispIncr 1.e-12 25 0
constraints Transformation
integrator LoadControl 1 1 1 1
algorithm Newton 
numberer RCM

# create the Analysis
analysis Static

#analyze 
analyze 2

#############################################################
# NOW APPLY LOADING SEQUENCE AND ANALYZE (plastic)
# rezero time
setTime 0.0
wipeAnalysis

equalDOF 3 4   1 2    ;#tie nodes 3 and 4

# create a LoadPattern
pattern UniformExcitation 1 1 -accel "Sine 0 10 $period -factor $accMul"

# create the Analysis
constraints Penalty 1.0e18 1.0e18  ;# Transformation;  # 
test NormDispIncr 1.e-12 25 0
algorithm Newton 
numberer RCM
system ProfileSPD
rayleigh $massProportionalDamping 0.0 $stiffnessProportionalDamping 0.
integrator Newmark $gamma  [expr pow($gamma+0.5, 2)/4]  
analysis VariableTransient 

#create the recorder
recorder Node -file disp.out   -time  -node 1 2 3 4 -dof 1 2 -dT  0.01 disp
recorder Node -file acce.out  -time  -node 1 2 3 4 -dof 1 2 -dT 0.01 accel
recorder Element -ele 1 -time -file stress1.out -dT 0.01 material 1 stress 
recorder Element -ele 1 -time -file strain1.out -dT 0.01 material 1 strain 
recorder Element -ele 1 -time -file stress3.out -dT 0.01 material 3 stress 
recorder Element -ele 1 -time -file strain3.out -dT 0.01 material 3 strain 

#analyze 
set startT [clock seconds]
analyze $numSteps $deltaT [expr $deltaT/100] $deltaT 10
set endT [clock seconds]
puts "Execution time: [expr $endT-$startT] seconds."

wipe  #flush ouput stream
