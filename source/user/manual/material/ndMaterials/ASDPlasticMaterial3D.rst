.. _ASDPlasticMaterial3D:

ASDPlasticMaterial3D
^^^^^^^^^^^^^^^^^^^

| This command is used to construct an ``ASDPlasticMaterial3D`` material object. ``ASDPlasticMaterial3D`` implements a large family of constitutive models based on the classical theory of elastoplasticity using advanced template metaprogramming. Users build new constitutive models by selecting the yield function, plastic-flow direction, elasticity law, and hardening models for the internal variables from several possible options for each component. 

| This is the 3D-specific implementation that provides enhanced features compared to the base ``ASDPlasticMaterial`` class, including multiple integration methods, tangent operator options, and extensive response capabilities.

To create a new model, specify the Yield Function type (``$YieldFunctionType``), Plastic Flow type (``$PlasticFlowType``), and Elasticity type (``$ElasticityType``). All internal variables and model parameters are set to zero unless specified by the user, which might or not make sense depending on context, and this initialization is printed out to the screen. 

After setting the ``$YieldFunctionType``, ``$PlasticFlowType`` and ``$ElasticityType``, you can give initial values to internal variables within the ``Begin_Internal_Variables`` ... ``End_Internal_Variables`` block. Then, the ``Begin_Model_Parameters`` ... ``End_Model_Parameters`` block is used to provide model parameter values (these can be changed during the analysis with the ``setParameter`` command as expected). Finally, model integration options are set within the ``Begin_Integration_Options`` ... ``End_Integration_Options`` code block. Specification blocks can occur in any order or ommitted. 

The complete command looks as follows::

   nDMaterial ASDPlasticMaterial3D $tag 
      $YieldFunctionType 
      $PlasticFlowType $
      ElasticityType 
      $IV_TYPE 
      Begin_Internal_Variables 
         $InternalVariable1 $$double_value1 $$double_value2... $$double_valueN1  
         $InternalVariable2 $$double_value1 $$double_value2... $$double_valueN2 
         #... (depends on how many internal variables the particular selected model has) 
      End_Internal_Variables 
      Begin_Model_Parameters 
         $ModelParameters1 $$double_value1 
         $ModelParameters2 $$double_value2 
         #... (depends on how many model parameters the particular selected model has) 
      End_Model_Parameters 
      Begin_Integration_Options 
         f_relative_tol $double_value 
         stress_relative_tol $double_value 
         n_max_iterations $int_value 
         return_to_yield_surface (0 or 1) 
         method (string) : Forward_Euler | Forward_Euler_Subincrement | Backward_Euler | Backward_Euler_LineSearch | Modified_Euler_Error_Control | Runge_Kutta_45_Error_Control
         tangent_operator (string) : Elastic | Numerical_Algorithmic_FirstOrder | Numerical_Algorithmic_SecondOrder | Continuum | Secant
      End_Integration_Options


Explanation

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, "Unique tag identifying this material."
   $YieldFunctionType, |string|, "Mandatory. Yield function to be used -> :ref:`YieldFunctionType`"
   $PlasticFlowType, |string|, "Mandatory. Plastic flow direction to be used -> :ref:`PlasticFlowType`"
   $ElasticityType, |string|, "Mandatory. Elastic model to be used -> :ref:`ElasticityType`"
   $IV_TYPE, |string|, "Mandatory. Hardening model for internal variables. Admitted types depend on YF, PF, and EL chosen.  "
   Begin_Internal_Variables, |string|, "Optional. Marks the beginning of the code block to set the internal variables. If ommitted, all internal variables are initialized to zero. You can specify as many of the following variables as wanted. Ommitted variables are initialized to zero. Number and name of variables that can be set is model dependent (once YF, PF, and EL are specified)"
   $InternalVariable1, |list of name/value pairs|, "Initial value of internal variable1. Dimension depends on internal variable type.  "
   $InternalVariable2, |list of name/value pairs|, "Initial value of internal variable2.  "
   "--", "--", "... (input as many as model supports)"
   End_Internal_Variables, |string|, "Mandatory if block started. Marks the end of the code block to set the internal variables"
   Begin_Model_Parameters, |string|, "Optional. Marks the beginning of the code block to set the model parameters"
   $ModelParameters, |list of name/value pairs|, "Values for parameters of the models to be used. This depends on the particular choices of ``$YieldFunctionType``, ``$PlasticFlowType``, ``$ElasticityType``, and ``$IV_type``. "
   "--", "--", "... (input as many as model supports)"
   End_Model_Parameters, |string|, "Mandatory if block started. Marks the beginning of the code block to set the model parameters"
   Begin_Integration_Options, |string|, "Optional. Marks the beginning of the code block to set the integration options. You can set any ammount "
   End_Integration_Options, |string|, "Mandatory if block started. Marks the beginning of the code block to set the model parameters"

|  The :ref:`YieldFunctionType`, :ref:`PlasticFlowType`, and :ref:`ElasticityType` have different variables and parameters to be set.

.. admonition:: Specification of internal variables (``$IV_TYPE``)

	All internal variables are specified in a single string with no spaces. Internal variables specifications are separated with a colon ``:``. After the name of the internal variable, the name of the hardening function must be provided in parenthesis. The specification string must end in a colon. The syntax is, thus:

	.. code-block::

		InternalVariable1(HardeningFunction1):InternalVariable2(HardeningFunction2):

	Internal variables are required for the yield function and plastic flow direction (see speficic components for details), and all internal variables must be provided with their hardening function otherwise instantiation fails. 

.. admonition:: Note

    Any internal variable or parameter that is not specified is set to zero by default.  


.. toctree::
   :caption: Arguments detailed description
   :maxdepth: 2

   ../ASDPlasticMaterial/YieldFunctions
   ../ASDPlasticMaterial/PlasticFlowType
   ../ASDPlasticMaterial/ElasticityType
   ../ASDPlasticMaterial/HardeningFunctions

.. _ASDPlasticMaterial3DTheory:

ASDPlasticMaterial3D Theory
"""""""""""""""""""""""""""""

The theoretical foundation is identical to :ref:`ASDPlasticTheory`. However, ``ASDPlasticMaterial3D`` provides additional implementation features:

* **Template Metaprogramming**: Uses C++ template metaprogramming for compile-time optimization
* **Multiple Integration Methods**: Offers several integration algorithms beyond the basic methods
* **Advanced Tangent Operators**: Provides different tangent computation strategies
* **Enhanced Response System**: Supports additional response queries and parameter updates

The material recieves the total (trial) strain :math:`\vec{\epsilon}^{\text{trial}}` from the finite element that contains it. From this, the trial strain increment is computed by subtracting the previously committed total strain:

.. math::
    \Delta \vec{\epsilon}^{\text{trial}} = \vec{\epsilon}^{\text{trial}} - \vec{\epsilon}^{\text{commit}}

The integration method selected determines how the stress increment is computed and how the plastic corrections are applied.

.. _`ASDPlasticMaterial3DIntegrationMethods`:
Advanced Integration Methods
""""""""""""""""""""""""""""

``ASDPlasticMaterial3D`` supports multiple integration algorithms beyond the basic Forward Euler and Runge-Kutta methods:

.. csv-table:: 
   :header: "Integration Method", "Description"
   :widths: 30, 50

   ``Forward_Euler``, "Basic explicit forward Euler method with yield surface crossing detection"
   ``Forward_Euler_Subincrement``, "Forward Euler with automatic subincrementation for large strain increments"
   ``Backward_Euler``, "Implicit backward Euler method for better stability"
   ``Backward_Euler_LineSearch``, "Backward Euler with line search for enhanced convergence"
   ``Modified_Euler_Error_Control``, "Modified Euler method with adaptive error control"
   ``Runge_Kutta_45_Error_Control``, "4th/5th order Runge-Kutta with adaptive error control (default)"

.. admonition:: Integration Method Selection

   The integration method is selected in the ``Begin_Integration_Options`` block using the ``method`` parameter. If not specified, ``Runge_Kutta_45_Error_Control`` is used by default.

.. _`ASDPlasticMaterial3DTangentOperators`:
Tangent Operator Types
"""""""""""""""""""""

``ASDPlasticMaterial3D`` provides several options for computing the consistent tangent operator:

.. csv-table:: 
   :header: "Tangent Operator", "Description"
   :widths: 30, 50

   ``Elastic``, "Returns the elastic tangent matrix (ignores plasticity)"
   ``Numerical_Algorithmic_FirstOrder``, "Computes algorithmic tangent using first-order finite differences"
   ``Numerical_Algorithmic_SecondOrder``, "Computes algorithmic tangent using second-order finite differences (more accurate but slower)"
   ``Continuum``, "Returns the continuum tangent operator"
   ``Secant``, "Returns the average of continuum and elastic tangents"

.. admonition:: Tangent Operator Selection

   The tangent operator type is selected in the ``Begin_Integration_Options`` block using the ``tangent_operator`` parameter. If not specified, an appropriate default is selected based on the integration method.

.. _`ASDPlasticMaterial3DIntegrationOptions`:
Integration Options
"""""""""""""""""""

.. csv-table:: 
   :header: "Parameter", "Type", "Description"
   :widths: 10, 10, 40

   $f_relative_tol, |double|, "Relative tolerance to evaluate the yield function crossing."
   $stress_relative_tol, |double|, "Tolerance for the convergece of the integration algorithm."
   $n_max_iterations, |int|, "Maximum number of iterations for constitutive integration."
   $return_to_yield_surface, |0 or 1|, "Whether to apply a return to yield surface algorithm after integration convergence."
   $method, |string|, "Constitutive integration method. See :ref:`ASDPlasticMaterial3DIntegrationMethods` for options"
   $tangent_operator, |string|, "Tangent operator computation method. See :ref:`ASDPlasticMaterial3DTangentOperators` for options"

The default integration method is **Runge_Kutta_45_Error_Control** that uses the classical RK45 ODE integration algorithm employing a 4-th order prediction of the stress increment together with a 5-order prediction to estimate the integration error. In this scheme the strain increment provided by the element to the Gauss point is sub-divided into sub-increments, a process which is automated such that the provided **$stress_relative_tol** is met. This method is provided as a robust standard method which is applicable across all possible combinations of components, although there are possibly better approaches for specific cases which might become available in the future. 

The different parameters are activated depending on the integration algorithm selected. The *Forward_Euler* family algorithms only uses the **$return_to_yield_surface** parameter, while **Runge_Kutta_45_Error_Control** uses the rest. 

The **$f_relative_tol** parameter comes into play when the yield surface is being crossed, that is, when the previous (committed) stress is within the yield surface and the elastic prediction of the stress increment brings the stress state beyond the yield surface. In that case, an elastic increment occurs until the yield surface is touched which requires iterations with the Brent root finding algorithm. This is used by all currently available integration methods. 


.. _`ASDPlasticMaterial3DOtherFeatures`:

Other Features
""""""""""""""""""

.. admonition:: General parameters

    These parameters are defined for all models. 

    .. csv-table:: 
       :header: "Parameter", "Type", "Description"
       :widths: 10, 10, 40

       ``MassDensity``, scalar, Defines the material mass density :math:`\rho`. 
       ``InitialP0``, scalar, Defines the initial mean pressure at which material constants will be evaluated at the first step.  


.. admonition:: Enhanced Responses  (`setResponse` and `getResponse` behavior)

    * *Basic responses*. ``stresses`` for stress, ``strains`` for strains, and ``pstrains`` for plastic strains. 
    * *Enhanced stress measures*. ``eqpstrain`` for equivalent plastic strain, ``PStress`` for mean stress (:math:`p = (σ_{11}+σ_{22}+σ_{33})/3`), ``J2Stress`` for J2 invariant of stress.
    * *Enhanced strain measures*. ``VolStrain`` for volumetric strain (:math:`ε_v = ε_{11}+ε_{22}+ε_{33}`), ``J2Strain`` for J2 invariant of strain.
    * *Internal variables*. You can request any and all internal variables by their specific name as an output. 

.. admonition:: Advanced `setParameter` behavior 

   * *State variable updates*. Can update stress, strain, plasticStrain and their trial variants directly.
   * *Parameter updates*. Can update any model parameter by name using the generic parameter system.
   * *Special K0 operations*. ``K02D`` and ``K03D`` for setting K0 stress states in 2D/3D conditions.

.. admonition:: Internal Variable Management

   ``ASDPlasticMaterial3D`` provides methods to inspect and manage internal variables:
   
   * ``getInternalVariablesNames()`` - Returns list of internal variable names
   * ``getInternalVariableSizeByName(name)`` - Returns size of specified internal variable
   * ``getInternalVariableIndexByName(name)`` - Returns index of specified internal variable
   * ``setInternalVariableByName(name, size, values)`` - Sets internal variable values
   * ``getParameterNames()`` - Returns list of model parameter names
   * ``setParameterByName(name, value)`` - Sets model parameter value

Implementation details
""""""""""""""""""""""

``ASDPlasticMaterial3D`` is implemented using C++ template metaprogramming, with a header-only design and using the "eigen" C++ library for high-performance array operations. This design provides modularity and the ability to mix and match components to create new models, while also providing high-performance because runtime polymorphism is avoided. 

Key implementation features:
* **Template-based architecture**: Compile-time generation of optimized code for each material configuration
* **Eigen library**: High-performance linear algebra operations
* **Voigt notation**: Efficient tensor representation using 6-component vectors
* **Component modularity**: Easy extension with new yield functions, flow rules, elasticity models, and hardening functions


Example
"""""""

The following example defines an instance of ``ASDPlasticMaterial3D`` with a Drucker-Prager yield function, a constant dilatancy plastic-flow direction, elastic-isotropic elasticity law and linear hardening for both internal variables, using advanced integration options.

.. admonition:: TCL code  

    .. code-block:: tcl

        nDMaterial ASDPlasticMaterial3D 1 \
            DruckerPrager_YF \
            ConstantDilatancy_PF \
            LinearIsotropic3D_EL \
            BackStress(TensorLinearHardeningFunction):VonMisesRadius(ScalarLinearHardeningFunction): \
            Begin_Internal_Variables \
                VonMisesRadius 1. \
                BackStress 0. 0. 0. 0. 0. 0. \
            End_Internal_Variables \
            Begin_Model_Parameters \
                YoungsModulus 1e8 \
                PoissonsRatio 0.3 \
                TensorLinearHardeningParameter 1e6 \
                ScalarLinearHardeningParameter 1e4 \
                Dilatancy 0.02 \
                MassDensity 2000. \
            End_Model_Parameters \
            Begin_Integration_Options \
                method Runge_Kutta_45_Error_Control \
                tangent_operator Continuum \
                f_relative_tol 1e-8 \
                stress_relative_tol 1e-6 \
                n_max_iterations 50 \
                return_to_yield_surface 1 \
            End_Integration_Options

.. admonition:: Python code  

    .. code-block:: python

        ops.nDMaterial("ASDPlasticMaterial3D", 1, 
        "DruckerPrager_YF",
        "ConstantDilatancy_PF",
        "LinearIsotropic3D_EL",
        "BackStress(TensorLinearHardeningFunction):VonMisesRadius(ScalarLinearHardeningFunction):",
        "Begin_Internal_Variables",
            "VonMisesRadius", 1.,
            "BackStress", 0., 0., 0., 0., 0., 0.,
        "End_Internal_Variables",
        "Begin_Model_Parameters",
            "YoungsModulus", 1e8,
            "PoissonsRatio", 0.3,
            "TensorLinearHardeningParameter", 1e6,
            "ScalarLinearHardeningParameter", 1e4,
            "Dilatancy", 0.02,
            "MassDensity", 2000.,
        "End_Model_Parameters",
        "Begin_Integration_Options",
            "method", "Runge_Kutta_45_Error_Control",
            "tangent_operator", "Continuum",
            "f_relative_tol", 1e-8,
            "stress_relative_tol", 1e-6,
            "n_max_iterations", 50,
            "return_to_yield_surface", 1,
        "End_Integration_Options",
        )

Example: Using Enhanced Response Queries
""""""""""""""""""""""""""""""""""""""""

To access the enhanced response capabilities of ``ASDPlasticMaterial3D``, you can use recorders with the following response queries:

.. admonition:: TCL Recorder Example  

    .. code-block:: tcl

        # Basic responses
        recorder Node -file stress.out -time -node 1 -dof 1 2 3 stress
        recorder Node -file strain.out -time -node 1 -dof 1 2 3 strain
        
        # Enhanced stress measures  
        recorder Node -file p_stress.out -time -node 1 -dof 1 PStress
        recorder Node -file j2_stress.out -time -node 1 -dof 1 J2Stress
        recorder Node -file eq_pstrain.out -time -node 1 -dof 1 eqpstrain
        
        # Enhanced strain measures
        recorder Node -file vol_strain.out -time -node 1 -dof 1 VolStrain  
        recorder Node -file j2_strain.out -time -node 1 -dof 1 J2Strain
        
        # Internal variable by name
        recorder Node -file backstress.out -time -node 1 -dof 1 BackStress
        recorder Node -file radius.out -time -node 1 -dof 1 VonMisesRadius

Example: Parameter Updates During Analysis
""""""""""""""""""""""""""""""""""""""""

``ASDPlasticMaterial3D`` supports parameter updates during analysis:

.. admonition:: TCL Parameter Update  

    .. code-block:: tcl

        # Update model parameters
        setParameter 1 YoungsModulus 2e8
        setParameter 1 PoissonsRatio 0.25
        setParameter 1 ScalarLinearHardeningParameter 2e4
        
        # Update internal variables
        setParameter 1 VonMisesRadius 1.5
        
        # Update stress state (for restart or initialization)
        setParameter 1 stress [list 1e6 1e6 1e6 0 0 0]

Example: Integration Method Selection
""""""""""""""""""""""""""""""""""""""""

Different integration methods for specific applications:

.. admonition:: Robust Integration (Recommended for most cases)  

    .. code-block:: tcl

        Begin_Integration_Options
            method Runge_Kutta_45_Error_Control
            tangent_operator Continuum
            f_relative_tol 1e-8
            stress_relative_tol 1e-6
            n_max_iterations 50
            return_to_yield_surface 1
        End_Integration_Options

.. admonition:: Fast Integration (For large models)  

    .. code-block:: tcl

        Begin_Integration_Options
            method Forward_Euler_Subincrement  
            tangent_operator Elastic
            return_to_yield_surface 1
        End_Integration_Options

.. admonition:: High Accuracy Integration (For research)  

    .. code-block:: tcl

        Begin_Integration_Options
            method Backward_Euler_LineSearch
            tangent_operator Numerical_Algorithmic_SecondOrder
            f_relative_tol 1e-12
            stress_relative_tol 1e-10
            n_max_iterations 100
            return_to_yield_surface 1
        End_Integration_Options


Code Developed by: **José A. Abell** (UANDES, Chile and ASDEA), **Guido Camata** and **Massimo Petracca**  (ASDEA Software, Italy).