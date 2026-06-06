.. _TwentyEightNodeBrickUP:

TwentyEightNodeBrickUP Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a 20-node hexahedral element for coupled u-p analysis. Eight corner nodes have pore-pressure DOFs; twelve midside nodes carry solid displacement only. Use with ``-ndm 3``. The registered command name is ``20_8_BrickUP``.

.. function:: element 20_8_BrickUP $eleTag $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8 $N9 $N10 $N11 $N12 $N13 $N14 $N15 $N16 $N17 $N18 $N19 $N20 $matTag $bulk $fmass $permX $permY $permZ <$bX $bY $bZ>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $N1 ... $N20, |integer|, twenty node tags in standard 20-node brick order
   $matTag, |integer|, tag of a previously defined ND material
   $bulk, |float|, combined undrained bulk modulus
   $fmass, |float|, fluid mass density
   $permX $permY $permZ, |float|, permeability in x; y; and z directions
   $bX $bY $bZ, |float|, optional body-force components (default 0.0)

.. note::

   Valid :ref:`elementRecorder` queries include ``force``, ``stiffness``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element 20_8_BrickUP 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2.2e6 1000.0 1.0e-5 1.0e-5 1.0e-5

   2. **Python Code**

   .. code-block:: python

      element('20_8_BrickUP', 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
              1, 2.2e6, 1000.0, 1.0e-5, 1.0e-5, 1.0e-5)

Code developed by: Zhaohui Yang, UC San Diego
