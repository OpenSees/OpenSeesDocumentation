.. _ASI3D8:

ASI3D8 Element
^^^^^^^^^^^^^^

This command constructs an eight-node quadrilateral fluid-structure interface element for coupled dam-reservoir analysis. The element connects four solid nodes (three displacement DOFs each) and four fluid nodes (one pressure DOF each). Use with compatible solid and fluid node DOF layouts in a 3D model.

.. function:: element ASI3D8 $eleTag $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $N1 $N2 $N3 $N4, |integer|, four solid-side interface nodes
   $N5 $N6 $N7 $N8, |integer|, four fluid-side interface nodes

.. note::

   1. Pair with :ref:`AC3D8` acoustic elements in the fluid domain and standard solid elements in the structure.

   2. The element enforces fluid-structure interaction tractions on the shared interface.

   3. Valid :ref:`elementRecorder` queries include ``force`` and ``stiffness``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element ASI3D8 1 1 2 3 4 101 102 103 104

   2. **Python Code**

   .. code-block:: python

      element('ASI3D8', 1, 1, 2, 3, 4, 101, 102, 103, 104)

Code developed by: Quan Gu, Yichao Gao, and Zhijian Qiu, Xiamen University
