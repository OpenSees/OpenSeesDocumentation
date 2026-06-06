.. _HDR:

HDR Element
^^^^^^^^^^^

This command constructs a three-dimensional high damping rubber (HDR) bearing element using the Grant et al. (2004) biaxial shear model. Axial and rotational behavior follow the same framework as :ref:`ElastomericX`. Use with ``-ndm 3 -ndf 6``.

.. function:: element HDR $eleTag $Nd1 $Nd2 $Gr $Kbulk $D1 $D2 $ts $tr $n $a1 $a2 $a3 $b1 $b2 $b3 $c1 $c2 $c3 $c4 <$x1 $x2 $x3 $y1 $y2 $y3> <$kc> <$PhiM> <$ac> <$sDratio> <$m> <$tc>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $Nd1 $Nd2, |integer|, end nodes
   $Gr, |float|, shear modulus of elastomer
   $Kbulk, |float|, bulk modulus of rubber
   $D1, |float|, internal diameter
   $D2, |float|, outer diameter excluding cover thickness
   $ts, |float|, single steel shim layer thickness
   $tr, |float|, single rubber layer thickness
   $n, |integer|, number of rubber layers
   $a1 $a2 $a3 $b1 $b2 $b3 $c1 $c2 $c3 $c4, |float|, Grant model shear parameters
   $kc, |float|, cavitation parameter (optional; default 10.0)
   $PhiM, |float|, damage parameter (optional; default 0.5)
   $ac, |float|, strength reduction parameter (optional; default 1.0)
   $sDratio, |float|, shear distance from iNode as fraction of length (optional; default 0.5)
   $m, |float|, element mass (optional; default 0.0)
   $tc, |float|, cover thickness (optional; default 0.0)

.. note::

   Use ``Parameters`` :ref:`elementRecorder` to obtain cavitation force; buckling capacity; and vertical stiffness.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element HDR 1 1 2 0.8 2.0e9 0.0 0.6 0.003 0.01 20 1.0 0.5 0.0 1.0 0.5 0.0 1.0 0.5 0.0 1.0

   2. **Python Code**

   .. code-block:: python

      element('HDR', 1, 1, 2, 0.8, 2.0e9, 0.0, 0.6, 0.003, 0.01, 20,
              1.0, 0.5, 0.0, 1.0, 0.5, 0.0, 1.0, 0.5, 0.0, 1.0)

Code developed by: Manish Kumar, University at Buffalo, SUNY
