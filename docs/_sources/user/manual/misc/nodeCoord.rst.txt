.. _nodeCoord:

nodeCoord Command
*****************

This command returns the current coordinate at a specified node.

.. function:: nodeCoord $nodeTag <$dim>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, tag identifying node whose velocities are sought
   $dim, |integer|, optional: specific crd dimension at the node (1 through ndm)

.. note::

   If optional $ddim is not provided, an array containing all coordinate components is returned.

.. admonition:: Example:

   The following example is used to set the variable **crdNode** to the nodal coordinates for the node given by the variable **nodeTag**.

   1. **Tcl Code** (note use of **set** and **[ ]**)

   .. code-block:: tcl

	set crdNode [nodeCoord $nodeTag]

   2. **Python Code**

   .. code-block:: python

	crdNode = nodeCoord(nodeTag)


Code developed by: |fmk|
