Newmark Method
-------------------

This command is used to construct a Newmark integrator object.

.. function:: integrator Newmark $gamma $beta

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $gamma, |float|,  :math:`\gamma` factor
   $beta, |float|, :math:`\beta` factor

.. note::
   1. If the accelerations are chosen as the unknowns and :math:`\beta` is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.
   
   2. Two common sets of choices are:
      
      Average Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{4}`)
      
      Linear Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{6}`)
   
   3. :math:`\gamma > \frac{1}{2}` results in numerical damping proportional to :math:`\gamma - \frac{1}{2}`
   
   4. The method is second order accurate if and only if :math:`\gamma = \frac{1}{2}`
   
   5. The method is conditionally stable for :math:`\beta >= \frac{\gamma}{2} >= \frac{1}{4}`


Theory
^^^^^^

The Newmark method is a one step implicit method for solving the transient problem, represented by the residual for the momentum equation:

.. math::
   
   R_{t + \Delta t} = F_{t+\Delta t}^{ext} - M \ddot U_{t + \Delta t} - C \dot U_{t + \Delta t} + F(U_{t + \Delta t})^{int}

Using the Taylor series approximation of :math:`U_{t+\Delta t}` and :math:`\dot U_{t+\Delta t}`:

.. math::

   U_{t+\Delta t} = U_t + \Delta t \dot U_t + \frac{\Delta t^2}{2} \ddot U_t + \frac{\Delta t^3}{6} \dddot U_t + \cdots

   \dot U_{t+\Delta t} = \dot U_t + \Delta t \ddot U_t + \frac{\Delta t^2}{2} \dddot U_t + \cdots

Newton truncated these using the following:

.. math::
   
   U_{t+\Delta t} = u_t + \Delta t \dot U_t + \frac{\Delta t^2}{2} \ddot U + \beta {\Delta t^3} \dddot U

   \dot U_{t + \Delta t} = \dot U_t + \Delta t \ddot U_t + \gamma \Delta t^2 \dddot U

in which he assumed linear acceleration within a time step, i.e.,

.. math::
   \dddot U = \frac{{\ddot U_{t+\Delta t}} - \ddot U_t}{\Delta t}

which results in the following expressions:

.. math::
   U_{t+\Delta t} = U_t + \Delta t \dot U_t + [(0.5 - \beta) \Delta t^2] \ddot U_t + [\beta \Delta t^2] \ddot U_{t+\Delta t}

   \dot U_{t+\Delta t} = \dot U_t + [(1-\gamma)\Delta t] \ddot U_t + [\gamma \Delta t ] \ddot U_{t+\Delta t}

The variables :math:`\beta` and :math:`\gamma` are numerical parameters that control both the stability of the method and the amount of numerical damping introduced into the system by the method. For :math:`\gamma=\frac{1}{2}` there is no numerical damping; for :math:`\gamma>=\frac{1}{2}` numerical damping is introduced. Two well known and commonly used cases are:

   1. Average Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{4}`)

   2. Constant Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{6}`)

The linearization of the Newmark equations gives:

.. math::
   dU_{t+\Delta t}^{i+1} = \beta \Delta t^2 d \ddot U_{t+\Delta t}^{i+1}

   d \dot U_{t+\Delta t}^{i+1} = \gamma \Delta t \ddot U_{t+\Delta t}^{i+1}

which gives the update formula when displacement increment is used as unknown in the linearized system as:

.. math::
   U_{t+\Delta t}^{i+1} = U_{t+\Delta t}^i + dU_{t+\Delta t}^{i+1}

   \dot U_{t+\Delta t}^{i+1} = \dot U_{t+\Delta t}^i + \frac{\gamma}{\beta \Delta t}dU_{t+\Delta t}^{i+1}

   \ddot U_{t+\Delta t}^{i+1} = \ddot U_{t+\Delta t}^i + \frac{1}{\beta \Delta t^2}dU_{t+\Delta t}^{i+1}

The linearization of the momentum equation using the displacements as the unknowns leads to the following linear equation:

.. math::
   K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = R_{t+\Delta t}^i

where,

.. math::
   K_{t+\Delta t}^{*i} = K_t + \frac{\gamma}{\beta \Delta t} C_t + \frac{1}{\beta \Delta t^2} M

and,

.. math::
   R_{t+\Delta t}^i = F_{t + \Delta t}^{ext} - F(U_{t + \Delta t}^{i-1})^{int} - C \dot U_{t+\Delta t}^{i-1} - M \ddot U_{t+ \Delta t}^{i-1}


.. admonition:: Example 

   The following example shows how to construct a Newmark Integrator.

   1. **Tcl Code**

   .. code-block:: tcl

      integrator Newmark 0.5 0.25

   2. **Python Code**

   .. code-block:: python

      integrator('Newmark', 0.5, 0.25)


.. [Newmark1959] Newmark, N.M. "A Method of Computation for Structural Dynamics" ASCE Journal of Engineering Mechanics Division, Vol 85. No EM3, 1959.


Code Developed by: |fmk|