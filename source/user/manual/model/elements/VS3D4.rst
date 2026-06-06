.. _VS3D4:

VS3D4 Element
^^^^^^^^^^^^^

This command constructs a four-node quadrilateral viscous-spring boundary element for absorbing and transmitting outgoing waves at solid domain boundaries. The element supports sensitivity analysis. Use with ``-ndm 3 -ndf 3``.

.. function:: element VS3D4 $eleTag $iNode $jNode $kNode $lNode $E $G $rho $R <$alphaN $alphaT>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four boundary nodes in counter-clockwise order
   $E, |float|, Young's modulus of the adjacent solid medium
   $G, |float|, shear modulus of the adjacent solid medium
   $rho, |float|, mass density (default 1.0)
   $R, |float|, distance from the boundary to the domain of interest (default 1.0)
   $alphaN, |float|, normal-wave correction factor (default 1.33)
   $alphaT, |float|, tangential-wave correction factor (default 0.67)

.. note::

   1. Intended for dam-foundation and other 3D wave-propagation models with artificial boundaries.

   2. Valid :ref:`elementRecorder` queries include ``force`` and ``stiffness``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element VS3D4 1 1 2 3 4 3.0e10 1.2e10 2400.0 50.0

   2. **Python Code**

   .. code-block:: python

      element('VS3D4', 1, 1, 2, 3, 4, 3.0e10, 1.2e10, 2400.0, 50.0)

Code developed by: Quan Gu, Yichao Gao, and Zhijian Qiu, Xiamen University
