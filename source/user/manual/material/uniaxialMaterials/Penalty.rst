.. _Penalty:

Penalty Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Penalty uniaxial material wrapper. The wrapper adds a small stiffness to its wrapped UniaxialMaterial. This helps avoid a singular stiffness due to perfect plasticity and is a lightweight alternative to placing the wrapped material in parallel with an ElasticMaterial.

.. function:: uniaxialMaterial Penalty $matTag $otherTag $penalty <-noStress>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $penalty,  |float|,    actual stiffness value added to the tangent (and optionally to stress); same units as material tangent
   -noStress, |string|,   (optional) if given, penalty stiffness is not added to stress, only to tangent

.. note::

   Use a small penalty value (the actual stiffness added) so that the response remains dominated by the wrapped material.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      set E 29000.0
      set penalty [expr 0.05 * $E]
      uniaxialMaterial Elastic 1 $E
      uniaxialMaterial Penalty 2 1 $penalty

   2. **Python Code**

   .. code-block:: python

      E = 29000.0
      penalty = 0.05 * E
      ops.uniaxialMaterial('Elastic', 1, E)
      ops.uniaxialMaterial('Penalty', 2, 1, penalty)

Code developed by: |mhs|
