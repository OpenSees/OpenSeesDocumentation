.. _ShellNL:

ShellNL Element
^^^^^^^^^^^^^^^

This command constructs a nine-node Lagrangian shell element with membrane and drilling degrees of freedom. The command names in OpenSees are ``ShellNL``, ``shellNL``, ``ShellMITC9``, or ``shellMITC9``. Use with ``-ndm 3 -ndf 6``.

.. function:: element ShellMITC9 $eleTag $n1 $n2 $n3 $n4 $n5 $n6 $n7 $n8 $n9 $secTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $n1 ... $n9, |integer|, nine nodes defining the element
   $secTag, |integer|, tag of a previously defined section object

.. note::

   1. This is a 3D element with 6 DOFs per node (54 total element DOFs).

   2. The section is typically a :ref:`PlateFiberSection` or :ref:`ElasticMembranePlateSection`.

   3. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section PlateFiber 1 1 10.0
      element ShellMITC9 1 1 2 3 4 5 6 7 8 9 1

   2. **Python Code**

   .. code-block:: python

      section('PlateFiber', 1, 1, 10.0)
      element('ShellMITC9', 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1)

Code developed by: Leopoldo Tesser, Diego A. Talledo
