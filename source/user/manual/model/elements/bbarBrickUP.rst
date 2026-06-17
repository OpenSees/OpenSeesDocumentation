.. _bbarBrickUP:

bbarBrickUP Element
^^^^^^^^^^^^^^^^^^^

This command constructs an eight-node brick element with the B-bar method for coupled u-p analysis of saturated porous media. Use with ``-ndm 3 -ndf 4``.

.. function:: element bbarBrickUP $eleTag $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8 $matTag $bulk $fmass $permX $permY $permZ <$bX $bY $bZ>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8, |integer|, eight node tags in standard brick order
   $matTag, |integer|, tag of a previously defined ND material
   $bulk, |float|, combined undrained bulk modulus
   $fmass, |float|, fluid mass density
   $permX $permY $permZ, |float|, permeability in x; y; and z directions
   $bX $bY $bZ, |float|, optional body-force components (default 0.0)

.. note::

   For the standard formulation without B-bar see :ref:`BrickUP`.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element bbarBrickUP 1 1 2 3 4 5 6 7 8 1 2.2e6 1000.0 1.0e-5 1.0e-5 1.0e-5

   2. **Python Code**

   .. code-block:: python

      element('bbarBrickUP', 1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2.2e6, 1000.0, 1.0e-5, 1.0e-5, 1.0e-5)

Code developed by: Zhaohui Yang, UC San Diego
