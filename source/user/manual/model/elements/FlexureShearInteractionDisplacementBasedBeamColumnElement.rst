.. _FlexureShearInteractionDisplacementBasedBeamColumnElement:

Flexure-Shear Interaction Displacement-Based Beam Column Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a distributed-plasticity, displacement-based beam-column element that couples flexural and shear deformations. The command name in OpenSees is ``dispBeamColumnInt``. The formulation follows Massone et al. (2006) and is limited to 2D analysis (``ndm=2``, ``ndf=3``).

.. function:: element dispBeamColumnInt $eleTag $iNode $jNode $numIntgrPts $secTag $transfTag $cRot <-mass $massDens>

.. function:: element dispBeamColumnInt $eleTag $iNode $jNode $numIntgrPts -sections {$secTag1 ...} $transfTag $cRot <-mass $massDens>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end node tags
   $numIntgrPts, |integer|, number of integration points along the element
   $secTag, |integer|, tag of a ``FiberSection2dInt`` section (same section at all points)
   $secTag1 ..., |listInt|, list of section tags when using ``-sections``
   $transfTag, |integer|, tag of a ``LinearInt`` geometric transformation
   $cRot, |float|, center of rotation as a fraction of element height from bottom (0 to 1)
   $massDens, |float|, element mass per unit length (optional; default 0.0)

.. note::

   1. This element requires the ``LinearInt`` geometric transformation and a ``FiberSection2dInt`` section created for strip (panel) modeling with flexure-shear interaction.

   2. Parameter $cRot distributes transverse displacement between flexural (curvature) and shear (shear strain) components.

   3. Valid :ref:`elementRecorder` queries include ``force``, ``stiffness``, and ``section $secNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      geomTransf LinearInt 1
      element dispBeamColumnInt 1 1 3 2 2 1 0.4

   2. **Python Code**

   .. code-block:: python

      geomTransf('LinearInt', 1)
      element('dispBeamColumnInt', 1, 1, 3, 2, 2, 1, 0.4)

Code developed by: Leo Massone, Kutay Orakcal, John Wallace
