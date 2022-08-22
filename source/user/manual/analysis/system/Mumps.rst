Mumps Solver
------------

This command is used to construct a sparse system of equations which uses the `Mumps <http://mumps-solver.org/>`_  solver. The following command is used to construct such a system:

.. function:: system Mumps

.. warning:: 

   It is presently limited to the parallel **OpenSeesSP** and **OpenSeesMP** applications.

.. admonition:: Example 

   The following example shows how to construct a sparse system solved using the Mumps solver.

   1. **Tcl Code**

   .. code-block:: tcl

      system Mumps

   2. **Python Code**

   .. code-block:: python

      system('Mumps')

Code developed by: |fmk|


