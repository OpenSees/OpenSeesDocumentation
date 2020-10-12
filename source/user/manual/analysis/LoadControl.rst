LoadControl Command
-------------------

This command is used to construct a LoadControl integrator object.

.. function:: integrator LoadControl $lambda <$numIter $minLambda $maxLambda>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $lambda, |float|,the load factor increment :math:`\lambda`
   $numIter, |integer|,   the number of iterations the user would like to occur in the solution algorithm. Optional: optional default = 1
   $minLambda, |float|, the min stepsize the user will allow. optional: defualt :math:`= \lambda_{min} = \lambda`
   $maxLambda, |float|, the max stepsize the user will allow. optional: default :math:`= \lambda_{max} = \lambda`

.. note::

   The change in applied loads that this causes depends on the active load patterns (those load patterns not set constant) and the loads in the load patterns. If the only active loads acting on the domain are in load patterns with a Linear time series with a factor of 1.0, this integrator is the same as the classical load control method.

   The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.

Theory
^^^^^^

In Load Control the time in the domain is set to :math:`t + \lambda_{t+1}` where,

      .. math::

         \lambda_{t+1} = \max \left ( \lambda_{min}, \min \left ( \lambda_{max}, \frac{\text{numIter}}{\text{lastNumIter}} \lambda_{t} \right ) \right )


where *lastNumIter* is number of steps required to achieve convergence in the previous step. Changing the step size based on number of iterations in previous step, allows user to reduce the step size when the analysis struggles to converge.


.. admonition:: Example 

   The following example shows how to construct a Load Control Integrator with a step size of **0.1**, which in a static analysis would increment the pseudo time by the **0.1** factor at each analysis step, thus requiring **10** analysis steps if the full load is considered to be applied when the pseudo domain time is **1.0**.

   1. **Tcl Code**

   .. code-block:: tcl

      integrator LoadControl 0.1

   2. **Python Code**

   .. code-block:: python

      integrator('LoadControl', 0.1)


Code Developed by: |fmk|
