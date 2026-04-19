.. _ElasticityType:

Elasticity Types
^^^^^^^^^^^^^^^

These components define the stress-strain relationship for the linear part of the model (see :ref:`ASDPlasticTheory`). 
.. math::
   \newcommand{\vec}[1]{\boldsymbol{#1}}
   \vec{\sigma} = \vec{E} \vec{\epsilon}
Where the operator :math:`\vec{E}` may depend on the material state, parameters, etc. 

.. note::
   When using :ref:`ASDPlasticMaterial3D`, elastic parameters can be updated during analysis using the ``setParameter`` command, allowing for simulation of materials with time-dependent or state-dependent elastic properties. This is particularly useful for modeling damage effects, temperature-dependent stiffness, or staged construction processes.


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

       ``YoungsModulus``, scalar, :math:`E`, Young's modulus (Pa or psi)
       ``PoissonsRatio``, scalar, :math:`\nu`, Poisson's ratio (dimensionless, typically 0.0-0.5)

.. admonition:: Usage in ASDPlasticMaterial3D

   LinearIsotropic3D_EL provides the fundamental elastic behavior for most engineering materials. With :ref:`ASDPlasticMaterial3D`:
   
   * Constant elastic properties throughout analysis
   * Efficient computation with closed-form tangent
   * Suitable for metals, concrete at small strains, and other linear elastic materials
   
   Monitor elastic behavior:
   
   .. code-block:: tcl
   
       # Update elastic parameters during analysis
       setParameter 1 YoungsModulus 3e10
       setParameter 1 PoissonsRatio 0.2

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
       ``PoissonsRatio``, scalar, :math:`\nu`, Poisson's ratio (dimensionless)
       ``ReferencePressure``, scalar, :math:`p_{ref}`, Reference pressure for the definition of Young's modulus (Pa).
       ``DuncanChang_MaxSigma3``, scalar, :math:`\sigma_{3max}`, Maximum confinement stress (Pa).
       ``DuncanChang_n``, scalar, :math:`n`, Exponent for Duncan-Chang law (typically 0.2-1.0).

.. admonition:: Usage in ASDPlasticMaterial3D

   DuncanChang_EL provides pressure-dependent elastic behavior, particularly useful for:
   
   * Soil materials with stiffness increasing with confinement
   * Rock materials exhibiting non-linear elastic response
   * Interfaces and joints with pressure-dependent behavior
   
   The Young's modulus varies with minimum principal stress :math:`\sigma_3` (compression negative):
   
   .. math::
      E(\sigma_3) = E_{ref} \cdot p_{ref} \cdot \left(\dfrac{\vert \sigma_3 \vert}{ p_{ref}} \right)^n
   
   Monitor pressure-dependent response:
   
   .. code-block:: tcl
   
       recorder Node -file pressure.out -time -node 1 -dof 1 PStress
       recorder Node -file j2_stress.out -time -node 1 -dof 1 J2Stress

