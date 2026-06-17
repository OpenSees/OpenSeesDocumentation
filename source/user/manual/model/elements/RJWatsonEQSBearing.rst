.. _RJWatsonEQSBearing:

RJWatsonEQSBearing Element
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs an RJ Watson EQS sliding bearing element with separate uniaxial materials for axial; shear; and moment directions. Shear friction uses a friction model. The iNode represents the sliding surface.

.. function:: element RJWatsonEqsBearing $eleTag $iNode $jNode $frnMdlTag $kInit -P $matTag -Vy $matTag -Mz $matTag <-orient $x1 $x2 $x3 $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. function:: element RJWatsonEqsBearing $eleTag $iNode $jNode $frnMdlTag $kInit -P $matTag -Vy $matTag -Vz $matTag -T $matTag -My $matTag -Mz $matTag <-orient <$x1 $x2 $x3> $y1 $y2 $y3> <-shearDist $sDratio> <-doRayleigh> <-mass $m> <-iter $maxIter $tol>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $frnMdlTag, |integer|, tag of a previously defined friction model
   $kInit, |float|, initial elastic stiffness in local shear direction
   $matTag, |integer|, uniaxial material tag for axial behavior (``-P``)
   $matTag, |integer|, uniaxial material tag for shear in local y (``-Vy``)
   $matTag, |integer|, uniaxial material tag for shear in local z (``-Vz``; 3D only)
   $matTag, |integer|, uniaxial material tag for torsion (``-T``; 3D only)
   $matTag, |integer|, uniaxial material tag for moment about local y (``-My``)
   $matTag, |integer|, uniaxial material tag for moment about local z (``-Mz``)
   $sDratio, |float|, shear distance from iNode as fraction of element length (optional; default 0.0)
   $m, |float|, element mass (optional; default 0.0)
   $maxIter $tol, |integer| |float|, equilibrium iteration limit and tolerance (optional)

.. note::

   1. In 2D problems use ``-Vy`` and ``-Mz``. In 3D problems use ``-Vy``, ``-Vz``, ``-T``, ``-My``, and ``-Mz``.

   2. Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, ``basicDisplacement``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element RJWatsonEqsBearing 1 1 2 1 250.0 -P 1 -Vy 2 -Mz 3

   2. **Python Code**

   .. code-block:: python

      element('RJWatsonEqsBearing', 1, 1, 2, 1, 250.0, '-P', 1, '-Vy', 2, '-Mz', 3)

Code developed by: Andreas Schellenberg, University of California, Berkeley
