.. _node:

node Command
************

This command is used to construct a Node object. It assigns coordinates and masses to the Node object. The assignment of mass is optional.

.. function:: node $nodeTag [ndm $coords] <-mass [ndf $massValues]>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, unique tag identifying node
   $coords,  |listFloat|,  **ndm** nodal coordinates
   $massValues, |listFloat|, optional **ndf** nodal mass values


.. admonition:: Example:

   The following examples demonstrate the commands in a script to add two nodes to domain in which the last model command specified an **ndm** of **2** and a **ndf** of 3. The two nodes to be added have node tags **3** and **4**. Node **3** is located at coordinates (168.0, 144.0) and node **4** at location (168.0,144.0). Node **4** is assigned a mass of (10.0, 10.0, 0.).

   1. **Tcl Code**

   .. code-block:: tcl

      node 3 168.0 0.0
      node 4 168.0 144.0 -mass 10.0 10.0 0.0

   2. **Python Code**

   .. code-block:: python

      node(3, 168.0,  0.0)
      node(4, 168.0,  0.0, '-mass', 10.0 10.0 0.0)


Code Developed by: |fmk|
