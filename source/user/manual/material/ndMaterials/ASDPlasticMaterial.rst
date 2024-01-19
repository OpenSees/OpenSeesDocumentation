.. _ASDPlasticMaterial:

ASDPlasticMaterial
^^^^^^^^^^^^^^^^^^

| This command is used to construct an ASDPlasticMaterial material object, a elastoplastic model for [!!!!! qué tipo de materiales ? materiales en general o enfocado a suelo ?] materials.
| !!!! It is based on continuum-damage theory, were the stress tensor can be explicitly obtained from the total strain tensor, without internal iterations at the constitutive level. This makes it fast and robust, suitable for the simulation of large-scale structures. Plasticity is added in a simplified way, in order to have the overall effect of inelastic deformation, but keeping the simplicity of continuum-damage models.
| !!!! To improve robustness and convergence of the simulation in case of strain-softening, this model optionally allows to use the IMPL-EX integration scheme (a mixed IMPLicit EXplicit integration scheme).


.. function::
   nDMaterial ASDPlasticMaterial $tag $YieldFunctionType $PlasticFlowType $ElasticityType
   Begin_Internal_Variables $InternalVariables End_Internal_Variables
   Begin_Model_Parameters $ModelParameters End_Model_Parameters
   

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, "Unique tag identifying this material."
   $YieldFunctionType, |string|, "Mandatory. Yield function to be used -> :ref:`YieldFunctionType`"
   $PlasticFlowType, |string|, "Mandatory. Plastic flow direction to be used -> :ref:`PlasticFlowType`"
   $ElasticityType, |string|, "Mandatory. Elastic model to be used -> :ref:`ElasticityType`"
   Begin_Internal_Variables, |string|, "Mandatory. String prefix to set all the function variables"
   $InternalVariables, |list|, "Mandatory. Variables to be used for the functions -> :ref:`FunctionVariables`"
   End_Internal_Variables, |string|, "Mandatory. String sufix to set all the function variables"
   Begin_Model_Parameters, |string|, "Mandatory. String prefix to set all the model parameters"
   $ModelParameters, |list|, "Mandatory. Parameters of the models to be used -> :ref:`ModelParameters`"
   End_Model_Parameters, |string|, "Mandatory. String sufix to set all the model parameters"

|  The :ref:`YieldFunctionType`, :ref:`PlasticFlowType` and the :ref:`ElasticityType` have different variables and parameters to be setted.


.. toctree::
   :caption: Arguments detailed description
   :maxdepth: 2

   ASDPlasticMaterial/YieldFunctions
   ASDPlasticMaterial/PlasticFlowType
   ASDPlasticMaterial/ElasticityType

.. _`FunctionVariables`:
Functions Variables
"""""""""""""""""""

.. _`ModelParameters`:
Model Parameters
""""""""""""""""



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
