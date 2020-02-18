SP_Constraint Commands
**********************

Single point constraints (SP_Constraints) are constraints that define the response of a single degree-of-freedom at a node. These constraints can be homogeneous **(=0.0)** or non-homogeneos. Non homogeneous SP_Constraints, which define the non-zero response of the degree-of-freedom, can be constant or time varying. In the OpenSees interpreters there are a number of commands to add a homogeneous SP_Constraint.

.. toctree::
   :maxdepth: 1

   fix
   fixX
   fixY
   fixZ

Non-homogeneous constraints are added with wither :ref:`sp` or :ref:`imposedMotion commands inside the :ref:`plainPattern` or :ref:`multisupportExcitation` commands.

