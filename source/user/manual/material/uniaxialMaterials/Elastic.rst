.. _Elastic:

Elastic Material
^^^^^^^^^^^^^^^^

This command constructs a linear elastic uniaxial material.

.. function:: uniaxialMaterial Elastic $matTag $E <$eta> <$Eneg>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique material tag
   $E, |float|, tangent stiffness
   $eta, |float|, optional damping tangent (default 0.0)
   $Eneg, |float|, optional stiffness in compression when different from tension (default = $E)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 3000.0

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 3000.0)

Code Developed by: |fmk|
