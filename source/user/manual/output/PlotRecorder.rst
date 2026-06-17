.. _plotRecorder:

Plot Recorder
^^^^^^^^^^^^^

The Plot recorder opens a graphical window and plots columns from a text file as the analysis progresses. The input file is typically the output of another recorder (for example, a :ref:`nodeRecorder`).

.. function:: recorder Plot $fileName $windowTitle $xLoc $yLoc $xPixels $yPixels -columns $xCol $yCol <-columns $xCol2 $yCol2 ...> <-dT $deltaT> <-rTolDt $rTol>
   :noindex:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileName, |string|, name of the file from which data is read
   $windowTitle, |string|, title displayed in the plot window
   $xLoc $yLoc, |integer|, screen coordinates of the top-left corner of the window (pixels)
   $xPixels $yPixels, |integer|, width and height of the plot window (pixels)
   $xCol $yCol, |integer|, column indices for the x and y axes (1-based)
   $deltaT, |float|, minimum time between plot updates (optional)
   $rTol, |float|, relative tolerance on $deltaT (optional, default 0.00001)

.. note::

   1. At least one ``-columns`` (or ``-cols`` / ``-col``) pair must be specified. Additional pairs may be supplied to overlay multiple curves.

   2. Column indices are 1-based. If the source recorder uses ``-time``, column 1 is typically time.

   3. This recorder requires a build with graphics support. It is available in the Tcl interpreter; there is no direct OpenSeesPy equivalent.

   4. The only way to save the plotted image is a screen capture.

   5. | The function returns a value:
      | SUCCESS: **>0** an integer tag that can be used as a handle to remove a recorder with the :ref:`remove` command.
      | FAILURE: **-1** recorder command failed (read the log)

.. admonition:: Example

   The following example plots column 2 (displacement) versus column 1 (time) from a node recorder output file.

   1. **Tcl Code**

   .. code-block:: tcl

      recorder Node -file node.out -time -node 1 -dof 2 disp
      recorder Plot node.out "Nodal Displacement" 10 10 400 400 -columns 1 2

Code developed by: |fmk|
