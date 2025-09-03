.. _vtkhdfRecorder:

VTKHDF Recorder
^^^^^^^^^^^^^^^

The VTKHDF recorder type is a *whole model* recorder designed to record the model geometry and metadata, along with selected response quantities. The output of this recorder is in the `.h5` file format, which can be visualized using visualization tools like ParaView. This recorder supports both sequential and parallel models (OpenSees and OpenSeesMP).

.. function:: recorder vtkhdf $fileBaseName $respType [-dT $timeStep] [-rTolDt $tolerance]
   :noindex:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileBaseName, |string|, Base name of the file to which output is sent (see note 1).

   $respType, |string|, A string indicating the response type to record (see note 2).

   -dT, |float|, Optional argument specifying the time interval between recordings (see note 6).

   -rTolDt, |float|, Optional argument specifying the relative tolerance for time step matching (see note 7).

.. note::

   1. The recorder writes files in the HDF5 format. The files are named using the convention `$fileBaseName.$respType.$rank.h5`, where `$rank` is the MPI rank of the processor (always 0 in sequential mode, varies in parallel mode).

   2. Valid response types for `$respType` include:

   .. code:: none

      disp
      vel
      accel
      stress3D6
      strain3D6
      stress2D3
      strain2D3
   3.  `disp`, `accel`, and `vel` are 3D vectors. For 2D or 1D models, the unused dimensions will be zero.
   
   4.  `stress3D6` and `strain3D6` represent 6-component average stresses and strains for 3D brick elements. If an element does not support this response, it will return zero. Not all brick elements provide support for these response types.
   
   5.  `stress2D3` and `strain2D3` represent 3-component average stresses and strains for 2D quad elements. If an element does not support these response types, it will return zero. Not all quad elements provide support for these response types.

   6. The `-dT` argument specifies the time interval between recording steps. If not provided, the recorder writes output at every step.

   7. The `-rTolDt` argument specifies the relative tolerance for matching time steps. This is useful in cases where time steps vary slightly due to numerical tolerances.

   8. Users who want to enable specific elements to support `stress3D6`, `strain3D6`, `stress2D3`, or `strain2D3` responses must implement these responses in the `getResponse` and `setResponse` methods of their respective element classes.

.. admonition:: Example:

   The following example demonstrates the use of the vtkhdf recorder command to store displacement results:

   .. code:: tcl

     recorder vtkhdf results.h5 -dT 0.1 -rTolDt 0.00001 disp accel vel stress3D6 strain3D6

   Execution results in the files `results.h5`, which contain the displacement, acceleration, velocity, for all nodes, and the 6-component average stress and strain for all 3D brick elements.  
   These files can be visualized in ParaView by opening the HDF5 file directly.


Code developed by: |amnp95|.

