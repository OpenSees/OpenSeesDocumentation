ProfileSPD System
-----------------

This command is used to construct a ProfileSPD linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems. The matrix is stored as shown below in a 1 dimensional array with only those values below the first non-zero row in any column being stored. This is sometimes also referred to as a skyline storage scheme. The following command is used to construct such a system:

.. function:: system ProfileSPD

An n×n matrix A= is a symmetric positive definite matrix if:

1. :math:`a_{i,j} = a_{j,i}`
2. :math:`y^T A y != 0` for all non-zero vectors y with real entries (:math:`y \in \mathbb{R}^n`).

In the skyline or profile storage scheme only the entries below the first no-zero row entry in any column are stored if storing by rows: The reason for this is that as no reordering of the rows is required in gaussian eleimination because the matrix is SPD, no non-zero entries will ocur in the elimination process outside the area stored.

For example, a symmetric 6-by-6 matrix with a structure as shown below:

.. math::

     \begin{bmatrix}
     A_{11} & A_{12} & 0      &   0    & 0     \\
     & A_{22}  & A_{23}  &  0     & A_{25} \\
     &         & A_{33}  & 0      & 0     \\
     &         &         & A_{44} & A_{45} \\
     & sym     &         &        & A_{55} 
     \end{bmatrix}

The matrix is stored as 1-d array

.. math::

   \begin{bmatrix}
   A_{11} & A_{12} & A_{22} & A_{23} & A_{33} & A_{44} & A_{25} &  0 & A_{45} & A_{55} 
   \end{bmatrix}

with a further array containing indices of diagonal elements:

.. math::

   \begin{bmatrix}
   1 & 3 & 5 & 6 & 10 
   \end{bmatrix}

.. admonition:: Example 

   The following example shows how to construct a ProfileSPD system

   1. **Tcl Code**

   .. code-block:: tcl

      system ProfileSPD


   2. **Python Code**

   .. code-block:: python

      system('ProfileSPD')

Code Developed by: |fmk|
