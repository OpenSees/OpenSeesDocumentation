.. _eigen:

eigen Command
*************

This command is used to perform the eigenvalue analysis.

.. function:: eigen <type> <$solver> $numEigenvalues

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
   $numEigenvalues, |integer|, number of eigenvalues required.
   $solver, |string|, "optional string detailing type of solver: -genBandArpack (default), -fullGenLapack, -symmBandLapack. Python users may also use the :ref:`PythonSparse eigenvalue solver <eigenPythonSparse>`."
   $type, |string|, optional string indicating type of eigenvalue problem to solve: 'general' (default) or 'standard'

.. admonition:: Returns
   
   A list containing the eigenvalues


.. note::
   1.  The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
   2.  The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.
   3. The -symmBandLapack option works only standard eigenvalue analysis of the stiffness matrix, i.e., K*x = lam*x
   4.  **Python users:** A :ref:`PythonSparse eigenvalue solver <eigenPythonSparse>` is available as well (OpenSeesPy only).


.. warning::

   The default eigen solver utilizes **ARPACK**, an iterative eigenvalue solver. Like other iterative methods, ARPACK can struggle to accurately compute eigenvectors when the model contains repeated (degenerate) eigenvalues or clusters of very closely spaced eigenvalues. The issue arises from difficulties in forming an orthonormal basis for the eigenspace numerically.

   In such cases, ARPACK may fail to find all of the requested eigenvalues, or it may return correct eigenvalues but incorrect eigenvectors. When **modal** damping is used, inaccurate eigenvectors may cause issues with the damping forces calculated. If you are unsure if this is an issue with your model, switch the **solver** used and check the reslts again -- this check works as the eigenvectors will vary greatly with the chosen solver when this issue exists.

   Fortunately, small adjustments to the **model** can prevent this numerical issue. In actuality, as material properties (e.g., Young’s modulus) or nodal masses are rarely identical and by introducing slight variations in your model, ARPACK is more likely to form the basis correctly.

   As an illustration of the problem, consider the following script (provided by mhscott):


   .. code::

      model Basic -ndm 1 -ndf 1
      node 0 0; fix 0 1
      node 1 0; mass 1 1.0
      node 2 0; mass 2 1.0
      node 3 0; mass 3 1.0
      node 4 0; mass 4 1.0

      set k 610
      uniaxialMaterial Elastic 1 $k

      element zeroLength 1 0 1 -mat 1 -dir 1
      element zeroLength 2 1 2 -mat 1 -dir 1
      element zeroLength 3 0 3 -mat 1 -dir 1
      element zeroLength 4 3 4 -mat 1 -dir 1

      systetm ProfileSPD
      numberer RCM
      
      set nModes 2
      set eigV [eigen $nModes]
      puts "Eigenvalues: $eigV"

      # print eigenvectors
      for {set i 1} {$i <= 4} {incr i 1}  {
         puts "$i [nodeEigenvector $i 1] [nodeEigenvector $i 2]"
      }


   will produce:

   .. code::
      
      Eigenvalues:  232.99926686256409880116   232.99926686256412722287  
      1    0.50235827201282656773    0.15501409223134476889
      2    0.81283275864641846287    0.25081806996552691302
      3    0.15501409223134465787   -0.50235827201282667875
      4    0.25081806996552685751   -0.81283275864641857389
   
   wheras if I change the mass at node **4** using:

   .. code::
      
      node 4 0; mass 4 1.0000000001   

   I would get:
   
   .. code::

      Eigenvalues:  232.99926679816474006657   232.99926686256424090971  
      1   -0.00000004574590262152    0.52573111211913170493
      2   -0.00000007401842538890    0.85065080835203654708
      3    0.52573111211146139610    0.00000004574590273254
      4    0.85065080819431726500    0.00000007401842544441
   

   For this in an academic setting dealing with small problems, the **-fullGenLapack** option will provide correct eigenvalues and eigenvectors to the original problem:

   .. code::   
      set eigV [eigen $nModes]

   will produce:
   
   .. code::
      
      Eigenvalues:   232.99926684570411339337   232.99926686256412722287  
      1    0.00000000000000000000   -0.52573111211913370333
      2    0.00000000000000000000   -0.85065080835203987775
      3    0.52573111209361389484    0.00000000000000000000
      4    0.85065080832527950605   -0.00000000000000000000
      
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

      # obtain 10 eigenvalues of the stiffness matrix
      set eigenvalues [eigen standard -symmBandLapack 10]

   2. **Python Code**

   .. code:: python

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      eigenvalues = eigen(10)
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      eigenvalues = eigen('-fullGenLapack', 10)

      # obtain 10 eigenvalues of the stiffness matrix
      eigenvalues = eigen('standard','-symmBandLapack',10)

      # PythonSparse: use a custom Python solver (e.g., SciPy eigsh)
      eigenvalues = eigen('PythonSparse', 10, {'solver': solver, 'scheme': 'CSR'})

PythonSparse Eigenvalue Solver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _eigenPythonSparse:

The **PythonSparse** eigen solver delegates the generalized eigenvalue problem :math:`\mathbf{K}\phi = \lambda \mathbf{M}\phi` to user-defined Python objects. Sparse stiffness (K) and mass (M) matrix buffers are exposed via zero-copy memoryviews, enabling the use of SciPy, CuPy, or custom eigensolvers without recompiling OpenSees. See :ref:`example below <eigenPythonSparseExample>` for a SciPy eigsh implementation.

.. function:: eigen PythonSparse $numEigenvalues <dict>?

   Perform eigenvalue analysis using a user-defined Python solver. The dict is the solver configuration; keys below.

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 12, 15, 53

   $numEigenvalues, int, Number of eigenvalues (and eigenvectors) to compute.
   dict, dict, Solver configuration; see dict options table below.

.. csv-table::
   :header: "Key", "Type", "Description"
   :widths: 12, 15, 53

   solver, Python object, "A Python object with a ``solve(**kwargs)`` method. Required."
   scheme, string, "Sparse format: ``'CSR'``, ``'CSC'``, ``'COO'``. Default: ``'CSR'``."

.. note::

   The PythonSparse eigen interface is available only when using the Python interpreter (OpenSeesPy).

The solver object must implement a ``solve(**kwargs)`` method. OpenSees passes the matrix data as keyword arguments: memoryviews (buffer-like objects) for arrays, and scalars for metadata. Use `numpy.frombuffer <https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html>`_ to interpret memoryviews as NumPy arrays without copying. The structure format depends on ``scheme``:

**CSR/CSC format** — compressed storage uses ``index_ptr`` and ``indices``:

.. csv-table::
   :header: "Keyword", "Type", "Description"
   :widths: 18, 15, 47

   index_ptr, memoryview, "Row pointers (CSR) or column pointers (CSC), int32."
   indices, memoryview, "Column indices (CSR) or row indices (CSC), int32."
   k_values, memoryview, "Stiffness matrix K coefficients (float64)."
   m_values, memoryview, "Mass matrix M coefficients (float64)."
   eigenvalues, memoryview, "Output buffer for eigenvalues (float64, writable). Write *in place*."
   eigenvectors, memoryview, "Output buffer for eigenvectors (float64, writable). Write *in place*, row-major: mode 0, mode 1, ..."
   num_eqn, int, "Number of equations."
   nnz, int, "Number of nonzeros (K and M share sparsity pattern)."
   matrix_status, string, "``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``."
   storage_scheme, string, "``'CSR'``, ``'CSC'``, or ``'COO'``."
   num_modes, int, "Number of modes requested."
   generalized, bool, "True for generalized (K, M); False for standard (K only)."
   find_smallest, bool, "True: smallest eigenvalues (e.g., frequency); False: largest."

**COO format** — coordinate storage uses ``row_indices`` and ``col_indices`` instead of ``index_ptr``/``indices``:

.. csv-table::
   :header: "Keyword", "Type", "Description"
   :widths: 18, 15, 47

   row_indices, memoryview, "Row indices for each nonzero, int32 (COO only)."
   col_indices, memoryview, "Column indices for each nonzero, int32 (COO only)."
   k_values, memoryview, "Stiffness matrix K coefficients (float64)."
   m_values, memoryview, "Mass matrix M coefficients (float64)."
   eigenvalues, memoryview, "Output buffer for eigenvalues (float64, writable). Write *in place*."
   eigenvectors, memoryview, "Output buffer for eigenvectors (float64, writable). Write *in place*."
   num_eqn, int, "Number of equations."
   nnz, int, "Number of nonzeros."
   matrix_status, string, "``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``."
   storage_scheme, string, "``'COO'``."
   num_modes, int, "Number of modes requested."
   generalized, bool, "True for generalized (K, M); False for standard (K only)."
   find_smallest, bool, "True: smallest eigenvalues; False: largest."

The ``solve`` method should return ``None`` on success, or raise an exception on failure.

.. warning:: **In-place output required**

   You **must** write eigenvalues and eigenvectors directly into the ``eigenvalues`` and ``eigenvectors`` buffers. OpenSees reads from these buffers; it does **not** use return values.

   **Do:** Use in-place assignment, e.g. ``np.frombuffer(eigenvalues, ...)[:] = eigvals`` and ``np.frombuffer(eigenvectors, ...)[:] = eigvecs.T.flatten()``

   **Do not:** Return the results or assign to new arrays without copying back into the buffers. OpenSees will use uninitialized or stale data.

.. _eigenPythonSparseExample:

.. admonition:: Example — SciPy Generalized Eigenvalue Solver

   This example uses `SciPy <https://scipy.org/>`_ and its `eigsh <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.eigsh.html>`_ (ARPACK symmetric eigensolver) to solve the generalized eigenvalue problem:

   .. code-block:: python

      import numpy as np
      import scipy.sparse as sp
      import scipy.sparse.linalg as sp_linalg
      import openseespy.opensees as ops

      class SciPyGeneralizedEigenSolver:
          def __init__(self, maxiter=None, tol=0.0):
              self.maxiter = maxiter
              self.tol = tol
              self._k_matrix = None
              self._m_matrix = None

          def solve(self, **kwargs):
              index_ptr = kwargs['index_ptr']
              indices = kwargs['indices']
              k_values = kwargs['k_values']
              m_values = kwargs['m_values']
              eigenvalues = kwargs['eigenvalues']
              eigenvectors = kwargs['eigenvectors']
              num_eqn = kwargs['num_eqn']
              nnz = kwargs['nnz']
              matrix_status = kwargs['matrix_status']
              num_modes = kwargs['num_modes']
              find_smallest = kwargs['find_smallest']

              indptr = np.frombuffer(index_ptr, dtype=np.int32, count=num_eqn + 1)
              idx = np.frombuffer(indices, dtype=np.int32, count=nnz)
              k_data = np.frombuffer(k_values, dtype=np.float64, count=nnz)
              m_data = np.frombuffer(m_values, dtype=np.float64, count=nnz)

              if matrix_status == 'STRUCTURE_CHANGED' or self._k_matrix is None:
                  self._k_matrix = sp.csr_matrix((k_data, idx, indptr),
                                                shape=(num_eqn, num_eqn))
                  self._m_matrix = sp.csr_matrix((m_data, idx, indptr),
                                                shape=(num_eqn, num_eqn))
              elif matrix_status == 'COEFFICIENTS_CHANGED':
                  self._k_matrix.data[:] = k_data
                  self._m_matrix.data[:] = m_data

              eigsh_kwargs = {
                  'k': num_modes,
                  'M': self._m_matrix,
                  'which': 'LM',
              }
              if find_smallest:
                  eigsh_kwargs['sigma'] = 0.0
              if self.maxiter is not None:
                  eigsh_kwargs['maxiter'] = self.maxiter
              if self.tol > 0.0:
                  eigsh_kwargs['tol'] = self.tol

              eigvals, eigvecs = sp_linalg.eigsh(self._k_matrix, **eigsh_kwargs)

              np.frombuffer(eigenvalues, dtype=np.float64,
                            count=num_modes)[:] = eigvals[:num_modes]
              np.frombuffer(eigenvectors, dtype=np.float64,
                            count=num_modes * num_eqn)[:] = eigvecs.T.flatten()

              return None

      solver = SciPyGeneralizedEigenSolver()
      eigenvalues = ops.eigen('PythonSparse', 10, {'solver': solver, 'scheme': 'CSR'})

.. seealso::

   * :ref:`systemPythonSparse` — PythonSparse interface for linear systems
   * The `EXAMPLES/SolverBenchmark <https://github.com/OpenSees/OpenSees/blob/master/EXAMPLES/SolverBenchmark/benchmark_python_sparse_eigen.py>`_ script demonstrates the PythonSparse eigen solver.

Code Developed by: |fmk|
