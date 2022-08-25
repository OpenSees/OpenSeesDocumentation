Plain Constraint Handler
^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Plain constraint handler. A plain constraint handler can only enforce homogeneous single point constraints (fix command) and multi-point constraints constructed where the constraint matrix is equal to the identity (equalDOF command). The following is the command to construct a plain constraint handler:

.. function:: constraints Plain

.. warning::

This constraint handler can only enforce homogeneous single point constraints (fix command) and multi-pont constraints where the constraint matrix is equal to the identity (equalDOF command).

It does not follow constraints, by that we mean the constrained node in a MP_Constraint cannot be a retained node in another MP_Constraint.


.. admonition:: Example 

   The following example shows how to construct a reverse Cuthill-McKee numberer.

   1. **Tcl Code**

   .. code-block:: tcl

      constraints Plain


   2. **Python Code**

   .. code-block:: python

      constraints('Plain')


Code Developed by: |fmk|
