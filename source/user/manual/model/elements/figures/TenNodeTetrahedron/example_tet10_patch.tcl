# TenNodeTetrahedron (quadratic 10-node tet, 4-point integration) checks.
#
# Fixes exercised (branch fix/tet10-integration vs upstream/master):
#   1. Jacobian/weight scaling of the 4-point rule (commit 2f3362a28)
#   2. setParameter/updateParameter reaching all 4 material points (a9430a76d)
#   3. heap overflow in eleResponse stresses|strains (110bb4dcc)
#
# Corners: (0,0,0) (2,0,0) (0,3,0) (0,0,1.5)  ->  V = 2*3*1.5/6 = 1.5
# Midside ordering (from shape functions): 5:1-2 6:2-3 7:3-1 8:1-4 9:3-4 10:2-4
proc build {b3} {
    wipe
    model BasicBuilder -ndm 3 -ndf 3
    set X {{0 0 0} {2 0 0} {0 3 0} {0 0 1.5}}
    set mids {{1 2} {2 3} {3 1} {1 4} {3 4} {2 4}}
    for {set i 0} {$i < 4} {incr i} { eval node [expr $i+1] [lindex $X $i] }
    set n 5
    foreach e $mids {
        set a [lindex $X [expr [lindex $e 0]-1]]; set b [lindex $X [expr [lindex $e 1]-1]]
        node $n [expr ([lindex $a 0]+[lindex $b 0])/2.] [expr ([lindex $a 1]+[lindex $b 1])/2.] [expr ([lindex $a 2]+[lindex $b 2])/2.]
        incr n
    }
    nDMaterial ElasticIsotropic 1 1000.0 0.25
    element TenNodeTetrahedron 1 1 2 3 4 5 6 7 8 9 10 1 0.0 0.0 $b3
}

proc applyUniformStrainBC {} {
    timeSeries Linear 2; pattern Plain 2 2 {
        for {set i 1} {$i <= 10} {incr i} {
            set x [lindex [nodeCoord $i] 0]
            sp $i 1 [expr 1e-3*$x]; sp $i 2 0.0; sp $i 3 0.0
        }
    }
    constraints Penalty 1e14 1e14; numberer Plain; system FullGeneral
    test NormUnbalance 1e-10 5; algorithm Linear
    integrator LoadControl 1.0; analysis Static
    analyze 1
}

set failed 0

# ------------------------------------------------------------------
# 1) Body-force patch test (fix #1: Jacobian/weight scaling).
#    Net reaction over all 10 nodes must equal -b3*V exactly: the
#    4-pt rule must reconstruct the true element volume.
# ------------------------------------------------------------------
build -2.0
timeSeries Constant 1; pattern Plain 1 1 {
    for {set i 1} {$i <= 10} {incr i} { sp $i 1 0.0; sp $i 2 0.0; sp $i 3 0.0 }
}
constraints Penalty 1e14 1e14; numberer Plain; system FullGeneral
test NormUnbalance 1e-10 5; algorithm Linear
integrator LoadControl 1.0; analysis Static
analyze 1
reactions
set Rz 0.0
for {set i 1} {$i <= 10} {incr i} { set Rz [expr $Rz + [nodeReaction $i 3]] }
set expRz 3.0
puts [format "BODYFORCE  sum Rz = %.10f  expected = %.10f" $Rz $expRz]
if {abs($Rz-$expRz) > 1e-6} { puts "  -> FAIL"; set failed 1 }

# ------------------------------------------------------------------
# 2) Uniform-strain patch test (fix #1 again, and fix #3: eleResponse
#    "stresses" used to overflow a size-6 static Vector with 24
#    doubles -- this call used to corrupt the heap / crash).
#    eps_xx = 1e-3 imposed on all nodes -> exact, identical stresses
#    at all 4 Gauss points.
# ------------------------------------------------------------------
build 0.0
applyUniformStrainBC
set s [eleResponse 1 stresses]
set exp {1.2 0.4 0.4 0 0 0}
puts "STRESSES  (expect per GP: $exp)"
puts $s
set maxerr 0.0
for {set g 0} {$g < 4} {incr g} {
    for {set k 0} {$k < 6} {incr k} {
        set e [expr abs([lindex $s [expr 6*$g+$k]] - [lindex $exp $k])]
        if {$e > $maxerr} { set maxerr $e }
    }
}
puts [format "PATCH max abs error = %.3e" $maxerr]
if {$maxerr > 1e-6} { puts "  -> FAIL"; set failed 1 }

# ------------------------------------------------------------------
# 3) setParameter/updateParameter reaching every material point
#    (fix #2: both the per-point branch and the "all points" loop
#    in TenNodeTetrahedron::setParameter stopped at point 1 upstream).
#
#    Each Gauss point holds an *independent copy* of the nDMaterial
#    (TenNodeTetrahedron::setDomain -> theMaterial.getCopy(...)), so
#    raising E only at Gauss point $gp must rescale the stress at
#    that point only (strain is fixed by the displacement BC, so for
#    an isotropic elastic material: sigma = E-dependent stiffness
#    tensor * fixed strain -> doubling E doubles sigma at that point).
# ------------------------------------------------------------------
set E0 1000.0
set E1 2000.0
set scale [expr $E1/$E0]
puts "SETPARAMETER  per-Gauss-point E override (E: $E0 -> $E1, scale = $scale)"
for {set gp 1} {$gp <= 4} {incr gp} {
    build 0.0
    applyUniformStrainBC
    set before [eleResponse 1 stresses]

    set ptag [expr 100+$gp]
    parameter $ptag element 1 material $gp E
    updateParameter $ptag $E1

    set after [eleResponse 1 stresses]

    set ok 1
    for {set g 0} {$g < 4} {incr g} {
        set expScale [expr {$g == $gp-1 ? $scale : 1.0}]
        for {set k 0} {$k < 6} {incr k} {
            set b [lindex $before [expr 6*$g+$k]]
            set a [lindex $after  [expr 6*$g+$k]]
            set e [expr abs($a - $expScale*$b)]
            if {$e > 1e-6} { set ok 0 }
        }
    }
    set targetBefore [lrange $before [expr 6*($gp-1)] [expr 6*($gp-1)+5]]
    set targetAfter  [lrange $after  [expr 6*($gp-1)] [expr 6*($gp-1)+5]]
    puts [format "  gp=%d  sigma_xx before=%.6f after=%.6f (expected %.6f)  other-points-unchanged=%s" \
        $gp [lindex $targetBefore 0] [lindex $targetAfter 0] [expr $scale*[lindex $targetBefore 0]] \
        [expr {$ok ? "yes" : "NO"}]]
    if {!$ok} { puts "  -> FAIL (gp=$gp)"; set failed 1 }
}

if {$failed} {
    puts "OVERALL: FAIL"
} else {
    puts "OVERALL: PASS"
}
