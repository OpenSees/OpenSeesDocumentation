# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #
# 2D Undrained Cyclic Direct Simple Shear Test Using One Element        #
# University of Washington, Department of Civil and Environmental Eng   #
# Geotechnical Eng Group, L. Chen, P. Arduino - Oct 2020                #
# Basic Units are m, kN and s unless otherwise specified				#
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #

wipe

# ------------------------ #
# Test Specific parameters #
# ------------------------ #
# Initial Vertical Stress
set sigvo -101.3
# cyclic stress ratio
set CSR 0.16
# max number of cycles
set maxCycles 20
# K0
set K0 0.5
# set Poisson's ratio to match user specified K0 for applying initial confinement
set nu_gravity [expr $K0 / (1+$K0)]
set nu_dynamic 0.3
# Cutoff shear strain
set maxStrain 0.03
# Permeablity
set perm 1.0e-9
# ---------primary parameters-------------
set Dr 0.55
set Go 677.0
set hpo 0.40
set rho 0.0
# ---------secondary parameters-------------
set Patm 101.3
# all initial stress dependant parameters have negative default values
# and will be calculated during initialization
set h0 -1.0
set emax 0.8
set emin 0.5
set eInit [expr $emax - ($emax - $emin)*$Dr ]
set nb 0.5
set nd 0.1
set Ado -1.0
set zmax -1.0
set cz 250.0
set ce -1.0
set phicv 33.0
set Cgd 2.0
set Cdr -1.0
set ckaf -1.0
set Q 10.0
set R 1.5
set m_m 0.01
set Fsed_min -1.0
set p_sedo -1.0
# ---------------------------------------------
# Rayleigh damping parameter
set damp   0.01
set omega1 1.0
set omega2 2.0
set a1 [expr 2.0*$damp/($omega1+$omega2)]
set a0 [expr $a1*$omega1*$omega2]

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHCreate ModelHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

# Create a 2D model with 3 Degrees of Freedom
model BasicBuilder -ndm 2 -ndf 3

# Create nodes
node 1	0.0	0.0
node 2	1.0	0.0
node 3 	1.0	1.0
node 4	0.0	1.0

# Create Fixities
fix 1 	1 1 1
fix 2 	1 1 1
fix 3	0 0 1
fix 4 	0 0 1

equalDOF 3 4 1 2

# Create material
#          PM4Sand  tag    Dr   Go   hpo   den  Patm  h0   emax   emin  nb  nd  Ado   zmax    cz    ce     phicv  nu
nDMaterial PM4Sand   1    $Dr  $Go  $hpo  $rho $Patm $h0  $emax $emin  $nb  $nd $Ado  $zmax  $cz   $ce	  $phicv  $nu_gravity $Cgd $Cdr $ckaf $Q $R $m_m $Fsed_min $p_sedo

# set e_init 0.6
# set rho1 0.0
# nDMaterial ManzariDafalias 1 82.35 0.33 $e_init 1.35 0.7 0.055 0.8 0.5 101.3 0.02 16.18 0.996 0.64 0.75 1.5 12.5 500.0 $rho1 1 0

# nDMaterial PressureDependMultiYield02 1 2 0.0 9.0e4 2.2e5 32 0.1 80 0.5\
                                          # 26. 0.067 0.23 0.06 0.27

# Using default values for secondary parameters
# nDMaterial PM4Sand $matTag 0.61 585.0 0.28 0.0
# nDMaterial PM4Silt $matTag 44.0 -1 585 100.0 0.0
# nDMaterial PM4Silt $matTag -1 0.5 585 100.0 0.0

# Create element
element SSPquadUP   1     1 2 3 4    1  1.0   2.2e6 1.0 $perm $perm $eInit  1.0e-6
# element quadUP  1     1 2 3 4  1.0  1 2.2e6 1.0 $perm $perm
# Create analysis
constraints Penalty 1e17 1e17
test        NormDispIncr 1.0e-5 35 0
algorithm   Newton
numberer    RCM
system      ProfileSPD
integrator  Newmark [expr 5.0 / 6.0] [expr  4.0 / 9.0]
rayleigh    $a0 $a1 0.0 0.0
analysis    VariableTransient

# Apply consolidation pressure
set pNode [expr $sigvo / 2.0]
pattern Plain 1 {Series -time {0 100 1e10} -values {0 1 1} -factor 1} {
	load 3  0.0  $pNode 0.0
	load 4  0.0  $pNode 0.0
}
updateMaterialStage -material 1 -stage 0

analyze 100 1

updateMaterialStage -material 1 -stage 1
setParameter -value 0 -ele 1 FirstCall 1
# update Poisson's ratio for analysis
setParameter -value $nu_dynamic -ele 1 poissonRatio 1

# damp out any gravity wave
analyze 100 100
analyze 100 1000

puts "Finished Gravity"

# Close drainage valves
for {set x 1} {$x< 5} {incr x} {
   remove sp $x 3
}
equalDOF 3 4 3
puts "finished update fixties"

# Hold load and redefine analysis
loadConst -time 0.0
wipeAnalysis

set period      		1.;
set dT 				5e-5;
set recDT     [expr 10 * $dT]
# Create recorders
recorder Node  -nodeRange 1 4  -time -dT $recDT -file Cycdisp.out  -dof 1 2 disp
recorder Node  -nodeRange 1 4  -time -dT $recDT -file Cycpress.out -dof 3 vel

# recorder for quadUP element
# recorder Element -ele 1 -time -dT $recDT -file Cycstress.out material 1 stress
# recorder Element -ele 1 -time -dT $recDT -file Cycstrain.out material 1 strain

# recorder for SSPquadUP element
recorder Element -ele 1 -time -dT $recDT -file Cycstress.out stress
recorder Element -ele 1 -time -dT $recDT -file Cycstrain.out strain
# Create analysis
constraints Penalty 1e17 1e17
test        NormDispIncr 1.0e-5 35 0
algorithm   KrylovNewton
numberer    RCM
system      ProfileSPD
integrator  Newmark [expr 5.0 / 6.0] [expr  4.0 / 9.0]
rayleigh    $a0 0.0 0.0 0.0
analysis    Transient

# This part is modified from PDMY03 driver by Arash Khosravifar

pattern Plain 2 "Sine 0 [expr $period*$maxCycles] $period" {
	load 3 [expr -$CSR*$sigvo*1.0*1.0*0.50] 0 0
	load 4 [expr -$CSR*$sigvo*1.0*1.0*0.50] 0 0
}

while {[expr abs([nodeDisp 4 1]/1.0)]<$maxStrain} {
	analyze 1 $dT
	puts "time = [getTime] sec"
}

wipe