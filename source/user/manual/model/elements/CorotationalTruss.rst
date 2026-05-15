.. _corotationalTruss:

Corotational Truss Element
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a corotational truss element object. The corotational formulation accounts for geometric nonlinearity (large displacements). There are two ways to construct the element: by specifying an area and a UniaxialMaterial, or by specifying a Section.

.. function:: element corotTruss $eleTag $iNode $jNode $A $matTag <-rho $rho> <-cMass> <-doRayleigh $rFlag>

   Construct a corotational truss element with cross-sectional area and a UniaxialMaterial.

.. function:: element corotTrussSection $eleTag $iNode $jNode $secTag <-rho $rho> <-cMass> <-doRayleigh $rFlag>

   Construct a corotational truss element with a Section identifier.

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

   #. When constructed with a UniaxialMaterial object, the corotational truss element considers strain-rate effects and is suitable for use as a damping element.
   #. The valid queries when creating an ElementRecorder object are 'axialForce,' 'stiff,' 'deformations,' 'material matArg1 matArg2...' and 'section sectArg1 sectArg2...'
   #. CorotTruss does not include Rayleigh damping by default.
   #. For backward compatibility, ``element corotTruss $eleTag $iNode $jNode $secTag`` still creates a CorotTrussSection element.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/Corotational_Truss_Element>`_

.. admonition:: Example

   The following example constructs a corotational truss element with tag **1** between nodes **2** and **4**, area **5.5**, and material tag **9**.

   1. **Tcl Code**

   .. code-block:: tcl

      element corotTruss 1 2 4 5.5 9

   2. **Python Code**

   .. code-block:: python

      ops.element('corotTruss', 1, 2, 4, 5.5, 9)

Code developed by: |mhs|
