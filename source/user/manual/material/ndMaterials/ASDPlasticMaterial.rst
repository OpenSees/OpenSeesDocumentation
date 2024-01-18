.. _ASDPlasticMaterial:

ASDPlasticMaterial
^^^^^^^^^^^^^^^^^^


| This command is used to construct an ASDPlasticMaterial material object, a elastoplastic model for [!!!!! qué tipo de materiales ? materiales en general o enfocado a suelo ?] materials.
| !!!! It is based on continuum-damage theory, were the stress tensor can be explicitly obtained from the total strain tensor, without internal iterations at the constitutive level. This makes it fast and robust, suitable for the simulation of large-scale structures. Plasticity is added in a simplified way, in order to have the overall effect of inelastic deformation, but keeping the simplicity of continuum-damage models.
| !!!! To improve robustness and convergence of the simulation in case of strain-softening, this model optionally allows to use the IMPL-EX integration scheme (a mixed IMPLicit EXplicit integration scheme).


.. function::
   nDMaterial ASDPlasticMaterial $tag
   $YieldFunctionType
   $PlasticFlowType
   $ElasticityType
   $InternalVariables
   $ModelParameters
   

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, "Unique tag identifying this material."
   $YieldFunctionType, |string|, "Mandatory. Yield function to be used -> :ref:`YieldFunctionType`"
   $PlasticFlowType, |string|, "Mandatory. Plastic flow direction to be used -> :ref:`PlasticFlowType`"
   $ElasticityType, |string|, "Mandatory. Elastic model to be used -> :ref:`ElasticityType`"
   $InternalVariables, |string|, "Mandatory. Variables to be used for the functions -> :ref:`FunctionVariables`"
   $ModelParameters, |string|, "Mandatory. Parameters of the models to be used -> :ref:`ModelParameters`"

.. _`FunctionVariables`:
Functions Variables
"""""""""""""""""""
.. _`YieldFunctionType`:
YieldFunctionType
'''''''''''''''''
| Aquí va una descripcion del efecto que tiene el YieldFunction
| Options to use:
.. csv-table:: 
   :header: "Argument", "Description"
   :widths: 10, 40

   VonMises_YF, "DESCRIPCION !"
   DruckerPrager_YF, "DESCRIPCION !"
   RoundedMohrCoulomb_YF, "DESCRIPCION !"
VonMises_YF
===========
Descripcion de la funcion

DruckerPrager_YF
================
Descripcion de la funcion

RoundedMohrCoulomb_YF
=====================
Descripcion de la funcion

.. _`PlasticFlowType`:
PlasticFlowType
'''''''''''''''
| Aquí va una descripcion del efecto que tiene el PlasticFlowType
| Options to use:
.. csv-table:: 
   :header: "Argument", "Description"
   :widths: 10, 40

   VonMises_PF, "DESCRIPCION !"
   DruckerPrager_PF, "DESCRIPCION !"
   ConstantDilatancy_PF, "DESCRIPCION !"

VonMises_PF
===========
Descripcion de la funcion

DruckerPrager_PF
================
Descripcion de la funcion

ConstantDilatancy_PF
====================
Descripcion de la funcion

.. _`ElasticityType`:
ElasticityType
''''''''''''''
| Aquí va una descripcion del efecto que tiene el Elasticity
| Options to use:
.. csv-table:: 
   :header: "Argument", "Description"
   :widths: 10, 40

   LinearIsotropic3D_EL, "DESCRIPCION !"
   DuncanChang_EL, "DESCRIPCION !"

LinearIsotropic3D_EL
====================
Descripcion de la funcion

DuncanChang_EL
==============
Descripcion de la funcion

.. _`ModelParameters`:
Model Parameters
""""""""""""""""

Theory
""""""

| In the following description, all variables without subscripts refer to the current time-step, while those with the :math:`n` and :math:`n-1` subscripts refer to the same variables at the two previous (known) time steps.
| The trial effective stress tensor is computed from the previous effective stress :math:`\bar{\sigma}_{n}` and the trial elastic stress increment :math:`C_{0}:\left (\varepsilon - \varepsilon_{n}\right )`:

.. math::
   \tilde{\sigma} = \bar{\sigma}_{n} + C_{0}:\left (\varepsilon - \varepsilon_{n}\right )

| It is then split into its positive (:math:`\tilde{\sigma}^{+}`) and negative (:math:`\tilde{\sigma}^{-}`) parts, using the positive principal stresses (:math:`\langle \tilde{\sigma}_{i} \rangle`) and their principal directions (:math:`p_{i}`):

.. math::
   \begin{align} \tilde{\sigma}^{+} = \sum_{i=1}^{3} \langle \tilde{\sigma}_{i} \rangle p_{i}\otimes p_{i} && \tilde{\sigma}^{-} = \tilde{\sigma} - \tilde{\sigma}^{+} \end{align}

| Two equivalent scalar stress measures for the tensile (:math:`\tilde{\tau}^+`) and compressive (:math:`\tilde{\tau}^-`) behaviors are obtained from the trial effective stress tensor :math:`\tilde{\sigma}` (or from its negative part :math:`\tilde{\sigma}^{-}` for the compressive behavior) using the following damage surfaces:

.. math::
   \tilde{\tau}^+ = f\left(\tilde{\sigma} \right) = H\left (\tilde{\sigma}_{max} \right )\left [\frac{1}{1-\alpha}\left(\alpha\tilde{I}_1+\sqrt[]{3\tilde{J}_2}+\beta\langle \tilde{\sigma}_{max} \rangle \right )\frac{1}{\phi} \right ]

.. math::
   \tilde{\tau}^- = f\left(\tilde{\sigma}^{-} \right) = \left [\frac{1}{1-\alpha}\left(\alpha\tilde{I}_1+\sqrt[]{3\tilde{J}_2}+\gamma\langle -\tilde{\sigma}_{max} \rangle \right ) \right ]

| where :math:`\tilde{I}_1` is the first invariant of :math:`\tilde{\sigma}` (or :math:`\tilde{\sigma}^{-}`), :math:`\tilde{J}_2` is the second invariant of the deviator of :math:`\tilde{\sigma}` (or :math:`\tilde{\sigma}^{-}`), :math:`\sigma_{max}` is the maximum principal stress of :math:`\tilde{\sigma}` (or :math:`\tilde{\sigma}^{-}`), :math:`\alpha = 4/33`, :math:`\beta = 23/3`, :math:`\phi = 10`, :math:`\gamma= 3(1 - K_c) / (2 K_c - 1)`.

| The equivalent stress measures :math:`\tilde{\tau}^+` and :math:`\tilde{\tau}^-` are converted into their trial total-strain counter-parts :math:`\tilde{x}^+` and :math:`\tilde{x}^-` accounting for the equivalent plastic strain from the previous step:

.. math::
   \tilde{x}^{\pm} = \frac{\tilde{\tau}^{\pm}}{E} + x_{pl,n}

| To impose the irreversibity of plasticity and damage, and to account for rate-dependency (if :math:`\eta \gt 0`), the current equivalent strain measures are updated as follows:

.. math::
   x^{\pm} = \begin{cases}    \frac{\eta}{\eta +\Delta t} x^{\pm}_n + \frac{\Delta t}{\eta +\Delta t} \tilde{x}^{\pm}, & \text{if } \tilde{x}^{\pm} > x^{\pm}_n\\ x^{\pm}_n, & \text{otherwise}           \end{cases}

| The equivalent total-strain measures are then plugged into the hardening-softening laws to obtain the plastic and cracking damage variables :math:`d_{pl}^{\pm}` and :math:`d_{cr}^{\pm}`, and the effective (:math:`\bar{\sigma}`) and nominal (:math:`\sigma`) stress tensors are computed as:

.. math::
   \begin{align} \bar{\sigma}^+ = \left (1-d^{+}_{pl}\right ) \tilde{\sigma}^+, && \bar{\sigma}^- = \left (1-d^{-}_{pl}\right ) \tilde{\sigma}^-, && \bar{\sigma} = \bar{\sigma}^+ + \bar{\sigma}^- \end{align}

.. math::
   \sigma = \left (1-d^{+}_{cr}\right ) \bar{\sigma}^+ + \left (1-d^{-}_{cr}\right ) \bar{\sigma}^-

Usage Notes
"""""""""""

.. admonition:: Responses

   * All responses available for the nDMaterial object: **stress** (or **stresses**), **strain** (or **strains**), **tangent** (or **Tangent**), **TempAndElong**.
   * **damage** or **Damage**: 2 components (:math:`d^+`, :math:`d^-`). The cracking damage variables. If option **-crackPlanes** is used, it gives the maximum values among all crack-planes.
   * **damage -avg** or **Damage -avg**: 2 components (:math:`d^+`, :math:`d^-`). Same as above. If option **-crackPlanes** is used, it gives the average values of the crack-planes.
   * **equivalentPlasticStrain** or **EquivalentPlasticStrain**: 2 components (:math:`x_{pl}^+`, :math:`x_{pl}^-`). The equivalent plastic strains. If option **-crackPlanes** is used, it gives the maximum values among all crack-planes.
   * **equivalentPlasticStrain -avg** or **EquivalentPlasticStrain -avg**: 2 components (:math:`x_{pl}^+`, :math:`x_{pl}^-`). Same as above. If option **-crackPlanes** is used, it gives the average values of the crack-planes.
   * **equivalentTotalStrain** or **EquivalentTotalStrain**: 2 components (:math:`x^+`, :math:`x^-`). The equivalent total strains. If option **-crackPlanes** is used, it gives the maximum values among all crack-planes.
   * **equivalentTotalStrain -avg** or **EquivalentTotalStrain -avg**: 2 components (:math:`x^+`, :math:`x^-`). Same as above. If option **-crackPlanes** is used, it gives the average values of the crack-planes.
   * **cw** or **crackWidth** or **CrackWidth**: 1 component (:math:`cw`). The equivalent tensile total strain minus the equivalent strain at the onset of crack, times the characteristic length of the parent element. If option **-crackPlanes** is used, it gives the maximum value among all crack-planes.
   * **cw -avg** or **crackWidth -avg** or **CrackWidth -avg**: 1 component (:math:`cw`). Same as above. If option **-crackPlanes** is used, it gives the average value of the crack-planes.
   * **crackInfo $Nx $Ny $Nz** or **CrackInfo $Nx $Ny $Nz**: 2 components (:math:`ID`, :math:`X`). Gives the 0-based index (ID) and the tensile equivalent total strain (X) of the crack-plane with the normal vector closest to (Nx, Ny, Nz).
   * **crushInfo $Nx $Ny $Nz** or **CrushInfo $Nx $Ny $Nz**: 2 components (:math:`ID`, :math:`X`). Same as above, but for the compressive response.

.. admonition:: Example 1 - Drawing the Damage Surface

   A Python example to draw the damage surface in the plane-stress case:
   

References
""""""""""

.. [Petracca2022] | Petracca, M., Camata, G., Spacone, E., & Pelà, L. (2022). "Efficient Constitutive Model for Continuous Micro-Modeling of Masonry Structures" International Journal of Architectural Heritage, 1-13 (`Link to article <https://www.researchgate.net/profile/Luca-Pela/publication/363656245_Efficient_Constitutive_Model_for_Continuous_Micro-Modeling_of_Masonry_Structures/links/6332e7f1165ca22787785134/Efficient-Constitutive-Model-for-Continuous-Micro-Modeling-of-Masonry-Structures.pdf>`_)

.. [Oliver2008] | Oliver, J., Huespe, A. E., & Cante, J. C. (2008). "An implicit/explicit integration scheme to increase computability of non-linear material and contact/friction problems" Computer Methods in Applied Mechanics and Engineering, 197(21-24), 1865-1889 (`Link to article <https://core.ac.uk/download/pdf/325948712.pdf>`_)

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
