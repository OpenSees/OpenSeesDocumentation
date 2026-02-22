.. _TensionOnly:

TensionOnly Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a TensionOnly uniaxial material wrapper. The wrapper returns zero stress and zero tangent when the wrapped material would return negative stress; it does not call ``commitState()`` on the wrapped material when stress is negative. So only tensile (positive) stress is returned.

.. function:: uniaxialMaterial TensionOnly $matTag $otherTag <-min $minStrain> <-max $maxStrain>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $minStrain, |float|,   (optional) minimum strain limit
   $maxStrain, |float|,   (optional) maximum strain limit

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 100.0
      uniaxialMaterial TensionOnly 2 1

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('TensionOnly', 2, 1)

Code developed by: |mhs|
