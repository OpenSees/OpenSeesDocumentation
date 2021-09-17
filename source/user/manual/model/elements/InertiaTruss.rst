.. _InertiaTruss:

InertiaTruss
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an InertiaTruss element object. 


.. function:: element InertiaTruss $eleTag $iNode $jNode $mr

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|,	unique element object tag
   $iNode $jNode, |integer|,  end nodes
   $mr, |float|,     the inertance or inertial mass of an Inertia Truss

.. note::

The valid queries to an InertiaTruss element when creating an ElementRecorder object are 'force' and ‘relAccel’, which output the axial force or relative acceleration between two end-nodes in local coordinates (along the element)

This element has been examined for modal analysis and linear/nonlinear time history analysis

.. admonition:: Example 

   The following example constructs an InertiaTruss element with tag 1 added between nodes 1 and 4 with the inertance of 2000.

    **Tcl Code**

   .. code-block:: tcl

      element InertiaTruss 1 1 4 2000

Code developed by: Xiaodong Ji, Yuhao Cheng, Yue Yu

First published in: Ji X, Cheng Y, Molina Hutt C. Seismic response of a tuned viscous mass damper (TVMD) coupled wall system. Eng Struct 2020;225:111252. https://doi.org/10.1016\/j.engstruct.2020.111252.
