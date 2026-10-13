# TenNodeTetrahedron: gmsh vs Abaqus (-numbering abaqus) node order.
# Node tags: 1-4 corners, 5:1-2 6:2-3 7:3-1 8:1-4, 9 on edge 3-4, 10 on edge 2-4.
# gmsh connectivity: 1..10.  Abaqus C3D10 connectivity: 1 2 3 4 5 6 7 8 10 9.
# Midside nodes are moved off the edges (curved element) so a wrong 9/10 assignment shows.
proc build {conn opts b3} {
    wipe; model BasicBuilder -ndm 3 -ndf 3
    set X {{0 0 0} {2 0 0} {0 3 0} {0 0 1.5}}
    set mids {{1 2} {2 3} {3 1} {1 4} {3 4} {2 4}}
    set bump {{0.05 -0.1 0.02} {0.1 0.05 -0.03} {-0.08 0.04 0.06} {0.03 0.07 -0.05} {-0.06 0.09 0.04} {0.07 -0.04 0.08}}
    for {set i 0} {$i < 4} {incr i} { eval node [expr $i+1] [lindex $X $i] }
    set n 5
    foreach e $mids d $bump {
        set a [lindex $X [expr [lindex $e 0]-1]]; set b [lindex $X [expr [lindex $e 1]-1]]
        set c {}
        foreach k {0 1 2} { lappend c [expr ([lindex $a $k]+[lindex $b $k])/2. + [lindex $d $k]] }
        eval node $n $c; incr n
    }
    nDMaterial ElasticIsotropic 1 1000.0 0.25
    eval element TenNodeTetrahedron 1 $conn 1 0.0 0.0 $b3 $opts
}
# Same quadratic displacement field and body force imposed on each element; results are compared between orderings.
proc run {conn opts} {
    build $conn $opts -2.0
    timeSeries Linear 1; pattern Plain 1 1 {
        for {set i 1} {$i <= 10} {incr i} {
            lassign [nodeCoord $i] x y z
            sp $i 1 [expr 1e-3*($x + 0.3*$y*$z)]; sp $i 2 [expr 1e-3*(0.5*$x*$x - 0.2*$z)]; sp $i 3 [expr 1e-3*($y*$y + 0.1*$x)]
        }
    }
    constraints Penalty 1e14 1e14; numberer Plain; system FullGeneral; test NormUnbalance 1e-10 5
    algorithm Linear; integrator LoadControl 1.0; analysis Static
    analyze 1
    return [list [eleResponse 1 forces] [eleResponse 1 stresses]]
}
proc swap910 {f} { return [concat [lrange $f 0 23] [lrange $f 27 29] [lrange $f 24 26]] }
proc maxdiff {a b} { set m 0.0; foreach x $a y $b { set d [expr abs($x-$y)]; if {$d > $m} {set m $d} }; return $m }
proc maxabs {a} { set m 0.0; foreach x $a { if {abs($x) > $m} {set m [expr abs($x)]} }; return $m }

lassign [run {1 2 3 4 5 6 7 8 9 10} ""] fg sg
lassign [run {1 2 3 4 5 6 7 8 10 9} "-numbering abaqus"] fa sa
lassign [run {1 2 3 4 5 6 7 8 10 9} ""] fw sw
puts [format "max |force|          = %.4e" [maxabs $fg]]
puts [format "ABAQUS forces vs gmsh (9<->10 swapped): max diff = %.3e" [maxdiff $fa [swap910 $fg]]]
puts [format "ABAQUS stresses vs gmsh:                max diff = %.3e" [maxdiff $sa $sg]]
puts [format "control: Abaqus conn WITHOUT flag:      max diff = %.3e (must be large)" [maxdiff $fw [swap910 $fg]]]

# patch test + body force in Abaqus order with straight edges (same check as smoke/tet10_patch.tcl)
wipe; model BasicBuilder -ndm 3 -ndf 3
set X {{0 0 0} {2 0 0} {0 3 0} {0 0 1.5}}
set n 1; foreach p $X { eval node $n $p; incr n }
foreach e {{1 2} {2 3} {3 1} {1 4} {2 4} {3 4}} {
    set a [lindex $X [expr [lindex $e 0]-1]]; set b [lindex $X [expr [lindex $e 1]-1]]
    node $n [expr ([lindex $a 0]+[lindex $b 0])/2.] [expr ([lindex $a 1]+[lindex $b 1])/2.] [expr ([lindex $a 2]+[lindex $b 2])/2.]; incr n
}
nDMaterial ElasticIsotropic 1 1000.0 0.25
element TenNodeTetrahedron 1 1 2 3 4 5 6 7 8 9 10 1 0.0 0.0 -2.0 -numbering abaqus
timeSeries Linear 1; pattern Plain 1 1 {
    for {set i 1} {$i <= 10} {incr i} { sp $i 1 [expr 1e-3*[lindex [nodeCoord $i] 0]]; sp $i 2 0.0; sp $i 3 0.0 }
}
constraints Penalty 1e14 1e14; numberer Plain; system FullGeneral; test NormUnbalance 1e-10 5
algorithm Linear; integrator LoadControl 1.0; analysis Static
analyze 1
reactions
set Rz 0.0; for {set i 1} {$i <= 10} {incr i} { set Rz [expr $Rz + [nodeReaction $i 3]] }
puts [format "ABAQUS BODYFORCE sum Rz = %.10f expected 3.0" $Rz]
set s [eleResponse 1 stresses]; set m 0.0
for {set g 0} {$g < 4} {incr g} { foreach k {0 1 2 3 4 5} e {1.2 0.4 0.4 0 0 0} { set d [expr abs([lindex $s [expr 6*$g+$k]]-$e)]; if {$d>$m} {set m $d} } }
puts [format "ABAQUS PATCH max abs error = %.3e" $m]
