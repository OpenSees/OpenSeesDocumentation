.. _truss:

Truss Element
^^^^^^^^^^^^^

This command is used to construct a truss element object. There are two ways to construct a truss element: by specifying an area and a UniaxialMaterial, or by specifying a Section.

.. function:: element truss $eleTag $iNode $jNode $A $matTag <-rho $rho> <-cMass> <-doRayleigh $rFlag>

   Construct a truss element with cross-sectional area and a UniaxialMaterial.

.. function:: element trussSection $eleTag $iNode $jNode $secTag <-rho $rho> <-cMass> <-doRayleigh $rFlag>

   Construct a truss element with a Section identifier.

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $iNode $jNode, |integer|, end node tags
   $A,        |float|,    cross-sectional area of element
   $matTag,   |integer|,  tag associated with previously-defined UniaxialMaterial
   $secTag,   |integer|,  tag associated with previously-defined Section
   $rho,      |float|,    mass per unit length (optional, default = 0.0)
   -cMass,    |string|,   use consistent mass matrix (optional; default is lumped)
   $rFlag,    |integer|,  "| Rayleigh damping flag (optional, default = 0)
   | 0 = NO RAYLEIGH DAMPING (default)
   | 1 = include Rayleigh damping"

.. note::

   #. The truss element does not include geometric nonlinearities, even when used with beam-columns utilizing P-Delta or Corotational transformations.
   #. When constructed with a UniaxialMaterial object, the truss element considers strain-rate effects and is suitable for use as a damping element.
   #. The valid queries to a truss element when creating an ElementRecorder object are 'axialForce,' 'forces,' 'localForce,' 'deformations,' 'material matArg1 matArg2...' and 'section sectArg1 sectArg2...'
   #. For backward compatibility, ``element truss $eleTag $iNode $jNode $secTag`` (four args after nodes) still creates a TrussSection element.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/Truss_Element>`_

.. admonition:: Example

   The following example constructs a truss element with tag **1** between nodes **2** and **4**, area **5.5**, and material tag **9** (from the OpenSees wiki).

   1. **Tcl Code**

   .. code-block:: tcl

      element truss 1 2 4 5.5 9

   2. **Python Code**

   .. code-block:: python

      ops.element('Truss', 1, 2, 4, 5.5, 9)

Code developed by: |fmk|
