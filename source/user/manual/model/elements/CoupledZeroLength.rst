.. _coupledZeroLength:

CoupledZeroLength Element
^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a CoupledZeroLength element object. The element is defined by two nodes at the same location and couples two degrees of freedom (dirn1 and dirn2) through a single UniaxialMaterial. Unlike a ZeroLength element, which provides a rectangular force interaction surface in a 2D plane, this element provides a circular force interaction surface in the plane of the two directions.

.. function:: element coupledZeroLength $eleTag $iNode $jNode $dirn1 $dirn2 $matTag <-doRayleigh $rFlag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $iNode $jNode, |integer|, end node tags
   $dirn1 $dirn2, |integer|, the two coupled directions (1 through ndf)
   $matTag,   |integer|,  tag associated with previously-defined UniaxialMaterial
   $rFlag,    |integer|,  "| optional, default = 0
   | 0 = NO RAYLEIGH DAMPING (default)
   | 1 = include Rayleigh damping"

**Theory**

If the change in element end displacements for the two DOFs of interest are :math:`\delta_1` and :math:`\delta_2`, the deformation (strain) of the uniaxial material is:

.. math::

   \epsilon = \sqrt{\delta_1^2 + \delta_2^2}

If the resulting force (stress from the uniaxial material) is :math:`\Sigma`, the forces in the two directions are:

.. math::

   F_1 = \frac{\Sigma \cdot \delta_1}{\epsilon}, \quad F_2 = \frac{\Sigma \cdot \delta_2}{\epsilon}

When :math:`\epsilon = 0`, the forces are computed using :math:`\Sigma` and the last committed set of displacements that were not zero.

.. note::

   The valid queries to this element when creating an ElementRecorder object are 'force' and 'material matArg1 matArg2 ...'.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/CoupledZeroLength_Element>`_

.. admonition:: Example

   The following example constructs a CoupledZeroLength element with tag **1** between nodes **2** and **4**, coupling directions **5** and **6**, with material tag **7** (from the OpenSees wiki).

   1. **Tcl Code**

   .. code-block:: tcl

      element coupledZeroLength 1 2 4 5 6 7

   2. **Python Code**

   .. code-block:: python

      ops.element('CoupledZeroLength', 1, 2, 4, 5, 6, 7)

Code developed by: |fmk|
