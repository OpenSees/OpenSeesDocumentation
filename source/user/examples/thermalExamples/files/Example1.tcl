##########################################################################################
# Code by Walker Maddalozzo & Dr. Erica Fischer - Oregon State Univeristy - April 2019
# Example: simple beam with thermal expansion
# Units: Newtons, mm, seconds


	wipe all;							# clear memory of past model definitions
	model BasicBuilder -ndm 2 -ndf 3;	# Define the model builder, ndm = #dimension, ndf = #dofs
	#source DisplayModel2D.tcl;			# procedure for displaying a 2D perspective of model
	#source DisplayPlane.tcl;			# procedure for displaying a plane in a model
	set dataDir Examples/Example1_OUTPUT;		# name of output folder
	file mkdir $dataDir; 			    # create output folder
	
	
#------------------------------------------------------------------------------
#  Geometric model                         
#                                          ________
#                                         |    |    |            4 fibers in section                 
#       1 |------------------------|2     |____|____| 0.4m
#         |<----------1m---------->|      |    |    |
#                                         |____|____|
#                                            0.2m
#------------------------------------------------------------------------------
###################################################################################################
#          Define Geometry, Nodes, Masses, and Constraints											  
###################################################################################################


###################################### NODE DEFINITIONS ###########################################
# http://opensees.berkeley.edu/wiki/index.php/Node_command

# node nodetag locx locy	
node 1 0 0;			
node 2 1000 0;	

###################################### BOUNDRY CONDITIONS #########################################
# http://opensees.berkeley.edu/wiki/index.php/Fix_command

#fix nodetag dofx dofy	dof moment about z [ 1 = fixed 0 = free ]; 

#Left end fixed - right end roller to allow expansion.
fix 1 1 1 0; #pinned
fix 2 0 1 0; #roller	

##################################### MATERIAL DEFINITIONS ########################################

set Es 210000; 		#Mpa	# steel Young's modulus;
set Fy 250;			#MPa	# steel yield strength;
set b 0.001;				# strain-hardening  ratio;
	
#uniaxialMaterial Steel01Thermal $matTag $Fy $E0 $b
uniaxialMaterial Steel01Thermal 1 $Fy $Es $b;


##################################### TRANSFORMATION DEFINITIONS ############################
# http://opensees.berkeley.edu/wiki/index.php/Geometric_Transformation_Command

#three transformation types can be chosen: Linear, PDelta, Corotational

# transforamtion: geomTransf $type $TransfTag;
set transftag 1
geomTransf Linear $transftag; 


###################################### ELEMENT GEOMETRY ############################################


# PATCH COMMAND: http://opensees.berkeley.edu/wiki/index.php/Patch_Command

section FiberThermal 1 -GJ $Es {

    	set numSubdivIJ 2;     # horizontal
		set numSubdivJK 2;     # vertical
		set yI -100;
		set zI -200;
		set yJ 100;
		set zJ -200;
		set yK 100;
		set zK 200;
		set yL -100;
		set zL 200;
		patch quad 1 $numSubdivIJ $numSubdivJK $yI $zI $yJ $zJ $yK $zK $yL $zL	
}		



###################################### ELEMENT PROPERTIES ###########################################

#dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;
element dispBeamColumnThermal 1 1 2 5 1 $transftag;

###################################### RECORDER OUTPUTS #############################################

# http://opensees.berkeley.edu/wiki/index.php/Recorder_Command

recorder Node -file $dataDir/Node2disp.out -time -node 2 -dof 1 disp;		# displacements of end node (2) DOF 1 Horizontal Direction


###################################### THERMAL LOADS  ###############################################

# Defining tempurature data for two extreme locations. Tempturature will be linearally interpolated betweent the two locations. 

set T 1180.; 	#Max Temp - DEG CELCIUS 
set Y1 200.; 	#top fiber of beam
set Y2 -200.;	#Bottom fiber of beam


#pattern Plain $PatternTag Linear { eleLoad -ele $eleTag -type -beamThermal $MaxTemp $ExtremeFiberLoc1 $MaxTemp $ExtremeFiberLoc2 };
pattern Plain 1 Linear { eleLoad -ele 1 -type -beamThermal $T $Y2 $T $Y1 };


set Nstep 1000;
set Factor [expr 1.0/$Nstep];

constraints Plain;     		
numberer Plain;			
system BandGeneral;		
test NormDispIncr 1e-12 500;
algorithm Newton;						
integrator LoadControl $Factor;
analysis Static;			
analyze $Nstep;


puts "Fire Done. End Time: [getTime]"

wipe;
