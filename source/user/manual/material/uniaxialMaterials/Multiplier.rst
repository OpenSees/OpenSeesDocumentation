.. _Multiplier:

Multiplier Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Multiplier uniaxial material wrapper. The wrapper multiplies the stress and tangent of its wrapped UniaxialMaterial by a factor. Typical uses include overstrength factors for materials and p-y multipliers for shadowing effects in pile groups.

.. function:: uniaxialMaterial Multiplier $matTag $otherTag $multiplier

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,     |integer|,  unique material tag
   $otherTag,   |integer|,  tag of a previously-defined UniaxialMaterial
   $multiplier, |float|,    factor applied to stress and tangent of the wrapped material

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 100.0
      uniaxialMaterial Multiplier 2 1 0.8

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('Multiplier', 2, 1, 0.8)

Code developed by: |mhs|
