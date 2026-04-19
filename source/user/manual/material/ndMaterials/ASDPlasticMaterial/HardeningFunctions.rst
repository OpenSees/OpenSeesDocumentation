.. _`HardeningFunctions`:

Hardening Functions
^^^^^^^^^^^^^^^^^^

Internal variables evolve accoding with their own laws to provide plastic hardening to the constitutive model. These laws are specified as hardening functions that specify an ODE for the evolution of the internal variable. Two types of internal variable are considered: scalar-valued and tensor-valued internal variables. These evolve in the following manner:
.. math::
   \newcommand{\vec}[1]{\boldsymbol{#1}}
   \newcommand{\state}{\sigma, \left\lbrace iv \right\rbrace, \left\lbrace param \right\rbrace }

   s^{\text{trial}} = s^{\text{commit}} + \Delta \lambda  h_s(\state)

   \vec{T}^{\text{trial}} = \vec{T}^{\text{commit}} + \Delta \lambda  \vec{h}_T(\state)

Where :math:`s` is a scalar-valued internal variable and :math:`\vec{T}` is a tensor-valued. These functions are used to define the hardening term in the plastic multiplier (see :ref:`ASDPlasticTheory`). 

.. note::
   When using :ref:`ASDPlasticMaterial3D`, hardening function parameters can be updated during analysis using ``setParameter``. Internal variables can be accessed by name for monitoring and recording. This enables real-time tracking of hardening evolution and allows for modeling of complex material behavior including state-dependent hardening, temperature effects, or damage-coupled hardening laws.

Available functions:


.. _ScalarValuedHF:

Hardening Functions for Scalar-Valued Internal Variables
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**ScalarLinearHardeningFunction**

Provides linear hardening for the scalar variable, as a function of the plastic flow direction :

.. math::
   h_s(\state) = H \cdot \sqrt{  (2/3) \vec{m} \cdot \vec{m} } 


Where :math:`\vec{m}` is the plastic flow direction computed at the current state. 

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

       ``ScalarLinearHardeningParameter``, scalar, :math:`H`, Linear hardening constant (Pa per unit plastic strain)

.. admonition:: Usage in ASDPlasticMaterial3D

   When used with :ref:`ASDPlasticMaterial3D`, ScalarLinearHardeningFunction provides:
   
   * Linear increase/decrease of scalar variable with plastic deformation
   * Isotropic hardening/softening behavior
   * Simple calibration with single parameter
   
   Monitor scalar internal variable evolution:
   
   .. code-block:: tcl
   
       recorder Node -file radius.out -time -node 1 -dof 1 VonMisesRadius
       # Update hardening parameter during analysis
       setParameter 1 ScalarLinearHardeningParameter 5e6


.. _TensorValuedHF:

Hardening Functions for Tensor-Valued Internal Variables
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**TensorLinearHardeningFunction**

Provides linear hardening for the tensor variable, as a function of the deviatoric plastic flow direction :

.. math::

   h_T(\state) = H \vec{m}_{dev}


Where :math:`\vec{m}_{dev}` is the deviatoric part of the plastic flow direction computed at the current state. 

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

       ``TensorLinearHardeningParameter``, scalar, :math:`H`, Linear hardening constant (dimensionless)

.. admonition:: Usage in ASDPlasticMaterial3D

   When used with :ref:`ASDPlasticMaterial3D`, TensorLinearHardeningFunction provides:
   
   * Linear evolution of backstress tensor
   * Kinematic hardening behavior
   * Translation of yield surface in stress space
   
   The backstress evolves in the direction of deviatoric plastic flow, providing Bauschinger effect modeling.
   
   Monitor tensor internal variable evolution:
   
   .. code-block:: tcl
   
       recorder Node -file backstress.out -time -node 1 -dof 1 2 3 4 5 6 BackStress
       # Update hardening parameter during analysis
       setParameter 1 TensorLinearHardeningParameter 0.01

**ArmstrongFrederickHardeningFunction**

A type of hardening with saturation.

.. math::
   h_T(\state) = (2 / 3) h_a \vec{m}_{dev} - c_r \sqrt{  (2/3) \vec{m}_{dev} \cdot \vec{m}_{dev} } \cdot  \vec{T}


Where :math:`\vec{m}_{dev}` is the deviatoric part of the plastic flow direction computed at the current state. Model paramters :math:`h_a` and :math:`c_r`  specify the maximum (saturation) value and the saturation rate. The saturation value for the internal variable will be such that:

.. math::
   \Vert \vec{T} \Vert = \sqrt{\dfrac{2}{3}} \dfrac{h_a}{c_r}

Setting :math:`c_r = 0` results in linear hardening. 

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

       ``AF_ha``, scalar, :math:`h_a`, Model constant for the linear part of the hardening model. Controls the rate of saturation (Pa).
       ``AF_cr``, scalar, :math:`c_r`, Model constant for saturation part of the hardening model. Controls saturation value (dimensionless).

.. admonition:: Usage in ASDPlasticMaterial3D

   When used with :ref:`ASDPlasticMaterial3D`, ArmstrongFrederickHardeningFunction provides:
   
   * Non-linear kinematic hardening with saturation
   * Dynamic recovery term for realistic cyclic response
   * Bauschinger effect modeling with memory
   
   The hardening combines:
   
   * **Linear term**: (2/3) :math:`h_a \vec{m}_{dev}` - drives hardening
   * **Recovery term**: :math:`-c_r \sqrt{(2/3) \vec{m}_{dev} \cdot \vec{m}_{dev}} \cdot \vec{T}` - provides saturation
   
   Setting :math:`c_r = 0` reduces to linear kinematic hardening.
   
   The saturation value for the internal variable will be:
   
   .. math::
      \Vert \vec{T} \Vert = \sqrt{\dfrac{2}{3}} \dfrac{h_a}{c_r}
   
   Monitor non-linear hardening:
   
   .. code-block:: tcl
   
       recorder Node -file backstress.out -time -node 1 -dof 1 2 3 4 5 6 BackStress
       recorder Node -file eqpstrain.out -time -node 1 -dof 1 eqpstrain
       # Update hardening parameters during analysis
       setParameter 1 AF_ha 1e8
       setParameter 1 AF_cr 100

