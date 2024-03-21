.. _ElasticityType:

Elasticity Types
^^^^^^^^^^^^^^^^

These components define the stress-strain relationship for the linear part of the model (see :ref:`ASDPlasticTheory`). 

.. math::
   \newcommand{\vec}[1]{\boldsymbol{#1}}
   \vec{\sigma} = \vec{E} \vec{\epsilon}

Where the operator :math:`\vec{E}` may depend on the material state, parameters, etc. 


.. _LinearIsotropic3D_EL:
LinearIsotropic3D_EL
""""""""""""""""""""

A classic!

.. math::
   \vec{E}\,=\,{\frac {E}{(1+\nu )(1-2\nu )}}{\begin{bmatrix}1-\nu &\nu &\nu &0&0&0\\\nu &1-\nu &\nu &0&0&0\\\nu &\nu &1-\nu &0&0&0\\0&0&0&{\frac {1-2\nu }{2}}&0&0\\0&0&0&0&{\frac {1-2\nu }{2}}&0\\0&0&0&0&0&{\frac {1-2\nu }{2}}\end{bmatrix}}


.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``YoungsModulus``, scalar, :math:`E`, Young's modulus
      ``PoissonsRatio``, scalar, :math:`\nu`, Poisson's ratio

.. _DuncanChang_EL:
DuncanChang_EL
""""""""""""""

This is a hypoelastic model that features pressure dependent behavior. It is composed of an isotropic elastic model where the Young's modulus has the following dependency on the maximum principal stress :math:`\sigma_3` (it is assumed that :math:`\sigma_1 \leq \sigma_2 \leq \sigma_3 < 0`).

.. math::
   E(\sigma_3) = E_{ref} \cdot p_{ref} \cdot \left(\dfrac{\vert \sigma_3 \vert}{ p_{ref}} \right)^n

Where :math:`E_{ref}` (dimensionless) specifies the Young's modulus at reference pressure :math:`p_{ref}` and :math:`n` is a material constant. A cut-off maximum confinement pressure :math:`\sigma_{3max}` at which the Young's modulus will be evaluated should the confinement be greater than that value. 

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``ReferenceYoungsModulus``, scalar, :math:`E_{ref}`, Dimensionless reference Young's modulus at reference pressure :math:`p_{ref}`.
      ``PoissonsRatio``, scalar, :math:`\nu`, Poisson's ratio
      ``ReferencePressure``, scalar, :math:`p_{ref}`, Reference pressure for the definition of Young's modulus.
      ``DuncanChang_MaxSigma3``, scalar, :math:`\sigma_{3max}`, Maximum confinement stress.
      ``DuncanChang_n``, scalar, :math:`\nu`, Exponent for Duncan-Chang law. 
