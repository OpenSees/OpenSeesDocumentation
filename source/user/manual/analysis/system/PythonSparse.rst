.. _systemPythonSparse:

PythonSparse System
------------------

The **PythonSparse** system delegates linear system solves (:math:`\mathbf{A}\mathbf{x} = \mathbf{b}`) to user-defined Python objects. Sparse matrix buffers (CSR, CSC, or COO format) are exposed to Python via zero-copy memoryviews, enabling efficient integration with SciPy, CuPy, nvmath, or custom solvers without writing C++ wrappers or recompiling OpenSees. See :ref:`CuPy (GPU) <pythonSparseExampleCupy>` and :ref:`SciPy (CPU) <pythonSparseExampleScipy>` examples below.

.. function:: system PythonSparse <dict>?

   Create a linear system that forwards sparse matrix data to a Python solver object. The dict is the solver configuration; see table below.

.. csv-table::
   :header: "Key", "Type", "Description"
   :widths: 12, 15, 53

   solver, Python object, "A Python object with a ``solve(**kwargs)`` method. Required."
   scheme, string, "Sparse format: ``'CSR'``, ``'CSC'``, ``'COO'``. Default: ``'CSR'``."
   writable, string or list, "Buffers the solver may modify: ``'values'`` (matrix coefficients), ``'rhs'`` (right-hand side), ``'values,rhs'`` or ``'all'``, or ``'none'``. Also accepts list form: ``['values', 'rhs']``. Default: ``'none'`` — only the solution buffer ``x`` is writable."

.. note::

   The PythonSparse interface is available only when using the Python interpreter (OpenSeesPy). Enabling ``writable`` for ``values`` or ``rhs`` allows in-place updates of the stiffness matrix and right-hand side vector; use only if you know what you are doing.

The solver object must implement a ``solve(**kwargs)`` method. OpenSees passes the matrix data as keyword arguments: memoryviews (buffer-like objects) for arrays, and scalars for metadata. Use `numpy.frombuffer <https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html>`_ to interpret memoryviews as NumPy arrays without copying. The structure format depends on ``scheme``:

**CSR/CSC format** — compressed storage uses ``index_ptr`` and ``indices``:

.. csv-table::
   :header: "Keyword", "Type", "Description"
   :widths: 18, 15, 47

   index_ptr, memoryview, "Row pointers (CSR) or column pointers (CSC), int32."
   indices, memoryview, "Column indices (CSR) or row indices (CSC), int32."
   values, memoryview, "Matrix coefficients (float64)."
   rhs, memoryview, "Right-hand side vector (float64)."
   x, memoryview, "Solution buffer (float64, writable). Write the solution *in place*."
   num_eqn, int, "Number of equations."
   nnz, int, "Number of nonzeros."
   matrix_status, string, "``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``."
   storage_scheme, string, "``'CSR'``, ``'CSC'``, or ``'COO'`` — which format was used."

**COO format** — coordinate storage uses ``row`` and ``col`` instead of ``index_ptr``/``indices``:

.. csv-table::
   :header: "Keyword", "Type", "Description"
   :widths: 18, 15, 47

   row, memoryview, "Row indices for each nonzero, int32 (COO only)."
   col, memoryview, "Column indices for each nonzero, int32 (COO only)."
   values, memoryview, "Matrix coefficients (float64)."
   rhs, memoryview, "Right-hand side vector (float64)."
   x, memoryview, "Solution buffer (float64, writable). Write the solution *in place*."
   num_eqn, int, "Number of equations."
   nnz, int, "Number of nonzeros."
   matrix_status, string, "``'UNCHANGED'``, ``'COEFFICIENTS_CHANGED'``, or ``'STRUCTURE_CHANGED'``."
   storage_scheme, string, "``'COO'``."

The ``solve`` method should return ``0`` on success, or a negative value to indicate failure.

.. warning:: **In-place output required**

   You **must** write the solution directly into the ``x`` buffer. OpenSees uses this buffer; it does **not** use return values or new arrays.

   **Do:** Use in-place assignment, e.g. ``np.frombuffer(x, dtype=np.float64, count=num_eqn)[:] = result``

   **Do not:** Return the solution, assign to a new variable, or write to a copy. The result will be ignored and the analysis will use uninitialized or stale data.

.. _pythonSparseExampleCupy:

.. admonition:: Example — CuPy Conjugate Gradient (GPU)

   This example uses `CuPy <https://cupy.dev/>`_ and its `cg <https://docs.cupy.dev/en/stable/reference/generated/cupyx.scipy.sparse.linalg.cg.html>`_ (conjugate gradient) solver to solve the linear system on an NVIDIA GPU. Note the use of ``np.frombuffer(array, dtype)[:] = result`` to write the solution in place:

   .. code-block:: python

      import numpy as np
      import cupy as cp
      import cupyx.scipy.sparse.linalg
      import openseespy.opensees as ops

      class CuPyCGSolver:
          def __init__(self, rtol=1e-5, atol=1e-12, maxiter=None):
              self.rtol = rtol
              self.atol = atol
              self.maxiter = maxiter
              self.A = None

          def solve(self, **kwargs):
              index_ptr = kwargs['index_ptr']
              indices = kwargs['indices']
              values = kwargs['values']
              rhs = kwargs['rhs']
              x = kwargs['x']
              num_eqn = kwargs['num_eqn']
              nnz = kwargs['nnz']
              matrix_status = kwargs['matrix_status']

              indptr = np.frombuffer(index_ptr, dtype=np.int32, count=num_eqn + 1)
              idx = np.frombuffer(indices, dtype=np.int32, count=nnz)
              vals = np.frombuffer(values, dtype=np.float64, count=nnz)

              if matrix_status == 'STRUCTURE_CHANGED' or self.A is None:
                  self.A = cp.sparse.csr_matrix(
                      (cp.asarray(vals), cp.asarray(idx), cp.asarray(indptr)),
                      shape=(num_eqn, num_eqn)
                  )
              elif matrix_status == 'COEFFICIENTS_CHANGED':
                  self.A.data[:] = cp.asarray(vals)

              rhs_gpu = cp.asarray(np.frombuffer(rhs, dtype=np.float64, count=num_eqn))
              x_gpu, info = cupyx.scipy.sparse.linalg.cg(
                  self.A, rhs_gpu, tol=self.rtol, atol=self.atol, maxiter=self.maxiter
              )

              np.frombuffer(x, dtype=np.float64, count=num_eqn)[:] = cp.asnumpy(x_gpu)
              return -int(info)

      solver = CuPyCGSolver(rtol=1e-8, atol=1e-12, maxiter=1000)
      ops.system('PythonSparse', {'solver': solver, 'scheme': 'CSR'})

.. _pythonSparseExampleScipy:

.. admonition:: Example — SciPy Direct Solve (CPU)

   This example uses `SciPy <https://scipy.org/>`_ and its `factorized <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.factorized.html>`_ (sparse LU factorization) for a direct solve on CPU:

   .. code-block:: python

      import numpy as np
      import scipy.sparse as sp
      import scipy.sparse.linalg as sp_linalg
      import openseespy.opensees as ops

      class SciPyspSolveSolver:
          def __init__(self):
              self.A = None
              self._solve_func = None

          def solve(self, **kwargs):
              index_ptr = kwargs['index_ptr']
              indices = kwargs['indices']
              values = kwargs['values']
              rhs = kwargs['rhs']
              x = kwargs['x']
              num_eqn = kwargs['num_eqn']
              nnz = kwargs['nnz']
              matrix_status = kwargs['matrix_status']

              indptr = np.frombuffer(index_ptr, dtype=np.int32, count=num_eqn + 1)
              idx = np.frombuffer(indices, dtype=np.int32, count=nnz)
              vals = np.frombuffer(values, dtype=np.float64, count=nnz)

              if matrix_status != 'UNCHANGED' or self._solve_func is None:
                  self.A = sp.csr_matrix((vals.copy(), idx.copy(), indptr.copy()),
                                        shape=(num_eqn, num_eqn))
                  self._solve_func = sp_linalg.factorized(self.A)

              rhs_arr = np.frombuffer(rhs, dtype=np.float64, count=num_eqn)
              x_arr = np.frombuffer(x, dtype=np.float64, count=num_eqn)
              x_arr[:] = self._solve_func(rhs_arr)
              return 0

      solver = SciPyspSolveSolver()
      ops.system('PythonSparse', {'solver': solver, 'scheme': 'CSR'})

Code developed by: `gaaraujo <https://github.com/gaaraujo>`_

.. seealso::

   * :ref:`eigenPythonSparse` — PythonSparse interface for generalized eigenvalue problems
   * The `EXAMPLES/SolverBenchmark <https://github.com/OpenSees/OpenSees/blob/master/EXAMPLES/SolverBenchmark/benchmark_python_sparse.py>`_ script in the OpenSees repository benchmarks PythonSparse against native solvers.
