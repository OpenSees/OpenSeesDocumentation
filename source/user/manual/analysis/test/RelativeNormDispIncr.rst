.. _RelativeNormDispIncr:

Relative Norm Displacement Increment
------------------------------------

This command constructs a convergence test that uses the norm of the solution, :math:`x` vector, of the matrix equation, :math:`Ax=b`. It compares the current norm to the norm at the first step, i.e. :math:`\frac{\sqrt({x_i}^T{x_i})}{\sqrt({x_1}^T{x_1})}`. What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, it is equal to the change in nodal displacements in the system due to the current unbalance.

.. function:: test RelativeNormDispIncr $tol $iter <$pFlag> <$nType>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tol, |float|, the tolerance criteria used to check for convergence
   $iter, |integer|, the max number of iterations to check before returning failure condition
   $pFlag, |integer|, " | print flag (optional: default is 0) valid options:
    | 0 print nothing
    | 1 print information on norms each time test() is invoked
    | 2 print information on norms and number of iterations at end of successful test
    | 4 at each step it will print the norms and also the <math>\Delta U</math> and <math>R(U)</math> vectors.
    | 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test."
   $nType, |integer|, "type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm ...))"

.. note::

   The convergence test compares the current norm of the displacement increment with the norm of the first step to determine if convergence has been achieved. As a consequence it will always take at least two steps to achieve convergence.

.. admonition:: Example

   The following examples demonstrate the command to create a RelativeNormDispIncr test which allows 10 iterations till failure with a 2-norm in the :math:`x` vector of **1.0e-2**.

   1. **Tcl Code**

   .. code-block:: tcl

      test RelativeNormDispIncr 1.0e-2  10 2

   2. **Python Code**

   .. code-block:: python

      test('RelativeNormDispIncr', 1.0e-2, 10, 2)

Code Developed by: |fmk|
