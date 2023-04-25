.. _getFixedNodes:

getFixedNodes Command
****************

This command returns the constrained nodes in the **Domain**.

.. function:: getFixedNodes

.. admonition:: Example:

   The following example is used to set the variable **fixedNodes** to current state of constrained nodes in the **Domain**

   1. **Tcl Code** (note use of **set** and **[ ]**)

   .. code-block:: tcl

	set fixedNodes [getFixedNodes]

   2. **Python Code**

   .. code-block:: python

	fixedNodes = getFixedNodes()


Code developed by: |fmk|
