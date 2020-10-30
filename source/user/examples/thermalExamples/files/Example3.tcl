##########################################################################################
# Code by Walker Maddalozzo & Dr. Erica Fischer - Oregon State Univeristy - April 2019
# Example: thermal expansion & deflection of a simple beam with a uniformaly distributed load 
# Units: Newtons, mm, seconds


###################################################################################################
#          Set Up & Source Definition									  
###################################################################################################
	wipe all;							# clear memory of past model definitions
	model BasicBuilder -ndm 2 -ndf 3;	# Define the model builder, ndm = #dimension, ndf = #dofs
	source WsectionThermal.tcl
	#source DisplayModel2D.tcl;			# procedure for displaying a 2D perspective of model	
	#source DisplayPlane.tcl;
	#procedure for displaying a plane in a model

	
	set dataDir Example3_OUTPUT;		# name of output folder
	file mkdir $dataDir; 


	# create output folder
	
############################# GEOMETERIC MODEL ############################################		
#
#                          
#                                         
#                                                                 
#       1 |---2---3---4---5---6---|7   
#         |<----------6m--------->|      
#                                         
#                                          
#
############################################################################################
#          Define Geometry, Nodes, Masses, and Constraints											  
############################################################################################


############################## NODAL DEFINITIONS ##########################################
# http://opensees.berkeley.edu/wiki/index.php/Node_command

# node nodetag locx locy	
node 1 0 0; #mm
node 2 1000 0; #mm
node 3 2000 0; #mm
node 4 3000 0; #mm
node 5 4000 0; #mm
node 6 5000 0; #mm
node 7 6000 0; #mm


#define boundary condition;

#fix nodetag dofx dofy	dofz [ 1 = fixed 0 = free ];

fix 1 1 1 0; #pinned

#switch between pin & roller to see the effects of restraining both ends of the beam
fix 7 1 1 0; #pinned  	
#fix 7 0 1 0; #roller
	
	
############################# MATERIAL DEFINITIONS #########################################	
	

set Fy 275;		#MPa	# steel yield strength
set Es 210000;	#MPa	# steel Young's modulus
set b 0.01;		# strain-hardening ratio	

set matTag 1;
#uniaxialMaterial Steel01Thermal $matTag $Fy $E0 $b
uniaxialMaterial Steel01Thermal $matTag $Fy $Es $b;

############################# SECTION PROPERTIES ###########################################	

# Wsection dimensions

	set d 355; 		#mm # depth of beam
	set bf 171.5; 	#mm # flange width
	set tf 11.5; 	#mm # flange thickness
	set tw 7.4; 	#mm # web thickness
	
	set nfdw 8;		# number of fibers along dw
	set nftw 1;		# number of fibers along tw
	set nfbf 1;		# number of fibers along bf
	set nftf 4;		# number of fibers along tf
	
	set secTag 1;

# sources Wsection.tcl which created a fibered section using dimensions d,bf,tf,tw and the number of fibers to be created. 

# Wsection $secTag $matTag $d $bf $tf $tw $nfdw $nftw $nfbf $nftf
WsectionThermal  $secTag $matTag $d $bf $tf $tw $nfdw $nftw $nfbf $nftf;



##################################### TRANSFORMATION DEFINITIONS ############################
# http://opensees.berkeley.edu/wiki/index.php/Geometric_Transformation_Command

#three transformation types can be chosen: Linear, PDelta, Corotational

# transforamtion: geomTransf $type $transfTag; 

set transfTag 1;
# Switch between Linear & Corotational to observe 2nd-order effects
geomTransf Linear $transfTag; 
#geomTransf Corotational $transfTag; 


############################# ELEMENT PROPERTIES ###########################################

#define beam element: dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;
#"numIntgrPts" is the number of integration points along the element;
#"TransfTag" is pre-defined coordinate-transformation;		
#element choice is 	dispBeamColumnTemperature		

#dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $transfTag;	

element dispBeamColumnThermal 1 1 2 5 $secTag $transfTag;
element dispBeamColumnThermal 2 2 3 5 $secTag $transfTag;
element dispBeamColumnThermal 3 3 4 5 $secTag $transfTag;
element dispBeamColumnThermal 4 4 5 5 $secTag $transfTag;
element dispBeamColumnThermal 5 5 6 5 $secTag $transfTag;
element dispBeamColumnThermal 6 6 7 5 $secTag $transfTag;


############################# RECORDER OUTPUTS #############################################

recorder Node -file $dataDir/Midspan_Disp.out -time -node 4 -dof 2 disp;
recorder Node -file $dataDir/RXNs.out -time -node 1 7 -dof 2 reaction;



############################# GRAVITY LOADS ################################################

pattern Plain 1 Linear {
#PK CREATE UNIFORM LOADS FOR BEAMS
set  UDL -10;    

for {set level 1} {$level <= 6} {incr level 1} {
	set eleID $level;
	eleLoad -ele $eleID -type -beamUniform $UDL 0; 
	}}	



	set NstepGravity 10;					# apply gravity in 10 steps
	set DGravity [expr 1.0/$NstepGravity];	# load increment
	set Tol 1.0e-8;							# convergence tolerance for test
	
	constraints Plain;						# how it handles boundary conditions
	numberer RCM;							# renumber dof's to minimize band-width (optimization)
	system UmfPack;							# how to store and solve the system of equations in the analysis (large model: try UmfPack)
	test NormDispIncr $Tol 100;				# determine if convergence has been achieved at the end of an iteration step
	algorithm Newton;						# use Newton's solution algorithm: updates tangent stiffness at every iteration
	integrator LoadControl $DGravity;		# determine the next time step for an analysis
	analysis Static;						# define type of analysis: static or transient
	analyze $NstepGravity;					# apply gravity
	
	
	
	
puts "Loading Done. End Time: [getTime]"

	loadConst -time 0.0	

############################# THERMAL LOADS  ###############################################

set T  1000; 			#Max Temp - DEG CELCIUS
set Y1 [expr $d/2]; 	#top fiber of beam
set Y2 [expr -$d/2]; 	#Bottom fiber of beam


pattern Plain 3 Linear {

	
	for {set level 1} {$level <= 6} {incr level 1} {
	set eleID $level
	eleLoad -ele $eleID -type -beamThermal $T $Y2 $T $Y1;
	}
	}


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
	


puts "Fire Done. End Time: [getTime]"

wipe;







