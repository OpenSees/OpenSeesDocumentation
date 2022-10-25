.. _fix:

fix Command
^^^^^^^^^^^

This command is used to construct a number of single-point homogeneous boundary constraints.

.. function:: fix $nodeTag (ndf $constrValues)

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, unique tag identifying the node to be constrained
   $constrValues, |listInt|, "| ndf constraint values (0 or 1) corresponding to the ndf 
   | degrees-of-freedom.
   | 0 unconstrained (or free)
   | 1 constrained (or fixed)"


.. admonition:: Example:

   The following examples demonstrate the commands in a script to add homogeneous boundary conditions
to nodes **1** and **2** for a model with **ndf** of 6. Node **1** is specified to be totally fixed, node **2** is only constrained in the second and fifth degree-of-freedom.

   1. **Tcl Code**

   .. code-block:: none

      fix 1 1 1 1 1 1 1 
      fix 2 0 1 0 0 1 0 

   1. **Python Code**

   .. code-block:: none

      fix(1,1,1,1,1,1,1) 
      fix(2,0,1,0,0,1,0) 

Code developed by: |fmk|