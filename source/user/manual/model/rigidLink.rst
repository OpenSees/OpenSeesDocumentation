Rigid Link
^^^^^^^^^^

This command is used to construct a single MP_Constraint object.

.. function:: rigidLink $type $masterNodeTag $slaveNodeTag

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $type, |string|,  "| string-based argument for rigid-link type:
   | **bar** only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node 
   | **beam** both the translational and rotational degrees of freedom are constrained."
   $masterNodeTag, |integer|, integer tag identifying the master node
   $slaveNodeTag, |integer|, integer tag identifying the slave node

.. note::
   The constraint object is constructed assuming small rotations.

.. admonition:: Example:

   The following command will constrain node **3** to move as node **2**

   1. **Tcl Code**

   .. code-block:: none

      rigidLink beam 2 3

   2. **Python Code**

   .. code-block:: python

      rigidLink('beam',2,3)