.. _CatenaryCableElement:

CatenaryCableElement
^^^^^^^^^^^^^^^^^^^^

This command constructs a two-node catenary cable element for static and dynamic analysis including thermal effects. The registered command name is ``CatenaryCable``. Use with ``-ndm 3 -ndf 3`` or ``-ndf 6``.

.. function:: element CatenaryCable $eleTag $iNode $jNode $weight $E $A $L0 $alpha $temperature_change $rho $errorTol $Nsubsteps $massType

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $weight, |float|, distributed weight per unit length
   $E, |float|, elastic modulus
   $A, |float|, cross-sectional area
   $L0, |float|, unstressed cable length
   $alpha, |float|, thermal expansion coefficient
   $temperature_change, |float|, temperature change from reference state
   $rho, |float|, mass density
   $errorTol, |float|, equilibrium iteration tolerance
   $Nsubsteps, |integer|, number of substeps for internal equilibrium iterations
   $massType, |integer|, mass matrix type: 0 lumped; 1 integration; 2 Clough-style; 3 equivalent truss

.. note::

   1. The element formulates catenary equilibrium internally and supports large displacements.

   2. Valid :ref:`elementRecorder` queries include ``force``, ``localForce``, and ``basicForce``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element CatenaryCable 1 1 2 0.1 2.0e11 0.001 10.0 1.2e-5 0.0 7850.0 1.0e-8 10 0

   2. **Python Code**

   .. code-block:: python

      element('CatenaryCable', 1, 1, 2, 0.1, 2.0e11, 0.001, 10.0, 1.2e-5, 0.0, 7850.0, 1.0e-8, 10, 0)

Code developed by: Pablo Ibanez and Jose Abell, Universidad de los Andes
