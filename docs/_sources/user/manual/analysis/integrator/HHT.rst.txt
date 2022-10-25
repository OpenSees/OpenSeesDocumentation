.. _HilberHughesTaylorMethod:

Hilber-Hughes-Taylor Method
--------------------------------
.. function:: integrator HHT $alpha <$gamma $beta> 

This command is used to construct a Hilber-Hughes-Taylor (HHT) integration object. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular Newmark method). Depending on choices of input parameters, the method can be unconditionally stable. 

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $alpha
     - |float|
     - :math:`\alpha` factor
   * - $gamma
     - |float|
     - :math:`\gamma` factor 
   * - $beta
     - |float|
     - :math:`\beta` factor
  
.. admonition:: Example 

   1. **Tcl Code**

   .. code-block:: tcl

       integrator HHT 0.9  

   1. **Python Code**

   .. code-block:: python

        integrator('HHT', 0.9)

.. note:: 
    :math:`\alpha` is defined differently that in the paper, we use :math:`\alpha = \alpha_{HHT} - 1` where :math:`\alpha_{HHT}` is that used in the paper.

        * Like Newmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
        * :math:`\alpha = 1.0` corresponds to the Newmark method.
        * :math:`\alpha` should be between 0.67 and 1.0. The smaller the :math:`\alpha` the greater the numerical damping.
        * :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is second order accurate and unconditionally stable when :math:`\alpha` is :math:`\tfrac{2}{3} <= \alpha <= 1.0`. The defaults are: :math:`\beta = \frac{(2 - \alpha)^2}{4}` and :math:`\gamma = \frac{3}{2} - \alpha`


Theory
^^^^^^^^
The HHT method (sometimes called the :math:` \alpha` method) is a one step implicit method for solving the transient problem which attempts to increase the amount of numerical damping present without degrading the order of accuracy. In the HHT method, the same Newmark approximations are used:

.. math::
    
    U_{t+\Delta t} = U_t + \Delta t \dot U_t + [(0.5 - \beta) \Delta t^2] \ddot U_t + [\beta \Delta t^2] \ddot U_{t+\Delta t}

.. math::
    
    \dot U_{t+\Delta t} = \dot U_t + [(1-\gamma)\Delta t] \ddot U_t + [\gamma \Delta t ] \ddot U_{t+\Delta t}

but the time-discrete momentum equation is modified:

.. math::
    
    R_{t + \alpha \Delta t} = F_{t+\Delta t}^{ext} - M \ddot U_{t + \Delta t} - C \dot U_{t+\alpha \Delta t} - F^{int}(U_{t + \alpha \Delta t})

`

where the displacements and velocities at the intermediate point are given by:

.. math::
    
    U_{t+ \alpha \Delta t} = (1 - \alpha) U_t + \alpha U_{t + \Delta t}

.. math::
    
    \dot U_{t+\alpha \Delta t} = (1-\alpha) \dot U_t + \alpha \dot U_{t + \Delta t}

Following the methods outlined for Newmarks method, loinearization of the nonlinear momentum equation results in the following linear equations:

.. math::

    K_{t+\Delta t}^{*i} d U_{t+\Delta t}^{i+1} = R_{t+\Delta t}^i

where

.. math::

    K_{t+\Delta t}^{*i} = \alpha K_t + \frac{\alpha \gamma}{\beta \Delta t} C_t + \frac{1}{\beta \Delta t^2} M

and

.. math::

    R_{t+\Delta t}^i = F_{t + \Delta t}^{ext} - F(U_{t + \alpha \Delta t}^{i-1})^{int} - C \dot U_{t+\alpha \Delta t}^{i-1} - M \ddot U_{t+ \Delta t}^{i-1}

The linear equations are used to solve for :math:`U_{t+\alpha \Delta t}, \dot U_{t + \alpha \Delta t} \ddot U_{t+\Delta t}`. Once convergence has been achieved the displacements and velocities at time :math:`t + \Delta t` can be computed. 