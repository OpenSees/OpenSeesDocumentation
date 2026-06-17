.. _ModifiedNewton:

Modified Newton Algorithm
--------------------------------
.. function:: algorithm ModifiedNewton <-initial> <-factorOnce>

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - -initial
     - |string|
     - optional flag to indicate to use initial stiffness iterations
   * - -factorOnce
     - |string|
     - optional flag to assemble and factor the tangent in the first analysis step, keep it fixed in all later steps, and update it only after a domain change (for example, nodes or elements added or removed).

.. note::

   Modified Newton already uses one tangent per equilibrium solve within each analysis step. ``-factorOnce`` carries that same tangent forward to later steps instead of reforming it each time. The fixed matrix is the current tangent by default, or the initial tangent with ``-initial``. Specifying ``-initial`` also enables ``-factorOnce`` automatically.

This command is used to construct a ModifiedNewton algorithm object, which uses the modified newton-raphson algorithm to solve the nonlinear residual equation. 
