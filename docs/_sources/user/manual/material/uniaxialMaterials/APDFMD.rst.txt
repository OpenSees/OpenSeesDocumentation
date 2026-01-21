.. _APDFMD :

APDFMD Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an APDFMD material that simulates the hysteretic response of an asynchronous parallel double-stage friction-metallic damper. 
A typical parallel double-stage friction-metallic damper is composed of a frictional sub-damper, a metallic sub-damper and an asynchronously activation system. In the first stage only the first frictional sub-damper works and when the deformation reaches to $ad2, the second metallic sub-damper actives, exhibiting the double-stage working mechanism.


.. function:: uniaxialMaterial APDFMD $matTag $fy1 $E1 $ad2 $fy2 $E2  $a2 $n2

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $fy1, |float|, Yield load of the first frictional sub-damper
   $E1, |float|, Initial stiffness of the first frictional sub-damper
   $ad2, |float|, Activation deformation of the second metallic sub-damper
   $fy2, |float|, Yield load of the second metallic sub-damper
   $E2, |float|, Initial stiffness of the second metallic sub-damper
   $a2, |float|, Parameters to control the nonlinear behavior of the second metallic sub-damper 
   $n2, |float|, Parameters to control the transition from elastic to plastic branches of the second metallic sub-damper

.. figure:: figures/APDFMD/APDFMD1.png
	:align: center
	:figclass: align-center

.. note::
Example:
   To verify the reliability of the APDFMD uniaxialMaterial, three sets of test and simulation results are selected for verification. Material parameters are shown in the following table (Units can be arbitrarily converted, but must be unified):

.. figure:: figures/APDFMD/APDFMD2.png
	:align: center
	:figclass: align-center

The input parameters for the material should be as follows:
    **Tcl Code**

   .. code-block:: tcl


      uniaxialMaterial  APDFMD   1   210  140    45    70   23.33    0.5  15
      uniaxialMaterial  APDFMD   1   200  172    3.5   75   16.66    0.5  15
      uniaxialMaterial  APDFMD   1   210  300    9.5   70   23.33    0.5  15


Using these parameters, comparison between the experimental and simulated load-deformation curves of APDFMD is shown in Fig. 2. 



.. figure:: figures/APDFMD/APDFMD3.png
	:align: center
	:figclass: align-center



Code Developed by: Linlin Xie, Cantian Yang, Bingyan Liu, Aiqun Li, Beijing University of Civil Engineering and Architecture.

References:

[1] Fred Segal, and Dimitri V, Val. Energy evaluation for Ramberg Osgood hysteretic model. Journal of engineering mechanics 2006; 132(9): 907-913. DOI: 10.1061/(ASCE)0733-9399(2006)132:9(907)
