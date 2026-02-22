.. _MinMax:

MinMax Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a MinMax uniaxial material wrapper. The wrapper forwards strain to the wrapped material and returns its stress and tangent until the material strain goes above a maximum or below a minimum. Once that condition is met in ``commitState()``, the wrapper stops updating the wrapped material (the material is treated as failed).

.. function:: uniaxialMaterial MinMax $matTag $otherTag <-min $minStrain> <-max $maxStrain>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $minStrain, |float|,   (optional) minimum strain; default -1.0e16
   $maxStrain, |float|,   (optional) maximum strain; default 1.0e16

.. note::

   After the strain limit is exceeded, the wrapper no longer calls the wrapped material.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Hardening 1 3.0 1.0 0.1
      uniaxialMaterial MinMax 2 1 -min -0.8

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Hardening', 1, 3.0, 1.0, 0.1)
      ops.uniaxialMaterial('MinMax', 2, 1, '-min', -0.8)

Code developed by: |mhs|
