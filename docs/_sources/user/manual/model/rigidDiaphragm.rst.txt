Rigid Diaphragm
^^^^^^^^^^^^^^^

This command is used to construct a number of Multi-Point Constraint (MP_Constraint) objects. These objects will constraint certain degrees-of-freedom at the listed slave nodes to move as if in a rigid plane with the master node.

.. function:: rigidDiaphragm $perpDirn $masterNodeTag $slaveNodeTag1 $slaveNodeTag2 ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $perpDirn, |integer|,  direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane)
   $masterNodeTag, |integer|,  integer tag identifying the master node
   $slaveNodeTag1 $slaveNodeTag2 ... , |integerList|, integar tags identifying the slave nodes

.. note::
   The constraint object is constructed assuming small rotations.

   The rigidDiaphragm command works only for problems in three dimensions with six-degrees-of-freedom at the nodes (ndf = 6).


.. admonition:: Example:

   The following command will constrain nodes **4,5,6** to move as if in the same 1-3 plane as node *22*.

   1. **Tcl Code**

   .. code-block:: none

      rigidDiaphragm 2 22 4 5 6

   1. **Tcl Code**

   .. code-block:: none

      rigidDiaphragm(2,22,4,5,6)