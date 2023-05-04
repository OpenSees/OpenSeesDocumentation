.. _zeroLength:

ZeroLength Element
^^^^^^^^^^^^^^^^^^

This command is used to construct a zeroLength element object, which is defined by two nodes at the same location. A zeroLength element is similar to a set of springs placed between two nodes, each spring providing the force displacement relationship for a specified degree-of-freedom. The nodes are connected by multiple UniaxialMaterial objects, which provide the force-deformation relationship for the element in that degree-of-freedom direction. 

.. function:: element zeroLength $eleTag $iNode $jNode -mat $matTag -dir $dir <-doRayleigh $rFlag> <-orient $x $yp>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element object tag
   $endNodes, |integerList|, 2 end nodes
   $matTags, |integerList|, list of **n** material tags
   $dirIDs, |integerList|, "| list of **n** degree-of-freedom directions
   | 1,2,3 - translation along local x,y,z axes,
   | 4,5,6 - rotation about local x,y,z axes"
   $x, |floatList|,  (optional) 3 components in global coordinates defining local x-axis 
   $yp, |floatList|, "| (optional) 3 components in global coordinates defining vector yp 
   | which lies in the local x-y plane for the element."
   $rFlag, |integer|, "| optional, default = 0
   | rFlag = 0 NO RAYLEIGH DAMPING (default)
   | rFlag = 1 include rayleigh damping"


.. note::

   If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

   The valid queries to a zero-length element when creating an ElementRecorder object are 'force,' 'deformation,' and 'material $i matArg1 matArg2 ...' Where $i is an integer indicating which of the materials whose data is to be output (a 1 corresponds to $matTag1, a 2 to $matTag2, and so on). 


.. warning::

   If the distance between end noes is not **0.0** a warning message will appear when the script is run. This is just a warning in case you have made a mistake as most users when they use zeroLength elements are wanting to use them in the more normal way. ZeroLength elements can be used between nodes with non-zero length.

.. admonition:: 

   The following examples demonstrate the commands in a script to add three zeroLength elements to domain. The three to be added have element tags **1**, **2**, and **3**. Element **1** has nodes **2** and **3** as its end ndes, has two materials **5** and **6** acting in directions **1** and **2**. Element **2** has as its end nodes **4** and **5**, has only one material **1** acting in direction **1**, the element has a global orientation.

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLength 1 2 4 -mat 5 6 -dir 1 2
      element zeroLength 2 4 5 -mat 1 -dir 1 -orient 1 1 0 -1 1 0
      element zeroLength 3 5 6 -mat 1 -dir 1 -doRayleigh 1

   2. **Python Code**

   .. code-block:: python

      element('zeroLength',1,2,4,'-mat',5,6,'-dir',1,2)
      element('zeroLength',2,4,5,'-mat',1,'-dir',1,'-orient',1,1,0,-1,1,0)
      element('zeroLength',3,5,6,'-mat',1,'-dir',1,'-doRayleigh',1)

Code Developed by: |glf|
