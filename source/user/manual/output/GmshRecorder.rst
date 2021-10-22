.. _gmshRecorder:

GMSH Recorder
^^^^^^^^^^^^^


The GMSH recorder type is a *whole model* recorder, that is it is meant to record all the model geometry and metadata along with selecetd response quantities. The output of this recorder is in the ``.msh`` file format (legacy version 2) which can be visualized with the `gmsh <https://gmsh.info/>`_ program. This recorder is enabled for use in parallel model (both OpenSeesMP and OpenSeesSP works).

.. function:: recorder gmsh $fileBaseName $respType
   :noindex:

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileBaseName, |string|, base-name of file to which output is sent (see note 1)

   $respType, |string|,  a string indicating response requested

.. note::

   1. This recorder writes several files readable by gmsh. The files are named using the convention be name ``$fileBaseName.$respType.$rank.msh`` where ``$rank`` is the MPI rank of current processor (always 0 in sequential mode, differs in parallel mode). The mesh information is always outputted (during the first write operation only, typically the first time-step) and stored in the file with name: ``$fileBaseName.mesh.$rank.msh``.
   

   2. The valid strings for respType are:

   .. code:: none

      disp
      vel
      accel
      partition
      eleResponse

   Note the response type ``partition`` is unique to this recorder type and it contains information on the partition each element was assigned (useful in parallel processing to check model partitioning).

   3. | The function returns a value:   
      | SUCCESS: **>0** an integer tag that can be used as a handle on the recorder for the remove a recorder in the :ref:`remove`.
      | FAILURE: **-1** recorder command failed (read the log)
   

.. admonition:: Example:

   The following examples demonstrate the use of the gmsh recorder command to store displacement results

   .. code:: tcl
   
     recorder gmsh results disp

   Execution results in the files ``results.mesh.0.msh`` (where mesh info is stored) and ``results.disp.0.msh`` (where displacement response at each node are stored). In gmsh, open first the `mesh` file and then merge the `disp` file into the current model to generate a post-processing view. 

Code developed by: |jaabell| based on code by |mhscott|, |zhuminjie| and |fmk|.
