.. _Tri31:

Tri31 Element
^^^^^^^^^^^^^

This command constructs a constant-strain triangular element using three nodes and one integration point. The command name in OpenSees is ``Tri31`` or ``tri31``. Use with ``-ndm 2 -ndf 2``.

.. function:: element Tri31 $eleTag $iNode $jNode $kNode $thick $type $matTag <$pressure $rho $b1 $b2>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode, |integer|, three nodes in counter-clockwise order
   $thick, |float|, element thickness
   $type, |string|, material formulation: ``PlaneStrain`` or ``PlaneStress``
   $matTag, |integer|, tag of an nD material
   $pressure, |float|, surface pressure (optional; default 0.0)
   $rho, |float|, element mass density per unit volume (optional; default 0.0)
   $b1 $b2, |float|, constant body forces in the domain (optional; default 0.0)

.. note::

   1. If all optional arguments are supplied, all four must be provided.

   2. Consistent nodal loads are computed from pressure and body forces.

   3. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element Tri31 1 1 2 3 1.0 PlaneStress 1

   2. **Python Code**

   .. code-block:: python

      element('Tri31', 1, 1, 2, 3, 1.0, 'PlaneStress', 1)

Code developed by: Roozbeh G. Mikola, N. Sitar
