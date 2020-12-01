*********
Example 3
*********

A 6m long beam has a uniform applied load of 10 kN/m. With the loading sustained, the beam is heated to a target temperature of 1180 :sup:`o` C.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: figures/Example3_fig1.png
	:align: center
	:width: 500px
	:figclass: align-center

**Elevation of beam and member cross-section**

Example overview: A steel beam is subjected to a uniform temperature
using a linear time-temperature history. Vertical midspan displacement
of the heated beam is recorded throughout the analysis. An investigation
is performed on the impact the following parameters have on the midspan
displacement of the beam: (i) including 2nd order geometric
transformations, and (ii) restraining the horizontal displacement of the
boundary conditions

Download Example 3   files:

:download:`Example3.tcl <files/Example3.tcl>`.

:download:`WsectionThermal.tcl <files/WsectionThermal.tcl>`.

:download:`Example 3 Outputs <files/Example3_OUTPUT.zip>`.

Objectives
----------


1. Develop a simply supported steel beam model using displacement-based
   beam elements with tempurature-dependent material properites,
2. Record the midspan vertical displacment due to a linear
   time-temperature heating curve and a uniformly distributed gravity
   load, and
3. Demonstrate the difference in midspan displacement of the beam when
   including 2nd order geometric transformations and restraining the
   beam against horizontal displacement of the beam ends.

Material
--------

The uniaxialMaterial Steel01Thermal includes temperature-dependent steel thermal and mechanical properties according to Eurocode 3 carbon steel. More details of Steel01 can be found at: `Steel01 Material <https://opensees.berkeley.edu/wiki/index.php/Steel01_Material>`__

.. function:: uniaxialMaterial Steel01Thermal $matTag $Fy $Es $b;

Es = 210000 MPa (Young’s modulus of elasticity at ambient temperatures)

Fy = 250 MPa (Yield strength of material at ambient temperatures)

b = 0.01 (Strain-Hardening Ratio)



Transformation
--------------

Both Linear & Corotational (Non-Linear)Transformations were used, and
the resulting midspan displacements of the beams were recorded to view
differences of including 2nd order bending effects.

    .. function:: geomTransf Linear $transftag;

or

    .. function:: geomTransf Corotational $transftag;

Learn more about geometric transofrmations: `Geometric
Transformation <http://opensees.berkeley.edu/wiki/index.php/Geometric_Transformation_Command>`__

section
-------

This example uses a W-shape beam, therefore an external .tcl script is used to define the fiber sections. This script uses fibersecThermal to procure a fibered W-shape section with a section tag to be used while defining elements. Eight fibers are used throughout the web and four fibers within each flange. 

In previous versions of OpenSees, a default value for torsional stiffness was used (GJ). In versions 3.1.0 and newer fiber sections require a value for torsional stiffness. This is a 2D example with negligible torsion, however a value is required. The Young's Modulus is used for convenience. 

Wsection dimensions:

    .. function:: set d 355; 	#mm	
    .. function:: set bf 171.5; #mm 	
    .. function:: set tf 11.5;  #mm	
    .. function:: set tw 7.4;  #mm		
    .. function:: set nfdw 8; #mm		
    .. function:: set nftw 1; #mm			
    .. function:: set nfbf 1; #mm			
    .. function:: set nftf 4; #mm			


* secTag - section tag
* matTag - material tag
* d  = nominal depth
* tw = web thickness
* bf = flange width
* tf = flange thickness
* nfdw = number of fibers along web depth 
* nftw = number of fibers along web thickness
* nfbf = number of fibers along flange width
* nftf = number of fibers along flange thickness 
* Gj = torsional stiffness

Wsection secTag matTag d bf tf tw nfdw nftw nfbf nftf Gj 

.. function:: Wsection 1 1 $d $bf $tf $tw 8 1 1 4 $Es

.. figure:: figures/Wsection_FiberSection.png
	:align: center
	:width: 500px
	:figclass: align-center

**Cross section of W-shape showing fibers in the flanges and the web**

Element
-------

dispBeamColumnThermal elements are used because temperature-dependent
thermal and mechanical steel properties can be applied to these
elements. Any portion of the structure that is being heated must use
elements that are compatible with uniaxialMaterial Steel01Thermal. At
the time this model was developed, dispBeamColumnThermal was the only
element type that could have tempurature-dependent thermal and
mechanical properties applied to them.

This example was developed using 6 elements along the length of the
beam.

dispBeamColumnThermal $eleTag $iNode $jNode $numIntgrPts $secTag $TransfTag;

.. function:: element dispBeamColumnThermal $secTag 1 2 5 $secTag $transftag;


This example will build off of the benchmarked examples and therefore
used 5 iteration points in each element to simulate the beam bending and
thermal expansion.


Output Recorders
----------------

$dataDir is defined at the beginning of the model, this creates a folder
within your working directory where output files will be saved. 

.. function:: set dataDir Examples/EXAMPLE3\_OUTPUT;

.. function:: file mkdir $dataDir;

Displacement of the midspan node (4) in DOF 2 (Vertical Displacement)

.. function:: recorder Node -file $dataDir/Midspan\_Disp.out" -time -node 4 -dof 2 disp;

Reaction forces at end nodes (nodes 1 & 7) 

.. function:: recorder Node -file $dataDir/RXNs.out -time -node 1 7 -dof 2 reaction;

Learn more about the Recorder Command: `Recorder Command <http://opensees.berkeley.edu/wiki/index.php/Recorder_Command>`__


Thermal Loading
---------------

This particular model is heating a beam to a set temperature over the
time period of the model. We are not asking OpenSees to use a specific
time-temperature curve, rather linearly ramp up the temperature from
ambient to 1180 :sup:`o` C.

Therefore, we set the maximum temperature as follows:

T = Max Temperature [:sup:`o` C] 

.. function:: set T 1180;

In OpenSees, the user can define 2 or 9 temperature data points
through the cross section. In a 2D analysis framework, like this
example, temperature data point locations are specified on the y-axis of
the local coordinate system (as shown in the figure above). And are
linearly interpolated between the defined points. Because this example
is using a uniformly heated beam, two temperature points on each extreme
fiber on the y-axis will be chosen. The beam has a depth of
$d, therefore, Y1 = $d/2 & Y2 = -$d/2 the top and bottom fibers
respectively.

Top fiber of beam 

.. function:: set Y1 [expr $d/2];

Bottom fiber of beam 

.. function:: set Y2 [expr -$d/2];

.. figure:: figures/Example3_fig2.png
	:align: center
	:width: 500px
	:figclass: align-center

**Location of defined input temperature locations on the member cross section**


The bottom extreme fiber temperature must be defined first. The target
maximum temperature for each extreme fiber is set to 1180 :sup:`o` C and will be
increased incrementally and linearly as the time step continues in the
analysis. An external temperature data set could also be used for more
complex temperature loading.

Using a plain linear loading pattern, Elements 1-6 will be heated to the
target tempurature, $T using a for loop for effecency. The syntax for this is: 

.. function:: pattern Plain 3 Linear {for {set level 1} {$level <= 6} {incr level 1} {set eleID $level eleLoad -ele $eleID -type -beamThermal $T $Y2 $T $Y1;}}


Thermal Analysis
----------------

Thermal loading is applied in 1000 steps, with a load factor of 0.001.
Each step is a 0.001 increment of the maximum temperature specified in
the thermal loading step: $T. The analysis is a static analysis and the
contraints of the beam are plain. 1000 increments was also used during
thermal analysis to allow for easy correlation between the input
temperatures and the recorded output.

A variety of load factors were examined and the solution converged when
a load factor of 0.001 was used. OpenSees is sensitive to the load
factor, therefore, it is important to ensure that benchmarking examples
are performed to determine the proper load factor to use in structural
fire engineering analyses.

.. function:: set Nstep 1000;

Thermal load is applied in 1000 steps. Each step is an 0.001 increment
of the maximum temperature specified in the thermal loading step $T
(1180)

.. function::  set Factor [expr 1.0/$Nstep];

.. function::  integrator LoadControl $Factor;

.. function::  analyze $Nstep;


Output Plots
------------

After the model has completed running, the results will be a vertical
midspan dislamcent of the recorded node. Since the temperature was
linearly ramped up from ambient to 1180 :sup:`o` C, the user can develop a
temperature history that matches every increment of the model.
Additionally,mid-span displacement of the beam when including 2nd order
geometric transformations, as well as restraining the horizontal
boundary conditions are plotted. The same model was excuted in the finite element software Abaqus additonally plotted as "AB". 


   .. figure:: figures/Example3_Output.png
	:align: center
	:width: 500px
	:figclass: align-center


Sources
-------

[1] W. Maddalozzo and E.C. Fischer, "Post-earthquake fire performance of steel buildings," World Conference on Earthquake Engineering, 17WCEE,
Sendai, Japan - September 13-18, 2020.
