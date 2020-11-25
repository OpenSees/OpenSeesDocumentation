Basic Truss Example
-------------------

This example is of a linear-elastic three bar truss, as shown in the figure, subject to static loads. The model has four nodes, labelled **1** through **4**, and three elements, labelled **1** through **3**. Nodes **1**, **2** ,and **3** are fixed and a loads of **100kip** and **-50kip** are imposed at node **4**. The elements all have a youngs modulus of **300ksi**, elements **2** and **3** have an area of **5in^2** and element **1** an area of **10in^***.

.. note::
Because the model is planar and is comprised of truss elements, the spatial dimension of the mesh (``ndm``) will be specified as **2** and the nodes will only be specified to have **2** degrees-of-freedom.



