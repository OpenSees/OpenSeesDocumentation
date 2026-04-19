.. _`YieldFunctionType`:

Yield Functions
^^^^^^^^^^^^^^^

Specifies the shape of the yield surface, i.e. locus of points in stress-space where the response of the material is linear. Points outside of yield surface are not allowed. Yield surfaces can have parameters and internal variables which define its shape and location. 

Yield Functions may define internal variables they need for their specification, as well as paramters. When specifying ``ASDPlasticMaterial`` or ``ASDPlasticMaterial3D`` instance, one must provide internal variables mentioned below, together with their hardening function. 

Yield functions are also responsible for providing their stress-derivative (:math:`\mathbf{n} = \partial f / \partial \boldsymbol{\sigma}`) as well as computing hardening term :math:`H` in the plastic multiplier (see :ref:`ASDPlasticTheory`). 

.. note::
   When using :ref:`ASDPlasticMaterial3D`, yield function internal variables can be accessed directly using enhanced response queries. This provides detailed insight into material state evolution during analysis.

Available functions:


.. _VonMises_YF:

VonMises_YF
"""""""""""

Defines a yield surface which corresponds to the `Von Mises Yield Criterion <https://en.wikipedia.org/wiki/Von_Mises_yield_criterion>`_. Its definition is:

.. math::
   \newcommand{\vec}[1]{\boldsymbol{#1}}
   \newcommand{\state}{\sigma, \left\lbrace iv \right\rbrace, \left\lbrace param \right\rbrace }
   \newcommand{\matorvec}[2]{
    \left[\begin{array}{#1}
        #2
    \end{array}\right]
    }
   f(\vec{\sigma}) = \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha}) } - \sqrt{ \dfrac{2}{3}} k

   \vec{s} = \vec{\sigma} - p \vec{I}

Where :math:`p = -(\sigma_{11} + \sigma_{22} + \sigma_{33})/3` is the mean stress (positive in compression), and :math:`\vec{I}` is the Kronecker delta in Voigt notation (:math:`\vec{I} = \matorvec{cccccc}{1 & 1 & 1 & 0 & 0 & 0}^T`). Finally, :math:`\vec{s}` is the deviatoric part of the stress vector in Voigt notation. 

.. admonition:: Internal variables defined

   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``BackStress``, Rank-6 Tensor , :math:`\vec{\alpha}`,  "Backstress, definining the location in stress space for the axis of the Von-Mises cylinder. "
      ``VonMisesRadius``, Scalar , :math:`k`,  "Shear strength, definining the radius of the Von-Mises cylinder in stress space. "

.. admonition:: Parameters required

   None required for the yield function itself. Parameters are defined by the internal variable hardening functions and elasticity model.

.. admonition:: Usage in ASDPlasticMaterial3D

   When using VonMises_YF with :ref:`ASDPlasticMaterial3D`, you can access the internal variables using enhanced response queries:
   
   * ``VonMisesRadius`` - Current radius of the yield surface
   * ``BackStress`` - Current backstress tensor (6 components in Voigt notation)
   
   These can be recorded using:
   
   .. code-block:: tcl
   
       recorder Node -file vonmises_radius.out -time -node 1 -dof 1 VonMisesRadius
       recorder Node -file backstress.out -time -node 1 -dof 1 BackStress


.. _DruckerPrager_YF:

DruckerPrager_YF
""""""""""""""""


Defines a yield surface which corresponds to the `Drucker-Prager Yield Criterion <https://en.wikipedia.org/wiki/Drucker%E2%80%93Prager_yield_criterion>`_. Its definition is:

.. math::
   f(\vec{\sigma}) = \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha}) } - \sqrt{ \dfrac{2}{3}} k p

Where all symbols are as before. In this case note that :math:`k`, defines the slope of the opening of the Drucker-Prager cone with respect to  :math:`p`, thus now the radius of the cone at a given confinement is :math:`kp`.

.. admonition:: Internal variables defined

   It uses the same variables as the Von-Mises yield function, but the ``VonMisesRadius`` is now unitless and should be defined with respect to a reference confinement. 

   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``BackStress``, Rank-6 Tensor , :math:`\vec{\alpha}`,  "Backstress, definining the location in stress space for the axis of the Drucker-Prager cone. "
      ``VonMisesRadius``, Scalar , :math:`k`,  "Shear strength at reference confinement, definining the radius of the DruckerPrager cone in stress space as  :math:`kp`"

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``Dilatancy``, Scalar, :math:`D`, "Dilatancy parameter from plastic flow model (if used)"

.. admonition:: Usage in ASDPlasticMaterial3D

   DruckerPrager_YF with :ref:`ASDPlasticMaterial3D` provides access to:
   
   * ``VonMisesRadius`` - Current strength parameter
   * ``BackStress`` - Current backstress tensor
   
   Enhanced stress measures are particularly useful:
   
   .. code-block:: tcl
   
       recorder Node -file p_stress.out -time -node 1 -dof 1 PStress
       recorder Node -file j2_stress.out -time -node 1 -dof 1 J2Stress


