.. _nodeAccel:

nodeAccel Command
*****************

This command returns the current acceleration at a specified node.

.. function:: nodeAccel $nodeTag <$dof>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, tag identifying node whose accelerations are sought
   $dof, |integer|, optional: specific dof at the node (1 through ndf)

.. note::

   If optional $dof is not provided, an array containing all acceleration components for every dof at the node is returned.

.. admonition:: Example:

   The following example is used to set the array/list **accel1** equal to the nodal accelerations at the node given by the variable **nodeTag**.

   1. **Tcl Code** (note use of **set** and **[ ]**)

   .. code-block:: tcl

	set accel1 [nodeAccel $nodeTag]

   2. **Python Code**

   .. code-block:: python

	accel1 = nodeAccel(nodeTag)


Code developed by: |fmk|
