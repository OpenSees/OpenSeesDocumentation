.. _AutoConstraintHandler:

Auto Constraint Handler
^^^^^^^^^^^^^^^^^^^^^^^

| This command is used to construct an Auto constraint handler.
| This handler combines the advantages of both the Transformation and the Penalty methods.
| In the current implementation, single-point constraints are handled with the Transformation method, while multi-point constraints are handled with the Penalty method.
| The following is the command to construct such a constraint handler:

.. function:: constraints Auto <-verbose> <-autoPenalty $oom> <-userPenalty $userPenalty>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

     -verbose, |string|, "(optional, default = not-defined) If defined, OpenSees will report some debug information."
     -autoPenalty $oom, |string| + |float|, "(optional, default = -autoPenalty defined, oom = 3). With this option, each multi-point constraint will be assigned an automatic penalty value :math:`\alpha_M=10^{koom + oom}`, where :math:`koom=round(\log_{10}(K))` is the approximate order-of-magnitute of the (initial) stiffness matrix at the nodes involved in the multi-point constraint."
     -userPenalty $userPenalty, |string| + |float|, "(optional, default = note-defined). If defined, a uniform penalty parameter :math:`\alpha_M=userPenalty` will be used for all multi-point constraints"

.. admonition:: Example 1

   The following example shows how to construct an Auto Method constraint handler with the default settings: automatic penalty values computed for each multi-point constraints

   1. **Tcl Code**

   .. code-block:: tcl

      constraints Auto


   2. **Python Code**

   .. code-block:: python

      constraints('Auto')

.. admonition:: Example 2

   The following example shows how to construct an Auto Method constraint handler with extra settings to print debug information (-verbose) and to compute penalty values for each constraints as 4 order-of-magnitute larger than the stiffness found on the nodes involved in each multi-point constraint.

   1. **Tcl Code**

   .. code-block:: tcl

      constraints Auto -verbose -autoPenalty 4


   2. **Python Code**

   .. code-block:: python

      constraints('Auto', '-verbose', '-autoPenalty', 4)

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
