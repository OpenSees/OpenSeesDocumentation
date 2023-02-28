.. _ViscoelasticGap :

Viscoelastic Gap Material
^^^^^^^^^^^^^^^^^^

This command is used to construct the uniaxial Jankowski Impact Material 

.. function:: uniaxialMaterial ViscoelasticGap  $matTag $K $c $gap

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $K, |float|,  stiffness.
   $C, |float|, damping coefficient.
   $gap, |float|, initial gap

.. note::

This material is implemented as a compression-only gap material, so $gap should be input as a negative value. Due to the viscous component of this material, a small tensile force is present at the end of an impact event.
.. Description::
This material model follows the constitutive law

  .. math:: f_c(t) = k(\delta(t)-g) + c \dot{\delta} (t)

where t is time, :math:`f_c (t)`  is the contact force, :math:`k` is the stiffness ($K), :math:`\delta(t)` is the indentation, g is the initial gap ($gap), c is the damping coefficient ($C) and :math:`\dot{\delta}(t)` is the indentation velocity.

Code Developed by: Patrick J. Hughes, UC San Diego

