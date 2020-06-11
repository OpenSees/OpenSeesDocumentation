FullGeneral System
------------------

This command is used to construct a Full General linear system of equation object. As the name implies, the class utilizes NO space saving techniques to cut down on the amount of memory used. If the matrix is of size, nxn, then storage for an nxn array is sought from memory when the program runs. When a solution is required, the Lapack routines DGESV and DGETRS are used. The following command is used to construct such a system:

.. function:: system FullGeneral

.. warning::
   1. This type of system should almost never be used in production! This is because it requires a lot more memory than every other solver and takes more time in the actual solving operation than any other solver. 
   2. It is required if the user is interested in looking at the global system matrix, using the **printA** command

.. admonition:: Example 

   The following example shows how to construct a FullGeneral system

   1. **Tcl Code**

   .. code-block:: tcl

      system FullGeneral


   2. **Python Code**

   .. code-block:: python

      system('FullGeneral')

Code Developed by: |fmk|