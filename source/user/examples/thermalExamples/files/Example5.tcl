##########################################################################################
# Code by Walker Maddalozzo & Dr. Erica Fischer - Oregon State Univeristy - May 2019
# Example: 2D frame with 2 bays:  where beam and column are subjected to fire from one side
# Units: Newtons, m, seconds



wipe all;					
set dataDir Example5_OUTPUT;	# name of output folder
file mkdir $dataDir; 					#create output folder		
		
model BasicBuilder -ndm 2 -ndf 3; #2D 3DOF

source WsectionThermal.tcl;




############################## NODAL DEFINITIONS ##########################################
# http://opensees.berkeley.edu/wiki/index.php/Node_command

node	1	0.000	0.000	;#Column 1 #SUPPORT A
node	2	0.000	0.118	;#Column 1
node	3	0.000	0.236	;#Column 1
node	4	0.000	0.354	;#Column 1
node	5	0.000	0.472	;#Column 1
node	6	0.000	0.590	;#Column 1
node	7	0.000	0.708	;#Column 1
node	8	0.000	0.826	;#Column 1
node	9	0.000	0.944	;#Column 1
node	10	0.000	1.062	;#Column 1
node	11	0.000	1.180	;#Column 1 #NODE U1

node	12	1.200	0.000	; #Column 2 #SUPPORT B
node	13	1.200	0.118	; #Column 2
node	14	1.200	0.236	; #Column 2
node	15	1.200	0.354	; #Column 2
node	16	1.200	0.472	; #Column 2 
node	17	1.200	0.59	; #Column 2
node	18	1.200	0.708	; #Column 2
node	19	1.200	0.826	; #Column 2
node	20	1.200	0.944	; #Column 2
node	21	1.200	1.062	; #Column 2
node	22	1.200	1.18	; #Column 2 #NODE U2

node	23	2.400	0.000	; #Column 3 #SUPPORT C
node	24	2.400	0.118	; #Column 3
node	25	2.400	0.236	; #Column 3
node	26	2.400	0.354	; #Column 3
node	27	2.400	0.472	; #Column 3
node	28	2.400	0.59	; #Column 3
node	29	2.400	0.708	; #Column 3
node	30	2.400	0.826	; #Column 3
node	31	2.400	0.944	; #Column 3
node	32	2.400	1.062	; #Column 3
node	33	2.400	1.18	; #Column 3

node	34	0.120	1.180	; #BEAM 1
node	35	0.24	1.180	; #BEAM 1
node	36	0.36	1.180	; #BEAM 1
node	37	0.48	1.180	; #BEAM 1
node	38	0.6		1.180	; #BEAM 1
node	39	0.72	1.180	; #BEAM 1
node	40	0.84	1.180	; #BEAM 1
node	41	0.96	1.180	; #BEAM 1
node	42	1.08	1.180	; #BEAM 1

node	43	1.32	1.180	; #BEAM 2
node	44	1.44	1.180	; #BEAM 2
node	45	1.56	1.180	; #BEAM 2
node	46	1.68	1.180	; #BEAM 2
node	47	1.8		1.180	; #BEAM 2
node	48	1.92	1.180	; #BEAM 2
node	49	2.04	1.180	; #BEAM 2
node	50	2.16	1.180	; #BEAM 2
node	51	2.28	1.180	; #BEAM 2


###################################### BOUNDRY CONDITIONS #########################################
# http://opensees.berkeley.edu/wiki/index.php/Fix_command

#fix nodetag dofx dofy	dof moment about z [ 1 = fixed 0 = free ];	
fix 1 1 1 0; 
fix 12 1 1 0; 
fix 23 1 1 0;
		
		
############################# MATERIAL DEFINITIONS #########################################	

set Es 210000000; 		#MPa	# steel initial Young's modulus;
set Fy 355000;			#MPa	# steel initial yield strength;
set b 0.001;		#0.1%	# strain-hardening  ratio;

set matTag 1;
#define steel01 material: $matTag $yieldStress $E $rat	
uniaxialMaterial Steel01Thermal $matTag $Fy $Es $b;

set secTag 1;
set d 0.080;		# depth
set bf 0.046;		# flange width
set tf 0.0052;		# flange thickness
set tw 0.0038;	    # web thickness
set nfdw 8;			# number of fibers along dw
set nftw 1;			# number of fibers along tw
set nfbf 1;			# number of fibers along bf
set nftf 4;			# number of fibers along tf


WsectionThermal  $secTag $matTag $d $bf $tf $tw $nfdw $nftw $nfbf $nftf	$Es



##################################### TRANSFORMATION DEFINITIONS ############################
# http://opensees.berkeley.edu/wiki/index.php/Geometric_Transformation_Command

#three transformation types can be chosen: Linear, PDelta, Corotational

set transfTag 1;
# transforamtion: geomTransf $type $TransfTag; 
geomTransf Corotational $transfTag  ; 

############################# ELEMENT PROPERTIES ###########################################


#define beam element: dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;
#"numIntgrPts" is the number of integration points along the element;
#"TransfTag" is pre-defined coordinate-transformation;		
#element choice is 	dispBeamColumnTemperature		

#dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $transfTag;			
	
element	dispBeamColumnThermal	1	1	2	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	2	2	3	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	3	3	4	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	4	4	5	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	5	5	6	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	6	6	7	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	7	7	8	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	8	8	9	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	9	9	10	3	$secTag $transfTag; #COLUMN 1
element	dispBeamColumnThermal	10	10	11	3	$secTag $transfTag; #COLUMN 1
							
element	dispBeamColumnThermal	11	12	13	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	12	13	14	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	13	14	15	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	14	15	16	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	15	16	17	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	16	17	18	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	17	18	19	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	18	19	20	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	19	20	21	3	$secTag $transfTag; #COLUMN 2
element	dispBeamColumnThermal	20	21	22	3	$secTag $transfTag; #COLUMN 2
							
element	dispBeamColumnThermal	21	23	24	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	22	24	25	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	23	25	26	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	24	26	27	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	25	27	28	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	26	28	29	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	27	29	30	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	28	30	31	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	29	31	32	3	$secTag $transfTag; #COLUMN 3
element	dispBeamColumnThermal	30	32	33	3	$secTag $transfTag; #COLUMN 3
							
element	dispBeamColumnThermal	31	11	34	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	32	34	35	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	33	35	36	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	34	36	37	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	35	37	38	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	36	38	39	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	37	39	40	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	38	40	41	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	39	41	42	3	$secTag $transfTag; #BEAM 1
element	dispBeamColumnThermal	40	42	22	3	$secTag $transfTag; #BEAM 1
							
element	dispBeamColumnThermal	41	22	43	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	42	43	44	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	43	44	45	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	44	45	46	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	45	46	47	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	46	47	48	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	47	48	49	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	48	49	50	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	49	50	51	3	$secTag $transfTag; #BEAM 2
element	dispBeamColumnThermal	50	51	33	3	$secTag $transfTag; #BEAM 2

	

############################################## OUTPUTS ######################################################################

recorder Node -file $dataDir/U1.out -time -node 11 -dof 1  disp;	# displacements of node U1 DOF 1
recorder Node -file $dataDir/U2.out -time -node 22 -dof 1  disp;	# displacements of node U2 DOF 1
recorder Node -file $dataDir/RXNS.out -time -node 1 12 23 -dof 2 3 reaction; #support RXNS





############################################## GRAVITY LOADING ##############################################################


#GRAVITY LOADS
pattern Plain 1 Linear {
load 4 0. -74.0 0.;
load 22 0. -74.0 0.;
load 33 2.85 -74.0 0.;
for {set i 31} {$i <= 50} {incr i} {
	eleLoad -ele $i -type -beamUniform -0.060 0. 0.;
}
};

set Nstep 100;  
set Factor [expr 1.0/$Nstep];

# GRAVITY LOAD ANALYSIS
constraints Plain;     		
numberer Plain;			
system BandGeneral;		
test NormDispIncr 1e-12 500 ; 		
algorithm Newton;
integrator LoadControl $Factor 	
analysis Static;			
analyze $Nstep;
loadConst -time 0.0

puts "Loads - Done!"

############################## THERMAL LOADING ###################################

set T  550; 			#Max Temp - DEG CELCIUS
set Y2 [expr -$d/2]; 	#top fiber of beam
set Y1 [expr $d/2]; 	#Bottom fiber of beam


pattern Plain 2 Linear {
	for {set i 1} {$i <= 20} {incr i} { eleLoad -ele $i -type -beamThermal $T $Y2 $T $Y1; }
	for {set i 31} {$i <= 40} {incr i} { eleLoad -ele $i -type -beamThermal $T $Y2 $T $Y1; }
};

	set Nstep 1000;  		
	set Factor [expr 1.0/$Nstep]; 		# first load increment;
	
	constraints Plain;					# how it handles boundary conditions
	numberer Plain;						# renumber dof's to minimize band-width (optimization)
	system UmfPack;
	test NormDispIncr 1e-6 1000;
	algorithm Newton;					# use Newton's solution algorithm: updates tangent stiffness at every iteration
	integrator LoadControl $Factor;		# determine the next time step for an analysis
	analysis Static;					# define type of analysis static or transient
	analyze $Nstep;						# apply fire load
	
puts "Fire - Done!"	
	
wipe;

