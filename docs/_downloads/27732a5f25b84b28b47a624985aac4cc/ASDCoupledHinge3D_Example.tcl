model basic -ndm 3 -ndf 6

# nodes
set L 1650
node 11 0 0 0
node 1 0 0 0
node 2 0 0 $L

set a_sl 1.0
set cunit 1.0

proc LvOverh { M V h } {
	global L
	set schema 1
	# Schema = 1 for cantilever - 0.5 for fix-fix
	if {abs($V) < 1e-6} {
		return [expr ($L * $schema) / $h]
	} else {
		return [expr abs($M) / abs($V) / $h]
	}
}

proc SeriesStiff {coeff} {
	global L
	set schema 1 
	# schema = 1 for cantilever - 8 for fix-fix
	return [expr 1.0/(1.0/$coeff - 1.0) * 3/$L * $schema]
}

# Section Coupled 7: Simplified Section
#simpleStrengthDomain Nmin? Nmax? MyMax? MzMax? NMMax?"
section ASDCoupledHinge3D 7 1000000000000.0 1000000000000.0 1000000000000.0 1000000000000.0 -simpleStrengthDomain -1.12e7 1.9e6 9.217e8 9.217e8 -4.2e6 -hardening 1.08 \
							-initialFlexuralStiffness "\[expr \[SeriesStiff \[expr min(0.6, max(0.2, \[expr 0.3 * (( 0.1 - __N__ / (302500.0 * 32.0))**0.8) * ((\[LvOverh __M__ __V__ 550.0])**0.72)]))]] * 244016666666666.66\]" "\[expr \[SeriesStiff \[expr min(0.6, max(0.2, \[expr 0.3 * (( 0.1 - __N__ / (302500.0 * 32.0))**0.8) * ((\[LvOverh __M__ __V__ 550.0])**0.72)]))]] * 244016666666666.66\]" \
							-thetaP "\[expr 0.13*(1+0.55*$a_sl)*pow(0.13, -__N__ / (302500.0*32.0)) * pow(0.02 + 40 * 0.007477509787056698, 0.65) * pow(0.57, 0.01 * $cunit * 32.0)\]" "\[expr 0.13*(1+0.55*$a_sl)*pow(0.13, -__N__ / (302500.0*32.0)) * pow(0.02 + 40 * 0.007477509787056698, 0.65) * pow(0.57, 0.01 * $cunit * 32.0)\]" \
							-thetaPC "\[expr (min(0.10,0.76*pow(0.031, -__N__ / (302500.0*32.0)) * pow(0.02 + 40 * 0.007477509787056698, 1.02)))+0.13*(1+0.55*$a_sl)*pow(0.13, -__N__ / (302500.0*32.0)) * pow(0.02 + 40 * 0.007477509787056698, 0.65) * pow(0.57, 0.01 * $cunit * 32.0)\]" "\[expr (min(0.10,0.76*pow(0.031, -__N__ / (302500.0*32.0)) * pow(0.02 + 40 * 0.007477509787056698, 1.02)))+0.13*(1+0.55*$a_sl)*pow(0.13, -__N__ / (302500.0*32.0)) * pow(0.02 + 40 * 0.007477509787056698, 0.65) * pow(0.57, 0.01 * $cunit * 32.0)\]"
section Elastic 8 32000.0 302500.0 7625520833.333333 7625520833.333333 14000.0 12887130208.333334

# beam_column_elements forceBeamColumn
# Geometric transformation command
geomTransf Linear 1 1.0 0.0 0.0
element forceBeamColumn 1   11 2  1 Lobatto 8 5

# zero_length_elements zeroLengthSection
element zeroLengthSection 2 1 11 7 -orient 0.0 0.0 1.0 0.0 -1.0 0.0

# BC
fix 1  1 1 1 1 1 1
fix 11 0 1 0 1 0 1
fix 2  0 1 0 1 0 1

# load
timeSeries Linear 1
pattern Plain 11 1 {
	load 2 0.0 0.0 -4000000.0 0.0 0.0 0.0
}

# analysis
set time 1.0
set nsteps 10
set dt [expr $time / $nsteps]
constraints Transformation
numberer Plain
system FullGeneral
test NormDispIncr 1e-10 40 1
algorithm NewtonLineSearch
integrator LoadControl $dt
analysis Static
analyze $nsteps
loadConst -time 0.0

pattern Plain 22 1 {
	sp 2 1 100.0
}

set time 1.0
set nsteps 20
set dt [expr $time / $nsteps]
constraints Transformation
numberer Plain
system FullGeneral
test NormDispIncr 1e-10 40 0
algorithm NewtonLineSearch
integrator LoadControl $dt
analysis Static
puts [format "%10s %10s" N M]
for {set i 0} {$i < $nsteps} {incr i} {
	analyze 1
	reactions
	set R [nodeReaction 1]
	set N [expr -([lindex $R 2])]
	set M [expr -([lindex $R 4])]
	puts [format "%10.3e %10.3e" $N $M]
}
