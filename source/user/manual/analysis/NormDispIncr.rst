.. _NormDispIncr:

Norm Displacement Increment
----------------------------

This command is used to construct a convergence test which uses the norm of the solution, :math:`x` vector, of the matrix equation, :math:`Ax=b` to determine if convergence has been reached. What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, it is equal to the change in nodal displacements in the system due to the current unbalance. The command to create a NormUnbalance test is the following:

.. function:: test NormDispIncr $tol $iter <$pFlag> <$nType>

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

   When using a :ref:`penalty` constraint handler, large forces (those necessary to enforce the constraint) are included in the :math:`x` vector. Even for very small changes in the displacement, if user has selected overly large penalty factor, large forces can appear in the :math:`x` vector.

.. admonition:: Example:

   The following examples demonstrate the command to create a NormDispIncr test which allows 10 iterations till failure with a 2-norm in the :math:`x` vector, i.e. :math:`\sqrt(x^T x)` of **1.0e-2**.

   1. **Tcl Code**

   .. code-block:: tcl

      test NormDispIncr 1.0e-2  10 2

   2. **Python Code**

   .. code-block:: python

      test('NormDispIncr', 1.0e-2, 10, 2)


Code Developed by: **fmk**