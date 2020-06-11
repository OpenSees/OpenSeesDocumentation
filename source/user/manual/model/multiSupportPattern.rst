.. _multisupportExcitation:

Multisupport Excitation
^^^^^^^^^^^^^^^^^^^^^^^

The Multi-Support pattern allows similar or different prescribed ground motions to be input at various supports in the structure. In OpenSees, the prescribed motion is applied using single-point constraints, the single-point constraints taking their constraint value from user created ground motions.

The command to generate a multi-support excitation contains in squirrelly brackets the commands to generate all the ground motions and the single-point constraints in the pattern. The command is as follows:


.. function: pattern MultipleSupport $patternTag {ground motion & imposed motion commands}

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $patternTag, |integer|, unique tag among load patterns
   groundMotion & imposed motion commands` , **commands**, command to generate a ground motion & constrain nodes


As will be demonstrated in the example, the actual support conditions that are applied depend on a series of additional commands :ref:`groundMotion` and :ref:`imposedMotion`. The :ref:`groundMotion` create ground motion objects, which are applied to a particular node with the :ref:`imposedMotion` command.

.. toctree::
   :maxdepth: 1

   groundMotion
   imposedMotion
   
.. warning::

   The results for the responses at the nodes are the **ABSOLUTE** values, and not relative values as in the case of a UniformExcitation.

   When using MultiSupport pattern, the ground motions are applied by specifying for each constrained node a ground motion. This is done using the :ref:`imposedMotion` command. The ground motions at each of the supports is specified using a :ref:`groundMotion`. When enforcing the constraint at the node, the imposedMotion constraint will obtain the **displacement** from the ground motion. If the groundMotion was built by user specifying the acceleration, the **trapezoidal** rule is used for integration to obtain the **displacements**.

.. admonition:: Example:

   The following example shows how to construct a **Multi-Support Excitation** pattern with a tag of **1* that will constrain the nodes **1**, **4**, and **7** to move in the **1** dof direction with the ground Motion supplied by the **groundMotion** with tag **101**, whose displacement is given by **timeSeries** with a tag of 3.

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
