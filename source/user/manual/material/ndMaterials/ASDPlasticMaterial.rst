.. _ASDPlasticMaterial:

ASDPlasticMaterial
^^^^^^^^^^^^^^^^^^

| This command is used to construct an ASDPlasticMaterial material object. ASDPlasticMaterial implements a large family of constitutive models based on the classical theory of elastoplasticity. Users build new constitutive models by selecting the yield function, plastic-flow direction, elasticity law, and hardening models for the internal variables from several possible options for each component. Currently, there are 60 unique possible choices, that will only grow as more options become available for each component. 

To create a new model, specify the Yield Function (YF) type, Plastic Flow (PF) type, and Elasticity (EL) type. If you specify these and nothing else, you'll get a print out of the internal variables and model parameters that define the model. All internal variables and model parameters are set to zero unless specified by the user, which might or not make sense depending on context. 

After setting the YF, PF and EL, you need to give initial values to internal variables within the |Begin_Internal_Variables| ... |End_Internal_Variables| block. Then, the |Begin_Model_Parameters| ... |End_Model_Parameters| block is used to provide model parameter values (these can be changed during the analysis with the setParameter command as expected). Finally, model integration options are set within the |Begin_Integration_Options| ... |End_Integration_Options| code block. Specification blocks can occur in any order. The complete command looks as follows:

.. function::
   nDMaterial ASDPlasticMaterial $tag \
         $YieldFunctionType \
         $PlasticFlowType \
         $ElasticityType \
         $IV_TYPE \
      Begin_Internal_Variables \
         $InternalVariable1 $$double_value1 $$double_value2... $$double_valueN1 \ 
         $InternalVariable2 $$double_value1 $$double_value2... $$double_valueN2 \
         ... (depends on how many internal variables the particular selected model has)
      End_Internal_Variables \
      Begin_Model_Parameters \
         $ModelParameters1 $$double_value1 \
         $ModelParameters2 $$double_value2 \
         ... (depends on how many model parameters the particular selected model has)
      End_Model_Parameters \
      Begin_Integration_Options \
          f_relative_tol $double_value \
          stress_relative_tol $double_value \
          n_max_iterations $int_value \
          return_to_yield_surface (0 or 1) \
          method (string) : Forward_Euler | Runge_Kutta_45_Error_Control \
      End_Integration_Options


Explanation

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, "Unique tag identifying this material."
   $YieldFunctionType, |string|, "Mandatory. Yield function to be used -> :ref:`YieldFunctionType`"
   $PlasticFlowType, |string|, "Mandatory. Plastic flow direction to be used -> :ref:`PlasticFlowType`"
   $ElasticityType, |string|, "Mandatory. Elastic model to be used -> :ref:`ElasticityType`"
   $IV_TYPE, |string|, "Mandatory. Hardening model for internal variables. Admitted types depend on YF, PF, and EL chosen.   -> :ref:`InternalVariables`"
   Begin_Internal_Variables, |string|, "Optional. Marks the beginning of the code block to set the internal variables. If ommitted, all internal variables are initialized to zero. You can specify as many of the following variables as wanted. Ommitted variables are initialized to zero. Number and name of variables that can be set is model dependent (once YF, PF, and EL are specified)"
   $InternalVariable1, |list|, "Mandatory. Initial value of internal variable1. Dimension depends on internal variable type.  -> :ref:`InternalVariables`"
   $InternalVariable2, |list|, "Mandatory. Initial value of internal variable2.  -> :ref:`InternalVariables`"
   End_Internal_Variables, |string|, "Mandatory if block started. Marks the end of the code block to set the internal variables"
   Begin_Model_Parameters, |string|, "Optional. Marks the beginning of the code block to set the model parameters"
   $ModelParameters, |list|, "Mandatory. Parameters of the models to be used. This depends on the particular choices of |YieldFunctionType|, |PlasticFlowType|, |ElasticityType|, and |IV_type|. "
   End_Model_Parameters, |string|, "Mandatory if block started. Marks the beginning of the code block to set the model parameters"
   Begin_Integration_Options, |string|, "Optional. Marks the beginning of the code block to set the integration options. You can set any ammount "
   End_Integration_Options, |string|, "Mandatory if block started. Marks the beginning of the code block to set the model parameters"

|  The :ref:`YieldFunctionType`, :ref:`PlasticFlowType`, :ref:`ElasticityType`, and :ref:`InternalVariables` have different variables and parameters to be set.


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
