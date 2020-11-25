.. _system:

system Command
**************

This command is used to construct the ``LinearSOE`` and ``LinearSolver`` objects to store and solve the system of equations, :math:`Ax=b` during each step.

.. function:: system systemType? arg1? ...

The type of ``LinearSOE`` created and the additional arguments required depends on the ``systemType``? provided in the command.

The following contain information about systemType? and the args required for each of the available system types:

.. toctree::

   BandGeneral
   BandSPD
   ProfileSPD
   SuperLU
   Umfpack
   FullGeneral
   SparseSYM
   Mumps
   Cusp
