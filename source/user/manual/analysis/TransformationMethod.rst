Transformation Method
^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a ``PenaltyMethod`` constraint handler, which enforces the constraints by using the penalty method. The following is the command to construct such a constraint handler:

.. function:: constraints Transformation

.. note::

   The single-point constraints when using the transformation method are done directly. The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.
Great care must be taken when multiple constraints are being enforced as the transformation method does not follow constraints:
      1. If a node is fixed, constrain it with the fix command and not equalDOF or other type of constraint.

      2. If multiple nodes are constrained, make sure that the retained node is not constrained in any other constraint.

.. admonition:: Example 

   The following example shows how to construct a Lagrange constraint handler

   1. **Tcl Code**

   .. code-block:: tcl

      numberer Transformation


   2. **Python Code**

   .. code-block:: python

      numberer('Transformation')

Code Developed by: |fmk|
