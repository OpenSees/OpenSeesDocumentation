.. _Series:

Series Material (Composite)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Series uniaxial material. It is a Composite-pattern aggregation of UniaxialMaterial objects in series: the same stress is carried by each component, and the combined strain and flexibility are determined by iterative state determination (same approach as in force-based beam elements).

.. function:: uniaxialMaterial Series $matTag $tag1 $tag2 ... $tagN <-iter $maxIter $tol>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $tag1 ..., |integer|,  tags of previously-defined UniaxialMaterial objects
   $maxIter,  |integer|, (optional) maximum iterations for state determination; default 1
   $tol,      |float|,    (optional) convergence tolerance; default 1e-10

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 100.0
      uniaxialMaterial Elastic 2 50.0
      uniaxialMaterial Series 3 1 2

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('Elastic', 2, 50.0)
      ops.uniaxialMaterial('Series', 3, 1, 2)

Code developed by: |mhs|
