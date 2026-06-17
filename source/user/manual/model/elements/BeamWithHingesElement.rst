.. _BeamWithHingesElement:

Beam With Hinges Element
^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a force-based beam-column element with plastic hinges at the ends using modified Gauss-Radau integration. The command name in OpenSees is ``beamWithHinges``. The element interior is elastic; nonlinear behavior is concentrated in user-defined hinge sections at ends I and J.

For 2D (``ndm=2``, ``ndf=3``):

.. function:: element beamWithHinges $eleTag $iNode $jNode $secTagI $LpI $secTagJ $LpJ $E $A $Iz $transfTag <-mass $massDens> <-iter $maxIters $tol> <-subdivide $numSub $subFac>

For 3D (``ndm=3``, ``ndf=6``):

.. function:: element beamWithHinges $eleTag $iNode $jNode $secTagI $LpI $secTagJ $LpJ $E $A $Iz $Iy $G $J $transfTag <-mass $massDens> <-iter $maxIters $tol> <-subdivide $numSub $subFac>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end node tags
   $secTagI $secTagJ, |integer|, section tags at ends I and J
   $LpI $LpJ, |float|, plastic hinge lengths at ends I and J
   $E $A $Iz, |float|, elastic properties of the interior (2D)
   $Iy $G $J, |float|, additional elastic properties of the interior (3D)
   $transfTag, |integer|, geometric transformation tag
   $massDens, |float|, element mass per unit length (optional; default 0.0)
   $maxIters, |integer|, maximum iterations for element compatibility (optional)
   $tol, |float|, compatibility tolerance used with ``-iter`` (optional)
   $numSub, |integer|, number of subdivisions used with ``-subdivide`` (optional)
   $subFac, |float|, subdivision factor used with ``-subdivide`` (optional)

.. note::

   1. This legacy format constrains the element interior to remain linear-elastic. For models where plasticity may spread beyond hinge regions, use :ref:`forceBeamColumn` with ``HingeRadau`` (or related) plastic-hinge integration instead.

   2. Hinge integration uses two-point Gauss-Radau over lengths ``4*LpI`` and ``4*LpJ`` at the element ends (six integration points total).

   3. Valid :ref:`elementRecorder` queries are the same as for :ref:`forceBeamColumn`.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element beamWithHinges 1 1 2 3 12.0 4 12.0 29000.0 20.0 800.0 1

   2. **Python Code**

   .. code-block:: python

      element('beamWithHinges', 1, 1, 2, 3, 12.0, 4, 12.0, 29000.0, 20.0, 800.0, 1)

Code developed by: |mhs|
