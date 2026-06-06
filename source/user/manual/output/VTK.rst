.. _vtkRecorder:

VTK Recorder
^^^^^^^^^^^^

The VTK recorder writes the model mesh and selected response quantities to VTK XML format for visualization in `ParaView <https://www.paraview.org/>`_. It creates a directory named after the recorder base name, writes a ParaView collection file (``.pvd``), and stores time-step data in ``.vtu`` files.

For newer workflows, consider also the :ref:`pvdRecorder`, which provides similar ParaView output.

.. function:: recorder vtk $baseName $respType1 $respType2 ... <-precision $nSD> <-dT $deltaT> <-rTolDt $rTol>
   :noindex:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $baseName, |string|, base name for the output directory and ``.pvd`` collection file
   $respType, |string|, response quantity to record (see note 2)
   $nSD, |integer|, output precision (optional, default 10)
   $deltaT, |float|, minimum time between writes (optional)
   $rTol, |float|, relative tolerance on $deltaT (optional, default 0.00001)

.. note::

   1. Valid nodal response types include:

   .. code:: none

      disp
      disp2
      disp3
      vel
      accel
      reaction
      reaction2
      reaction3
      mass
      unbalancedLoad
      eigen $mode

   2. Element response may be requested with ``eleResponse`` followed by the same arguments used in an :ref:`elementRecorder` (for example, ``eleResponse localForce``).

   3. This recorder is available in the Tcl interpreter. It is not registered in the standard OpenSeesPy recorder map; use Tcl or the :ref:`pvdRecorder` / :ref:`gmshRecorder` for Python-based visualization workflows.

   4. Open ``$baseName.pvd`` in ParaView to animate results over time.

   5. | The function returns a value:
      | SUCCESS: **>0** an integer tag that can be used as a handle to remove a recorder with the :ref:`remove` command.
      | FAILURE: **-1** recorder command failed (read the log)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      recorder vtk results disp accel -dT 0.1

Code developed by: |fmk|
