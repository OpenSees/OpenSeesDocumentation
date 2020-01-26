.. _nodeRecorder:

Node Recorder
^^^^^^^^^^^^^

.. function:: recorder(Node, <-file $filename>,<-xml $filename>,<-binary $filename>,<-tcp $inetAddress $port>, <-precision  $nSD>, <-timeSeries $tsTag>,<-time>,<-dT $deltaT>, <-closeOnWrite>, <-node  $nodeTags>,< -nodeRange $startNode $endNode>,<-region $regionTag> -dof $dofs $respType)
   :noindex:

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileName, |string|, name of file to which output is sent.
   $inetAddr, |string|, ip address ("xx.xx.xx.xx") of remote machine
   $port, |integer|, port on remote machine awaiting tcp
   $nSD, |integer|, number of significant digits (optional: default is 6)
   -time, |string|, optional: places domain time in first output column.
   -closeOnWrite, |string|, optional: opens and closes file on each write.
   $deltaT, |float|, optional: time interval for recording.
   $tsTag, |integer|, the tag of a previously constructed TimeSeries. 
   $nodes, |listInteger|, optional: tags of nodes whose response is being recorded
   $startNode, |integer|, optional: tag for start node
   $startNode, |integer|, optional: tag for end node 
   $regionTag, |integer|, optional: tag of previously defined region.
   $dofs, |integerList|, list of dof at nodes whose response is requested.
   $respType, |string|,  a string indicating response required.

.. note::
   1. Only one of the optionss -file, -xml, -binary, -tcp may be used. The option specifies where the data is going to be sent.

   2. Similarily only one of the -node, -nodeRange, -region options ma be specified.

   3. The valid strings for respType are:

   .. code:: none

      disp
      vel
      accel
      incrDisp
      eigen $mode
      reaction
      rayleighForces!

   4. | The function returns a value:   
      | SUCCESS: **>0** an integer tag that can be used as a handle on the recorder for the remove a recorder in the :ref:`remove`.
      | FAILURE: **-1** recorder command failed (read the log)
   To remove a recorder using the :ref:`remove` you need to save this tag in a variable for use later in the script.

   5. $deltaT, |float|, optional: time interval for recording. will record when next step is $deltaT greater than last recorder step. (optional. default: records at every time step)

   6. If the **-timeSeries** option is being used, the recorded results are those obtained from the time series for the current time added to the response quantity measures. Need as many time series tags as dof specified. Useful for obtaining for example total acceleration as opposed to relative if user using UniformAcceleration to impose a ground motion.

   7. The -closeOnWrite option will slow the program down. It is useful if you want to see just exactly where the applocation is, as files are only written to disk when the operating system feels like it under typical operation.


.. admonition:: Example:

   The following examples demonstrate the use of the recorder Node command.


   Generates output file nodesD.out that contains relative displacements in x and y direction at nodes 1, 2, 3, and 4. The output file will contain 9 columns (time, disp. in x at node 1, disp. in y at node 1, ... , disp. in y at node 4))

   .. code:: tcl
   
   recorder Node -file nodesD.out -time -node 1 2 3 4 -dof 1 2 disp;
   recorder Node -file nodesA.out -timeSeries 1 -time -node 1 2 3 4 -dof 1 accel;

   .. code:: python

Code developed by: |fmk|