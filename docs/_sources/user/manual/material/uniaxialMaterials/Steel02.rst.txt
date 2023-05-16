
.. _steel02:

Steel02 Material
^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.


.. function:: uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2 <$a1 $a2 $a3 $a4 $sigInit>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|,	    integer tag identifying material
   $Fy, |float|, yield strength
   $E0, |float|, initial elastic tangent
   $b, |float|, strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
   R0 $CR1 $CR2, 3 |float|, parameters to control the transition from elastic to plastic branches.
   $a1, |float|, isotropic hardening parameter. (optional: default = 0.0). see note. 
   $a2, |float|, isotropic hardening parameter (optional: default = 1.0). see note.
   $a3, |float|, isotropic hardening parameter. (optional: default = 0.0). see note.
   $a4, |float|, isotropic hardening parameter. (optional: default = 1.0). see note.
   $sigInit, |float|, Initial Stress Value (optional: default = 0.0) 


.. note::

   $a1 and $a2: increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0). 

   $a3 and $a4: increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0). 

   Recommended values: $R0=between 10 and 20, $cR1=0.925, $cR2=0.15

   If $siginit is specified, strain is calculated from epsP=$sigInit/$E

   .. code::

      if (sigInit!= 0.0) { 
      	 double epsInit = sigInit/E; 
	 eps = trialStrain+epsInit; 
      } else {
         eps = trialStrain;
      }


.. [FilippouEtAl1983] Filippou, F. C., Popov, E. P., Bertero, V. V. (1983). "Effects of Bond Deterioration on Hysteretic Behavior of Reinforced Concrete Joints". Report EERC 83-19, Earthquake Engineering Research Center, University of California, Berkeley.


.. _fig-steel02:

.. figure:: figures/Steel02/Steel02Monotonic.jpg
	:align: center
	:figclass: align-center

	Steel02 Material -- Material Parameters of Monotonic Envelope

.. figure:: figures/Steel02/Steel02HystereticA.jpg
	:align: center
	:figclass: align-center

	Steel02 Material -- Default Hysteretic Behavior (NO isotropic hardening)

.. admonition:: Example 

   The following is used to construct a Steel02 mataerial with a tag of **1**, a yield strength of $60.0** and an initial tangent stiffness of **30000,0**.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Steel02 60.0 30000.0 0.1 20.0 .925 .15

   2. **Python Code**

   .. code-block:: python

      uniaxialMaterial('Steel02',60.0,30000.0, 0.1, 20.0, .925, .15)

Code Developed by: |mhs|
