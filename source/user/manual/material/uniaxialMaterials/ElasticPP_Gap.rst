.. _ElasticPP_Gap:

Elastic-Perfectly Plastic Gap Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs an elastic-perfectly plastic gap uniaxial material.

.. function:: uniaxialMaterial ElasticPPGap $matTag $E $Fy $gap <$eta damage>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique material tag
   $E, |float|, initial stiffness
   $Fy, |float|, yield force
   $gap, |float|, initial gap
   $eta, |float|, optional damping tangent (default 0.0)
   damage, |string|, optional ``damage`` flag to enable damage behavior

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial ElasticPPGap 1 1000.0 10.0 0.01

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('ElasticPPGap', 1, 1000.0, 10.0, 0.01)

Code Developed by: |fmk|
