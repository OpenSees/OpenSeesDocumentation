.. _ElastomericBearingBoucWen:

ElastomericBearingBouc-Wen Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-node elastomeric bearing element with Bouc-Wen shear hysteresis (2D unidirectional or 3D coupled). Non-shear directions use user-defined :ref:`uniaxialMaterial` objects.

.. function:: element elastomericBearingBoucWen $eleTag $iNode $jNode $kInit $qd $alpha1 $alpha2 $mu $eta $beta $gamma -P $matTag -Mz $matTag <-orient $x1 $x2 $x3 $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. function:: element elastomericBearingBoucWen $eleTag $iNode $jNode $kInit $qd $alpha1 $alpha2 $mu $eta $beta $gamma -P $matTag -T $matTag -My $matTag -Mz $matTag <-orient <$x1 $x2 $x3> $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

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
   $eta, |float|, yielding exponent (default 1.0)
   $beta, |float|, first Bouc-Wen shape parameter (default 0.5)
   $gamma, |float|, second Bouc-Wen shape parameter (default 0.5)
   $matTag, |integer|, uniaxial material tag for axial behavior (``-P``)
   $matTag, |integer|, uniaxial material tag for torsion (``-T``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local y (``-My``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local z (``-Mz``)
   $sDratio, |float|, shear distance from iNode as fraction of element length (optional; default 0.5)
   $m, |float|, element mass (optional; default 0.0)
   $maxIter $tol, |integer| |float|, equilibrium iteration limit and tolerance (optional)

.. note::

   1. By default the bearing does not contribute to Rayleigh damping. Use ``-doRayleigh`` to include it.

   2. Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, ``basicDisplacement``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element elastomericBearingBoucWen 1 1 2 20.0 2.50 0.02 0.0 3.0 1.0 0.5 0.5 -P 1 -Mz 2

   2. **Python Code**

   .. code-block:: python

      element('elastomericBearingBoucWen', 1, 1, 2, 20.0, 2.50, 0.02, 0.0, 3.0, 1.0, 0.5, 0.5, '-P', 1, '-Mz', 2)

Code developed by: Andreas Schellenberg, University of California, Berkeley
