.. _driftRecorder:

Drift Recorder
^^^^^^^^^^^^^^

The Drift recorder records the displacement drift between pairs of nodes. Drift is computed as the relative displacement along a specified degree of freedom divided by the distance between the node pair, measured in a perpendicular global direction. This is commonly used for inter-story drift in building models.

.. function:: recorder Drift <-file $fileName> <-xml $fileName> <-binary $fileName> <-fileCSV $fileName> <-precision $nSD> <-time> <-dT $deltaT> <-rTolDt $rTol> <-closeOnWrite> -iNode $iNode1 $iNode2 ... -jNode $jNode1 $jNode2 ... -dof $dof -perpDirn $dirn
   :noindex:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileName, |string|, file to which output is sent (one of ``-file``, ``-xml``, ``-binary``, or ``-fileCSV``)
   $nSD, |integer|, number of significant digits (optional, default 6)
   -time, |string|, place domain time in the first column of each output line
   $deltaT, |float|, record only when elapsed time since last write exceeds this value
   $rTol, |float|, relative tolerance on $deltaT (optional, default 0.00001)
   -closeOnWrite, |string|, open and close the output file on each write
   $iNode1 $iNode2 ..., |listInt|, tags of the first node in each drift pair
   $jNode1 $jNode2 ..., |listInt|, tags of the second node in each drift pair (same length as ``-iNode`` list)
   $dof, |integer|, global degree of freedom along which relative displacement is measured (1 through ndf)
   $dirn, |integer|, global direction used to compute the distance between nodes (1 = X, 2 = Y, 3 = Z)

.. note::

   1. The number of nodes listed after ``-iNode`` must equal the number listed after ``-jNode``. Node pairs are matched by position in the two lists.

   2. Only one output destination option may be used: ``-file``, ``-xml``, ``-binary``, or ``-fileCSV``.

   3. | The function returns a value:
      | SUCCESS: **>0** an integer tag that can be used as a handle to remove a recorder with the :ref:`remove` command.
      | FAILURE: **-1** recorder command failed (read the log)

.. admonition:: Example

   The following example records drift in DOF 1 between node pairs (1, 3) and (2, 4), using the Y direction to compute story height.

   1. **Tcl Code**

   .. code-block:: tcl

      recorder Drift -file drift.out -time -iNode 1 2 -jNode 3 4 -dof 1 -perpDirn 2

   2. **Python Code**

   .. code-block:: python

      recorder('Drift', '-file', 'drift.out', '-time', '-iNode', 1, 2, '-jNode', 3, 4, '-dof', 1, '-perpDirn', 2)

Code developed by: |mhs|
