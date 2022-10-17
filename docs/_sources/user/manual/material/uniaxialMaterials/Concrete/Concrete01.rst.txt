.. _Concrete01 :

Concrete01 Material -- Zero Tensile Strength
^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas). 

.. function:: uniaxialMaterial Concrete01  $matTag $fpc $epsc0 $fpcu $epsu

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $fpc, |float|,  concrete compressive strength at 28 days (compression is negative)* .
   $epsc0, |float|, concrete strain at maximum strength* .
   $fpcu, |float|, concrete crushing strength*.
   $epsU, |float|, concrete strain at crushing strength*.

.. note::
  * Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
  * The initial slope for this model is (2*$fpc/$epsc0)

Typical Hysteretic Stress-Strain Relation for material 

.. figure:: figures/Concrete01/Concrete01.gif
  :align: center
  :figclass: align-center

.. Example::
  .. code-bloc::
    uniaxialMaterial Concrete01 1 -4.0 -0.002 0.0 -0.005; 

  The code above would create a Concrete01 uniaxial material with tag 1 with compression strength of 4.0 at strain 0.002 and reaches ultimate strength of 0.0 at strain of 0.005

Code Developed by: Filip Filippou, UC Berkeley
Images Developed by Silvia Mazzoni

