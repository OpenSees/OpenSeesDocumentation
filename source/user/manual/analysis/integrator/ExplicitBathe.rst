.. _ExplicitBathe:

ExplicitBathe
-------------
.. function:: integrator ExplicitBathe $p $compute_critical_timestep?

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $p, |float|, Damping parameter (0 < p < 1, typically 0.54)
   $compute_critical_timestep, |int|, Optional flag to compute critical timestep (0 or 1)

.. note::
   * The method is second-order accurate and explicit.
   * Only mass matrix is assembled on RHS (no tangent matrix required).
   * Critical time step is approximately 2× larger than central difference method.
   * For stability: :math:`\Delta t \leq \frac{2}{\omega_{max}}`
   * Typical p values: 0.54-0.95 for optimal numerical damping.

Theory
^^^^^^

The ExplicitBathe method is a two-step explicit integration scheme with built-in numerical damping. The method performs two sub-steps per time step:

1. First step: :math:`t \rightarrow t + p\Delta t`
2. Second step: :math:`t + p\Delta t \rightarrow t + \Delta t`

The integration coefficients are computed from the damping parameter p:

.. math::

   q_1 = \frac{1 - 2p}{2p(1-p)}

   q_2 = 0.5 - p \cdot q_1

   q_0 = -q_1 - q_2 + 0.5

The method offers enhanced stability compared to standard central difference, with a critical time step approximately twice as large. The parameter p controls numerical damping, with higher values providing more damping but reduced accuracy.

.. admonition:: Example 

   1. **Tcl Code**

   .. code-block:: tcl

      integrator ExplicitBathe 0.54

   2. **Python Code**

   .. code-block:: python

       integrator('ExplicitBathe', 0.54)

.. [Noh2013] Noh, G., & Bathe, K.J. (2013). "An explicit time integration scheme for the analysis of wave propagations." Computers & Structures, 129, 178-193.

Code Developed by: |jaabell|
