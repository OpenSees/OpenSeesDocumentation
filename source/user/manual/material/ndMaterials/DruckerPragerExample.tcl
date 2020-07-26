#########################################################
##
# File is generated for the purposes of testing the#
#Drucker-Prager model --> conventional triaxial #
# compression test#
##
#   Created:  03.16.2009 CRM#
#   Updated:  12.02.2011 CRM#
##
# ---> Basic units used are kN and meters#
##
#########################################################

#-------------------------------------------------------
# create the modelBuilder and build the model
#-------------------------------------------------------
wipe

model BasicBuilder -ndm 3 -ndf 3

#--create the nodes
node 11.00.00.0
node 21.01.00.0
node 3 0.01.00.0
node 40.00.00.0
node 51.00.01.0
node 6 1.01.01.0
node 7 0.01.01.0
node 8 0.00.01.0

#--triaxial test boundary conditions
fix 1 0 1 1
fix 2 0 0 1
fix 31 0 1
fix 4 1 1 1
fix 50 1 0
fix 6 0 0 0
fix 71 0 0
fix 8 1 1 0

#--define material parameters for the model
#---bulk modulus
set k       27777.78
#---shear modulus
set G       9259.26
#---yield stress
set sigY    5.0
#---failure surface and associativity
set rho     0.398
set rhoBar  0.398
#---isotropic hardening
set Kinf    0.0
set Ko     0.0
set delta1  0.0
#---kinematic hardening
set H     0.0
set theta   1.0
#---tension softening
set delta2  0.0
#---mass density
        set mDen    1.7

#--material models
#   type         tag  k   G   sigY   rho   rhoBar   Kinf   Ko   delta1   delta2   H   theta   density 
nDMaterial DruckerPrager 2    $k  $G  $sigY  $rho  $rhoBar  $Kinf  $Ko  $delta1  $delta2  $H  $theta  $mDen

#--create the element
#type tag  nodesmatID  bforce1  bforce2  bforce3
element stdBrick 1    1 2 3 4 5 6 7 8   2      0.0      0.0      0.0

puts "model Built..."

#-------------------------------------------------------
# create the recorders
#-------------------------------------------------------
set step 0.1

# record nodal displacements
recorder Node -file displacements1.out -time -dT $step -nodeRange 1 8 -dof 1 2 3 disp

# record the element stress, strain, and state at one of the Gauss points
recorder Element -ele 1 -time -file stress1.out  -dT $step  material 2 stress
recorder Element -ele 1 -time -file strain1.out  -dT $step  material 2 strain
recorder Element -ele 1 -time -file state1.out   -dT $step  material 2 state

puts "recorders set..."

#-------------------------------------------------------
# create the loading
#-------------------------------------------------------

#--pressure magnitude
set p 10.0
set pNode [expr -$p/4] 

#--loading object for hydrostatic pressure
pattern Plain 1 {Series -time {0 10 100} -values {0 1 1} -factor 1} { 
    load 1  $pNode 0.00.0
    load 2  $pNode$pNode0.0
    load 3  0.0$pNode  0.0
    load 5  $pNode  0.00.0
    load 6  $pNode$pNode0.0
    load 7 0.0$pNode0.0
}

#--loading object deviator stress
pattern Plain 2 {Series -time {0 10 100} -values {0 1 5} -factor 1} { 
    load 5  0.00.0$pNode
    load 6  0.00.0$pNode
    load 7  0.00.0$pNode
    load 8  0.00.0$pNode
}

#-------------------------------------------------------
# create the analysis
#-------------------------------------------------------

integrator LoadControl 0.1
numberer RCM
system SparseGeneral
constraints Transformation
test NormDispIncr 1e-5 10 1
algorithm Newton
analysis Static

puts "starting the hydrostatic analysis..."
set startT [clock seconds]
analyze 1000

set endT [clock seconds]
puts "triaxial shear application finished..."
puts "loading analysis execution time: [expr $endT-$startT] seconds."

wipe