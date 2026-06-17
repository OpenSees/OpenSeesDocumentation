.. _ElastomericBearingPlasticity:

ElastomericBearingPlasticity Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-node elastomeric bearing element with coupled shear plasticity (2D) or bidirectional plasticity (3D). Force-deformation in the non-shear directions is defined by user-supplied :ref:`uniaxialMaterial` objects. The command name ``elastomericBearing`` is an alias for ``elastomericBearingPlasticity``.

.. function:: element elastomericBearingPlasticity $eleTag $iNode $jNode $kInit $qd $alpha1 $alpha2 $mu -P $matTag -Mz $matTag <-orient $x1 $x2 $x3 $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m>

.. function:: element elastomericBearingPlasticity $eleTag $iNode $jNode $kInit $qd $alpha1 $alpha2 $mu -P $matTag -T $matTag -My $matTag -Mz $matTag <-orient <$x1 $x2 $x3> $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $kInit, |float|, initial elastic stiffness in local shear direction
   $qd, |float|, characteristic strength
   $alpha1, |float|, post-yield stiffness ratio of linear hardening component
   $alpha2, |float|, post-yield stiffness ratio of nonlinear hardening component
   $mu, |float|, exponent of nonlinear hardening component
   $matTag, |integer|, uniaxial material tag for axial behavior (``-P``)
   $matTag, |integer|, uniaxial material tag for torsion (``-T``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local y (``-My``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local z (``-Mz``)
   $sDratio, |float|, shear distance from iNode as fraction of element length (optional; default 0.5)
   $m, |float|, element mass (optional; default 0.0)

.. note::

   1. By default the bearing does not contribute to Rayleigh damping. Use ``-doRayleigh`` to include it.

   2. Specify realistic axial stiffness; extremely large values can cause numerical sensitivity.

   3. Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, ``basicDisplacement``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element elastomericBearingPlasticity 1 1 2 20.0 2.50 0.02 0.0 3.0 -P 1 -Mz 2

   2. **Python Code**

   .. code-block:: python

      element('elastomericBearingPlasticity', 1, 1, 2, 20.0, 2.50, 0.02, 0.0, 3.0, '-P', 1, '-Mz', 2)

Code developed by: Andreas Schellenberg, University of California, Berkeley
