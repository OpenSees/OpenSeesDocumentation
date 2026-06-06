.. _Shell:

Shell Element
^^^^^^^^^^^^^

This command constructs a four-node shell element using the Bathe MITC4 formulation with membrane and drilling degrees of freedom. The command names in OpenSees are ``shell``, ``Shell``, ``shellMITC4``, or ``ShellMITC4``.

Use with ``-ndm 3 -ndf 6``. The section is typically a :ref:`PlateFiberSection`, :ref:`ElasticMembranePlateSection`, or layered shell section.

.. function:: element ShellMITC4 $eleTag $iNode $jNode $kNode $lNode $secTag <-updateBasis> <-damp $dampTag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order
   $secTag, |integer|, tag of a previously defined section object
   -updateBasis, |string|, update the element local basis during analysis (optional)
   $dampTag, |integer|, tag of an elemental damping object used with ``-damp`` (optional)

.. note::

   1. This is a 3D element with 6 DOFs per node and cannot be used in a 2D domain.

   2. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section PlateFiber 1 1 10.0
      element ShellMITC4 1 1 2 3 4 1

   2. **Python Code**

   .. code-block:: python

      section('PlateFiber', 1, 1, 10.0)
      element('ShellMITC4', 1, 1, 2, 3, 4, 1)

Code developed by: Ed Love; reimplementation by Leopoldo Tesser, Diego A. Talledo, Veronique Le Corvec
