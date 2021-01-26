.. _lblAnalysisCommands:

Analysis Commands
-----------------

In OpenSees, an analysis is an object which is composed by the aggregation of component objects. It is the component objects which define the type of analysis that is performed on the model. The component classes, as shown in the figure below, consist of the following:

#. Constraint Handler -- determines how the constraint equations are enforced in the analysis -- how it handles the boundary conditions/imposed displacements
#. DOF Numberer -- determines the mapping between equation numbers in the system of equation and the degrees-of-freedom at the nodes
#. SystemOfEqn & Solver -- it specifies how to store and solve the system of equations :math:`Ax=b`
#. Convergence Test -- determines when convergence has been achieved.
#. Solution Algorithm -- determines the sequence of steps taken to solve the non-linear equation at the current time step
#. Integrator -- determines the equations to solve, the predictive step, and how to update the response at the nodes given the solution to :math:`Ax=b`

.. figure:: figures/OpenSeesAnalysis.png
	:align: center
	:figclass: align-center

	OpenSees Analysis

.. toctree::
   :maxdepth: 1

   analysis/constraints
   analysis/numberer
   analysis/system
   analysis/test
   analysis/algorithm
   analysis/integrator
   analysis/analysis
   analysis/analyze
   analysis/eigen
   analysis/modalProperties
   analysis/responseSpectrum


