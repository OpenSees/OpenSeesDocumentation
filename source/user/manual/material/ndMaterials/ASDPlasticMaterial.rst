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
   $ModelParameters, |list|, "Values for parameters of the models to be used. This depends on the particular choices of |YieldFunctionType|, |PlasticFlowType|, |ElasticityType|, and |IV_type|. "
   End_Model_Parameters, |string|, "Mandatory if block started. Marks the beginning of the code block to set the model parameters"
   Begin_Integration_Options, |string|, "Optional. Marks the beginning of the code block to set the integration options. You can set any ammount "
   End_Integration_Options, |string|, "Mandatory if block started. Marks the beginning of the code block to set the model parameters"

|  The :ref:`YieldFunctionType`, :ref:`PlasticFlowType`, :ref:`ElasticityType`, and :ref:`InternalVariables` have different variables and parameters to be set.


.. toctree::
   :caption: Arguments detailed description
   :maxdepth: 2

   ./ASDPlasticMaterial/YieldFunctions
   ./ASDPlasticMaterial/PlasticFlowType
   ./ASDPlasticMaterial/ElasticityType

.. _`FunctionVariables`:
Functions Variables
"""""""""""""""""""

.. _`ModelParameters`:
Integration Options
"""""""""""""""""""

.. csv-table:: 
   :header: "Parameter", "Type", "Description"
   :widths: 10, 10, 40

   $f_relative_tol, |double|, "Relative tolerance to evaluate the yield function crossing."
   $stress_relative_tol, |double|, "Tolerance for the convergece of the integration algorithm."
   $n_max_iterations, |int|, "Maximum number of iterations for constitutive integration."
   $return_to_yield_surface, |0 or 1|, "Whether to apply a return to yield surface algorithm after integration convergence."
   $method, |string|, "Constitutive integration method. Options: Forward_Euler, Runge_Kutta_45_Error_Control"

The default integration method is **Runge_Kutta_45_Error_Control** that uses the classical RK45 ODE integration algorithm employing a 4-th order prediction of the stress increment together with a 5-order prediction to estimate the integration error. In this scheme the strain increment provided by the element to the Gauss point is sub-divided into sub-increments, a process which is automated such that the provided **$stress_relative_tol** is met. This method is provided as a robust standard method which is applicable across all possible combinations of components, although there are possibly better approaches for specific cases which might become available in the future. 

The different parameters are activated depending on the integration algorithm selected. The *Forward_Euler* algorithm only uses the **$return_to_yield_surface** parameter, while **Runge_Kutta_45_Error_Control** uses the rest. 

The **$f_relative_tol** parameter comes into play when the yield surface is being crossed, that is, when the previous (committed) stress is within the yield surface and the elastic prediction of the stress increment brings the stress state beyond the yield surface. In that case, an elastic increment occurs until the yield surface is touched which requires iterations with the Brent root finding algorithm. This is used by both currently available integration methods. 






.. admonition:: Responses 

   * You can request any and all internal variables by their specific name as an output. 

.. admonition:: setParameter 

   * You can set the value of all parameters with their variable name at any point. 

Example
"""""""



Code Developed by: **José A. Abell** at UANDES, Chile and ASDEA and **Massimo Petracca** at ASDEA Software, Italy.
