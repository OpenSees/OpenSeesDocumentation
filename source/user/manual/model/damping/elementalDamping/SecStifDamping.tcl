wipe; 

# Create a 2D model with 3 Degrees of Freedom
model BasicBuilder -ndm 2 -ndf 3; 

# Create secant stiffness-proportional damping
# Ref. [1] Tian Y, Huang Y, Qu Z, Fei Y, Lu X. 2022. High-performance uniform damping model for response history analysis in OpenSees. Journal of Earthquake Engineering. 2022. http://dx.doi.org/10.1080/13632469.2022.2124557 
damping SecStiff 1 0.05

set Tol 1.0e-8;    
set numStep 1000;
set PI [expr 4.0 * atan(1.0)]
set E 1.0
set A 1.0
set L 1.0
set I 0.08
set m 1
set v 20
set k [expr $E*$A/$L]
set d0 1.0
set wn [expr sqrt($k/$m)]

# Create nodes
node 11 0 0 -mass $m $m 0
node 12 $L 0 -mass $m  $m  0

# Create Fixities
fix 11 1 1 1
fix 12 0 1 1

# Create geometric transformation
geomTransf Linear 1

# Create element
element elasticBeamColumn 1 11 12 $A $E $I 1 -damp 1

set tag 1
set tStart 0
set tEnd 100
set period 1.0
set cFactor 1.0

# Create time series
timeSeries Trig $tag $tStart $tEnd $period -factor $cFactor

# Create node recorder
recorder Node -file disp1.txt -time -node 11 12 -dof 1  disp
recorder Node -file vel1.txt -time -node 11 12 -dof 1  vel
recorder Node -file accel1.txt -timeSeries $tag -time -node 11 12 -dof 1  accel

set patternTag 10010
set dir 1

# Create Uniform Excitation load
pattern UniformExcitation $patternTag $dir -accel $tag

# Analyze
constraints Transformation;
numberer RCM;
system FullGeneral
test NormDispIncr 1e-3 100 0
algorithm NewtonLineSearch 0.75
integrator Newmark 0.5 0.25
analysis Transient
set dt 0.01
set tEQ 100
while {[getTime] < $tEQ} {analyze 1 $dt;}


