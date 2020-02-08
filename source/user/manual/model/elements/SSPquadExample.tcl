#########################################################
#                #
# Coarse-mesh cantilever beam analysis.  The beam is    #
# modeled with only 4 elements and uses anti-symmetry.  #
##
# ---> Basic units used are kN and meters#
##
#########################################################

wipe

model BasicBuilder -ndm 2 -ndf 2

# beam dimensions
set L 24.0
set D 3.0

# define number and size of elements 
set nElemX 4
set nElemY 1
set nElemT [expr $nElemX*$nElemY]
set sElemX [expr $L/$nElemX]
set sElemY [expr $D/$nElemY]

set nNodeX [expr $nElemX + 1]
set nNodeY [expr $nElemY + 1]
set nNodeT [expr $nNodeX*$nNodeY]

# create the nodes
set nid   1
set count 0.0
for {set j 1} {$j <= $nNodeY} {incr j 1} {
    for {set i 1} {$i <= $nNodeX} {incr i 1} {
	node $nid [expr 0.0 + $count*$sElemX] [expr ($j-1)*$sElemY]
	set nid   [expr $nid + 1]
	set count [expr $count + 1]
    }
    set count 0.0
}

# boundary conditions
fix 1   1 1
fix [expr $nElemY*$nNodeX+1]   1 0
for {set k 2} {$k <= $nNodeX} {incr k 1} {
    fix $k 1 0
}

# define material
set matID 1
set E     20000
set nu    0.25
nDMaterial ElasticIsotropic $matID $E $nu

# create elements
set thick 1.0
set b1 0.0
set b2 0.0
set count 1
for {set j 1} {$j <= $nNodeY} {incr j 1} {
    for {set i 1} {$i <= $nNodeX} {incr i 1} {
	if {($i < $nNodeX) && ($j < $nNodeY)} {
	    set nI [expr $i+($j-1)*$nNodeX]
	    set nJ [expr $i+($j-1)*$nNodeX+1]
	    set nK [expr $i+$j*$nNodeX+1]
	    set nL [expr $i+$j*$nNodeX]
	    element SSPquad $count  $nI $nJ $nK $nL $matID "PlaneStrain" $thick $b1 $b2

	    set count [expr $count+1]
	}
    }
}

# create recorders
set step 0.1

recorder Node -time -file results/d1p1m1.out -dT $step -nodeRange 1 $nNodeT -dof 1 2 disp
recorder Element -eleRange 1 $nElemT -time -file results/s1p1m1.out  -dT $step  stress
recorder Element -eleRange 1 $nElemT -time -file results/e1p1m1.out  -dT $step  strain

# create loading
set P -300.0;

pattern Plain 3 {Series -time {0 10 15} -values {0 1 1} -factor 1} { 
    load $nNodeT   0.0 [expr 0.1875*$P]
    load $nNodeX   0.0 [expr 0.3125*$P]

    load [expr $nNodeX+1]   0.0 [expr -0.1875*$P]
}

# create analysis

integrator LoadControl 0.1
numberer RCM
system SparseGeneral
constraints Transformation
test NormDispIncr 1e-5 40 1
algorithm Newton
analysis Static

analyze 105

wipe