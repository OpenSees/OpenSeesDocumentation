.. _BeamContact2D:

BeamContact2D Element
^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-dimensional beam-to-surface contact element. A beam segment (nodes i-j) contacts a secondary node through a Lagrange multiplier node. Use with ``-ndm 2``.

.. function:: element BeamContact2D $eleTag $iNode $jNode $secondaryNode $lambdaNode $matTag $width $gapTol $forceTol <$cSwitch>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, beam end nodes
   $secondaryNode, |integer|, secondary (contact) node
   $lambdaNode, |integer|, Lagrange multiplier node
   $matTag, |integer|, tag of a contact ND material
   $width, |float|, beam width used in contact geometry
   $gapTol, |float|, gap tolerance for contact detection
   $forceTol, |float|, force tolerance for contact equilibrium
   $cSwitch, |integer|, optional initial contact flag

.. note::

   A penalty variant is available as ``BeamContact2Dp``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element BeamContact2D 1 1 2 10 11 1 0.5 1.0e-6 1.0e-6

   2. **Python Code**

   .. code-block:: python

      element('BeamContact2D', 1, 1, 2, 10, 11, 1, 0.5, 1.0e-6, 1.0e-6)

Code developed by: Chris McGann, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
