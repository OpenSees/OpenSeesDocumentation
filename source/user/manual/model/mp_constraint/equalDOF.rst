EqualDOF Constraints
^^^^^^^^^^^^^^^^^^^^

This command is used to construct a multi-point constraint between nodes where the degrees-of-freedom at the constrained node move exactly the same as the degrees-of-freedom at the other node, the retained node.


.. function::     equalDOF $rNodeTag $cNodeTag $dof1 $dof2 ..

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $rNodeTag, |integer|,	   integer tag identifying the retained - the master node (rNode)
   $cNodeTag, |integer|,	   integer tag identifying the constrained - slave node (cNode)
   $dof1 $dof2 ..., |integerList|, "| list of nodal degrees-of-freedom that are constrained at the cNode 


.. note::

   retained node also known as the **master** node.

   constarined node alsoe node as the **slave** node.

   valid range of $dof is 1 through **ndf** of the **slave** node

.. admonition:: Example:

   The following command will impose the displacenents at dof's **1, 3, and 5** at node **2** to be the same as those of node **33*.

   1. **Tcl Code**

   .. code-block:: none

      equalDOF 2 33 1 3 5;

   1. **Tcl Code**

   .. code-block:: python

      equalDOF(2,33,1,3,5);





.. admonition:: Reference:

   Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., "Concepts and Applications of Finite Element Analysis," 4th edition, John Wiley and Sons publishers, 2002.

Code developed by: |fmk|
