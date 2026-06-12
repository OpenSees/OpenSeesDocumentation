.. _AV3D4:

AV3D4 Element
^^^^^^^^^^^^^

This command constructs a four-node quadrilateral acoustic absorbing-transmitting boundary element for fluid domain edges in dam-reservoir analysis. The element requires an ``AcousticMedium`` ND material. Use with ``-ndm 3 -ndf 1`` on fluid boundary nodes.

.. function:: element AV3D4 $eleTag $iNode $jNode $kNode $lNode $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four boundary nodes in counter-clockwise order
   $matTag, |integer|, tag of a previously defined ``AcousticMedium`` material

.. note::

   1. Define the acoustic material first: ``nDMaterial AcousticMedium $matTag $K $rho <$gamma>``.

   2. For solid-side absorbing boundaries see :ref:`VS3D4`. For interior fluid elements see :ref:`AC3D8`.

   3. Valid :ref:`elementRecorder` queries include ``force`` and ``stiffness``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      nDMaterial AcousticMedium 1 2.2e9 1000.0
      element AV3D4 1 1 2 3 4 1

   2. **Python Code**

   .. code-block:: python

      nDMaterial('AcousticMedium', 1, 2.2e9, 1000.0)
      element('AV3D4', 1, 1, 2, 3, 4, 1)

Code developed by: Quan Gu, Yichao Gao, and Zhijian Qiu, Xiamen University
