# 3D free-field site response using conforming TenNodeTetrahedronUP elements.
# Geometry, layers, materials, drainage, dashpots, and input motion match
# freeField3D.tcl. Units are kN, m, and s.

proc freshFile {fileName} {
    global resultsDir
    set fileName [file join $resultsDir $fileName]
    set channel [open $fileName w]
    close $channel
    # Preserve the filename as one word for eval recorder commands.
    return [list $fileName]
}

proc fixMixedNode {nodeTag pressureNodeTags fixX fixY fixZ} {
    if {[dict exists $pressureNodeTags $nodeTag]} {
        fix $nodeTag $fixX $fixY $fixZ 0
    } else {
        fix $nodeTag $fixX $fixY $fixZ
    }
}

set here [file normalize [file dirname [info script]]]
cd $here
# Write generated results beside this script in the results folder.
set resultsDir [file join [file dirname [file normalize [info script]]] results]
file mkdir $resultsDir

wipe

# -----------------------------------------------------------------------------
# Geometry and discretization
# -----------------------------------------------------------------------------
set soilThick 30.0
set grade 2.0
set numLayers 3
set layerThick(1) 20.0
set layerThick(2) 8.0
set layerThick(3) 2.0
set nElemY(1) 40
set nElemY(2) 16
set nElemY(3) 4
set nElemT 60
set sElemX 2.0
set sElemZ 2.0
set waterTable 2.0
set waterHeight [expr {$soilThick - $waterTable}]

for {set layer 1} {$layer <= $numLayers} {incr layer} {
    set sElemY($layer) [expr {$layerThick($layer) / $nElemY($layer)}]
}

# Corner tags 1--244 retain the numbering of freeField3D.tcl: four corners at
# each of the 61 elevations. Edge-midpoint tags are appended during meshing.
# Default ndf=4 is used only by pressure-carrying corner nodes.
model BasicBuilder -ndm 3 -ndf 4
set pressureNodeTags [dict create]
set pressureNodes {}
set soilNodeTags {}
array set nodeX {}
array set nodeY {}
array set nodeZ {}
array set cornerTag {}
array set nodesByY {}

set level 0
set yCoord 0.0
for {set layer 1} {$layer <= $numLayers} {incr layer} {
    for {set localLevel 0} {$localLevel < $nElemY($layer)} {incr localLevel} {
        foreach {position x z} {0 0.0 0.0 1 2.0 0.0 2 2.0 2.0 3 0.0 2.0} {
            set tag [expr {4 * $level + $position + 1}]
            set cornerTag($level,$position) $tag
            set nodeX($tag) $x
            set nodeY($tag) $yCoord
            set nodeZ($tag) $z
            node $tag $x $yCoord $z
            dict set pressureNodeTags $tag 1
            lappend pressureNodes $tag
            lappend soilNodeTags $tag
            lappend nodesByY([format "%.12f" $yCoord]) $tag
            if {$yCoord >= $waterHeight - 1.0e-10} {
                fix $tag 0 0 0 1
            }
        }
        incr level
        set yCoord [expr {$yCoord + $sElemY($layer)}]
    }
}
# Add the four top corner nodes, which are not created by the half-open loops.
foreach {position x z} {0 0.0 0.0 1 2.0 0.0 2 2.0 2.0 3 0.0 2.0} {
    set tag [expr {4 * $level + $position + 1}]
    set cornerTag($level,$position) $tag
    set nodeX($tag) $x
    set nodeY($tag) $soilThick
    set nodeZ($tag) $z
    node $tag $x $soilThick $z
    dict set pressureNodeTags $tag 1
    lappend pressureNodes $tag
    lappend soilNodeTags $tag
    lappend nodesByY([format "%.12f" $soilThick]) $tag
    fix $tag 0 0 0 1
}
set nextNodeTag [expr {4 * ($level + 1) + 1}]

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------
set slope [expr {atan($grade / 100.0)}]
set g -9.81
set fluidDensity 1.0

nDMaterial PressureDependMultiYield02 3 3 1.8 9.0e4 2.2e5 32 0.1 \
    101.0 0.5 26 0.067 0.23 0.06 0.27 20 5.0 3.0 1.0 \
    0.0 0.77 0.9 0.02 0.7 101.0
set xWgt(3) 0.0
set yWgt(3) [expr {$g * cos($slope)}]
set zWgt(3) [expr {$g * sin($slope)}]
set xPerm(3) 1.0e-2; set yPerm(3) 1.0e-2; set zPerm(3) 1.0e-2
set uBulk(3) 2.2e6
set eVoid(3) 0.77
set n(3) [expr {$eVoid(3)/(1.0 + $eVoid(3))}]

nDMaterial PressureDependMultiYield02 2 3 2.24 9.0e4 2.2e5 32 0.1 \
    101.0 0.5 26 0.067 0.23 0.06 0.27 20 5.0 3.0 1.0 \
    0.0 0.77 0.9 0.02 0.7 101.0
set xWgt(2) 0.0
set yWgt(2) [expr {$g * cos($slope)}]
set zWgt(2) [expr {$g * sin($slope)}]
set xPerm(2) 1.0e-5; set yPerm(2) 1.0e-5; set zPerm(2) 1.0e-5
set uBulk(2) 2.2e6
set eVoid(2) 0.77
set n(2) [expr {$eVoid(2)/(1.0 + $eVoid(2))}]

nDMaterial PressureDependMultiYield02 1 3 2.45 1.3e5 2.6e5 39 0.1 \
    101.0 0.5 26 0.010 0.0 0.35 0.0 20 5.0 3.0 1.0 \
    0.0 0.47 0.9 0.02 0.7 101.0
set xWgt(1) 0.0
set yWgt(1) [expr {$g * cos($slope)}]
set zWgt(1) [expr {$g * sin($slope)}]
set xPerm(1) 1.0e-2; set yPerm(1) 1.0e-2; set zPerm(1) 1.0e-2
set uBulk(1) 2.2e6
set eVoid(1) 0.47
set n(1) [expr {$eVoid(1)/(1.0 + $eVoid(1))}]

# -----------------------------------------------------------------------------
# Conforming C3D10-UP mesh
# -----------------------------------------------------------------------------
# Six positive-orientation tetrahedra about the hexahedron diagonal 0--6.
# The y/z axis exchange relative to generate_c3d10_column_mesh.py is corrected
# by swapping each tetrahedron's second and third corner.
set localTets {
    {0 2 1 6}
    {0 3 2 6}
    {0 7 3 6}
    {0 4 7 6}
    {0 5 4 6}
    {0 1 5 6}
}
# TenNodeTetrahedronUP order: 12, 23, 13, 14, 34, 24.
# Thus local nodes 9 and 10 are the 3-4 and 2-4 edge nodes, respectively.
set edgeOrder {{0 1} {1 2} {0 2} {0 3} {2 3} {1 3}}
set edgeNodeTags [dict create]
set elementTags {}
array set layerElementTags {}
set elementTag 1

for {set cell 0} {$cell < $nElemT} {incr cell} {
    if {$cell < 40} {
        set layer 1
    } elseif {$cell < 56} {
        set layer 2
    } else {
        set layer 3
    }
    set hex [list \
        $cornerTag($cell,0) $cornerTag($cell,1) \
        $cornerTag($cell,2) $cornerTag($cell,3) \
        $cornerTag([expr {$cell + 1}],0) $cornerTag([expr {$cell + 1}],1) \
        $cornerTag([expr {$cell + 1}],2) $cornerTag([expr {$cell + 1}],3)]

    foreach localTet $localTets {
        set corners {}
        foreach localIndex $localTet { lappend corners [lindex $hex $localIndex] }
        set midsideNodes {}
        foreach edge $edgeOrder {
            set first [lindex $corners [lindex $edge 0]]
            set second [lindex $corners [lindex $edge 1]]
            if {$first < $second} {
                set edgeKey "$first,$second"
            } else {
                set edgeKey "$second,$first"
            }
            if {![dict exists $edgeNodeTags $edgeKey]} {
                set midTag $nextNodeTag
                incr nextNodeTag
                dict set edgeNodeTags $edgeKey $midTag
                set x [expr {0.5 * ($nodeX($first) + $nodeX($second))}]
                set y [expr {0.5 * ($nodeY($first) + $nodeY($second))}]
                set z [expr {0.5 * ($nodeZ($first) + $nodeZ($second))}]
                set nodeX($midTag) $x
                set nodeY($midTag) $y
                set nodeZ($midTag) $z
                node $midTag $x $y $z -ndf 3
                lappend soilNodeTags $midTag
                lappend nodesByY([format "%.12f" $y]) $midTag
            }
            lappend midsideNodes [dict get $edgeNodeTags $edgeKey]
        }
        eval element TenNodeTetrahedronUP $elementTag $corners $midsideNodes $layer \
            [expr {$uBulk($layer)/$n($layer)}] $fluidDensity 1.0 1.0 1.0 \
            $xWgt($layer) $yWgt($layer) $zWgt($layer)
        lappend elementTags $elementTag
        lappend layerElementTags($layer) $elementTag
        incr elementTag
    }
}
set nSoilNodes [llength $soilNodeTags]
set nTetElements [llength $elementTags]
puts "Created $nSoilNodes mixed-DOF nodes and $nTetElements TenNodeTetrahedronUP elements."

# -----------------------------------------------------------------------------
# Free-field constraints and drainage
# -----------------------------------------------------------------------------
# All displacement nodes at a common elevation move together, matching the
# one-element-wide free-field column assumption in the SSPbrickUP model.
set levelMasterNodes {}
set baseMaster -1
set topMaster -1
set topY -1.0e30
foreach yKey [lsort -real [array names nodesByY]] {
    set levelNodes [lsort -integer -unique $nodesByY($yKey)]
    set retained [lindex $levelNodes 0]
    lappend levelMasterNodes $retained
    if {abs($yKey) < 1.0e-10} { set baseMaster $retained }
    if {$yKey > $topY} { set topY $yKey; set topMaster $retained }
    foreach constrained [lrange $levelNodes 1 end] {
        equalDOF $retained $constrained 1 2 3
    }
    if {abs($yKey) < 1.0e-10} {
        foreach nodeTag $levelNodes {
            # Vertical and transverse base fixity; x remains connected to the dashpot.
            fixMixedNode $nodeTag $pressureNodeTags 0 1 1
        }
    }
}

# -----------------------------------------------------------------------------
# Lysmer dashpots
# -----------------------------------------------------------------------------
model BasicBuilder -ndm 3 -ndf 3
set dashF $nextNodeTag; incr nextNodeTag
set dashX $nextNodeTag; incr nextNodeTag
set dashZ $nextNodeTag; incr nextNodeTag
node $dashF 0.0 0.0 0.0
node $dashX 0.0 0.0 0.0
node $dashZ 0.0 0.0 0.0
fix $dashF 1 1 1
fix $dashX 0 1 1
fix $dashZ 1 1 0
equalDOF $baseMaster $dashX 1
equalDOF $baseMaster $dashZ 3
set colArea [expr {$sElemX * $sElemZ}]
set rockVS 700.0
set rockDen 2.5
set dashpotCoeff [expr {$rockVS * $rockDen * $colArea}]
uniaxialMaterial Viscous 4 $dashpotCoeff 1
element zeroLength $elementTag $dashF $dashX -mat 4 -dir 1
incr elementTag
element zeroLength $elementTag $dashF $dashZ -mat 4 -dir 3

# -----------------------------------------------------------------------------
# Analysis parameters and gravity
# -----------------------------------------------------------------------------
set motionDT 0.005
set motionSteps 7990
set duration [expr {$motionDT * $motionSteps}]
set vsMax 250.0
set minSize $sElemY(1)
for {set layer 2} {$layer <= $numLayers} {incr layer} {
    if {$sElemY($layer) < $minSize} { set minSize $sElemY($layer) }
}
set kTrial [expr {$minSize / pow($vsMax, 0.5)}]
if {$motionDT <= $kTrial} {
    set nSteps $motionSteps
    set dT $motionDT
} else {
    set nSteps [expr {int(floor($duration / $kTrial) + 1)}]
    set dT [expr {$duration / $nSteps}]
}
set gamma 0.5
set beta 0.25

eval recorder Node -file [freshFile c3d10UP_Gdisplacement.out] -time -node $soilNodeTags -dof 1 2 3 disp
eval recorder Node -file [freshFile c3d10UP_GporePressure.out] -time -node $pressureNodes -dof 4 vel
eval recorder Element -file [freshFile c3d10UP_Gstress_gp1.out] -time -ele $elementTags material 1 stress
eval recorder Element -file [freshFile c3d10UP_Gstrain_gp1.out] -time -ele $elementTags material 1 strain

model BasicBuilder -ndm 3 -ndf 4
for {set layer 1} {$layer <= $numLayers} {incr layer} {
    updateMaterialStage -material $layer -stage 0
}
constraints Penalty 1.0e14 1.0e14
test NormDispIncr 1.0e-5 30 1
algorithm Newton
numberer RCM
system UmfPack
integrator Newmark $gamma $beta
analysis Transient
set startT [clock seconds]
set ok [analyze 20 500.0]
if {$ok != 0} { error "Elastic gravity analysis failed at [getTime], code $ok" }
puts "Finished with elastic gravity analysis..."

for {set layer 1} {$layer <= $numLayers} {incr layer} {
    updateMaterialStage -material $layer -stage 1
}
set ok [analyze 40 0.05]
if {$ok != 0} { error "Plastic gravity analysis failed at [getTime], code $ok" }
puts "Finished with plastic gravity analysis..."

# Replace the high gravity-stage permeability by each layer's physical value.
foreach layer {1 2 3} {
    foreach elementTag $layerElementTags($layer) {
        setParameter -value $xPerm($layer) -ele $elementTag xPerm
        setParameter -value $yPerm($layer) -ele $elementTag yPerm
        setParameter -value $zPerm($layer) -ele $elementTag zPerm
    }
}
puts "Finished updating permeabilities for dynamic analysis..."

# -----------------------------------------------------------------------------
# Dynamic recorders and loading
# -----------------------------------------------------------------------------
setTime 0.0
wipeAnalysis
remove recorders
set recDT [expr {10.0 * $motionDT}]
eval recorder Node -file [freshFile c3d10UP_displacement.out] -time -dT $recDT -node $soilNodeTags -dof 1 2 3 disp
eval recorder Node -file [freshFile c3d10UP_velocity.out] -time -dT $recDT -node $soilNodeTags -dof 1 2 3 vel
eval recorder Node -file [freshFile c3d10UP_acceleration.out] -time -dT $recDT -node $soilNodeTags -dof 1 2 3 accel
eval recorder Node -file [freshFile c3d10UP_porePressure.out] -time -dT $recDT -node $pressureNodes -dof 4 vel
eval recorder Node -file [freshFile c3d10UP_level_disp.out] -time -dT $recDT -node $levelMasterNodes -dof 1 2 3 disp
eval recorder Element -file [freshFile c3d10UP_stress_gp1.out] -time -dT $recDT -ele $elementTags material 1 stress
eval recorder Element -file [freshFile c3d10UP_strain_gp1.out] -time -dT $recDT -ele $elementTags material 1 strain

set velocityFile yerbaNSvelocity.out
timeSeries Path 10 -dt $motionDT -filePath $velocityFile -factor $dashpotCoeff
pattern Plain 10 10 {
    # Base corner node has ux, uy, uz, and pore-pressure DOFs.
    load $baseMaster 1.0 0.0 0.0 0.0
}
puts "Dynamic loading created..."

constraints Penalty 1.0e14 1.0e14
test NormDispIncr 1.0e-3 55 1
algorithm KrylovNewton
numberer RCM
system UmfPack
integrator Newmark $gamma $beta
analysis Transient

set ok [analyze $nSteps $dT]
if {$ok != 0} {
    puts "Did not converge at [getTime]; reducing time step by two."
    set completedTime [getTime]
    set remainingSteps [expr {int(ceil(($duration - $completedTime) / ($dT / 2.0)))}]
    set dT [expr {$dT / 2.0}]
    set ok [analyze $remainingSteps $dT]
}
if {$ok != 0} {
    puts "Did not converge at [getTime]; reducing time step by two again."
    set completedTime [getTime]
    set remainingSteps [expr {int(ceil(($duration - $completedTime) / ($dT / 2.0)))}]
    set dT [expr {$dT / 2.0}]
    set ok [analyze $remainingSteps $dT]
}
if {$ok != 0} { error "Dynamic analysis failed at [getTime], code $ok" }

set endT [clock seconds]
puts "Finished with TenNodeTetrahedronUP dynamic analysis at [getTime]."
puts "Analysis execution time: [expr {$endT - $startT}] seconds"
wipe
