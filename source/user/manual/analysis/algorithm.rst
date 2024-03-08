.. _algorithm:

algorithm Command
*****************

This command is used to construct a SolutionAlgorithm object, which determines the sequence of steps taken to solve the non-linear equation.

.. function:: algorithm algorithmType? arg1? ...

The type of solution algorithm created and the additional arguments required depends on the algorithmType? provided in the command.


The following contain information about algorithmType? and the args required for each of the available algorithm types:

.. toctree::

   algorithm/LinearAlgorithm
   algorithm/Newton
   algorithm/NewtonLineSearch
   algorithm/ModifiedNewton
   algorithm/KrylovNewton
   algorithm/SecantNewton
   algorithm/BFGS
   algorithm/Broyden
   algorithm/ExpressNewton

