.. _elasticBeamColumn:

Elastic Beam Column Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an elasticBeamColumn element object. The arguments for the construction of an elastic beam-column element depend on the dimension of the problem, ndm:

For a two-dimensional problem:

.. function:: element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-mass $massDens> <-cMass>

For a three-dimensional problem:

.. function:: element elasticBeamColumn $eleTag $iNode $jNode $A $E $G $J $Iy $Iz $transfTag <-mass $massDens> <-cMass>
.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|,	unique element object tag
   $iNode $jNode, |integer|,  end nodes
   $A, |float|,     cross-sectional area of element
   $E, |float|,      Young's Modulus
   $G, |float|,     Shear Modulus
   $J, |float|,     torsional moment of inertia of cross section
   $Iz, |float|,    second moment of area about the local z-axis
   $Iy, |float|,    second moment of area about the local y-axis
   $transfTag, |integer|,    identifier for previously-defined coordinate-transformation object
   $massDens, |float|, element mass per unit length (optional: default = 0.0)
   -cMass, |string|, to form consistent mass matrix (optional)

.. note::

The valid queries to an elastic beam-column element when creating an ElementRecorder object are 'force'.


.. admonition:: Example 

   The following example constructs an elastic element with tag **1** between nodes **2** and **4** with an area of **5.5**, E of **100.0** and an Iz of **1e6** which uses the geometric transformation object with a tag of **9**

   1. **Tcl Code**

   .. code-block:: tcl

      element elasticBeamColumn 1 2 4 5.5 100.0 1e6 9; 

   2. **Python Code**

   .. code-block:: python

      element('elasticBeamColumn',1,2,4,5.5,100.0, 1.0e6, 9)

Code developed by: |fmk|


