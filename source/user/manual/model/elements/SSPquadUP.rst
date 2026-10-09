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
   $k1 $k2, |float|, permeability in global x and y directions (hydraulic conductivity divided by the unit weight of the pore fluid)
   $e, |float|, void ratio
   $alpha, |float|, "pressure stabilization parameter; the element's authors recommend :math:`\alpha = 0.25h^2/(\rho c^2)`, with :math:`h` the element size and :math:`\rho c^2 = K + 4G/3` the P-wave modulus of the solid phase"
   $b1 $b2, |float|, optional body-force components (default 0.0)
   $Pup $Plow $Pleft $Pright, |float|, "optional normal tractions on the solid along sides 3-4, 1-2, 4-1 and 2-3, positive along the outward normal (default 0.0). They act in full from the start rather than through a load pattern, and can be changed with the ``pressureUpperSide``, ``pressureLowerSide``, ``pressureLeftSide`` and ``pressureRightSide`` parameters."

.. note::

   1. The pore pressure at a node is the velocity response of DOF 3, so record it with a :ref:`nodeRecorder` of ``-dof 3 vel``.

   2. Valid :ref:`elementRecorder` queries are ``stress2D3`` and ``strain2D3``, which return the element's stress and strain, and the queries of its nDMaterial, such as ``stress`` and ``strain``, which are passed on unchanged.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element SSPquadUP 1 1 2 3 4 1 1.0 2.2e6 1000.0 1.0e-5 1.0e-5 0.5 1.0

   2. **Python Code**

   .. code-block:: python

      element('SSPquadUP', 1, 1, 2, 3, 4, 1, 1.0, 2.2e6, 1000.0, 1.0e-5, 1.0e-5, 0.5, 1.0)

Code developed by: Chris McGann, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
