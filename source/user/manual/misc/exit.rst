.. _exit:

exit Command
************

This command is used to exit the program in a controlled way.

.. function:: exit

This command is used to terminate the application, invoking the necessary destructors on all the objects. This is needed for example to ensure files get closed and that the parallel interpreters shutdown correctly.

.. admonition:: Example:

   The following demonstrates the use of the exit command!

   1. **Tcl Code**

   .. code-block:: none

      exit

   2. **Python Code**

   .. code-block:: python

      exit()


Code Developed by: |fmk|
