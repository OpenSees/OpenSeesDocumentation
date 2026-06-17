.. _NineFourNodeQuadUP:

NineFourNodeQuadUP Element
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a nine-node quadrilateral element (nine-four node) for coupled u-p plane-strain analysis. Corner nodes carry pore pressure; midside nodes carry solid displacement only. Use with ``-ndm 2``. The registered command name is ``9_4_QuadUP``.

.. function:: element 9_4_QuadUP $eleTag $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8 $N9 $thick $matTag $bulk $fmass $permX $permY <$b1 $b2>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8 $N9, |integer|, nine node tags
   $thick, |float|, element thickness
   $matTag, |integer|, tag of a previously defined ND material
   $bulk, |float|, combined undrained bulk modulus
   $fmass, |float|, fluid mass density
   $permX $permY, |float|, permeability in x and y directions
   $b1 $b2, |float|, optional body-force components (default 0.0)

.. note::

   Valid :ref:`elementRecorder` queries include ``force``, ``stiffness``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element 9_4_QuadUP 1 1 2 3 4 5 6 7 8 9 1.0 1 2.2e6 1000.0 1.0e-5 1.0e-5

   2. **Python Code**

   .. code-block:: python

      element('9_4_QuadUP', 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1.0, 1, 2.2e6, 1000.0, 1.0e-5, 1.0e-5)

Code developed by: Zhaohui Yang, UC San Diego
