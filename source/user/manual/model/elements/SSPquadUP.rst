.. _SSPquadUP:

SSPquadUP Element
^^^^^^^^^^^^^^^^^

This command constructs a stabilized single-point quadrilateral element with u-p formulation for plane-strain analysis of fluid-saturated porous media. Use with ``-ndm 2 -ndf 3``.

.. function:: element SSPquadUP $eleTag $iNode $jNode $kNode $lNode $matTag $t $fBulk $fDen $k1 $k2 $e $alpha <$b1 $b2> <$Pup $Plow $Pleft $Pright>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order
   $matTag, |integer|, tag of a previously defined ND material
   $t, |float|, element thickness
   $fBulk, |float|, fluid bulk modulus
   $fDen, |float|, fluid mass density
   $k1 $k2, |float|, permeability in local x and y directions
   $e, |float|, void ratio
   $alpha, |float|, :math:`1 - K_s/K_f` parameter
   $b1 $b2, |float|, optional body-force components (default 0.0)
   $Pup $Plow $Pleft $Pright, |float|, optional boundary pore pressures on element edges

.. note::

   Valid :ref:`elementRecorder` queries include ``force``, ``stress``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element SSPquadUP 1 1 2 3 4 1 1.0 2.2e6 1000.0 1.0e-5 1.0e-5 0.5 1.0

   2. **Python Code**

   .. code-block:: python

      element('SSPquadUP', 1, 1, 2, 3, 4, 1, 1.0, 2.2e6, 1000.0, 1.0e-5, 1.0e-5, 0.5, 1.0)

Code developed by: Chris McGann, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
