.. _ElasticNoTension:

Elastic No Tension Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs an elastic uniaxial material with no tensile strength. In OpenSees the material type is ``ENT``.

.. function:: uniaxialMaterial ENT $matTag $E <$A $B>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique material tag
   $E, |float|, stiffness in compression
   $A, |float|, optional tension scaling factor (default 0.0)
   $B, |float|, optional tension-shape parameter (default 1.0)

In compression the stress is :math:`\sigma = E \varepsilon`; in tension it is :math:`\sigma = A E \tanh(B \varepsilon)` when :math:`A \neq 0`, and zero when :math:`A = 0` (the default).

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial ENT 1 3000.0

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('ENT', 1, 3000.0)

Code Developed by: |fmk|
