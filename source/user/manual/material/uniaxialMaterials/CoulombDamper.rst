.. _CoulombDamper:

CoulombDamper Material
^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct the uniaxial CoulombDamper material producing elastic stiffness and friction force.

.. function:: uniaxialMaterial CoulombDamper $matTag $Tangent $FrictionFoce -tol $tol -numFlipped $numFlipped -reduceFc -dampOutTangent $dampOutTangent

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $Tangent, |float|,  the tangent stiffness for strain.
   $FrictionFoce, |float|, the friction force opposite to strain rate.
   $tol, |float|, the tolerance to check if strain rate is small.
   $numFlipped, |integer|, the number of times that the strain rate is flipped before adjusting friction force.
   -reduceFc, |string|, reducing friction force if strain rate is flipped several times.
   $dampOutTangent, |float|, giving a constant damping tangent if strain rate is flipped several times.


