# Plane-strain SSPquadUP version of freeField3D_SSPbrickUP.tcl.
# One counterclockwise four-node quadrilateral per original column cell.
# Units: kN, m, s. Soil DOFs: ux, uy, integral(p); nodeVel DOF 3 is pressure.
# Same materials, layering, drainage, gravity stages and x input motion as 3D.
# Plane strain omits the original out-of-plane motion and g*sin(slope).
# Thickness=2 m preserves the original 2 m x 2 m base area and x dashpot.
# Retain the original freeField3D_SSPbrickUP.tcl stabilization coefficient alpha.

set here [file normalize [file dirname [info script]]]
set resultsDir [file join $here results]
file mkdir $resultsDir
wipe

# Geometry and mesh (layer 1 is at the bottom).
set soilThick 30.0
set grade 2.0
set numLayers 3
set layerThick(1) 20.0
set layerThick(2) 8.0
set layerThick(3) 2.0
set nElemY(1) 40
set nElemY(2) 16
set nElemY(3) 4
set width 2.0
set thickness 2.0
set waterTable 2.0
set waterHeight [expr {$soilThick-$waterTable}]
set nCells 0
for {set k 1} {$k <= $numLayers} {incr k} {
    set sElemY($k) [expr {$layerThick($k)/$nElemY($k)}]
    incr nCells $nElemY($k)
}
set nSoilNodes [expr {2*($nCells+1)}]
set nSoilElements $nCells

# Two nodes at every elevation, numbered left then right, bottom to top.
model BasicBuilder -ndm 2 -ndf 3
set nodesInfo [open [file join $resultsDir sspquadup_nodesInfo.dat] w]
set level 0
set y 0.0
for {set k 1} {$k <= $numLayers} {incr k} {
    for {set j 0} {$j < $nElemY($k)} {incr j} {
        foreach {side x} [list 0 0.0 1 $width] {
            set tag [expr {2*$level+$side+1}]
            node $tag $x $y
            puts $nodesInfo "$tag $x $y"
            if {$y >= $waterHeight-1.0e-10} { fix $tag 0 0 1 }
        }
        incr level
        set y [expr {$y+$sElemY($k)}]
    }
}
foreach {side x} [list 0 0.0 1 $width] {
    set tag [expr {2*$level+$side+1}]
    node $tag $x $soilThick
    puts $nodesInfo "$tag $x $soilThick"
    fix $tag 0 0 1
}
close $nodesInfo

# Free-field displacement ties; pressures remain independent except drainage.
fix 1 0 1 0
fix 2 0 1 0
equalDOF 1 2 1
for {set level 1} {$level <= $nCells} {incr level} {
    equalDOF [expr {2*$level+1}] [expr {2*$level+2}] 1 2
}

# Material dimension is 2 (PlaneStrain); remaining parameters match 3D.
set slope [expr {atan($grade/100.0)}]
set g -9.81
nDMaterial PressureDependMultiYield02 3 2 1.8 9.0e4 2.2e5 32 0.1 \
                                      101.0 0.5 26 0.067 0.23 0.06 \
                                      0.27 20 5.0 3.0 1.0 \
                                      0.0 0.77 0.9 0.02 0.7 101.0
set xWgt(3)  0.0
set yWgt(3)  [expr $g*cos($slope)]
set uBulk(3) 2.2e6
set xPerm(3) 1.0e-2
set yPerm(3) 1.0e-2
set eVoid(3) 0.77

nDMaterial PressureDependMultiYield02 2 2 2.24 9.0e4 2.2e5 32 0.1 \
                                      101.0 0.5 26 0.067 0.23 0.06 \
                                      0.27 20 5.0 3.0 1.0 \
                                      0.0 0.77 0.9 0.02 0.7 101.0
set xWgt(2)  0.0
set yWgt(2)  [expr $g*cos($slope)]
set uBulk(2) 2.2e6
set xPerm(2) 1.0e-5
set yPerm(2) 1.0e-5
set eVoid(2) 0.77

nDMaterial PressureDependMultiYield02 1 2 2.45 1.3e5 2.6e5 39 0.1 \
                                      101.0 0.5 26 0.010 0.0 0.35 \
                                      0.0 20 5.0 3.0 1.0 \
                                      0.0 0.47 0.9 0.02 0.7 101.0
set xWgt(1)  0.0
set yWgt(1)  [expr $g*cos($slope)]
set uBulk(1) 2.2e6
set xPerm(1) 1.0e-2
set yPerm(1) 1.0e-2
set eVoid(1) 0.47


# One quadrilateral per rectangle: bottom-left, bottom-right, top-right, top-left.
set alpha 1.5e-6
set cell 0
set eleTag 0
set connectivity {}
set elemInfo [open [file join $resultsDir sspquadup_elementInfo.dat] w]
puts $elemInfo "# tag node1 node2 node3 node4 layer cell"
for {set k 1} {$k <= $numLayers} {incr k} {
    set firstElement($k) [expr {$eleTag+1}]
    for {set j 0} {$j < $nElemY($k)} {incr j} {
        set n1 [expr {2*$cell+1}]
        set n2 [expr {$n1+1}]
        set n3 [expr {$n1+3}]
        set n4 [expr {$n1+2}]
        incr eleTag
        # As in freeField3D_SSPbrickUP.tcl: high permeability during gravity.
        # Pass fluid bulk directly; SSPquadUP computes porosity internally.
        element SSPquadUP $eleTag $n1 $n2 $n3 $n4 $k $thickness \
            $uBulk($k) 1.0 1.0 1.0 $eVoid($k) $alpha $xWgt($k) $yWgt($k)
        lappend connectivity [list $eleTag $n1 $n2 $n3 $n4 $k]
        puts $elemInfo "$eleTag $n1 $n2 $n3 $n4 $k [expr {$cell+1}]"
        incr cell
    }
    set lastElement($k) $eleTag
}
close $elemInfo
if {$eleTag != $nSoilElements} { error "Unexpected quadrilateral count" }
puts "SSPquadUP column: $nSoilNodes soil nodes, $nSoilElements quadrilaterals."

# One horizontal Lysmer dashpot; auxiliary nodes have displacement DOFs only.
model BasicBuilder -ndm 2 -ndf 2
set dashF [expr {$nSoilNodes+1}]
set dashX [expr {$nSoilNodes+2}]
node $dashF 0.0 0.0
node $dashX 0.0 0.0
fix $dashF 1 1
fix $dashX 0 1
equalDOF 1 $dashX 1
set rockVS 700.0
set rockDen 2.5
set colArea [expr {$width*$thickness}]
set dashpotCoeff [expr {$rockVS*$rockDen*$colArea}]
uniaxialMaterial Viscous [expr {$numLayers+1}] $dashpotCoeff 1
element zeroLength [expr {$nSoilElements+1}] $dashF $dashX \
    -mat [expr {$numLayers+1}] -dir 1
model BasicBuilder -ndm 2 -ndf 3

# GiD mesh contains only soil nodes and quadrilaterals.
set meshFile [open [file join $resultsDir sspquadup_freeField2D.flavia.msh] w]
puts $meshFile "MESH ffSSPquadUP dimension 2 ElemType Quadrilateral Nnode 4"
puts $meshFile "Coordinates"
for {set tag 1} {$tag <= $nSoilNodes} {incr tag} {
    puts $meshFile "$tag [join [nodeCoord $tag] { }] 0.0"
}
puts $meshFile "End Coordinates"
puts $meshFile "Elements"
foreach entry $connectivity { puts $meshFile [join $entry { }] }
puts $meshFile "End Elements"
close $meshFile

# Recorder columns: time, followed by node/element tags in ascending order.
# Element stress2D3/strain2D3 have xx, yy, xy (engineering shear strain).
proc recordColumn {prefix recDT} {
    global resultsDir nSoilNodes nSoilElements
    recorder Node -file [file join $resultsDir ${prefix}displacement.out] \
        -time -dT $recDT -nodeRange 1 $nSoilNodes -dof 1 2 disp
    recorder Node -file [file join $resultsDir ${prefix}velocity.out] \
        -time -dT $recDT -nodeRange 1 $nSoilNodes -dof 1 2 vel
    recorder Node -file [file join $resultsDir ${prefix}acceleration.out] \
        -time -dT $recDT -nodeRange 1 $nSoilNodes -dof 1 2 accel
    recorder Node -file [file join $resultsDir ${prefix}porePressure.out] \
        -time -dT $recDT -nodeRange 1 $nSoilNodes -dof 3 vel
    recorder Element -file [file join $resultsDir ${prefix}stress.out] \
        -time -dT $recDT -eleRange 1 $nSoilElements stress2D3
    recorder Element -file [file join $resultsDir ${prefix}strain.out] \
        -time -dT $recDT -eleRange 1 $nSoilElements strain2D3
}
recordColumn sspquadup_G 0.0

# Analysis settings and staged gravity from freeField3D_SSPbrickUP.tcl.
set motionDT 0.005
set motionSteps 7990
set duration [expr {$motionDT*$motionSteps}]
# Retain the source model's selected motion timestep, 0.005 s.
set dT $motionDT
set gamma 0.5
set beta 0.25
# Rayleigh damping remains disabled, as in freeField3D.tcl.
for {set k 1} {$k <= $numLayers} {incr k} {
    updateMaterialStage -material $k -stage 0
}
constraints Penalty 1.0e14 1.0e14
test NormDispIncr 1.0e-5 30 1
algorithm Newton
numberer Plain
system SparseGeneral
integrator Newmark $gamma $beta
analysis Transient
set startT [clock seconds]
set ok [analyze 20 500.0]
if {$ok != 0} { error "Elastic gravity failed at [getTime], code $ok" }
puts "Finished with elastic gravity analysis..."
for {set k 1} {$k <= $numLayers} {incr k} {
    updateMaterialStage -material $k -stage 1
}
set ok [analyze 40 0.05]
if {$ok != 0} { error "Plastic gravity failed at [getTime], code $ok" }
puts "Finished with plastic gravity analysis..."

# Apply layer permeabilities to the quadrilaterals in each layer.
# SSPquadUP uses hPerm/vPerm; Tri31UP uses xPerm/yPerm.
for {set k 1} {$k <= $numLayers} {incr k} {
    setParameter -value $xPerm($k) -eleRange $firstElement($k) $lastElement($k) hPerm
    setParameter -value $yPerm($k) -eleRange $firstElement($k) $lastElement($k) vPerm
}
setTime 0.0
wipeAnalysis
remove recorders
set recDT [expr {10*$motionDT}]
recordColumn sspquadup_ $recDT

# Same incident-wave velocity record and x-direction force factor as 3D.
set velocityFile [file join $here yerbaNSvelocity.out]
if {![file isfile $velocityFile]} { error "Input motion not found: $velocityFile" }
timeSeries Path 10 -dt $motionDT -filePath $velocityFile -factor $dashpotCoeff
pattern Plain 10 10 {
    load 1 1.0 0.0 0.0
}
constraints Penalty 1.0e14 1.0e14
test NormDispIncr 1.0e-3 55 1
algorithm KrylovNewton
numberer Plain
system SparseGeneral
integrator Newmark $gamma $beta
analysis Transient
set ok [analyze $motionSteps $dT]
# Up to two timestep halvings, as in the original; retry only remaining time.
for {set retry 0} {$ok != 0 && $retry < 2} {incr retry} {
    set dT [expr {$dT/2.0}]
    set remaining [expr {int(ceil(($duration-[getTime])/$dT-1.0e-8))}]
    puts "Reducing timestep to $dT at [getTime]; $remaining remaining steps."
    set ok [analyze $remaining $dT]
}
if {$ok != 0} { error "SSPquadUP dynamic analysis failed at [getTime], code $ok" }
if {abs([getTime]-$duration) > 1.0e-7} { error "Dynamic analysis ended short of $duration" }
puts "Finished with SSPquadUP dynamic analysis at [getTime] s."
puts "Analysis execution time: [expr {[clock seconds]-$startT}] seconds"
wipe
