.. _SingleFrictionPendulumBearing:

SingleFrictionPendulumBearing Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-node single concave friction pendulum bearing. The iNode is the concave sliding surface and the jNode is the articulated slider. Shear behavior includes post-yield stiffening from the concave surface and uses a friction model.

.. function:: element singleFPBearing $eleTag $iNode $jNode $frnMdlTag $Reff $kInit -P $matTag -Mz $matTag <-orient $x1 $x2 $x3 $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. function:: element singleFPBearing $eleTag $iNode $jNode $frnMdlTag $Reff $kInit -P $matTag -T $matTag -My $matTag -Mz $matTag <-orient <$x1 $x2 $x3> $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes (iNode is concave surface)
   $frnMdlTag, |integer|, tag of a previously defined friction model
   $Reff, |float|, effective radius of concave sliding surface
   $kInit, |float|, initial elastic stiffness in local shear direction
   $matTag, |integer|, uniaxial material tag for axial behavior (``-P``)
   $matTag, |integer|, uniaxial material tag for torsion (``-T``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local y (``-My``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local z (``-Mz``)
   $sDratio, |float|, shear distance from iNode as fraction of element length (optional; default 0.0)
   $m, |float|, element mass (optional; default 0.0)
   $maxIter $tol, |integer| |float|, equilibrium iteration limit and tolerance (optional; defaults 20 and 1e-8)

.. note::

   1. The axial uniaxial material is modified for no-tension behavior.

   2. For pressure-velocity-temperature dependent friction see :ref:`FPBearingPTV`.

   3. Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, ``basicDisplacement``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element singleFPBearing 1 1 2 1 34.68 250.0 -P 1 -Mz 2 -orient 0 1 0 -1 0 0

   2. **Python Code**

   .. code-block:: python

      element('singleFPBearing', 1, 1, 2, 1, 34.68, 250.0, '-P', 1, '-Mz', 2, '-orient', 0, 1, 0, -1, 0, 0)

Code developed by: Andreas Schellenberg, University of California, Berkeley
