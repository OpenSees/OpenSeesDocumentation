.. _Damper:

Damper Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Damper uniaxial material wrapper. The wrapper uses the stress-strain response of any UniaxialMaterial as a **stress versus strain-rate** relationship for damping. The conversion is done by passing strain rate as strain and the material tangent as the damping tangent in the state determination.

.. function:: uniaxialMaterial Damper $matTag $otherTag <-factors $fact1 $fact2 ...>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $fact1 ..., |float|,   (optional) factors for multiple materials

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 100.0
      uniaxialMaterial Damper 2 1

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('Damper', 2, 1)

Code developed by: |mhs|
