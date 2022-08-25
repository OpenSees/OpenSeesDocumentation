Umfpack System
--------------

This command is used to construct a sparse system of equations which uses the `UmfPack <https://people.sc.fsu.edu/~jburkardt/cpp_src/umfpack/umfpack.html>`_  solver. The following command is used to construct such a system:

.. function:: system Umfpack <-lvalueFact $LVALUE>

(LVALUE*the number of nonzero entries) is the amount of additional memory set aside for fill in during the matrix solution, by default the LVALUE factor is 10. You only need to experiment with this if you get error messages back about LVALUE being too small.

.. admonition:: Example 

   The following example shows how to construct a SuperLU system

   1. **Tcl Code**

   .. code-block:: tcl

      system Umfpack

   2. **Python Code**

   .. code-block:: python

      system('Umfpack')


Code developed by: |fmk|

.. [REFERNCES]

   1. A column pre-ordering strategy for the unsymmetric-pattern multifrontal method, T. A. Davis, ACM Transactions on Mathematical Software, vol 30, no. 2, June 2004, pp. 165-195.

   2. Algorithm 832: UMFPACK, an unsymmetric-pattern multifrontal method, T. A. Davis, ACM Transactions on Mathematical Software, vol 30, no. 2, June 2004, pp. 196-199.

   3. A combined unifrontal/multifrontal method for unsymmetric sparse matrices, T. A. Davis and I. S. Duff, ACM Transactions on Mathematical Software, vol. 25, no. 1, pp. 1-19, March 1999.
   
   4. An unsymmetric-pattern multifrontal method for sparse LU factorization, T. A. Davis and I. S. Duff, SIAM Journal on Matrix Analysis and Applications, vol 18, no. 1, pp. 140-158, Jan. 1997.
   