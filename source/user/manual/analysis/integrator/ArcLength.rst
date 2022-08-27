.. _ArcLengthControl:

Arc-Length Control
--------------------------------
.. function:: integrator ArcLength $s $alpha 

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $s
     - |float|
     - the arcLength
   * - $alpha
     - |float|
     - a scaling factor on the reference loads. 
 

This command is used to construct an ArcLength integrator object. In an analysis step with ArcLength we seek to determine the time step that will result in our constraint equation being satisfied. 