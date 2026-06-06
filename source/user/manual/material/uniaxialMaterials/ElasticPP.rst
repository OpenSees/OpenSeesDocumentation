.. _ElasticPP:

Elastic-Perfectly Plastic Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs an elastic-perfectly plastic uniaxial material.

.. function:: uniaxialMaterial ElasticPP $matTag $E $epsP <$epsN $eps0>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique material tag
   $E, |float|, tangent stiffness
   $epsP, |float|, strain at which material yields in tension
   $epsN, |float|, optional strain at which material yields in compression (default = -$epsP)
   $eps0, |float|, optional initial strain (default 0.0)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial ElasticPP 1 3000.0 0.02

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('ElasticPP', 1, 3000.0, 0.02)

Code Developed by: |fmk|
