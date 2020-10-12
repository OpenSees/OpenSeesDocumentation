.. _LinearAlgorithm:

Linear Algorithm
----------------

This command is used to construct a Linear algorithm object which takes one iteration to solve the system of equations.

.. function:: algorithm Linear <-initial> <-factorOnce>


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   -initial, |string|,  optional flag to indicate to use initial stiffness
   -factorOnce, |string|, optional flag to indicate to only set up and factor matrix once

.. note:: 
   
   As the tangent matrix typically will not change during the analysis in case of an elastic system it is highly advantageous to use the -factorOnce option. Do not use this option if you have a nonlinear system and you want the tangent used to be actual tangent at time of the analysis step.

   The Linear algorithm REQUIRES NO :ref:`test` and will complain if one is provided. This means that convergence is not checked.

   Certain transient explicit :ref:`integration` schemes require a Linear algorithm.

.. admonition:: Example:

   The following examples demonstrate the command to create a Linear solution algorithm.

   1. **Tcl Code**

   .. code-block:: tcl

      algorithm Linear

   2. **Python Code**

   .. code-block:: python

      algorithm('Linear')


Code Developed by: |fmk|
