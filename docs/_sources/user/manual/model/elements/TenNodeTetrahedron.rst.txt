.. _TenNodeTetrahedron:

TenNodeTetrahedron Element
^^^^^^^^^^^^^^^^^^^^^^^^^^


This command is used to construct an ten-node tetrahedron element object, which uses the standard isoparametric formulation.

.. admonition:: Command

   **element TenNodeTetrahedron $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $node9 $node10 $matTag <$b1 $b2 $b3> <doInitDisp?> **

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|,	unique element object tag
   $node1 .. $node10, 10 |integer|, nodes of tet (ordered as shown in fig below)
   $matTag, |integer|, tag of nDMaterial
   $b1 $b2 $b3, |listFloat|, optional: body forces in global x y z directions
   <-doInitDisp $value>, |bool|, optional: consider initial displacements if $value is 0

This element is based on second-order interpolation of nodal quantities, this means that the strain and stress field inside the element are linearly interpolated. Four Gauss-points inside the element are used for integration. 


.. figure:: figures/TenNodeTetrahedron/TenNodeTetrahedron.png
	:align: center
	:figclass: align-center

	TenNodeTetrahedron Element Node Numbering

.. note::

   The valid queries to a `TenNodeTetrahedron` element when creating an ElementRecorder object are 'forces', 'stresses,' ('strains' version > 2.2.0) and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

   This element can only be defined after a :ref:`model` with **-ndm 3 -ndf 3**

.. admonition:: Example 

   The following example constructs a TenNodeTetrahedron element with tag **1** between nodes **1, 2, 3, 4, 5, 6, 7, 8, 9, 10** with an nDMaterial of tag **1** and body forces given by varaiables **b1, b2, b3**.

   1. **Tcl Code**

   .. code-block:: tcl

      element TenNodeTetrahedron 1 1 2 3 4 5 6 7 8 9 10 1 $b1 $b2 $b3

   2. **Python Code**

   .. code-block:: python

      element('TenNodeTetrahedron',1, 1,2,3,4,5,6,7,8,9,10, 1, b1, b2, b3)

Code Developed by: `José Antonio Abell <www.joseabell.com>`_ and José Luis Larenas (UANDES). For bugs and features, start a new issue on the `OpenSees github repo <https://github.com/OpenSees/OpenSees>`_ and tag me (@jaabell). 
