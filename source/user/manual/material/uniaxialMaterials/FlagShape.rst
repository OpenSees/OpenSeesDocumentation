.. _FlagShape:

FlagShape Material
^^^^^^^^^^^^^^^^^^

This command is used to construct the uniaxial FlagShape material 

.. function:: uniaxialMaterial FlagShape $matTag $E $fy $Eh <$beta>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $E, |float|,  initial stiffness.
   $fy, |float|, yield force.
   $Eh, |float|, plastic stiffness.
   $beta, |float|, parameter controlling flag behavior (optional with default value of: 0.0).

.. note::

   The value of $beta should range from 0 to 1. Bilinear elastic response is obtained with beta=0 while beta=1 gives bilinear hysteretic response. Values between 0 and 1 will give flag-shape response.
   
.. Description::

Response of FlagShape material for E=100, fy=100, and Eh=10 showing variation in beta parameter:

   .. figure:: figures/FlagShape.png
      :align: center
      :figclass: align-center

Code Developed by: Chin-Long Lee (Univ. of Canterbury) and Lei Zhang

.. [Lee2020] Lee CL (2020) Sparse proportional viscous damping model for structures with large number of degrees of freedom. Journal of Sound and Vibration; 478.  DOI: 10.1016/j.jsv.2020.115312.
   
