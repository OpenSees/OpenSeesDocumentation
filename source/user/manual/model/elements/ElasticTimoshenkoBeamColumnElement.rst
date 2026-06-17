.. _ElasticTimoshenkoBeamColumnElement:

Elastic Timoshenko Beam Column Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs an elastic Timoshenko beam-column element that includes shear deformation. The command name in OpenSees is ``ElasticTimoshenkoBeam`` (aliases ``ElasticTimoshenkoBeam2d`` / ``ElasticTimoshenkoBeam3d``). Section properties may be supplied directly or through a previously defined section object.

For a two-dimensional problem (``ndm=2``, ``ndf=3``):

.. function:: element ElasticTimoshenkoBeam $eleTag $iNode $jNode $E $G $A $Iz $Avy $transfTag <-mass $massDens> <-cMass> <-geomNonlinear>

.. function:: element ElasticTimoshenkoBeam $eleTag $iNode $jNode $secTag $transfTag <-mass $massDens> <-cMass> <-geomNonlinear>

For a three-dimensional problem (``ndm=3``, ``ndf=6``):

.. function:: element ElasticTimoshenkoBeam $eleTag $iNode $jNode $E $G $A $J $Iz $Iy $Avy $Avz $transfTag <-mass $massDens> <-cMass> <-geomNonlinear>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end node tags
   $E, |float|, Young's modulus
   $G, |float|, shear modulus
   $A, |float|, cross-sectional area
   $J, |float|, torsional moment of inertia (3D)
   $Iz $Iy, |float|, second moments of area
   $Avy $Avz, |float|, shear areas for local y and z directions
   $secTag, |integer|, tag of a section object (alternative to explicit properties)
   $transfTag, |integer|, geometric transformation tag
   $massDens, |float|, element mass per unit length (optional; default 0.0)
   -cMass, |string|, form consistent mass matrix (optional)
   -geomNonlinear, |string|, enable geometric nonlinearity flag (optional)

.. note::

   1. The valid queries to an elastic Timoshenko beam element when creating an :ref:`elementRecorder` are ``force``.

   2. For solid rectangular sections, the shear area is typically 5/6 of the gross area; for solid circular sections, 9/10 of the gross area; for I-shapes, the shear area may be approximated as the web area.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element ElasticTimoshenkoBeam 1 2 4 100.0 45.0 6.0 4.5 5.0 9

   2. **Python Code**

   .. code-block:: python

      element('ElasticTimoshenkoBeam', 1, 2, 4, 100.0, 45.0, 6.0, 4.5, 5.0, 9)

Code developed by: Andreas Schellenberg
