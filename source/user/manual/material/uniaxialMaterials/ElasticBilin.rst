.. _ElasticBilin:

Elastic Bilinear Material
^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a bilinear elastic uniaxial material. Also accepted as ``ElasticBilinear``.

.. function:: uniaxialMaterial ElasticBilin $matTag $E1P $E2P $eps2P <$E1N $E2N $eps2N>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique material tag
   $E1P, |float|, initial stiffness in tension
   $E2P, |float|, secondary stiffness in tension
   $eps2P, |float|, strain at which secondary stiffness begins in tension
   $E1N, |float|, optional initial stiffness in compression
   $E2N, |float|, optional secondary stiffness in compression
   $eps2N, |float|, optional strain at which secondary stiffness begins in compression

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial ElasticBilin 1 3000.0 300.0 0.01

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('ElasticBilin', 1, 3000.0, 300.0, 0.01)

Code Developed by: |fmk|
