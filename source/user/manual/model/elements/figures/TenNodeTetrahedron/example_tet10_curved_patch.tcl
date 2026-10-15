# Uniform-strain patch test on ONE Tet10 with straight vs curved edges (mid-edge nodes moved off the midpoints).
# Imposed u = (1e-3 x, 0, 0) on all 10 nodes. An isoparametric element reproduces any linear field exactly,
# straight or curved, so every Gauss point must give sigma = (1.2, 0.4, 0.4, 0, 0, 0) for E=1000, nu=0.25.
proc run {ele bumpScale} {
    wipe; model BasicBuilder -ndm 3 -ndf 3
    set X {{0 0 0} {2 0 0} {0 3 0} {0 0 1.5}}
    if {$ele == "TenNodeTetrahedron"} { set mids {{1 2} {2 3} {3 1} {1 4} {3 4} {2 4}} } else { set mids {{1 2} {2 3} {3 1} {1 4} {2 4} {3 4}} }
    set bump {{0.05 -0.1 0.02} {0.1 0.05 -0.03} {-0.08 0.04 0.06} {0.03 0.07 -0.05} {-0.06 0.09 0.04} {0.07 -0.04 0.08}}
    for {set i 0} {$i < 4} {incr i} { eval node [expr $i+1] [lindex $X $i] }
    set n 5
    foreach e $mids d $bump {
        set a [lindex $X [expr [lindex $e 0]-1]]; set b [lindex $X [expr [lindex $e 1]-1]]
        set c {}; foreach k {0 1 2} { lappend c [expr ([lindex $a $k]+[lindex $b $k])/2. + $bumpScale*[lindex $d $k]] }
        eval node $n $c; incr n
    }
    nDMaterial ElasticIsotropic 1 1000.0 0.25
    element $ele 1 1 2 3 4 5 6 7 8 9 10 1
    timeSeries Linear 1; pattern Plain 1 1 { for {set i 1} {$i <= 10} {incr i} { sp $i 1 [expr 1e-3*[lindex [nodeCoord $i] 0]]; sp $i 2 0.0; sp $i 3 0.0 } }
    constraints Penalty 1e14 1e14; numberer Plain; system FullGeneral; test NormDispIncr 1e-14 5; algorithm Linear
    integrator LoadControl 1.0; analysis Static; analyze 1
    set s [eleResponse 1 stresses]; set m 0.0
    for {set g 0} {$g < 4} {incr g} { foreach k {0 1 2 3 4 5} e {1.2 0.4 0.4 0 0 0} { set d [expr abs([lindex $s [expr 6*$g+$k]]-$e)]; if {$d>$m} {set m $d} } }
    # element force equilibrium: sum of nodal forces must vanish
    set f [eleResponse 1 forces]; set r 0.0
    foreach k {0 1 2} { set t 0.0; for {set i 0} {$i < 10} {incr i} { set t [expr $t+[lindex $f [expr 3*$i+$k]]] }; if {abs($t)>$r} {set r [expr abs($t)]} }
    return [format "%-22s bump=%.1f  patch max stress error = %.3e   |sum nodal forces| = %.3e" $ele $bumpScale $m $r]
}
foreach ele {TenNodeTetrahedron TenNodeTetrahedronStd} { foreach s {0.0 1.0 3.0} { puts [run $ele $s] } }
