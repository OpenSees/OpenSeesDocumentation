.. _MinimumUnbalancedDisplacementNorm:

MinimumUnbalancedDisplacementNorm
--------------------------------------


This command is used to construct a StaticIntegrator object of type MinUnbalDispNorm.

.. function:: integrator MinUnbalDispNorm $dlambda11 <$Jd $minLambda $maxLambda>

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $dlambda11
     - |float|
     - First load increment (pseudo-time step) at the first iteration in the next invocation of the analysis command.
   * - $Jd
     - |float|
     - Factor relating first load increment at subsequent time steps. (optional, default: 1.0)
   * - $minLambda
     - |float| 
     - arguments used to bound the load increment (optional, default: $dLambda11)
   * - $maxLambda
     - |float| 
     - arguments used to bound the load increment (optional, default: $dLambda11)

Theory
^^^^^^
The load increment at iteration i, :math:`d\lambda_{1,i}` is related to load increment at i-1, :math:`d\lambda_{1,i-1}`, and the number of iteration at (i-1), :math:`J_{i-1}` by the following:

:math:`d\lambda_{1,i} = d\lambda_{1,i-1} \frac{J_d}{J_{i-1}}`