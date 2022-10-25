.. _NewtonLineSearch:

Newton Line Search Algorithm
----------------
This command is used to construct a NewtonLineSearch algorithm object which introduces line search to the Newton-Raphson algorithm to solve the nonlinear residual equation. Line search increases the effectiveness of the Newton method when convergence is slow due to roughness of the residual. The command is of the following form: 

.. function:: algorithm NewtonLineSearch <-type $typeSearch> <-tol $tol> <-maxIter $maxIter> <-minEta $minEta> <-maxEta $maxEta> 

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $typeSearch, |string|,  Line Search Algorithm. Optional Default is InitialInterpolated. Valid Types are: Bisection Secant RegulaFalsi
   InitialInterpolated.
   $tol, |float|,  tolerance for search. optional. The default is 0.8.
   $maxIter, |integer|, maximum number of iteration to try. The default is 10.
   $minEta, |float|, a minimum :math:`\eta` value. Optional; The default is 0.1
   $maxEta, |float|, a maximum :math:`\eta` value. Optional; The default is 10.0

Theory
^^^^^^^^^^^^^^

The rationale behind line search is that:
    1. The direction behind :math:`\delta_U` found by the Newton-Raphson method is often a good direction, but the step size :math:`\Delta_U` is not.
    2. It is cheaper to compute the residual for several point along :math:`\Delta_U` rather than form and factor a new system Jacobian.

In NewtonLineSearch, the regular Newton-Raphson method is used to compute the :math:`\Delta_U` but the update that is used is modified.. The modified update is:

:math:`U_{n+1} = U_n + \eta \delta_U`


The different line search algorithms use different root finding methods to obtain <math>\eta\,\!</math>, a root to the function <math>s(\eta)</math> defined as: 

:math:`s_\eta = \delta_U R(U_{n} + \eta \delta_U)`

with
:math:`s_0 = \delta-U R(U_n)`

Code Developed by: |fmk|
