.. _ExplicitDifference:

Explicit Difference
--------------------------------
.. function:: integrator Explicitdifference  

.. note:: 
    * When using Rayleigh damping, the damping ratio of high vibration modes is overrated, and the critical time step size will be much smaller. Hence Modal damping is more suitable for this method.
    * There should be no zero element on the diagonal of the mass matrix when using this method.
    * Diagonal solver should be used when lumped mass matrix is used because the equations are uncoupled.
    * For stability :math:`\delta t \leq (\sqrt{\xi^2 +1} - \xi) \frac{2}{\omega}` 


.. admonition:: Example 

   1. **Tcl Code**

   .. code-block:: tcl

      integrator Explicitdifference 

   2. **Python Code**

   .. code-block:: python

       integrator('ExplicitDifference')
