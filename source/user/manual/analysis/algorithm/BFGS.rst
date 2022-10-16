.. _BFGS:

BFGS Algorithm
----------------
.. function:: algorithm BFGS <$count>

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $count
     - |integer|
     - number of iterations within a time step until a new tangent is formed
 

This command is used to construct a BFGS algorithm object for symmetric systems which performs successive rank-two updates of the tangent at the first iteration of the current time step.
