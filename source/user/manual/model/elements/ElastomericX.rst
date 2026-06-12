.. _ElastomericX:

ElastomericX Element
^^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional elastomeric bearing element that formulates all six directional material models internally from geometric and rubber properties. It extends the :ref:`ElastomericBearingBoucWen` formulation without requiring user-supplied uniaxial materials. Use with ``-ndm 3 -ndf 6``.

.. function:: element ElastomericX $eleTag $Nd1 $Nd2 $Fy $alpha $Gr $Kbulk $D1 $D2 $ts $tr $n <$x1 $x2 $x3 $y1 $y2 $y3> <$kc> <$PhiM> <$ac> <$sDratio> <$m> <$cd> <$tc> <$tag1> <$tag2> <$tag3> <$tag4>

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
   $tag1, |integer|, include cavitation and post-cavitation (optional; default 0)
   $tag2, |integer|, include buckling load variation (optional; default 0)
   $tag3, |integer|, include horizontal stiffness variation (optional; default 0)
   $tag4, |integer|, include vertical stiffness variation (optional; default 0)

.. note::

   1. Characteristic strength is :math:`Q_d = F_y(1-\alpha)`; do not confuse with :math:`F_y`.

   2. Use ``Parameters`` :ref:`elementRecorder` to obtain cavitation force; buckling capacity; vertical stiffness; and horizontal stiffness.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element ElastomericX 1 1 2 100.0 0.1 0.8 2.0e9 0.0 0.6 0.003 0.01 20 0 1 0 1 0 0 10.0 0.5 1.0 0.5 0.0 0.0 0.0 1 0 0 0

   2. **Python Code**

   .. code-block:: python

      element('ElastomericX', 1, 1, 2, 100.0, 0.1, 0.8, 2.0e9, 0.0, 0.6, 0.003, 0.01, 20,
              0, 1, 0, 1, 0, 0, 10.0, 0.5, 1.0, 0.5, 0.0, 0.0, 0.0, 1, 0, 0, 0)

Code developed by: Manish Kumar, University at Buffalo, SUNY
