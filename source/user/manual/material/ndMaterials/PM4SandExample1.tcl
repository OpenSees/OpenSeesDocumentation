# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #
# 2D Undrained Direct Simple Shear Test Using One Element #
# University of Washington, Department of Civil and Environmental Eng   #
# Geotechnical Eng Group, L. Chen, P. Arduino - Jan 2018               #
# Basic Units are m, kN and s unless otherwise specified#
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #

wipe

# ------------------------ #
# Test Specific parameters #
# ------------------------ #
# Initial Vertical Stress
set sigvo -101.3
set K0 0.5
# set Poisson's ratio to match user specified K0
set nu [expr $K0 / (1+$K0)]
# Deviatoric strain (Cyclic)
set devDisp 0.10
# Permeablity
set perm 1.0e-9
# Initial void ratio
# relative density
set Dr 0.35   
# max and min void ratio  
set emax 0.8
set emin 0.5
set eInit [expr $emax - ($emax - $emin)*$Dr ]
# other primary parameters
set G0 476.0
set hpo 0.53
set rho 1.42

# Rayleigh damping parameter
set damp   0.02
set omega1 0.2
set omega2 20.0
set a1 [expr 2.0*$damp/($omega1+$omega2)]
set a0 [expr $a1*$omega1*$omega2]

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHCreate ModelHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

# Create a 2D model with 3 Degrees of Freedom
model BasicBuilder -ndm 2 -ndf 3

# Create nodes
node 10.00.0
node 21.00.0
node 3 1.01.0
node 40.01.0

# Create Fixities
fix 1 1 1 1
fix 2 1 1 1
fix 30 0 1
fix 4 0 0 1
 
equalDOF 3 4 1 2

# Create material
#          PM4Sand  tag    Dr   G0   hpo   den  Patm  h0     emax   emin  nb   nd  Ado   zmax    cz    ce     phicv  nu 
nDMaterial PM4Sand   1    $Dr  $G0  $hpo  $rho 101.3 -1.00   $emax  $emin 0.5  0.1  -1.0  -1.0  250.0  -1.00  33.0  $nu
 
# Create element
element SSPquadUP   1     1 2 3 4    1  1.0   2.2e6 1.0 $perm $perm $eInit  1.0e-5

# Create recorders
recorder Node  -nodeRange 1 4  -time -file Cycdisp.out  -dof 1 2 disp
recorder Node  -nodeRange 1 4  -time -file Cycpress.out -dof 3 vel
recorder Element -ele 1 -time -file Cycstress.out stress
recorder Element -ele 1 -time -file Cycstrain.out strain

# Create analysis
constraints Transformation
test        NormDispIncr 1.0e-5 35 1
algorithm   Newton
numberer    RCM
system      SparseGeneral
integrator  Newmark [expr 5.0 / 6.0] [expr  4.0 / 9.0]
rayleigh    $a0 $a1 0.0 0.0
analysis    Transient

# Apply consolidation pressure
set pNode [expr $sigvo / 2.0]
pattern Plain 1 {Series -time {0 100 1e10} -values {0 1 1} -factor 1} {
    load 3  0.0  $pNode 0.0
    load 4  0.0  $pNode 0.0
}
updateMaterialStage -material 1 -stage 0

analyze 100 1
set vDisp [nodeDisp 3 2]
set ts1 "{Series -time {100 80000 1.0e10} -values {1.0 1.0 1.0} -factor 1}"
eval "pattern Plain 2 $ts1 {
sp 3 2 $vDisp
sp 4 2 $vDisp
}"

# Close drainage valves
for {set x 1} {$x< 5} {incr x} {
   remove sp $x 3
}

analyze 25 1
puts "Removed drainage fixities."

updateMaterialStage -material 1 -stage 1
setParameter -value 0 -ele 1 FirstCall 1
analyze 25 1

puts "finished update fixties"

set ts2 "{Series -time {150 5150 1.0e10} -values {0.0 1.0 1.0} -factor 1}"

eval "pattern Plain 3 $ts2 {
sp 3 1 $devDisp
}"
# update Poisson's ratio for analysis
setParameter -value 0.3 -ele 1 poissonRatio 1
analyze 5000 1

wipe