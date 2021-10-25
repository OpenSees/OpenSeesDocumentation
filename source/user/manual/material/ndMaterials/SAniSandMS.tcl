set test_type "drained_triaxial_cyc" ;# Used in recorders.tcl

wipe
 
# Create a 3D model with 4 Degrees of Freedom
model BasicBuilder -ndm 3 -ndf 3
 
# Confinement Stress
set pConf -200.0

# Increment of q added at constant p0 (will be the average during cyclic loading)
set delta_qav -75.0; 

# Amplitude of cyclic deviatoric stress
set delta_qcyc -60.0; 


set G0        110.  ; # [Adimensional]
set nu        0.05  ; # [Adimensional]
set e_init    0.72  ; # [Adimensional]
set Mc        1.27  ; # [Adimensional]
set c         0.712 ; # [Adimensional]
set lambda_c  0.049 ; # [Adimensional]
set e0        0.845 ; # [Adimensional]
set ksi       0.27  ; # [Adimensional]
set P_atm     101.3 ; # [kPa]
set m         0.01  ; # [Adimensional]
set h0        5.95  ; # [Adimensional]
set ch        1.01  ; # [Adimensional]
set nb        2.0   ; # [Adimensional]
set A0        1.06  ; # [Adimensional]
set nd        1.17  ; # [Adimensional]
set z_max     4     ; # For SAniSand [Adimensional]
set cz        0     ; # For SAniSand [Adimensional]
set mu0       260.  ; # For SAniSand [Adimensional]
set zeta      0.0005; # For SAniSand [Adimensional]
set beta      1     ; # For SAniSand [Adimensional]
set w1        0.5   ;
set w2        2     ;
set Den       1.584 ; # [Mg/m^3]
set intScheme 3     ; # Corresponds to Modified-Euler integration scheme
set TanType   1     ; # 0: elastic stiffness, 1: continuum elastoplastic stiffness
set JacoType  1     ; # Not used in explicit methods
set TolF      1.0e-6; # Tolerances, not used in explicit
set TolR      1.0e-6; # Tolerances, not used in explicit

#Reference atmospheric pressure
set P_ref $P_atm
 
# Create material   
nDMaterial SAniSandMS  1 $G0 $nu $e_init $Mc $c $lambda_c $e0 $ksi $P_atm $m $h0 $ch $nb $A0 $nd $zeta $mu0 $beta $Den  $intScheme $TanType $JacoType $TolF $TolR
set type "RK"


# Create nodes
node 1  1.0 0.0 0.0
node 2  1.0 1.0 0.0
node 3  0.0 1.0 0.0 
node 4  0.0 0.0 0.0
node 5  1.0 0.0 1.0
node 6  1.0 1.0 1.0
node 7  0.0 1.0 1.0
node 8  0.0 0.0 1.0
 
# Create Fixities
fix 1   0 1 1 
fix 2   0 0 1 
fix 3   1 0 1 
fix 4   1 1 1 
fix 5   0 1 0 
fix 6   0 0 0 
fix 7   1 0 0 
fix 8   1 1 0 
 
 

# Create element
#       SSPbrickUP  tag    i j k l m n p q  matTag  fBulk  fDen    k1    k2   k3   void   alpha    <b1 b2 b3>
element SSPbrick   1     1 2 3 4 5 6 7 8    1
 
recorder Element -file ${type}_${test_type}_stress.out -ele 1  -time stress
recorder Element -file ${type}_${test_type}_strain.out -ele 1 -time strain


# Create analysis
constraints Transformation
test        NormDispIncr 1.0e-4 20 0
algorithm   Newton
numberer    RCM
system      BandGeneral
integrator  LoadControl 0.0001
analysis    Static
 
 
# Apply confinement pressure
set pNode [expr $pConf / 4.0]
pattern Plain 1 {Series -time {0 1 100} -values {0 1 1} -factor 1} {
    load 1  $pNode  0.0    0.0    
    load 2  $pNode  $pNode 0.0    
    load 3  0.0     $pNode 0.0    
    load 4  0.0     0.0    0.0    
    load 5  $pNode  0.0    $pNode 
    load 6  $pNode  $pNode $pNode 
    load 7  0.0     $pNode $pNode 
    load 8  0.0     0.0    $pNode 
}
analyze 10000
 



loadConst


puts "Starting monotonic analysis"


# Apply confinement pressure
set delta_sigma_a [expr $delta_qav*2./3.]
set delta_sigma_r [expr -$delta_sigma_a/2]
set pNode2 [expr $delta_sigma_r / 4.0 ]
set pNode1 [expr $delta_sigma_a / 4.0]
pattern Plain 3 {Series -time {1 2 100} -values {0 1 1} -factor 1} {
    load 1  $pNode2  0.0     0.0    
    load 2  $pNode2  $pNode2 0.0    
    load 3  0.0      $pNode2 0.0    
    load 4  0.0      0.0     0.0    
    load 5  $pNode2  0.0     $pNode1 
    load 6  $pNode2  $pNode2 $pNode1 
    load 7  0.0      $pNode2 $pNode1 
    load 8  0.0      0.0     $pNode1 
}


integrator LoadControl 0.0001
analyze 10000
 



loadConst




puts "Starting cyclic analysis"


set Ncyc 1000
set NcycActuallyDo 1000
set dT      [expr 0.001]
set tmax    [expr $NcycActuallyDo]
set numStep [expr int(2.0*$tmax / $dT)]
 







set qlist [list 0]
set timelist [list 2]

for {set i 1} {$i <= $Ncyc} {incr i} {
   lappend qlist [expr $delta_qcyc/4.0] [expr -$delta_qcyc/4.0]     
   lappend timelist [expr 2*$i + 1] [expr 2*$i + 2]
}

set tsq "{Series      -time {$timelist} -values {$qlist} }" ;#-factor 1}"
puts $tsq

# return


eval "pattern Plain 4 $tsq { load 5  0 0 1.0;  }"
eval "pattern Plain 5 $tsq { load 6  0 0 1.0;  }"
eval "pattern Plain 6 $tsq { load 7  0 0 1.0;  }"
eval "pattern Plain 7 $tsq { load 8  0 0 1.0;  }"





# Analyze and use substepping if needed
set remStep $numStep
set success 0
integrator  LoadControl $dT
proc subStepAnalyze {dT subStep} {
    if {$subStep > 10} {
        return -10
    }
    for {set i 1} {$i < 3} {incr i} {
        puts "Try dT = $dT"
        # set success [analyze 1 $dT]
        integrator  LoadControl $dT
        set success [analyze 1]
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
 
puts "Finished static Start analysis"
set startT [clock seconds]


set startTime  [getTime]
while {$success != -10} {
    set subStep 0
    integrator  LoadControl $dT
    set success [analyze $remStep  $dT]
    if {$success == 0} {
        puts "Analysis Finished"
        break
    } else {
        set curTime  [getTime]
        puts "Analysis failed at $curTime . Try substepping."
        set success  [subStepAnalyze [expr $dT/2.0] [incr subStep]]
        set curStep  [expr int(($curTime-$startTime)/$dT + 1)]
        set remStep  [expr int($numStep-$curStep)]
        puts "Current step: $curStep , Remaining steps: $remStep"
    }
}
set endT [clock seconds]
puts "loading analysis execution time: [expr $endT-$startT] seconds."





wipe
