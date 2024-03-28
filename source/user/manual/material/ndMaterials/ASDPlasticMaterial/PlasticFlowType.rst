.. _PlasticFlowType:

Plastic Flow Directions
^^^^^^^^^^^^^^^^^^^^^^^

Specifies the direction of plastic flow :math:`\mathbf{m}` used to define the evolution of the plastic strain (see :ref:`ASDPlasticTheory`).


Plastic Flow Directions may define internal variables they need for their specification, as well as paramters. When specifying the ``ASDPlasticMaterial`` instance, once must provide the internal variables mentioned below, together with their hardening function, when defining the internal variables. 


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

      ``BackStress``, Rank-6 Tensor , :math:`\vec{\alpha}`,  "Backstress, definining the location in stress space for the axis of the Von-Mises cylinder. "

.. admonition:: Parameters required

   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70


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

   .. csv-table:: 
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70



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
      :header: "IV Name", "Type", "Symbol", "Description"
      :widths: 10, 10, 10, 70

      ``Dilatancy``, Scalar, :math:`D`, "Defines the rate of dilatancy with plastic flow. Positive values specify negative plastic volumetric change."
