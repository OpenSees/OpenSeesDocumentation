.. _Concrete02 :

Concrete02 Material -- Linear Tension Softening
^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial concrete material as described in [Yassin1994]_
.. function:: uniaxialMaterial Concrete02 $matTag $fpc $epsc0 $fpcu $epsU $lambda $ft $Ets 

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $fpc, |float|,  concrete compressive strength at 28 days (compression is negative)* .
   $epsc0, |float|, concrete strain at maximum strength* .
   $fpcu, |float|, concrete crushing strength*.
   $epsU, |float|, concrete strain at crushing strength*.
   $lambda, |float|, ratio between unloading slope at $epscu and initial slope.
   $ft, |float|, tensile strength.
   $ets, |float|, tension softening stiffness (absolute value) (slope of the linear tension softening branch) 

.. note::
  * Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
  * The initial slope for this model is (2*$fpc/$epsc0)

Typical Hysteretic Stress-Strain Relation for material 

.. figure:: figures/Concrete02/Concrete02.jpg
  :align: center
  :figclass: align-center

Comparison with Concrete01

.. figure:: figures/Concrete02/Concrete02Hysteretic.jpg
  :align: center
  :figclass: align-center

Code Developed by: Filip Filippou, UC Berkeley
Images Developed by Silvia Mazzoni

.. [Yassin1994]  Mohd Hisham Mohd Yassin, "Nonlinear Analysis of Prestressed Concrete Structures under Monotonic and Cycling Loads", PhD dissertation, University of California, Berkeley, 1994. 