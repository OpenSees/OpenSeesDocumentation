.. _ModifiedNewton:

Modified Newton Algorithm
--------------------------------
.. function:: algorithm ModifiedNewton <-initial> 

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - -initial
     - |string|
     - optional flag to indicate to use initial stiffness iterations

This command is used to construct a ModifiedNewton algorithm object, which uses the modified newton-raphson algorithm to solve the nonlinear residual equation. 
