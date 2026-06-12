.. _LeadRubberX:

LeadRubberX Element
^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional lead-rubber bearing element extending :ref:`ElastomericX` with strength degradation in the lead core due to heating. Use with ``-ndm 3 -ndf 6``.

.. function:: element LeadRubberX $eleTag $Nd1 $Nd2 $Fy $alpha $Gr $Kbulk $D1 $D2 $ts $tr $n <$x1 $x2 $x3 $y1 $y2 $y3> <$kc> <$PhiM> <$ac> <$sDratio> <$m> <$cd> <$tc> <$qL> <$cL> <$kS> <$aS> <$tag1> <$tag2> <$tag3> <$tag4> <$tag5>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $Nd1 $Nd2, |integer|, end nodes
   $Fy, |float|, yield strength
   $alpha, |float|, post-yield stiffness ratio
   $Gr, |float|, shear modulus of elastomer
   $Kbulk, |float|, bulk modulus of rubber
   $D1, |float|, internal diameter
   $D2, |float|, outer diameter excluding cover thickness
   $ts, |float|, single steel shim layer thickness
   $tr, |float|, single rubber layer thickness
   $n, |integer|, number of rubber layers
   $kc, |float|, cavitation parameter (optional; default 10.0)
   $PhiM, |float|, damage parameter (optional; default 0.5)
   $ac, |float|, strength reduction parameter (optional; default 1.0)
   $sDratio, |float|, shear distance from iNode as fraction of length (optional; default 0.5)
   $m, |float|, element mass (optional; default 0.0)
   $cd, |float|, viscous damping parameter (optional; default 0.0)
   $tc, |float|, cover thickness (optional; default 0.0)
   $qL, |float|, density of lead (optional; default 11200 kg/m3)
   $cL, |float|, specific heat of lead (optional; default 130 N-m/kg C)
   $kS, |float|, thermal conductivity of steel (optional; default 50 W/m C)
   $aS, |float|, thermal diffusivity of steel (optional; default 1.41e-05 m2/s)
   $tag1, |integer|, include cavitation and post-cavitation (optional; default 0)
   $tag2, |integer|, include buckling load variation (optional; default 0)
   $tag3, |integer|, include horizontal stiffness variation (optional; default 0)
   $tag4, |integer|, include vertical stiffness variation (optional; default 0)
   $tag5, |integer|, include lead-core heating degradation (optional; default 0)

.. note::

   1. Default heating parameters are in SI units; override them when using imperial units.

   2. Use ``Parameters`` :ref:`elementRecorder` to obtain cavitation force; buckling capacity; vertical stiffness; horizontal stiffness; temperature increase; and yield strength.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element LeadRubberX 1 1 2 150.0 0.1 0.8 2.0e9 0.0 0.6 0.003 0.01 20

   2. **Python Code**

   .. code-block:: python

      element('LeadRubberX', 1, 1, 2, 150.0, 0.1, 0.8, 2.0e9, 0.0, 0.6, 0.003, 0.01, 20)

Code developed by: Manish Kumar, University at Buffalo, SUNY
