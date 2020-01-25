.. _nodeDisp:

nodeDisp Command
****************

This command returns the current displacement at a specified node.

.. function:: nodeDisp $nodeTag <$dof>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, tag identifying node whose displacements are sought
   $dof, |integer|, optional: specific dof at the node (1 through ndf)

.. note::

   If optional $dof is not provided, an array containing all displacement components for every dof at the node is returned.

.. admonition:: Example:

   The following example is used to set the variable **disp1** to the nodal displacement at node given by the variable **nodeTag** in the **1** degree-of-freedom direction.

   1. **Tcl Code** (note use of **set** and **[ ]**)

   .. code-block:: tcl

	set disp1 [nodeDisp $nodeTag 1]

   2. **Python Code**

   .. code-block:: python

	disp1 = nodeDisp(nodeTag,1)


Code developed by: |fmk|
