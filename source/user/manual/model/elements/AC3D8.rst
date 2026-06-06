.. _AC3D8:

AC3D8 Element
^^^^^^^^^^^^^

This command constructs an eight-node hexahedral acoustic fluid element for dam-reservoir and fluid-domain modeling. Each node carries one pressure DOF. The element requires an ``AcousticMedium`` ND material. Use with ``-ndm 3 -ndf 1`` for the fluid mesh.

.. function:: element AC3D8 $eleTag $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8 $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $N1 ... $N8, |integer|, eight node tags in standard brick order
   $matTag, |integer|, tag of a previously defined ``AcousticMedium`` material

.. note::

   1. Define the acoustic material first: ``nDMaterial AcousticMedium $matTag $K $rho <$gamma>``.

   2. For fluid-structure coupling at interfaces see :ref:`ASI3D8`. For acoustic boundaries see :ref:`AV3D4`.

   3. Valid :ref:`elementRecorder` queries include ``force`` and ``stiffness``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      nDMaterial AcousticMedium 1 2.2e9 1000.0
      element AC3D8 1 1 2 3 4 5 6 7 8 1

   2. **Python Code**

   .. code-block:: python

      nDMaterial('AcousticMedium', 1, 2.2e9, 1000.0)
      element('AC3D8', 1, 1, 2, 3, 4, 5, 6, 7, 8, 1)

Code developed by: Quan Gu, Yichao Gao, and Zhijian Qiu, Xiamen University
