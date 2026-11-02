.. _SteelDRCV:

SteelDRCV Material
^^^^^^^^^^^^^^^^^^

This command constructs a rate-dependent steel material with phenomenological bond-slip pinching for cyclic loading. It extends the SteelDRC model by incorporating two mechanisms: (1) strain-rate effects via an additive Voigt-type viscous overstress, and (2) quadrant-dependent pinching for stiffness degradation at the steel--concrete interface.

.. function:: uniaxialMaterial SteelDRCV $tag $Es $fy $eu $fu $esh <-Psh $Psh> <-shPoint $esh1 $fsh1> <-omegaFac $omegaFac> <-fractStrain $eft> <-bausch $bauschType> <-stiffOutput $stiffopt> <-viscousDamper $krate $nrate> <-Dfu $Dfu> <-lambda $lambda> <-np $np>

.. list-table::
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $tag
     - |integer|
     - Unique material tag
   * - $Es
     - |float|
     - Young's modulus (MPa)
   * - $fy
     - |float|
     - Yield stress (MPa)
   * - $eu
     - |float|
     - Uniform elongation (strain at peak stress)
   * - $fu
     - |float|
     - Ultimate stress (MPa)
   * - $esh
     - |float|
     - Strain at onset of strain hardening
   * - $Psh
     - |float|
     - Exponent for the strain-hardening branch of the backbone curve (default = 3.0)
   * - $esh1 $fsh1
     - |float|
     - Intermediate strain-hardening point: strain and stress coordinates. When provided, the intermediate point is used instead of ``$Psh``.
   * - $omegaFac
     - |float|
     - Factor controlling the area under the Bauschinger curve (default = 1.0)
   * - $eft
     - |float|
     - Fracture strain beyond uniform elongation in tension (default = -1, i.e., no post-peak stress drop)
   * - $bauschType
     - |integer|
     - Function type for the Bauschinger curve: 1 = cubic Bezier (default)
   * - $stiffopt
     - |integer|
     - Type of stiffness returned: 0 = tangent (default)
   * - $krate
     - |float|
     - Viscous overstress coefficient (default = 0.0). Recommended: 125 for Grade 60 reinforcing steel.
   * - $nrate
     - |float|
     - Viscous overstress exponent (default = 1.0). Recommended: 0.75 for Grade 60 reinforcing steel.
   * - $Dfu
     - |float|
     - Unloading-branch length as a fraction of the yield stress (default = 1.0). Recommended: 1.15 for Grade 60 reinforcing steel.
   * - $lambda
     - |float|
     - Pinching curvature factor (default = 1.5, range: 0.5--2.5). Controls the extent of stiffness reduction during reloading across cracked concrete sections.
   * - $np
     - |float|
     - Pinching sharpness exponent (default = 1.0, range: 0.5--3.5). Controls the shape of the stiffness reduction curve.

.. note::

   **Strain-rate effects.** The viscous overstress is computed as :math:`f_{sd} = \mathrm{sign}(\dot{\varepsilon})\; k_{\mathrm{rate}}\; |\dot{\varepsilon}|^{n_{\mathrm{rate}}}` and added to the rate-independent mechanical stress :math:`f_{sh}` so that the total stress is :math:`f_s = f_{sh} + f_{sd}`. The model requires the analysis time step ``ops_Dt`` to be defined before the material is invoked.

   **Pinching.** The pinching formulation is governed by two dimensionless parameters: the curvature factor :math:`\lambda` and the sharpness exponent :math:`n_p`. These control the stiffness reduction observed when reinforcing bars cross cracked concrete sections due to bond-slip at the steel--concrete interface.

   All input values must be in consistent units. The model uses engineering stress and strain.

.. admonition:: Example

   The following creates a SteelDRCV material for A706 Grade 60 reinforcing steel with strain-rate and pinching effects:

   1. **Tcl**

   .. code-block:: tcl

      uniaxialMaterial SteelDRCV 1 200000.0 420.0 0.09 656.0 0.005 -Psh 3.93 -omegaFac 1.03 -viscousDamper 125.0 0.75 -Dfu 1.15 -lambda 1.5 -np 1.0

   2. **Python**

   .. code-block:: python

      uniaxialMaterial('SteelDRCV', 1, 200000.0, 420.0, 0.09, 656.0, 0.005, '-Psh', 3.93, '-omegaFac', 1.03, '-viscousDamper', 125.0, 0.75, '-Dfu', 1.15, '-lambda', 1.5, '-np', 1.0)


References
""""""""""

.. [VelasquezBedoya2026] Velásquez Bedoya, J. F. (2026). "A Rate-Dependent and Pinching-Sensitive Constitutive Model for Reinforcing Steel." PhD Dissertation, University of California, San Diego.

Code developed by: **Juan Fernando Velásquez Bedoya** (Universidad Nacional de Colombia, Facultad de Minas. Medellín), `jfvelasq@unal.edu.co <mailto:jfvelasq@unal.edu.co>`_
