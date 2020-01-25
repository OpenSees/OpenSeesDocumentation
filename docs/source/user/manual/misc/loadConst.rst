.. _loadConst:

loadConst Command
*****************

This command is used to set the loads constant in the domain and to also set the time in the domain. When setting the loads constant, the procedure will invoke setLoadConst() on all LoadPattern objects which exist in the domain at the time the command is called.

.. function::  loadConst <-time $pseudoTime>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $pseudoTime, |float|, Time domain is to be set to (optional)

.. note::
   
   Load Patterns added afer this command is invoked are not set to constant.


.. admonition:: Example:

   The following examples demonstrate the command to set the loads constant and to also rest the time to 0.0, which is the most common use of the command.

   1. **Tcl Code**

   .. code-block:: tcl

      loadConst -time 0.0

   2. **Python Code**

   .. code-block:: python

      loadConst('-time',0.0)


Code Developed by: |fmk|



Code Developed by: |fmk|