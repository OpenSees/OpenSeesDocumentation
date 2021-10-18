
.. _recorder:

recorder Command
****************

This command is used to generate a recorder object which is to monitor what is happening during the analysis and generate output for the user. The output may go to the screen, files, databases, or to remote processes through the TCP/IP options.

.. function:: recorder $recorderType $arg1 $arg2 ...

The type of recorder created and the additional arguments required depends on the $recorderType provided in the command.

.. toctree::
   :caption: 1. Recorders to record Node Information
   :maxdepth: 1

   NodeRecorder
   EnvelopeNodeRecorder
   DriftRecorder

.. toctree::
   :caption: 2. Recorders to record Element Information
   :maxdepth: 1

   ElementRecorder
   EnvelopeElementRecorder

.. toctree::
   :caption: 3. Recorders for Graphic output
   :maxdepth: 1

   PlotRecorder
   VTK

.. toctree::
   :caption: 4. Recorders for whole-model output
   :maxdepth: 1

   PVDRecorder
   MPCORecorder
   GmshRecorder

.. note::

   The function returns a value:
   
   **>0** an integer tag that can be used as a handle on the recorder for the remove a recorder in the :ref:`remove`.

   **-1** recorder command failed if integer -1 returned.

Code Developed by: |fmk|