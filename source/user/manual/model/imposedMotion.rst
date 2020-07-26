.. _imposedMotion:

Imposed Motion Command
^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an ImposedMotionSP constraint which is used to enforce the response of a dof at a node in the model. The response enforced at the node at any give time is obtained from the GroundMotion object associated with the constraint.

.. function:: imposedMotion $nodeTag $dirn $gMotionTag

   $nodeTag, |integer|, tag of node on which constraint is to be placed
   $dof, |integer|, dof of enforced response. Valid range is from 1 through ndf at node.
   $gMotionTag, |integer|,   pre-defined GroundMotion object tag

.. admonition:: Example:

   The following example shows how to construct a **Multi-Suppert Excitation** pattern with a tag of **1* that will constrain the nodes **1**, **4**, and **7** to move in the **1** dof direcection with the ground Motion supplied by the **groundMotion** with tag **101**, whose displacement is given by **timeSeries** with a tag of 3.

   1. **Tcl Code**

   .. code:: tcl

      timeSeries Path 3 -filePath elCentroDisp.dat -dt 0.02
      pattern MultipleSupport  1  {
   	   groundMotion 101 Series -disp 3

   	   imposedSupportMotion 1 1 101
   	   imposedSupportMotion 4 1 101
   	   imposedSupportMotion 7 1 101
      }

   2. **Python Code**

   .. code:: python

      timeSeries('Path', 3, '-dt', 0.02, '-filePath', 'elCentroDisp.dat')
      pattern('MultiSupport', 1)	 
      groundMotion(101, 'Series', '-disp', 3)
      imposedSupportMotion(1,1,101)
      imposedSupportMotion(4,1,101)
      imposedSupportMotion(7,1,101)

Code Developed by: |fmk|