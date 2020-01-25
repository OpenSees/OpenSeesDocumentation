.. _wipe:

wipe Command
************

This command is used to clear the domain objects, the recorders, and any analysis objects. It resets the time in the **Domain** to **0.0**.a

.. function:: wipe

This command is used to start over without having to exit and restart the interpreter. This is useful for example if you want to subject the model to multiple ground motions or subject different models to the same ground motion! It causes all elements, nodes, constraints, loads to be removed from the domain. In addition it deletes all recorders, analysis objects and all material objects created by the model builder. 

.. admonition:: Example:

   The following demonstrates the use of the wipe command.

   1. **Tcl Code**

   .. code-block:: none

      wipe

   2. **Python Code**

   .. code-block:: python

      wipe()


Code Developed by: |fmk|