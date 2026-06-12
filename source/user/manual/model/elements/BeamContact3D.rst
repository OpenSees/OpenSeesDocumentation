.. _BeamContact3D:

BeamContact3D Element
^^^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional beam-to-surface contact element. A beam segment (nodes i-j) contacts a secondary node through a Lagrange multiplier node. Use with ``-ndm 3``.

.. function:: element BeamContact3D $eleTag $iNode $jNode $secondaryNode $lambdaNode $radius $crdTransf $matTag $tolGap $tolF <$cSwitch>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, beam end nodes
   $secondaryNode, |integer|, secondary (contact) node
   $lambdaNode, |integer|, Lagrange multiplier node
   $radius, |float|, beam radius used in contact geometry
   $crdTransf, |integer|, tag of a coordinate transformation for the beam
   $matTag, |integer|, tag of a contact ND material
   $tolGap, |float|, gap tolerance for contact detection
   $tolF, |float|, force tolerance for contact equilibrium
   $cSwitch, |integer|, optional initial contact flag

.. note::

   A penalty variant is available as ``BeamContact3Dp``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element BeamContact3D 1 1 2 10 11 0.25 1 1 1.0e-6 1.0e-6

   2. **Python Code**

   .. code-block:: python

      element('BeamContact3D', 1, 1, 2, 10, 11, 0.25, 1, 1, 1.0e-6, 1.0e-6)

Code developed by: Kathryn Petek, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
