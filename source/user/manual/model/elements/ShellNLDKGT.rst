.. _ShellNLDKGT:

ShellNLDKGT Element
^^^^^^^^^^^^^^^^^^^

This command constructs a three-node triangular shell element with geometric nonlinearity based on the updated Lagrangian formulation. It extends the :ref:`ShellDKGT` element for large-deformation analysis. Use with ``-ndm 3 -ndf 6``.

.. function:: element ShellNLDKGT $eleTag $iNode $jNode $kNode $secTag <-damp $dampTag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode, |integer|, three nodes in clockwise or counter-clockwise order
   $secTag, |integer|, tag of a previously defined section object
   $dampTag, |integer|, tag of an elemental damping object used with ``-damp`` (optional)

.. note::

   1. The section may be a :ref:`PlateFiberSection`, :ref:`ElasticMembranePlateSection`, or layered shell section.

   2. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section PlateFiber 1 1 10.0
      element ShellNLDKGT 1 1 2 3 1

   2. **Python Code**

   .. code-block:: python

      section('PlateFiber', 1, 1, 10.0)
      element('ShellNLDKGT', 1, 1, 2, 3, 1)

Code developed by: Shuhao Zhang, Xinzheng Lu
