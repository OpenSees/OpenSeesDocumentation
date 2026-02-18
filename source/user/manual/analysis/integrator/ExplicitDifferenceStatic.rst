.. _ExplicitDifferenceStatic:

ExplicitDifferenceStatic
------------------------
.. function:: integrator ExplicitDifferenceStatic

.. note::
   * Uses leap-frog integration with velocities at half time steps.
   * FLAC-style local non-viscous damping (α = 0.59) for pseudo-static analysis.
   * Only mass matrix is required (no tangent matrix assembly).
   * Velocity sign memory prevents chatter near zero velocity.
   * For stability: :math:`\Delta t \leq \frac{2}{\omega_{max}}`
   * Suitable for quasi-static and dynamic problems with adaptive damping.

Theory
^^^^^^

The ExplicitDifferenceStatic method is an explicit difference scheme with FLAC-style local non-viscous damping. The method uses a leap-frog approach where:

* Velocities are defined at half time steps: :math:`v_{n+1/2}`
* Displacements are defined at full time steps: :math:`d_n`

The damping force uses an adaptive FLAC-style approach:

.. math::

   F_{damping} = -\alpha \cdot |F_{unbalanced}| \cdot sign(v)

where α = 0.59 by default. The method includes velocity sign memory with a deadband (1e-4) to prevent numerical chatter when velocities approach zero.

The central difference equations are:

.. math::

   v_{n+1/2} = v_{n-1/2} + \Delta t \cdot a_n

   d_{n+1} = d_n + \Delta t \cdot v_{n+1/2}

This integrator is particularly effective for quasi-static analysis and problems where adaptive local damping is beneficial, such as rock mechanics and soil-structure interaction problems.

.. admonition:: Example 

   1. **Tcl Code**

   .. code-block:: tcl

      integrator ExplicitDifferenceStatic

   2. **Python Code**

   .. code-block:: python

       integrator('ExplicitDifferenceStatic')

.. [Cundall1987] Cundall, P.A. (1987). "Distinct Element Models of Rock and Soil Structure." In Analytical and Computational Methods in Engineering Rock Mechanics, 129-163.

Code Developed by: |jaabell|
