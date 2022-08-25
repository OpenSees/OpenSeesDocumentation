Reverse Cuthill McKee Numberer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an RCM degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. An RCM numberer uses the reverse Cuthill-McKee scheme to order the matrix equations. The command to construct an RCM numberer is a follows:

.. function:: numberer RCM

.. note::

   For very small problems and for the sparse matrix solvers which provide their own numbering scheme, order is not really important so plain numberer is just fine. For large models and analysis using solver types other than the sparse solvers, the order will have a major impact on performance of the solver and the plain handler is a poor choice.

.. admonition:: Example 

   The following example shows how to construct a reverse Cuthill-McKee numberer.

   1. **Tcl Code**

   .. code-block:: tcl

      numberer RCM


   2. **Python Code**

   .. code-block:: python

      numberer('RCM')

.. [REFERNCES]

   E. Cuthill and J. McKee. Reducing the bandwidth of sparse symmetric matrices In Proc. 24th Nat. Conf. ACM, pages 157–172, 1969.

   J. A. George and J. W-H. Liu, Computer Solution of Large Sparse Positive Definite Systems, Prentice-Hall, 1981


Code Developed by: |fmk|
