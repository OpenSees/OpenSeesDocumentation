
.. _steel02:

Steel02 Material
^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.


.. function:: uniaxialMaterial Steel02 $matTag $Fy $E $b $R0 $cR1 $cR2 <$a1 $a2 $a3 $a4 $sigInit>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

$matTag	    integer tag identifying material
$Fy	    yield strength
$E0	    initial elastic tangent
$b	    strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
Recommended values: $R0=between 10 and 20, $cR1=0.925, $cR2=0.15

$a1	    isotropic hardening parameter, increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0). (optional)
$a2	    isotropic hardening parameter (see explanation under $a1). (optional default = 1.0).
$a3	    isotropic hardening parameter, increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0). (optional default = 0.0)
$a4	    isotropic hardening parameter (see explanation under $a3). (optional default = 1.0)
$sigInit    Initial Stress Value (optional, default: 0.0) the strain is calculated from epsP=$sigInit/$E
if (sigInit!= 0.0) { double epsInit = sigInit/E; eps = trialStrain+epsInit; } else eps = trialStrain;


   $matTag, |integer|, integer tag identifying material
   $Fy, |float|, yield strength
   $E0, |float|, initial elastic tangent
   $b, |float|, strain-hardening ratio (ratio between post-yield tangent and initial elastic tangent)
   $R0 $CR1 $CR2, |float|, parameters to control the transition from elastic to plastic branches.
   $a1, |float|, optional: isotropic hardening parameter: increase of compression yield envelope as proportion of yield strength after a plastic strain of $a2*($Fy/E0).
   $a2, |float|, optional:isotropic hardening parameter (see explanation under $a1)
   $a3, |float|, optional: isotropic hardening parameter: increase of tension yield envelope as proportion of yield strength after a plastic strain of $a4*($Fy/E0)
   $a4, |float|, optional: isotropic hardening parameter (see explanation under $a3)


.. note::
   Recommended values: $R0=between 10 and 20, $cR1=0.925, $cR2=0.15

..REFERENCE:

Filippou, F. C., Popov, E. P., Bertero, V. V. (1983). "Effects of Bond Deterioration on Hysteretic Behavior of Reinforced Concrete Joints". Report EERC 83-19, Earthquake Engineering Research Center, University of California, Berkeley.



.. _fig-mdof:

.. figure:: figures/Steel02.gif
	:align: center
	:figclass: align-center

	Steel01

.. figure:: figures/Steel01HystereticA.jpg
	:align: center
	:figclass: align-center

	Steel01 Material -- Default Hysteretic Behavior (NO isotropic hardening)

.. figure:: figures/Steel01HystereticB.jpg
	:align: center
	:figclass: align-center

	Steel01 Material -- Hysteretic Behavior of Model with Isotropic Hardening in Compression

.. figure:: figures/Steel01HystereticC.jpg
	:align: center
	:figclass: align-center

	Steel01 Material -- Hysteretic Behavior of Model with Isotropic Hardening in Tension

.. admonition:: Example 

   The following is used to construct a Steel01 mataerial with a tag of **1**, a yield strength of $60.0** and an initial tangent stiffness of **30000,0**.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Steel01 60.0 30000.0

   2. **Python Code**

   .. code-block:: python

      uniaxialMaterial('Steel01',60.0,30000.0)

Code Developed by: |fmk|
