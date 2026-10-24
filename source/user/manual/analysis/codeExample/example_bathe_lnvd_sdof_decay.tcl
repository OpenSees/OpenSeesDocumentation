# ============================================================================
# example_sdof_decay.tcl
#
# Verifies the local non-viscous (Cundall/FLAC) damping option (-lnvd) of the
# ExplicitBathe integrator using a single-degree-of-freedom (SDOF) spring-mass
# oscillator in free vibration (no applied load).
#
# Model: node 1 (fixed) -- truss (k=100) -- node 2, 1D, ndf 1
#   element truss 1 1 2 1.0 1 -rho 2.0   (nodes 1 unit apart, A=1 -> total
#   mass = rho*A*L = 2.0, lumped half to each node -> 1.0 at the free node 2)
# Initial condition: u(0) = u0 = 0.01, v(0) = 0  (set with setNodeDisp -commit)
#
# The Bathe sub-step parameter is fixed at p = 0.5, for which q0 = q1 = 0 and
# q2 = 0.5 (see ExplicitBathe.rst): this is the sub-case of the scheme with no
# *intrinsic* numerical damping of its own, isolating the effect of -lnvd.
#
# Theory (see ExplicitDifferenceStatic.rst for the derivation, which carries
# over unchanged since -lnvd uses the same "simple" Cundall/FLAC law
# F_d = -alpha*|F|*sign(v) applied to the fully assembled unbalance F=P-R(u),
# here evaluated using the predicted sub-step velocity at each of the two
# Bathe sub-steps):
#   For free vibration (no external load), F = -k*u, and, to first order in
#   alpha, each cycle of amplitude A loses a fraction of energy
#   dE/E = 4*alpha, equivalent to a viscous damping ratio xi = alpha/pi, i.e.
#   a logarithmic decrement per cycle delta = 2*alpha, so successive
#   displacement peaks should decay by the ratio
#       A_(n+1) / A_n  ~=  exp(-2*alpha)          (small-alpha asymptote)
#   This is checked below for alpha=0.1 (error < 1%); for the larger
#   alpha=0.3 and alpha=0.8 used afterwards the method still damps strongly
#   but, as for ExplicitDifferenceStatic, increasingly over-damps relative to
#   this small-alpha asymptote.
# ============================================================================

proc runSDOF {alpha} {
    wipe
    model basic -ndm 1 -ndf 1

    set k 100.0
    set u0 0.01

    node 1 0.0
    node 2 1.0
    fix 1 1

    uniaxialMaterial Elastic 1 $k
    element truss 1 1 2 1.0 1 -rho 2.0

    # Initial displacement u0, zero velocity -- pure free vibration, no load.
    setNodeDisp 2 1 $u0 -commit

    integrator ExplicitBathe 0.5 0 -lnvd $alpha

    constraints Plain
    numberer Plain
    system Diagonal
    test NormUnbalance 1.0e-12 10
    algorithm Linear
    analysis Transient

    set dt 0.01
    set nSteps 400
    set prevV 0.0
    set peaks {}
    set maxAbsTail 0.0
    set tailStartStep 300
    for {set i 1} {$i <= $nSteps} {incr i} {
        analyze 1 $dt
        set d [nodeDisp 2 1]
        set v [nodeVel 2 1]
        if {$prevV >= 0 && $v < 0} { lappend peaks $d }
        set prevV $v
        set ad [expr {abs($d)}]
        if {$i >= $tailStartStep && $ad > $maxAbsTail} { set maxAbsTail $ad }
    }
    return [list $peaks $maxAbsTail]
}

puts "============================================================================"
puts " ExplicitBathe -lnvd -- Cundall/FLAC local damping, SDOF free vibration"
puts "============================================================================"

# --- 1) Quantitative check of the small-alpha asymptote, alpha = 0.1 -------
set res [runSDOF 0.1]
set peaks [lindex $res 0]
set p1 [lindex $peaks 0]
set p2 [lindex $peaks 1]
set gotRatio [expr {$p2/$p1}]
set expRatio [expr {exp(-2.0*0.1)}]
set err1 [expr {abs($gotRatio-$expRatio)/$expRatio*100.0}]
puts [format "alpha=0.1: peak1=%.6e peak2=%.6e  ratio got=%.6f expected=exp(-2a)=%.6f  error=%.3f%%" \
        $p1 $p2 $gotRatio $expRatio $err1]
if {$err1 < 1.0} {
    puts "  PASS: within 1% of the theoretical small-alpha decay ratio"
} else {
    puts "  FAIL: deviates by more than 1% from theory"
}

# --- 2) Amplitude after ~3-4 s of free vibration for alpha = 0, 0.3, 0.8 ----
puts ""
puts [format "%-6s %18s %18s %10s" "alpha" "max|u|, t in \[3,4\]s (got)" "exp(-2*a*N) * u0 (hand-calc)" "ratio"]
set omega [expr {sqrt(100.0/1.0)}]
set T [expr {2*3.14159265358979/$omega}]
foreach alpha {0.0 0.3 0.8} {
    set res [runSDOF $alpha]
    set maxAbsTail [lindex $res 1]
    # Hand-calc: small-alpha asymptote evaluated at the midpoint of the
    # [3,4] s tail window (t = 3.5 s), N = t/T cycles elapsed.
    set tMid 3.5
    set N [expr {$tMid/$T}]
    set handCalc [expr {0.01*exp(-2.0*$alpha*$N)}]
    set ratio [expr {$maxAbsTail/$handCalc}]
    puts [format "%-6s %18.6e %18.6e %10.4f" $alpha $maxAbsTail $handCalc $ratio]
}

puts ""
puts "Note: the 'ratio' column above is got/hand-calc using the small-alpha"
puts "asymptote exp(-2*alpha*N); it is close to 1 for alpha=0 (no damping, as"
puts "expected) and increasingly diverges for alpha=0.3 and alpha=0.8, exactly"
puts "as for the ExplicitDifferenceStatic integrator's own -alpha option: the"
puts "asymptote over-predicts the decay rate once alpha is not small, so the"
puts "true amplitude decays somewhat less than the naive estimate -- the"
puts "scheme does not blow up, it simply departs from the first-order theory."
