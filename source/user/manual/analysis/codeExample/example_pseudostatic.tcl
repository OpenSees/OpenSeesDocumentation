# ============================================================================
# example_pseudostatic.tcl
#
# Demonstrates using ExplicitDifferenceStatic as a pseudo-static / dynamic
# relaxation tool: a chain of n truss "springs" with lumped masses, loaded
# with constant nodal forces (representing, e.g., a soil column's self
# weight), is relaxed with strong Cundall/FLAC local damping until velocities
# vanish and the displacements converge to the static (hand-calculated)
# solution.
#
# Model: node 0 (fixed) -- k -- node 1 -- k -- node 2 -- k -- node 3 -- k -- node 4
#        each free node i=1..n carries lumped mass m and constant load P
#
# Hand calculation (static equilibrium of the chain):
#   Tension in spring i (connecting node i-1 to node i) must carry the sum
#   of all loads applied at nodes i, i+1, ..., n:
#       T_i = (n - i + 1) * P
#   Elongation of spring i:  delta_i = T_i / k
#   Cumulative displacement at node i:
#       u_i = sum_{j=1}^{i} delta_j = sum_{j=1}^{i} (n - j + 1) * P / k
#   For n=4, P=2, k=1000:
#       u_1 = 4*P/k = 0.008
#       u_2 = u_1 + 3*P/k = 0.014
#       u_3 = u_2 + 2*P/k = 0.018
#       u_4 = u_3 + 1*P/k = 0.020
# ============================================================================

wipe
model basic -ndm 1 -ndf 1

set n 4
set k 1000.0
set m 1.0
set P 2.0

node 0 0.0
fix 0 1
for {set i 1} {$i <= $n} {incr i} {
    node $i [expr {double($i)}]
    mass $i $m
}

uniaxialMaterial Elastic 1 $k
for {set i 1} {$i <= $n} {incr i} {
    element truss $i [expr {$i-1}] $i 1.0 1
}

pattern Plain 1 "Constant" {
    for {set i 1} {$i <= $n} {incr i} {
        load $i $P
    }
}

# Default local damping (alpha=0.59, combined) -- no -alpha/-simple flags.
integrator ExplicitDifferenceStatic

constraints Plain
numberer Plain
system FullGeneral
test NormUnbalance 1.0e-12 10
algorithm Linear
analysis Transient

# Conservative dt: the n-DOF chain's highest mode is faster than the
# single-DOF estimate omega=sqrt(k/m), so apply a generous safety factor.
set omega [expr {sqrt($k/$m)}]
set dt [expr {2.0/$omega*0.2}]

set nSteps 4000
for {set j 1} {$j <= $nSteps} {incr j} {
    analyze 1 $dt
}

puts "========================================================================"
puts " ExplicitDifferenceStatic -- pseudo-static relaxation of a loaded chain"
puts "========================================================================"
puts [format "dt = %.6g, nSteps = %d, t_total = %.4g (s)" $dt $nSteps [expr {$nSteps*$dt}]]
puts ""
puts [format "%-6s %16s %16s %16s %10s" "node" "disp (got)" "disp (expected)" "vel (got)" "err %"]

set maxErr 0.0
for {set i 1} {$i <= $n} {incr i} {
    set u 0.0
    for {set j 1} {$j <= $i} {incr j} {
        set u [expr {$u + ($n-$j+1)*$P/$k}]
    }
    set got [nodeDisp $i 1]
    set v [nodeVel $i 1]
    set err [expr {abs($got-$u)/$u*100.0}]
    if {$err > $maxErr} { set maxErr $err }
    puts [format "%-6d %16.8f %16.8f %16.3e %10.4f" $i $got $u $v $err]
}

puts ""
if {$maxErr < 0.1} {
    puts [format "PASS: max displacement error = %.4f %% (< 0.1 %%), velocities ~ 0" $maxErr]
} else {
    puts [format "FAIL: max displacement error = %.4f %%" $maxErr]
}
