# ============================================================================
# example_sdof_decay.tcl
#
# Verifies the local non-viscous (Cundall/FLAC) damping of the
# ExplicitDifferenceStatic integrator using a single-degree-of-freedom (SDOF)
# spring-mass oscillator in free vibration (no applied load).
#
# Model: node 1 (fixed) -- truss (k) -- node 2 (mass m), 1D, ndf 1
# Initial condition: u(0) = u0, v(0) = 0  (set with setNodeDisp -commit)
#
# Theory (see ExplicitDifferenceStatic.rst):
#   For free vibration (no external load) the unbalance is B = -k*u, so
#   dB/dt = -k*v, i.e. sign(dB/dt) = -sign(v) at all times (away from the
#   velocity-sign deadband). Substituting into the "combined" damping law
#       F_d = 0.5*alpha*|B|*(sign(dB/dt) - sign(v))
#   gives F_d = -alpha*|B|*sign(v), i.e. for this particular problem the
#   "combined" formulation collapses onto the "simple" one,
#       F_d = -alpha*|B|*sign(v).
#   A first-order (small alpha) energy balance over one cycle of amplitude A,
#   frequency omega, gives an equivalent viscous damping ratio
#       xi = alpha / pi
#   and hence a logarithmic decrement per cycle of
#       delta = 2*pi*xi = 2*alpha
#   so successive displacement peaks should decay by the ratio
#       A_(n+1) / A_n  ~=  exp(-2*alpha)
#   (this is the "checked quantity" below; it is a small-alpha asymptote, so
#   the match degrades as alpha approaches 1).
# ============================================================================

proc runSDOF {alpha mode} {
    wipe
    model basic -ndm 1 -ndf 1

    set k 1000.0
    set m 1.0
    set u0 1.0

    node 1 0.0
    node 2 1.0
    fix 1 1
    mass 2 $m

    uniaxialMaterial Elastic 1 $k
    element truss 1 1 2 1.0 1

    set omega [expr {sqrt($k/$m)}]
    set T [expr {2*3.14159265358979/$omega}]

    # Initial displacement u0, zero velocity -- pure free vibration, no load.
    setNodeDisp 2 1 $u0 -commit

    if {$mode eq "simple"} {
        integrator ExplicitDifferenceStatic -alpha $alpha -simple
    } else {
        integrator ExplicitDifferenceStatic -alpha $alpha
    }

    constraints Plain
    numberer Plain
    system FullGeneral
    test NormUnbalance 1.0e-12 10
    algorithm Linear
    analysis Transient

    set dt [expr {$T/400.0}]
    set nCycles 6
    set nSteps [expr {int($nCycles*$T/$dt)}]

    set prevDisp $u0
    set prevVel 0.0
    set peaks {}
    for {set i 1} {$i <= $nSteps} {incr i} {
        analyze 1 $dt
        set d [nodeDisp 2 1]
        set v [nodeVel 2 1]
        if {$prevVel >= 0 && $v < 0} {
            lappend peaks $prevDisp
        }
        set prevDisp $d
        set prevVel $v
    }
    return $peaks
}

puts "========================================================================"
puts " ExplicitDifferenceStatic -- Cundall/FLAC local damping, SDOF free vibration"
puts "========================================================================"
puts [format "%-6s %-10s %14s %14s %14s %10s" "alpha" "mode" "peak1" "peak2" "ratio" "exp(-2a)"]

foreach alpha {0.0 0.3 0.8} {
    foreach mode {combined simple} {
        set peaks [runSDOF $alpha $mode]
        set p1 [lindex $peaks 0]
        set p2 [lindex $peaks 1]
        set ratio [expr {$p2/$p1}]
        set expected [expr {exp(-2.0*$alpha)}]
        puts [format "%-6s %-10s %14.6f %14.6f %14.6f %10.6f" $alpha $mode $p1 $p2 $ratio $expected]
    }
}

puts ""
puts "Check (small-alpha asymptote xi = alpha/pi, decay ratio = exp(-2*alpha)):"
set peaksC [runSDOF 0.1 combined]
set got [expr {[lindex $peaksC 1]/[lindex $peaksC 0]}]
set expected [expr {exp(-2.0*0.1)}]
set err [expr {abs($got-$expected)/$expected*100.0}]
puts [format "  alpha=0.1 combined: got ratio = %.6f, expected = %.6f, error = %.3f %%" $got $expected $err]
if {$err < 1.0} {
    puts "  PASS: within 1% of the theoretical small-alpha decay ratio"
} else {
    puts "  FAIL: deviates by more than 1% from theory"
}

puts ""
puts "Note: for this unloaded free-vibration problem, 'combined' and '-simple'"
puts "give (numerically) identical decay, because sign(dB/dt) = -sign(v)"
puts "always holds when the unbalance B is purely elastic (B=-k*u). The two"
puts "forms only differ once the unbalance's time-derivative sign decouples"
puts "from the velocity sign, e.g. under nonlinear material response or"
puts "time-varying external load (see the pseudo-static example)."
