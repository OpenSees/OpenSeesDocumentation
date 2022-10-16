.. _CentralDifference:

Central Difference
--------------------------------
.. function:: integrator CentralDifference 

.. note:: 
    * The calculation of :math:`U_{t+\Delta t}`, as shown below, is based on using the equilibrium equation at time t. For this reason the method is called an explicit integration method.
    * If there is no rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.
    * For stability, :math:`\frac{\Delta t}{T_n} < \frac{1}{\pi}` 


THEORY:
^^^^^^^^^

The Central difference approximations for velocity and acceleration:

    :math:` v_n = \frac{d_{n+1} - d_{n-1}}{2 \Delta t}`

    :math:` a_n = \frac{d_{n+1} - 2 d_n + d_{n-1}}{\Delta t^2}`

In the Central Difference method we determine the displacement solution at time :math:`t+\delta t` by considering the the eqilibrium equation for the finite element system in motion at time t:

    :math:`M \ddot U_t + C \dot U_t + K U_t = R_t`

which when using the above two expressions of becomes:

    :math:` \left ( \frac{1}{\Delta t^2} M + \frac{1}{2 \Delta t} C \right ) U_{t+\Delta t} = R_t - \left (K - \frac{2}{\Delta t^2}M \right )U_t - \left (\frac{1}{\Delta t^2}M - \frac{1}{2 \Delta t} C \right) U_{t-\Delta t} `