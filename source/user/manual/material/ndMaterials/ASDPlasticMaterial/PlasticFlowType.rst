.. _PlasticFlowType:

Plastic Flow Directions
^^^^^^^^^^^^^^^^^^^^^^

Specifies the direction of plastic flow :math:`\mathbf{m}` used to define evolution of the plastic strain (see :ref:`ASDPlasticTheory`). The plastic flow direction determines how plastic strain components develop and influences both volumetric and deviatoric plastic deformation.

Plastic Flow Directions may define internal variables they need for their specification, as well as paramters. When specifying the ``ASDPlasticMaterial`` or ``ASDPlasticMaterial3D`` instance, one must provide internal variables mentioned below, together with their hardening function, when defining internal variables. 

.. note::
   :ref:`ASDPlasticMaterial3D` provides enhanced monitoring of plastic flow effects through specialized response queries like ``VolStrain`` and ``J2Strain`` to track volumetric and deviatoric plastic deformation separately.

Available functions:


.. _`VonMises_PF`:
VonMises_PF
"""""""""""
Defines a plastic flow direction derived from the `Von Mises Yield Criterion <https://en.wikipedia.org/wiki/Von_Mises_yield_criterion>`_. Its definition. It is the stress-derivative of the :ref:`VonMises_YF`.

.. math::
   \newcommand{\vec}[1]{\boldsymbol{#1}}
   \mathbf{m} = \dfrac{\partial f}{\partial \vec{\sigma}} = \dfrac{\vec{s} - \vec{\alpha} }{ \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha})}}

.. admonition:: Internal variables defined

   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

       ``BackStress``, Rank-6 Tensor , :math:`\vec{\alpha}`,  "Backstress, definining location in stress space for axis of Von-Mises cylinder. "

.. admonition:: Parameters required

   None required for VonMises plastic flow. Parameters are inherited from associated yield function and hardening functions.

.. admonition:: Usage in ASDPlasticMaterial3D

   When using VonMises_PF with :ref:`ASDPlasticMaterial3D`, the plastic flow direction is automatically computed as the stress derivative of the Von Mises yield function. This provides:
   
   * Associated plastic flow (flow rule equals yield function gradient)
   * No volumetric plastic strain (isochoric plastic deformation)
   * Purely deviatoric plastic response
   
   You can monitor plastic strain components:
   
   .. code-block:: tcl
   
       recorder Node -file plastic_strain.out -time -node 1 -dof 1 2 3 4 5 6 pstrain


.. _`DruckerPrager_PF`:
DruckerPrager_PF
""""""""""""""""
Defines a plastic flow direction derived from the `Drucker-Prager Yield Criterion <https://en.wikipedia.org/wiki/Drucker%E2%80%93Prager_yield_criterion>`_.  It is the stress-derivative of the :ref:`DruckerPrager_YF`.

.. math::

        \mathbf{m} = \dfrac{\partial f}{\partial \vec{\sigma}} = \dfrac{\vec{s} - \vec{\alpha} }{ \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha})}} - \dfrac{\sqrt{2/3}k}{3} \vec{I} ;

.. admonition:: Internal variables defined

   It uses the same variables as the Von-Mises yield function, but the ``VonMisesRadius`` is now unitless and should be defined with respect to a reference confinement. 

   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``BackStress``, Rank-6 Tensor , :math:`\vec{\alpha}`,  "Backstress, definining the location in stress space for the axis of the Drucker-Prager cone. "
      ``VonMisesRadius``, Scalar , :math:`k`,  "Shear strength at reference confinement, definining the radius of the DruckerPrager cone in stress space as  :math:`kp`"

.. admonition:: Parameters required

   None required for DruckerPrager plastic flow. Uses parameters from yield function.

.. admonition:: Usage in ASDPlasticMaterial3D

   DruckerPrager_PF provides non-associated flow when used with pressure-sensitive yield functions. Key characteristics:
   
   * Pressure-dependent plastic flow (includes volumetric component)
   * Associated flow with Drucker-Prager yield surface
   * Suitable for geomaterials exhibiting dilatancy or contractancy
   
   Monitor volumetric plastic strain:
   
   .. code-block:: tcl
   
       recorder Node -file vol_strain.out -time -node 1 -dof 1 VolStrain


.. _`ConstantDilatancy_PF`:
ConstantDilatancy_PF
""""""""""""""""""""

Von-Mises PF provides no volumetric change (dilatancy) during plasticity. On the other hand Drucker-Prager PF provides a constant negative volumetric change which is proportional to the current value of the :math:`k` parameter. This PF defines a controllable dilatancy during plasticity by specifying a constant dilatancy coeficient :math:`D`. 


.. math::

        \mathbf{m} = \dfrac{\partial f}{\partial \vec{\sigma}} = \dfrac{\vec{s} - \vec{\alpha} }{ \sqrt{ (\vec{s} - \vec{\alpha}) \cdot (\vec{s} - \vec{\alpha})}} - \dfrac{D}{3} \vec{I} ;

.. admonition:: Internal variables defined


   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``BackStress``, Rank-6 Tensor , :math:`\vec{\alpha}`,  "Backstress, definining the location in stress space for the axis of the Drucker-Prager cone. "

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "Parameter Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

       ``Dilatancy``, Scalar, :math:`D`, "Defines the rate of dilatancy with plastic flow. Positive values specify negative plastic volumetric change."

.. admonition:: Usage in ASDPlasticMaterial3D

   ConstantDilatancy_PF provides non-associated flow with controllable dilatancy. This is particularly useful for:
   
   * Concrete and rock materials (positive dilatancy)
   * Dense sands (positive dilatancy initially, then contractancy)
   * Loose sands (continuous contractancy)
   
   Monitor dilatancy effects:
   
   .. code-block:: tcl
   
       recorder Node -file vol_strain.out -time -node 1 -dof 1 VolStrain
       recorder Node -file j2_strain.out -time -node 1 -dof 1 J2Strain


