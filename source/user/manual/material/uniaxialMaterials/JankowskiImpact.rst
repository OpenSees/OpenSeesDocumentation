.. _JankowskiImpact :

Jankowski Impact Material
^^^^^^^^^^^^^^^^^^

This command is used to construct the uniaxial Jankowski Impact Material 

.. function:: uniaxialMaterial JankowskiImpact  $matTag $Kh $xi $Meff $gap <$n>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $Kh, |float|,  nonlinear Hertz contact stiffness.
   $xi, |float|, impact damping ratio.
   $Meff, |float|, effective mass.
   $gap, |float|, initial gap
   $n, |float|, indentation exponent (optional with default value of  1.5).

.. note::

   This material is implemented as a compression-only gap material, so $gap should be input as a negative value.

.. Description::
This material model follows the constitutive law

  .. math:: f_c(t) = \left\{ \begin{array}{ }k_h (\delta(t)-g)^n + c_J(t) \dot{\delta}(t) & \quad \dot{\delta}(t) > 0 \\ k_h (\delta(t)-g)^n                 & \quad {\dot{\delta(t)} \leq 0} \end{array}\right.

where t is time, :math:`f_c (t)`  is the contact force, :math:`k_h` is the nonlinear Hertz contact stiffness ($Kh), :math:`\delta(t)` is the indentation, g is the initial gap ($gap), n is the indentation exponent ($n), and :math:`\dot{\delta}(t)` is the indentation velocity. Damping is only applied during the approach phase, when :math:`\delta (t) > 0`. The damping coefficient :math:`c_J`` is computed as

   .. math:: c_h = 2 \xi_j \sqrt{ m_{\textrm{eff}} k_h (\delta(t) -g)^{n-1}}

where :math:`m_{\textrm{eff}}` is the effective mass of the system ($Meff), computed using the masses of the coliding bodies :math:`m_1` and :math:`m_2`:
   
   .. math:: m_{\textrm{eff}} = \frac{m_1 m_2}{m_1 + m_2}
      
The damping ratio :math:`\xi_j` ($xi) is usually related to the coefficient of restitution, represented by e. The recommended form of :math:`\xi_j` is

   .. math:: \xi = \frac{9\sqrt{5}}{2} (\frac{1-e^2}{e(e(9\pi-16)+16)})

Response of the JankowskiImpact  material during impact:

   .. figure:: figures/JankowskiImpact_responses.png
      :align: center
      :figclass: align-center

Note that the flat displacement from 0 to roughly minus 0.01 inch displacement is caused by the gap parameter.

Code Developed by: Patrick J. Hughes, UC San Diego


.. [Jankowski2005]  Non-linear viscoelastic modelling of earthquake-induced structural pounding. Earthquake Engineering and Structural Dynamics 2005; 34(6): 595–611. DOI: 10.1002/eqe.434.

.. [Jankowski2006] Analytical expression between the impact damping ratio and the coefficient of restitution in the non-linear viscoelastic model of structural pounding. Earthquake Engineering and Structural Dynamics 2006; 35(4): 517–524. DOI: 10.1002/eqe.537.

.. [Jankowski2007] Jankowski R. Theoretical and experimental assessment of parameters for the non-linear viscoelastic model of structural pounding. Journal of Theoretical and Applied Mechanics (Poland) 2007.

.. [Hughes2020]  Hughes PJ, Mosqueda G. Evaluation of uniaxial contact models for moat wall pounding simulations. Earthquake Engineering and Structural Dynamics 2020(March): 12–14. DOI: 10.1002/eqe.3285.