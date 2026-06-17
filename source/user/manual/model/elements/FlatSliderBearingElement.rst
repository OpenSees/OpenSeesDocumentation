.. _FlatSliderBearingElement:

FlatSliderBearingElement
^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-node flat slider bearing element. The iNode represents the flat sliding surface and the jNode the slider. Shear behavior uses a friction model; axial and rotational behavior use :ref:`uniaxialMaterial` objects. The axial material is modified for no-tension behavior to capture uplift.

.. function:: element flatSliderBearing $eleTag $iNode $jNode $frnMdlTag $kInit -P $matTag -Mz $matTag <-orient $x1 $x2 $x3 $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. function:: element flatSliderBearing $eleTag $iNode $jNode $frnMdlTag $kInit -P $matTag -T $matTag -My $matTag -Mz $matTag <-orient <$x1 $x2 $x3> $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes (iNode is flat sliding surface)
   $frnMdlTag, |integer|, tag of a previously defined friction model
   $kInit, |float|, initial elastic stiffness in local shear direction
   $matTag, |integer|, uniaxial material tag for axial behavior (``-P``)
   $matTag, |integer|, uniaxial material tag for torsion (``-T``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local y (``-My``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local z (``-Mz``)
   $sDratio, |float|, shear distance from iNode as fraction of element length (optional; default 0.0)
   $m, |float|, element mass (optional; default 0.0)
   $maxIter $tol, |integer| |float|, equilibrium iteration limit and tolerance (optional; defaults 20 and 1e-8)

.. note::

   1. P-Delta moments are transferred entirely to the flat sliding surface (iNode) by default.

   2. Friction depends on axial force and slip rate; use a smaller time step for dynamic analysis when needed.

   3. Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, ``basicDisplacement``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element flatSliderBearing 1 1 2 1 250.0 -P 1 -Mz 2 -orient 0 1 0 -1 0 0

   2. **Python Code**

   .. code-block:: python

      element('flatSliderBearing', 1, 1, 2, 1, 250.0, '-P', 1, '-Mz', 2, '-orient', 0, 1, 0, -1, 0, 0)

Code developed by: Andreas Schellenberg, University of California, Berkeley
