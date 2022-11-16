.. _Broyden:

Broyden Algorithm
--------------------------------
.. function:: algorithm Broyden <$count>

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $count
     - |integer|
     - number of iterations within a time step until a new tangent is formed
 

This command is used to construct a Broyden algorithm object for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.