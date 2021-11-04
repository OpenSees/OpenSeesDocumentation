.. _getCrdTransfTags:

getCrdTransfTags Command
************************

This command returns a list of all defined coordinate transformation object tags

.. function:: getCrdTransfTags

.. admonition:: Example:

   The following example is used to set the variable **currentTime** to current state of **time** in the **Domain**

   1. **Tcl Code** (note use of **set** and **[ ]**)

   This example creates a set of **geomTransf** objects and the asks for a list of all the created objects using the 
   command **getCrdTransfTags** and assigning the list to the variable called **allCrdTransfTags**, then prints them.

   .. code-block:: tcl

      model BasicBuilder -ndm 3 -ndf 6
      
      geomTransf Linear 1        0                -1               0                -jntOffset 100              0                0                -0               -0               -0              
      geomTransf Linear 2        0                -1               0                -jntOffset 0                0                0                -0               -0               -0              
      geomTransf Linear 3        0                -1               0                -jntOffset 0                0                0                -0               -0               -0              
      geomTransf Linear 4        0                -1               0                -jntOffset 0                0                0                -0               -0               -0              
      geomTransf Linear 5        0                -1               0                -jntOffset 0                0                0                -0               -0               -0              
      
      set allCrdTransfTags [getCrdTransfTags]
      
      puts $allCrdTransfTags

   2. **Python Code**

   .. code-block:: python

      # missing


Code developed by: |fmk|
