.. _plainPattern:

Plain Pattern
^^^^^^^^^^^^^

This command allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects.

.. function:: pattern Plain $patternTag $tsTag <-fact $cFactor> {load commands}

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $patternTag, |integer|,   unique tag among load patterns
   $tsTag, |integer|, the tag of the time series to be used in the load pattern
   $cFactor, |float|, constant factor (optional: default=1.0)


.. toctree::
   :maxdepth: 1

   load
   eleLoad
   sp


.. note::
   
   The loads (element, nodal, constraints) in a Plain Load pattern are **reference** loads. The actual load applied to a node or element is the product of the **$cFactor**, the reference load, and a **load factor**. The **load factor**, which is obtained from the associated :ref:`timeSeries` is a function of the **time** in the domain and the time series object.

.. warning::

   Tcl and Python differ here. In the Tcl interpreter the commands to create loads and constraints come in the squirrelly brackets after the command. In python, any load or constraints defined after a pattern are added to that pattern. This is as shown in following example.

.. admonition:: Example:

   The following example demonstrates how to create a **Linear** time series, and associate it with a **Plain** load pattern which contains **nodal loads** to be applied to nodes **3** and **4** of reference magnitude **(0,-50)** and **(50.0, -100)** respectively. 

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
