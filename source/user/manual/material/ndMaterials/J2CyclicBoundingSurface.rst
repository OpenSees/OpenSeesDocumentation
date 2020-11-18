.. _PM4Sand:

J2CyclicBoundingSurface Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Code Developed by: **Alborz Ghofrani** and |pedro| at U.Washington.

This command is used to construct a J2CyclicBoundingSurface material ([Borja-Amies1994]_).

   J2CyclicBoundingSurface $matTag $G $K $Su $Den $h $m $h0 $chi $beta

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, tag identifying material
   $G, |float|,   Shear modulus
   $K, |float|,   Bulk modulus
   $su, |float|,  Undrained shear strength
   $Den, |float|, Mass density of the material
   $h, |float|,   Hardening parameter
   $m, |float|,   Hardening exponent
   $h0 , |float|, Initial hardening parameter
   $chi, |float|,    "Initial damping (viscous). chi = 2*dr_o/omega (dr_o = damping ratio at zero strain, omega = angular frequency)"
   $beta, |float|,   "Integration variable (0 = explicit, 1 = implicit, 0.5 = midpoint rule)"

.. note::

   The material formulations for the J2CyclicBoundingSurface object are "ThreeDimensional" and "PlaneStrain".

   Valid Element Recorder queries are **stress**, **strain**

   Elastic response could be enforced by

   .. code::

       updateMaterialStage -material $matTag -stage 0

   Elastoplastic by

   .. code::

      updateMaterialStage -material $matTag -stage 1

.. [Borja-Amies1994] Borja R., Amies A., "Multiaxial Cyclic Plasticity Model for Clays". Journal of Geotech. Engrg., 1994, 120(6):1051-1070


.. admonition:: Example 1

   This example, provides an conventional triaxial compression test using one 8-node SSPBrick element and J2CyclicBoundingSurface material model.

   .. literalinclude:: J2CyclicBoundingSurfaceExample1.tcl
      :language: tcl
