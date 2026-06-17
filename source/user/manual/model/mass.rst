.. _mass:

mass Command
************

This command assigns lumped mass values to an existing node. The number of mass values must match the number of degrees of freedom at the node.

.. function:: mass $nodeTag $m1 $m2 ...

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, tag of the node whose mass is being set
   $m1 $m2 ..., |listFloat|, nodal mass values for each DOF (diagonal lumped mass matrix)

.. note::

   Mass can also be assigned when a node is created using the :ref:`node` command with the ``-mass`` option.

.. admonition:: Example

   The following example assigns mass in the x and z directions at node 2 for a 6-DOF model.

   1. **Tcl Code**

   .. code-block:: tcl

      mass 2 2.5 0.0 2.5 0.0 0.0 0.0

   2. **Python Code**

   .. code-block:: python

      ops.mass(2, 2.5, 0.0, 2.5, 0.0, 0.0, 0.0)

Code Developed by: |fmk|
