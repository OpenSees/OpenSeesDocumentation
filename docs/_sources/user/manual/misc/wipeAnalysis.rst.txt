.. _wipeAnalysis:

wipeAnalysis Command
********************

The wipeAnalysis command is used to remove all the analysis objects. 

.. function:: wipeAnalsyis

This command is needed for example when the user wishes to switch from a static analysis to a transient analysis, e.g. when switching from the initial gravity load analysis to an analysis of the subsequent response due to earthquake loading.

.. warning::
   * The time in the domain is not reset as in the :ref:`wipe`.
   * The state of the model does not change, i.e. the loads remain active and will change with subsequent analyze commands unless a :ref:`loadConst` is issued.
   * There is NO space between the wipe and Analysis. Putting a space results in domain and recorder objects also being remove, e.g. a :ref:`wipe`.

.. admonition:: Example:

   The following demonstrates the use of the wipe command.

   1. **Tcl Code**

   .. code-block:: none

      wipeAnalysis

   2. **Python Code**

   .. code-block:: python

      wipeAnalysis()


Code Developed by: |fmk|

