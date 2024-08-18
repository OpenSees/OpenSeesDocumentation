.. _InitStrain:

InitStrain Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a InitStrain material object. It is a wrapper that imposes an inital-strain to another nDMaterial such that :math:`\sigma = f\left (\varepsilon + \varepsilon_{0}\right )`.


.. function:: nDMaterial InitStrain $matTag $otherTag $eps0_11 <$eps0_22 $eps0_33 $eps0_12 $eps0_23 $eps0_13>


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, "unique tag identifying this init-strain material wrapper"
   $otherTag, |integer|, "unique tag identifying the previously defined nD material"
   $eps0_11 <$eps0_22 $eps0_33 $eps0_12 $eps0_23 $eps0_13>, 1 or 6 |float|, "initial strain values. If only one is given, a volumetric strain = eps0_11 is imposed."

Usage Notes
"""""""""""

.. admonition:: Limitations

   * The only material formulation for the InitStrain material object is "ThreeDimensional".
   * The only material formulation allowed for the sub-material object is "ThreeDimensional".

.. admonition:: Responses

   * All responses available for the nDMaterial object: **stress** (or **stresses**), **strain** (or **strains**), **tangent** (or **Tangent**), **TempAndElong**.

.. admonition:: Example 1 - Simple Linear Validation

   | :download:`InitStrainExample.py`

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
