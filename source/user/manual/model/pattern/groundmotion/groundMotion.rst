.. _groundMotion:

Ground Motion
^^^^^^^^^^^^^

The groundMotion command is used to construct a GroundMotion object used by the ImposedMotionSP constraints in a MultipleSupportExcitation object. This command is of the following form:

.. function:: groundMotion $tag $type arg1? ...

The type of GroundMotion created and the additional arguments required depends on the type? provided in the command. The following contain information about type? and the args required for each of the available ground motion types:


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, unique tag among ground motions in load pattern
   $type, |string|, the type of ground motion
   $args, |floatList|, args specific to the type of motion

There are presently two type of groundMotions that can be created: 1) :ref:`plainGroundMotion` and 2) :ref:`interpolaatedGroundMotion`

.. _plainGroundMotion:

Plain Ground Motion
"""""""""""""""""""

Each GroundMotion object is associated with a number of TimeSeries objects, which define the acceleration, velocity and displacement records for that ground motion. The particular form of the command is as follows:

.. function:: groundMotion $gmTag Plain <-accel $tsTag> <-vel $tsTag> <-disp $tsTag> <-int (IntegratorType intArgs)> <-fact $cFactor>)
where

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $gmTag, |integer|, unique tag among ground motions in load pattern
   $tsTag, |integer|, tag of TimeSeries object created using timeSeries command.
   integratorType, |string|, string inteagting type of integration (optional, default=Trapezoidal). See NOTES below.
   $cFactor, |float|, factor to be applied to motions (optional: default=1.0)

.. note::

   The displacements are the ones used in the ImposedMotions to set nodal response.

   Any combination of the acceleration, velocity and displacement time-series can be specified.

   If only the acceleration TimeSeries is provided, numerical integration will be used to determine the velocities and displacements. If only velocity are provided, numerical integration is used to obtain the displacements.

   For earthquake excitations it is important that the user provide the displacement time history, as the one generated using the trapezoidal method will not provide good results.


.. _interpolatedGroundMotion:

Interpolated Ground Motion
""""""""""""""""""""""""""

This command is used to construct an interpolated GroundMotion object, where the motion is determined by combining several previously defined ground motions in the load pattern. The command is as follows:

.. function:: groundMotion $tag Interpolated $gmTag1 $gmTag2 ... -fact $fact1 $fact2 ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, unique tag among ground motions in load pattern
   $gmTags, |integerList|, the tags of existing ground motions in pattern to be used for interpolation.
   $factors, |floatList|, the interpolation factors.



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

