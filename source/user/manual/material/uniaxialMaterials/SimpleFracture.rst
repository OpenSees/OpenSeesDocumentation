.. _SimpleFracture:

SimpleFracture Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a SimpleFracture uniaxial material wrapper. The wrapper imposes tensile fracture on the wrapped material: after the strain exceeds a specified maximum tensile strain, the wrapper provides compressive stress based on an estimate of the elastic strain.

.. function:: uniaxialMaterial SimpleFracture $matTag $otherTag $maxStrain

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $maxStrain, |float|,   maximum tensile strain (fracture strain)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Hardening 1 3.0 1.0 0.1
      uniaxialMaterial SimpleFracture 2 1 0.8

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Hardening', 1, 3.0, 1.0, 0.1)
      ops.uniaxialMaterial('SimpleFracture', 2, 1, 0.8)

Code developed by: |mhs|
