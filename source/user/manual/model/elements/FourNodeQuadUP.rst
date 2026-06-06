.. _FourNodeQuadUP:

FourNodeQuadUP Element
^^^^^^^^^^^^^^^^^^^^^^

This command constructs a four-node plane-strain quadrilateral element for coupled solid-fluid (u-p) analysis of saturated porous media based on Biot theory. Each node has two solid displacement DOFs and one pore-pressure DOF. Use with ``-ndm 2 -ndf 3``. The registered command name is ``quadUP``.

.. function:: element quadUP $eleTag $iNode $jNode $kNode $lNode $thick $matTag $bulk $fmass $hPerm $vPerm <$b1 $b2 $t>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order
   $thick, |float|, element thickness
   $matTag, |integer|, tag of a previously defined ND material
   $bulk, |float|, combined undrained bulk modulus relating pore pressure and volumetric strain
   $fmass, |float|, fluid mass density
   $hPerm $vPerm, |float|, permeability in horizontal and vertical directions
   $b1 $b2, |float|, optional body-force components (default 0.0)
   $t, |float|, optional uniform normal traction; positive in tension (default 0.0)

.. note::

   1. Record pore pressure at nodes with a :ref:`nodeRecorder` on DOF 3.

   2. Valid :ref:`elementRecorder` queries include ``force``, ``stiffness``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element quadUP 1 1 2 3 4 1.0 1 2.2e6 1000.0 1.0e-5 1.0e-5

   2. **Python Code**

   .. code-block:: python

      element('quadUP', 1, 1, 2, 3, 4, 1.0, 1, 2.2e6, 1000.0, 1.0e-5, 1.0e-5)

Code developed by: Zhaohui Yang, UC San Diego
