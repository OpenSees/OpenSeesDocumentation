Rigid Diaphragm
^^^^^^^^^^^^^^^

This command is used to construct a number of Multi-Point Constraint (MP_Constraint) objects. These objects will constraint certain degrees-of-freedom at the listed constrained nodes to move as if in a rigid plane with the retained node.

.. function:: rigidDiaphragm $perpDirn $retainedNodeTag $constrainedNodeTag1 $constrainedNodeTag2 ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $perpDirn, |integer|,  direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane)
   $retainedNodeTag, |integer|,  integer tag identifying the master node
   $constrainedNodeTag1 $constrainedNodeTag2 ... , |integerList|, integar tags identifying the slave nodes

.. note::
   1. The constraint object is constructed assuming small rotations.

   2. The rigidDiaphragm command works only for problems in three dimensions with six-degrees-of-freedom at the nodes (ndf = 6).


.. admonition:: Example:

   The following command will constrain nodes **4,5,6** to move as if in the same 1-2 plane as node *22*. The constraint matrix added for each of the constrained nodes, which defines the motion of degrees-of-freedom (**x**, **y**, **rZ**) or (**1**, **2**, and **6**) at node **4,5,6** relative to those same degrees-of-freedom at the retained node **22** is as follows:

      .. math::
        :label: rigidConstraintBeam3D

	\begin{bmatrix}
		1 & 0 & -\Delta Y \\
		0 & 1 & \Delta X \\
		0 & 0 & 1
	\end{bmatrix}

      where :math:`\Delta X` is **x** (or **1**) coordinate of constrained node minus the **x** coordinate of the retained node and :math:`\Delta Y` is **y** (or **2**) coordinate of constrained node minus the y coordinate of the retained node and :math:`\Delta Y` 


   1. **Tcl Code**

   .. code-block:: none

      rigidDiaphragm 3 22 4 5 6

   2. **Python Code**

   .. code-block:: none

      rigidDiaphragm(3,22,4,5,6)


   
