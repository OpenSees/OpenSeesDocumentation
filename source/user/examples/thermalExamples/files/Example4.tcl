##########################################################################################
# Code by Walker Maddalozzo & Dr. Erica Fischer - Oregon State Univeristy - May 2019
# Example: 2D frame: heated with a parametric fire curve
# Units: Newtons, m, seconds

wipe;					
set dataDir Example4_OUTPUT;					# name of output folder
file mkdir $dataDir; 			    # create output folder			
model BasicBuilder -ndm 2 -ndf 3;
source WsectionThermal.tcl; 


############################## NODAL DEFINITIONS ##########################################
# http://opensees.berkeley.edu/wiki/index.php/Node_command

#Left column
node 1	0.0	0.0;
node 2	0.0	350;
node 3	0.0 700;
node 4	0.0 1050;
node 5	0.0 1400;
node 6	0.0 1750;
node 7	0.0 2100;
node 8	0.0 2450;
node 9	0.0 2800;
node 10 0.0 3150;
node 11 0.0 3500;

#Beam
node 12 6000 0.0;
node 13 6000 350;
node 14 6000 700;
node 15 6000 1050;
node 16 6000 1400;
node 17 6000 1750;
node 18 6000 2100;
node 19 6000 2450;
node 20 6000 2800;
node 21 6000 3150;
node 22 6000 3500;

# Right column
node 23 600 3500;
node 24 1200 3500;
node 25 1800 3500;
node 26 2400 3500;
node 27 3000 3500;
node 28 3600 3500;
node 29 4200 3500;
node 30 4800 3500;
node 31 5400 3500;

###################################### BOUNDRY CONDITIONS #########################################
# http://opensees.berkeley.edu/wiki/index.php/Fix_command

#fix nodetag dofx dofy	dof moment about z [ 1 = fixed 0 = free ]; 	
fix 1 1 1 1; 
fix 12 1 1 1; 

#For this analysis it is considered that the horizontal displacements of nodes 11 & 22 are restricted to represent lateral bracing.
fix 11 1 0 0;
fix 22 1 0 0;
		
	
############################# MATERIAL DEFINITIONS #########################################		
		
#Steel01Thermal Material properties
set Es 210000; 		#MPa	# steel Young's modulus;
set Fy 275;			#MPa	# steel yield strength;
set b 0.01;			# strain-hardening  ratio 1%

set matTag 1;

uniaxialMaterial Steel01Thermal $matTag $Fy $Es $b;

############################### MEMBER SECTIONS #############################################

set secTag 1;
set d 160;		# depth
set bf 82;		# flange width
set tf 7.4;		# flange thickness
set tw 5.0;	    # web thickness

set nfdw 8;		# number of fibers along dw
set nftw 1;		# number of fibers along tw
set nfbf 1;		# number of fibers along bf
set nftf 4;		# number of fibers along tf


# Wsection $sectag
WsectionThermal  $secTag $matTag $d $bf $tf $tw $nfdw $nftw $nfbf $nftf	$Es;
	

##################################### TRANSFORMATION DEFINITIONS ############################
# http://opensees.berkeley.edu/wiki/index.php/Geometric_Transformation_Command

#three transformation types can be chosen: Linear, PDelta, Corotational

# transforamtion: geomTransf $type $TransfTag; 
set transfTag 1
geomTransf Corotational $transfTag  ; 


############################# ELEMENT PROPERTIES ###########################################

#define beam element: dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;
#"numIntgrPts" is the number of integration points along the element;
#"TransfTag" is pre-defined coordinate-transformation;		
#element choice is 	dispBeamColumnTemperature		

#dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;
				
element	dispBeamColumnThermal	1	1	2	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	2	2	3	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	3	3	4	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	4	4	5	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	5	5	6	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	6	6	7	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	7	7	8	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	8	8	9	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	9	9	10	3	$secTag $transfTag; #column1
element	dispBeamColumnThermal	10	10	11	3	$secTag $transfTag; #column1

element	dispBeamColumnThermal	11	12	13	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	12	13	14	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	13	14	15	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	14	15	16	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	15	16	17	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	16	17	18	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	17	18	19	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	18	19	20	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	19	20	21	3	$secTag $transfTag; #column2
element	dispBeamColumnThermal	20	21	22	3	$secTag $transfTag; #column2

element	dispBeamColumnThermal	21	11	23	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	22	23	24	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	23	24	25	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	24	25	26	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	25	26	27	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	26	27	28	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	27	28	29	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	28	29	30	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	29	30	31	3	$secTag $transfTag; #beam1
element	dispBeamColumnThermal	30	31	22	3	$secTag $transfTag; #beam1

############################# RECORDER OUTPUTS #############################################

#Reaction forces at end nodes. (1 & 12)
recorder Node -file $dataDir/RXNS.out -time -node 1 12 -dof 2 3 reaction;

#Displacement of the beam mid-span node (27), DOF 2 (Vertical Displacement)
recorder Node -file $dataDir/Midspan_BeamDisp.out -time -node 27 -dof 2 disp;


############################# GRAVITY LOADS ################################################


pattern Plain 1 Linear {
set  UDL -2;    
  eleLoad -ele 21 -type -beamUniform $UDL 0
  eleLoad -ele 22 -type -beamUniform $UDL 0 
  eleLoad -ele 23 -type -beamUniform $UDL 0
  eleLoad -ele 24 -type -beamUniform $UDL 0 
  eleLoad -ele 25 -type -beamUniform $UDL 0
  eleLoad -ele 26 -type -beamUniform $UDL 0 
  eleLoad -ele 27 -type -beamUniform $UDL 0
  eleLoad -ele 28 -type -beamUniform $UDL 0 
  eleLoad -ele 29 -type -beamUniform $UDL 0 
  eleLoad -ele 30 -type -beamUniform $UDL 0 
}
	
	
set Tol 1.0e-12;
set NstepGravity 10;					# apply gravity in 10 steps

constraints Plain;						# boundary conditions handling
numberer RCM;							# renumber dof's to minimize band-width (optimization)
system UmfPack;							# how to store and solve the system of equations in the analysis (large model: try UmfPack)
test NormDispIncr $Tol 500;				# determine if convergence has been achieved at the end of an iteration step  | Tolerance | Number of iterations
algorithm Newton;						# use Newton's solution algorithm: updates tangent stiffness at every iteration				
integrator LoadControl [expr 1.0/$NstepGravity];		# time step size
analysis Static;						# define type of analysis: static or transient
analyze $NstepGravity;					# apply gravity
	
	
puts "Gravity Loading done"

loadConst -time 0.0	


puts "Fire Loading"

 
 
	set Y9 [expr -$d/2];
	set Y8 [expr -($d/2 - 0.99*$tf)];
	set Y7 [expr -($d/2 - $tf)];
	set Y6 [expr 0.0-$d*0.99];
	set Y5 0.0;
	set Y4 [expr 0.0+$d*0.99];
	set Y3 [expr ($d/2 - $tf)];
	set Y2 [expr ($d/2 - 0.99*$tf)];
	set Y1 [expr $d/2];



############################## BEAMS  #################################################


#TEMPURATURE LOADING FOR THE BEAM
pattern Plain 11 Linear {

for {set level 21} {$level <= 30} {incr level 1} {
	set eleID $level;
	eleLoad -ele $eleID -type -beamThermal -source BeamTemp.txt $Y9 $Y8 $Y7 $Y6 $Y5 $Y4 $Y3 $Y2 $Y1;
	}}	

	
	
############################## COLUMNS  ################################################



pattern Plain 13 Linear {

#TEMPURATURE LOADING FOR THE LEFT COLUMN
for {set level 1} {$level <= 10} {incr level 1} {
	set eleID $level;
	eleLoad -ele $eleID -type -beamThermal -source Column1Temp.txt $Y9 $Y8 $Y7 $Y6 $Y5 $Y4 $Y3 $Y2 $Y1; 
	}}	
	
	

#TEMPURATURE LOADING FOR THE RIGHT COLUMN
pattern Plain 14 Linear {


for {set level 11} {$level <= 20} {incr level 1} {
	set eleID $level;
	eleLoad -ele $eleID -type -beamThermal -source Column2Temp.txt $Y9 $Y8 $Y7 $Y6 $Y5 $Y4 $Y3 $Y2 $Y1; 
	}}	



############################## COLUMNS  ###################################################


set Nstep 1000; #NUMBER OF STEPS TO BE ANALYIZED

constraints Plain;					# how it handles boundary conditions
numberer Plain;						# renumber dof's to minimize band-width (optimization)
system UmfPack;
test NormDispIncr 1e-12 1000;
algorithm Newton;					# use Newton's solution algorithm: updates tangent stiffness at every iteration	
 		
set Factor [expr 1.0/$Nstep]; 	# first load increment;
integrator LoadControl $Factor;	# determine the next time step for an analysis
analysis Static;			# define type of analysis static or transient
analyze $Nstep;		# apply fire load
	
puts "Fire done"



wipe;



