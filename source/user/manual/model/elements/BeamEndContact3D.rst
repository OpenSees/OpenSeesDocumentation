.. _BeamEndContact3D:

BeamEndContact3D Element
^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional contact element between a beam end (nodes i-j) and a secondary node using a Lagrange multiplier node. Use with ``-ndm 3``.

.. function:: element BeamEndContact3D $eleTag $iNode $jNode $secondaryNode $lambdaNode $radius $gapTol $forceTol <$cFlag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, beam end nodes
   $secondaryNode, |integer|, secondary (contact) node
   $lambdaNode, |integer|, Lagrange multiplier node
   $radius, |float|, beam radius used in contact geometry
   $gapTol, |float|, gap tolerance for contact detection
   $forceTol, |float|, force tolerance for contact equilibrium
   $cFlag, |integer|, optional initial contact flag

.. note::

   A penalty variant is available as ``BeamEndContact3Dp``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element BeamEndContact3D 1 1 2 10 11 0.25 1.0e-6 1.0e-6

   2. **Python Code**

   .. code-block:: python

      element('BeamEndContact3D', 1, 1, 2, 10, 11, 0.25, 1.0e-6, 1.0e-6)

Code developed by: Chris McGann, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
