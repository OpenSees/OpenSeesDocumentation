# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #
# 3D Undrained Conventional Triaxial Compression Test Using One Element #
# University of Washington, Department of Civil and Environmental Eng   #
# Geotechnical Eng Group, A. Ghofrani, P. Arduino - Dec 2013            #
# Basic units are m, Ton(metric), s#
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH #

wipe

# ------------------------ #
# Test Specific parameters #
# ------------------------ #
# Confinement Stress
set pConf -300.0
# Deviatoric strain
set devDisp -0.3
# Permeablity
set perm 1.0e-10
# Initial void ratio
set vR 0.8

# Rayleigh damping parameter
set damp   0.1
set omega1 0.0157
set omega2 64.123
set a1 [expr 2.0*$damp/($omega1+$omega2)]
set a0 [expr $a1*$omega1*$omega2]

# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHCreate ModelHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
# HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

# Create a 3D model with 4 Degrees of Freedom
model BasicBuilder -ndm 3 -ndf 4

# Create nodes
node 11.00.00.0
node 21.01.00.0
node 3 0.01.00.0
node 40.00.00.0
node 51.00.01.0
node 6 1.01.01.0
node 7 0.01.01.0
node 8 0.00.01.0

# Create Fixities
fix 1 0 1 1 1
fix 2 0 0 1 1
fix 31 0 1 1
fix 4 1 1 1 1
fix 50 1 0 1
fix 6 0 0 0 1
fix 71 0 0 1
fix 8 1 1 0 1


# Create material
#          ManzariDafalias  tag    G0   nu   e_init   Mc    c    lambda_c    e0    ksi   P_atm   m    h0   ch    nb  A0      nd   z_max   cz    Den  
nDMaterial ManzariDafalias   1    125  0.05   $vR    1.25  0.712   0.019    0.934  0.7    100   0.01 7.05 0.968 1.1 0.704    3.5    4     600  1.42  

# Create element
#       SSPbrickUP  tag    i j k l m n p q  matTag  fBulk  fDen    k1    k2   k3   void   alpha    <b1 b2 b3>
element SSPbrickUP   1     1 2 3 4 5 6 7 8    1     2.2e6   1.0  $perm $perm $perm  $vR   1.5e-9 

# Create recorders
recorder Node    -file disp.out   -time -nodeRange 1 8 -dof 1 2 3 disp
recorder Node    -file press.out  -time -nodeRange 1 8 -dof 4     vel
recorder Element -file stress.out -time stress
recorder Element -file strain.out -time strain
recorder Element -file alpha.out  -time alpha
recorder Element -file fabric.out -time fabric


# Create analysis
constraints Penalty 1.0e18 1.0e18
test        NormDispIncr 1.0e-5 20 1
algorithm   Newton
numberer    RCM
system      BandGeneral
integrator  Newmark 0.5 0.25
rayleigh    $a0 0. $a1 0.0
analysis    Transient

# Apply confinement pressure
set pNode [expr $pConf / 4.0]
pattern Plain 1 {Series -time {0 10000 1e10} -values {0 1 1} -factor 1} {
    load 1  $pNode  0.0    0.0    0.0
    load 2  $pNode  $pNode 0.0    0.0
    load 3  0.0     $pNode 0.0    0.0
    load 4  0.0     0.0    0.0    0.0
    load 5  $pNode  0.0    $pNode 0.0
    load 6  $pNode  $pNode $pNode 0.0
    load 7  0.0     $pNode $pNode 0.0
    load 8  0.0     0.0    $pNode 0.0
}
analyze 100 100

# Let the model rest and waves damp out
analyze 50  100

# Close drainage valves
for {set x 1} {$x<9} {incr x} {
   remove sp $x 4
}
analyze 50 100

# Read vertical displacement of top plane
set vertDisp [nodeDisp 5 3]
# Apply deviatoric strain
set lValues [list 1 [expr 1+$devDisp/$vertDisp] [expr 1+$devDisp/$vertDisp]]
set ts "{Series -time {20000 1020000 10020000} -values {$lValues} -factor 1}"

# loading object deviator stress
eval "pattern Plain 2 $ts { 
sp 5  3$vertDisp
sp 6  3$vertDisp
sp 7  3 $vertDisp
sp 8  3 $vertDisp
}"

# Set number and length of (pseudo)time steps
set dT      100
set numStep 10000

# Analyze and use substepping if needed
set remStep $numStep
set success 0
proc subStepAnalyze {dT subStep} {
    if {$subStep > 10} {
	return -10
    }
    for {set i 1} {$i < 3} {incr i} {
	puts "Try dT = $dT"
	set success [analyze 1 $dT]
	if {$success != 0} {
	    set success [subStepAnalyze [expr $dT/2.0] [expr $subStep+1]]
	    if {$success == -10} {
		puts "Did not converge."
		return success
	    }
	} else {
	    if {$i==1} {
		puts "Substep $subStep : Left side converged with dT = $dT"
	    } else {
		puts "Substep $subStep : Right side converged with dT = $dT"
	    }
	}
    }
    return success
}

puts "Start analysis"
set startT [clock seconds]

while {$success != -10} {
    set subStep 0
    set success [analyze $remStep  $dT]
    if {$success == 0} {
	puts "Analysis Finished"
	break
    } else {
	set curTime  [getTime]
	puts "Analysis failed at $curTime . Try substepping."
	set success  [subStepAnalyze [expr $dT/2.0] [incr subStep]]
        set curStep  [expr int(($curTime-20000)/$dT + 1)]
        set remStep  [expr int($numStep-$curStep)]
	puts "Current step: $curStep , Remaining steps: $remStep"
    }
}
set endT [clock seconds]
puts "loading analysis execution time: [expr $endT-$startT] seconds."

wipe