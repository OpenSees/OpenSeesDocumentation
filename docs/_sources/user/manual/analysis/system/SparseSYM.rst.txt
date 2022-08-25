SparseSYM Solver
----------------

This command is used to construct a sparse symmetric system of equations which uses a row-oriented solution method in the solution phase. The following command is used to construct such a system:

.. function:: system SparseSYM

.. note:: 

   Versions of OpenSees up to and including 2.2.0 used SparseSPD instead of SparseSYM as the option to create this system. The code is more general than the SPD moniker implies, working for negative definite as well as positive definite. For backward compatibility this old option continues to work.

.. admonition:: Example 

   The following example shows how to construct a SparseSYM system:

   1. **Tcl Code**

   .. code-block:: tcl

      system SparseSYM

   2. **Python Code**

   .. code-block:: python

      system('SparseSYM')

Code developed by: `J. Peng <https://www.linkedin.com/in/james-peng-a6194b13/>`_

.. [REFERENCES]

Kincho H. Law and David R. McKay, “A Parallel Row-Oriented Sparse Solution Method for Finite Element Structural Analysis,” International Journal for Numerical Methods in Engineering, 36:2895-2919, 1993.
