.. _`HardeningFunctions`:

Hardening Functions
^^^^^^^^^^^^^^^^^^^

Internal variables evolve accoding with their own laws to provide plastic hardening to the constitutive model. These laws are specified as hardening functions that specify an ODE for the evolution of the internal variable. Two types of internal variable are considered: scalar-valued and tensor-valued internal variables. These evolve in the following manner:

.. math::
   \newcommand{\vec}[1]{\boldsymbol{#1}}
   \newcommand{\state}{\sigma, \left\lbrace iv \right\rbrace, \left\lbrace param \right\rbrace }

   s^{\text{trial}} = s^{\text{commit}} + \Delta \lambda  h_s(\state)

   \vec{T}^{\text{trial}} = \vec{T}^{\text{commit}} + \Delta \lambda  \vec{h}_T(\state)

Where :math:`s` is a scalar-valued internal variable and :math:`\vec{T}` is tensor-valued. These functions are used to define the hardening term in the plastic multiplier (see :ref:`ASDPlasticTheory`).

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
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``ScalarLinearHardeningParameter``, scalar, :math:`H`, Linear hardening constant


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
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``TensorLinearHardeningFunction``, scalar, :math:`H`, Linear hardening constant

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
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``AF_ha``, scalar, :math:`h_a`, Model constant for the linear part of the hardening model. Controls the rate of saturation.
      ``AF_cr``, scalar, :math:`c_r`, Model constant for saturation part of the hardening model. Controls the saturation value. 