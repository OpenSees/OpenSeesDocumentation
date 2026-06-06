.. _TripleFrictionPendulumBearing:

TripleFrictionPendulumBearing Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs the original triple friction pendulum (TFP) bearing element of Becker and Mahin. It models four sliding interfaces with geometry and friction coefficients specified directly. For the series-model element of Dao et al. see :ref:`TripleFrictionPendulum`. For heating effects see :ref:`TripleFrictionPendulumX`.

.. function:: element TFP $eleTag $iNode $jNode $R1 $R2 $R3 $R4 $D1 $D2 $D3 $D4 $d1 $d2 $d3 $d4 $mu1 $mu2 $mu3 $mu4 $h1 $h2 $h3 $h4 $H0 $colLoad <$K>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $R1 $R2 $R3 $R4, |float|, radii of inner bottom; inner top; outer bottom; outer top sliding surfaces
   $D1 $D2 $D3 $D4, |float|, diameters of inner bottom; inner top; outer bottom; outer top sliding surfaces
   $d1 $d2 $d3 $d4, |float|, diameters of inner bottom; inner top; outer bottom; outer top sliders
   $mu1 $mu2 $mu3 $mu4, |float|, friction coefficients at the four sliding surfaces
   $h1 $h2 $h3 $h4, |float|, heights from each sliding surface to bearing center
   $H0, |float|, total height of bearing
   $colLoad, |float|, initial axial load on bearing (used for first step only)
   $K, |float|, vertical spring stiffness (optional; default 1.0e15)

.. note::

   Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, ``basicDisplacement``, ``relativeDisp``, ``plasticDisp``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element TFP 1 1 2 12.0 12.0 88.0 88.0 12.0 12.0 44.0 44.0 8.0 8.0 12.5 12.5 0.02 0.02 0.09 0.12 3.0 3.0 4.5 4.5 12.5 45.0

   2. **Python Code**

   .. code-block:: python

      element('TFP', 1, 1, 2, 12.0, 12.0, 88.0, 88.0, 12.0, 12.0, 44.0, 44.0,
              8.0, 8.0, 12.5, 12.5, 0.02, 0.02, 0.09, 0.12, 3.0, 3.0, 4.5, 4.5, 12.5, 45.0)

Code developed by: Tracy Becker, University of California, Berkeley
