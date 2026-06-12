.. _ShellNLDKGQ:

ShellNLDKGQ Element
^^^^^^^^^^^^^^^^^^^

This command constructs a four-node quadrilateral shell element with geometric nonlinearity based on the updated Lagrangian formulation. It extends the :ref:`ShellDKGQ` element for large-deformation analysis. Use with ``-ndm 3 -ndf 6``.

.. function:: element ShellNLDKGQ $eleTag $iNode $jNode $kNode $lNode $secTag <-damp $dampTag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in clockwise or counter-clockwise order
   $secTag, |integer|, tag of a previously defined section object
   $dampTag, |integer|, tag of an elemental damping object used with ``-damp`` (optional)

.. note::

   1. The section may be a :ref:`PlateFiberSection`, :ref:`ElasticMembranePlateSection`, or layered shell section.

   2. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section PlateFiber 1 1 10.0
      element ShellNLDKGQ 1 1 2 3 4 1

   2. **Python Code**

   .. code-block:: python

      section('PlateFiber', 1, 1, 10.0)
      element('ShellNLDKGQ', 1, 1, 2, 3, 4, 1)

Code developed by: Lisha Wang, Xinzheng Lu, Linlin Xie, Song Cen, Quan Gu
