##########################################################################################
# Code by Walker Maddalozzo & Dr. Erica Fischer - Oregon State Univeristy - April 2019
#
# Example 2: simply restained beam with thermal expansion. Left half of beam stays at ambient tempurature, 
# while the right side is subjected to a tempurature rise to 1180 deg Celcius. Displacement recorded at 
# midsnap node of beam. 
#
# Units: Newtons, m, seconds

###################################################################################################
#          Set Up & Source Definition									  
###################################################################################################

	wipe all;									# clear memory of past model definitions
	#	'basic', 'number of dimensions [ndm], number of degrees of freedom [ndf]'
	model BasicBuilder -ndm 2 -ndf 3;   		# Define the model builder, ndm = #dimension, ndf = #dofs	
	set dataDir Example2_OUTPUT;		# name of output folder
	file mkdir $dataDir;						# create output folder
	
	
############################# GEOMETERIC MODEL ####################################################
#                         
#                                          ________
#                                         |    |    |            4 fibers in section                 
#       1 |------------2------------|3    |____|____| 200mm
#         |<-----1m----|----1m----->|     |    |    |
#         |<-----------2m---------->|     |____|____|
#                                            400mm
#
###################################################################################################
#          Define Geometry, Nodes, Masses, and Constraints											  
###################################################################################################


###################################### NODE DEFINITIONS ###########################################

#node $nodetag $locx $locy	
node 1 0 0;			
node 2 1000 0; #mm
node 3 2000 0; #mm

###################################### BOUNDRY CONDITIONS #########################################
# http://opensees.berkeley.edu/wiki/index.php/Fix_command

#fix nodetag dofx dofy	dof3(rotation) [ 1 = fixed 0 = free ]; 
fix 1 1 1 0; #PINNED	
fix 2 0 1 0; #vertical restraint
fix 3 1 1 0; #PINNED

##################################### MATERIAL DEFINITIONS ########################################

set Es 210000; 		#MPa	# steel initial Young's modulus;
set Fy 250;			#MPa	# steel initial yield strength;
set b 0.001;		#0.1%	# strain-hardening  ratio;
			
set matTag 1	
#uniaxialMaterial Steel01Thermal $matTag $Fy $E0 $b
uniaxialMaterial Steel01Thermal $matTag $Fy $Es $b;

##################################### TRANSFORMATION DEFINITIONS ############################
# http://opensees.berkeley.edu/wiki/index.php/Geometric_Transformation_Command

#three transformation types can be chosen: Linear, PDelta, Corotational

# transforamtion: geomTransf $type $transfTag;
set transfTag 1;
geomTransf Linear $transfTag ; 


###################################### ELEMENT GEOMETRY ############################################	
# PATCH COMMAND: http://opensees.berkeley.edu/wiki/index.php/Patch_Command

set secTag 1;
section FiberThermal $secTag -GJ $Es {

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
		patch quad $matTag $numSubdivIJ $numSubdivJK $yI $zI $yJ $zJ $yK $zK $yL $zL	
}


###################################### ELEMENT PROPERTIES ###########################################

#dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;

element dispBeamColumnThermal 1 1 2 5 $secTag $transfTag; #Element 1

element dispBeamColumnThermal 2 2 3 5 $secTag $transfTag; 	


############################# RECORDER OUTPUTS ######################################################

# http://opensees.berkeley.edu/wiki/index.php/Recorder_Command

#Displacment at center node DOF 1 (Horizontal Direction)
recorder Node -file $dataDir/MidspanNodeDisp.out -time -node 2  -dof  1  disp;

#Boundry RXNs
recorder Node -file $dataDir/BoundryRXN.out -time -node 1 3  -dof 1 2 reaction;

#Section forces in Element 1 & 2
recorder Element -file $dataDir/ele_force_1.out -time -ele 1 section 2 force
recorder Element -file $dataDir/ele_force_2.out -time -ele 2 section 2 force

####################################### THERMAL LOADS  ###############################################

set T 1180;  	#Max Temp - DEG CELCIUS
set Y1 -100; 	#Top fiber of beam - mm
set Y2 100;		#Bottom fiber of beam - mm


#pattern Plain PatternTag Linear   { eleLoad -ele $eleTag -type -beamThermal $Tempurature1 $Location 1 $Tempurature2 $Location2;}
pattern Plain 1 Linear {
	eleLoad -ele 1 -type -beamThermal 0  $Y1  0  $Y2;
	eleLoad -ele 2 -type -beamThermal $T $Y1 $T $Y2;
}

set Nsteps 1000;
set Factor [expr 1.0/$Nsteps];


constraints Plain;     		
numberer Plain;			
system BandGeneral;		
test NormDispIncr 1e-12 500 ;
algorithm ModifiedNewton;						
integrator LoadControl $Factor;
analysis Static;			
analyze $Nsteps;


puts "Fire Done. End Time: [getTime]"

wipe;





