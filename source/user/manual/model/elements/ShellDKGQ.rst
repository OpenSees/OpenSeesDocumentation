.. _ShellDKGQ:

ShellDKGQ Element
^^^^^^^^^^^^^^^^^

This command constructs a four-node quadrilateral shell element based on generalized conforming element theory. The bending part uses the DKQ thin-plate formulation; the membrane part uses the GQ12 element with drilling DOF. Use with ``-ndm 3 -ndf 6``.

.. function:: element ShellDKGQ $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampTag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in clockwise or counter-clockwise order
   $secTag, |integer|, tag of a previously defined section object
   $dampTag, |integer|, tag of an elemental damping object used with ``-damp`` (optional)

.. note::

   1. The section may be a :ref:`PlateFiberSection`, :ref:`ElasticMembranePlateSection`, or layered shell section.

   2. This is the linear small-deformation formulation. For geometric nonlinearity see :ref:`ShellNLDKGQ`.

   3. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section PlateFiber 1 1 10.0
      element ShellDKGQ 1 1 2 3 4 1

   2. **Python Code**

   .. code-block:: python

      section('PlateFiber', 1, 1, 10.0)
      element('ShellDKGQ', 1, 1, 2, 3, 4, 1)

Code developed by: Lisha Wang, Xinzheng Lu, Linlin Xie, Song Cen, Quan Gu
