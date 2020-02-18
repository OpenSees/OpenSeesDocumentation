.. _load:

load Command
""""""""""""

This command is used to construct a NodalLoad object.

.. function:: load $nodeTag (ndf $LoadValues)

The nodal load is added to the LoadPattern being defined in the enclosing scope of the pattern command.


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $nodeTag, |integer|, tag of node on which loads act
   $LoadValues, |listFloat|, **ndf** load values that are to be applied to the node.

.. admonition:: Example:

   The following example demonstrates how to create a **Linear** time series, and asociate it with a **Plain** load pattern which contains **nodal loads** to be applied to nodes **3** and **4** of reference magnitude **(0,-50)** and **(50.0, -100)** respectivily. 

   1. **Tcl Code**

   .. code-block:: tcl

      timeSeries Linear 2
      pattern Plain 1 2 {
      	      load  3   0.0  -50.0  0.0
    	      load  4   50.0  -100.0 0.0
      }

   2. **Python Code**

   .. code-block:: python

      timeSeries("Linear", 2)
      pattern("Plain", 1, 2)
      load(3, 0.0, -50.0)
      load(4, 50.0, -100.0)



Code Developed by: |fmk|
