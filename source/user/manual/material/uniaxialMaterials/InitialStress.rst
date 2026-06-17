.. _InitialStress:

InitStress Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an InitStress (or InitialStress) uniaxial material wrapper. The wrapper imposes an initial stress on the wrapped material. After the constructor, the wrapper passes through the wrapped material response with the initial stress offset.

.. function:: uniaxialMaterial InitStress $matTag $otherTag $sig0

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $sig0,     |float|,    initial stress

.. note::

   Run one analysis step with dt = 0 (e.g. static with integrator LoadControl 0.0) so that initial stresses are in equilibrium.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Hardening 1 3.0 1.0 0.1
      uniaxialMaterial InitStress 2 1 0.3

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Hardening', 1, 3.0, 1.0, 0.1)
      ops.uniaxialMaterial('InitStress', 2, 1, 0.3)

Code developed by: |mhs|
