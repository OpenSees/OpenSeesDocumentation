.. _ParallelSection:

ParallelSection
^^^^^^^^^^^^^^^

This command constructs a section that acts in parallel with two or more existing sections. The resultant section deformation is the sum of the component section deformations, and the section forces are shared among the components.

.. function:: section Parallel $secTag $secTag1 $secTag2 ...

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag for the parallel section
   $secTag1 $secTag2 ..., |listInt|, tags of previously defined sections connected in parallel

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section Parallel 3 1 2

   2. **Python Code**

   .. code-block:: python

      ops.section('Parallel', 3, 1, 2)

Code Developed by: |mhs|
