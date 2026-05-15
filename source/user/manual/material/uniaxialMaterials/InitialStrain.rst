.. _InitialStrain:

InitStrain Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an InitStrain (or InitialStrain) uniaxial material wrapper. The wrapper imposes an initial strain on the wrapped material so that the effective strain seen by the wrapped material is the applied strain plus the initial strain. After the constructor, no special state is maintained.

.. function:: uniaxialMaterial InitStrain $matTag $otherTag $eps0

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $eps0,     |float|,    initial strain

.. note::

   It is good practice to run one analysis step with dt = 0 when using initial strain (and initial stress) wrappers so that the model is in equilibrium.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Hardening 1 3.0 1.0 0.1
      uniaxialMaterial InitStrain 2 1 -0.1

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Hardening', 1, 3.0, 1.0, 0.1)
      ops.uniaxialMaterial('InitStrain', 2, 1, -0.1)

Code developed by: |mhs|
