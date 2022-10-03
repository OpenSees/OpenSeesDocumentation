fixY Command
************

This command is used to construct multiple homogeneous single-point boundary constraints for all nodes whose z-coordinate lies within a specified distance from a specified coordinate.

.. function: fixZ $xCoordinate (ndf $ConstrValues) <-tol $tol>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $zCoordinate, |float|, z-coordinate of nodes to be constrained
   $constrValues, |intList|, "| ndf constraint values (0 or 1) corresponding to the ndf 
   | degrees-of-freedom.
   | 0 unconstrained (or free)
   | 1 constrained (or fixed) "
   $tol, |float|, user-defined tolerance (optional: default = 1e-10)

.. admonition:: Example:

   The following example demonstrate the command to fix the first 3 degrees-of-freedom at all nodes in the model at z location **30.0**.

   1. **Tcl Code**

   .. code-block:: none

      fixZ 30.0 1 1 1 0 0 0 

   2. **Python Code**

   .. code-block:: none

      fixZ(30.0, 1, 1, 1, 0, 0, 0)

Code Developed by: **fmk**