.. _ElasticBeamColumnElementWithStiffnessModifiers:

Elastic Beam Column Element with Stiffness Modifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This element models a prismatic elastic beam-column member using stiffness modifiers that account for the presence of end rotational springs. It is intended for dynamic analysis of frame structures with concentrated plasticity hinges, where numerical damping from standard elastic elements can be problematic.

The command names in OpenSees are ``ModElasticBeam2d`` and ``ModElasticBeam3d``. Full formulation details, stiffness modifier definitions, and references are given in :ref:`ModElasticBeam`.

For ``ndm=2``:

.. function:: element ModElasticBeam2d $eleTag $iNode $jNode $A $E $Iz $K11 $K33 $K44 $transfTag <-mass $massDens> <-cMass>

For ``ndm=3``:

.. function:: element ModElasticBeam3d $eleTag $iNode $jNode $A $E $G $J $Iy $Iz $K11y $K33y $K44y $K11z $K33z $K44z $transfTag <-mass $massDens> <-cMass>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end node tags
   $A, |float|, cross-sectional area
   $E, |float|, Young's modulus
   $G, |float|, shear modulus (3D only)
   $J, |float|, torsional inertia (3D only)
   $Iz $Iy, |float|, second moments of area
   $K11 $K33 $K44, |float|, stiffness modifier coefficients (2D)
   $K11y $K33y $K44y, |float|, stiffness modifiers for bending about local y (3D)
   $K11z $K33z $K44z, |float|, stiffness modifiers for bending about local z (3D)
   $transfTag, |integer|, geometric transformation tag
   $massDens, |float|, element mass per unit length (optional; default 0.0)
   -cMass, |string|, form consistent mass matrix (optional)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element ModElasticBeam2d 1 1 2 10.0 29000.0 100.0 1.0 1.0 1.0 1

   2. **Python Code**

   .. code-block:: python

      element('ModElasticBeam2d', 1, 1, 2, 10.0, 29000.0, 100.0, 1.0, 1.0, 1.0, 1)

Code developed by: |fmk|
