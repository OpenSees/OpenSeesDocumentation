.. _eigen:

eigen Command
*************

This command is used to perform the eigenvalue analysis.

.. function:: eigen <$solver> $numEigenvalues

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
   $numEigenvalues, |integer|, number of eigenvalues required.
   $solver, |string|, "optional string detailing type of solver: -genBandArpack, -symmBandLapack, -fullGenLapack (default: -genBandArpack)."

.. admonition:: Returns
   
   A list containing the eigenvalues


.. note::
   1.  The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
   2.  The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.

Theory
^^^^^^
|  A *generalized eigenvalue problem* for two symmetric matrices :math:`K` and :math:`M` of size :math:`n \times n` is given by:

.. math::
   \left (K - \lambda M \right ) \Phi = 0

|  where:
   
   *  :math:`K` is the stiffness matrix
   *  :math:`M` is the mass matrix
   *  :math:`\lambda` is the eigenvalue
   *  and :math:`\Phi` is the associated eigenvector

.. admonition:: Example
   
   The following example shows how to use the eigen command to obtain a list of eigenvalues.

   1. **Tcl Code**
   
   .. code:: tcl

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      set eigenvalues [eigen 10]
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      set eigenvalues [eigen -fullGenLapack 10]

   2. **Python Code**

   .. code:: python

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      eigenvalues = eigen(10)
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      eigenvalues = eigen('-fullGenLapack', 10)

Code Developed by: |fmk|
