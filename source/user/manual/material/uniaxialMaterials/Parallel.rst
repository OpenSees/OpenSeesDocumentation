.. _Parallel:

Parallel Material (Composite)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Parallel uniaxial material. It is a Composite-pattern aggregation of UniaxialMaterial objects acting in parallel: the same strain is applied to each component, and the combined stress and tangent are the (optionally weighted) sum of the component responses.

.. function:: uniaxialMaterial Parallel $matTag $tag1 $tag2 ... <-factors $fact1 $fact2 ...>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $tag1 ..., |integer|,  tags of previously-defined UniaxialMaterial objects
   $fact1 ..., |float|,  (optional) weighting factors; if omitted, all factors are 1

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 100.0
      uniaxialMaterial Elastic 2 50.0
      uniaxialMaterial Parallel 3 1 2

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('Elastic', 2, 50.0)
      ops.uniaxialMaterial('Parallel', 3, 1, 2)

Code developed by: |fmk| (ParallelModel); |mhs| (ParallelMaterial).
