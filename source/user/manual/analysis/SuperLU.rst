SuperLU System
--------------

This command is used to construct a SparseGEN linear system of equation object. As the name implies, this class is used for sparse matrix systems. The solution of the sparse matrix is carried out using .. `SuperLU <https://portal.nersc.gov/project/sparse/superlu/>`_. To following command is used to construct such a system:

.. function:: system SuperLU

.. note::

  1. When using the SuperLU system, the software will renumber the equations to ensure a fast solve. As a consequence it is a waste of time specifying anything but a Plain numberer.
  2. The original and still working command was ``system SparseGEN``

.. admonition:: Example 

   The following example shows how to construct a SuperLU system

   1. **Tcl Code**

   .. code-block:: tcl

      system SuperLU

   2. **Python Code**

   .. code-block:: python

      system('SuperLU')


Code developed by: |fmk|

.. [REFERENCES]

   James W. Demmel and Stanley C. Eisenstat and John R. Gilbert and Xiaoye S. Li and Joseph W. H. Liu, "A supernodal approach to sparse partial pivoting", SIAM J. Matrix Analysis and Applications, 20(3), 720-755, 1999.

