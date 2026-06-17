.. _bbarQuadUP:

bbarQuadUP Element
^^^^^^^^^^^^^^^^^^

This command constructs a four-node plane-strain quadrilateral element with the B-bar method to mitigate volumetric locking in coupled u-p analysis. Use with ``-ndm 2 -ndf 3``.

.. function:: element bbarQuadUP $eleTag $iNode $jNode $kNode $lNode $thick $matTag $bulk $fmass $hPerm $vPerm <$b1 $b2 $t>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order
   $thick, |float|, element thickness
   $matTag, |integer|, tag of a previously defined ND material
   $bulk, |float|, combined undrained bulk modulus
   $fmass, |float|, fluid mass density
   $hPerm $vPerm, |float|, permeability in horizontal and vertical directions
   $b1 $b2, |float|, optional body-force components (default 0.0)
   $t, |float|, optional uniform normal traction (default 0.0)

.. note::

   For the standard formulation without B-bar see :ref:`FourNodeQuadUP`.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element bbarQuadUP 1 1 2 3 4 1.0 1 2.2e6 1000.0 1.0e-5 1.0e-5

   2. **Python Code**

   .. code-block:: python

      element('bbarQuadUP', 1, 1, 2, 3, 4, 1.0, 1, 2.2e6, 1000.0, 1.0e-5, 1.0e-5)

Code developed by: Zhaohui Yang, UC San Diego
