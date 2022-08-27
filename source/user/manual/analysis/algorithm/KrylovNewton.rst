.. _KrylovNewton:

Krylov-Newton Algorithm
--------------------------------
.. function:: algorithm KrylovNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim> 

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $tangIter
     - |string|
     - tangent to iterate on, options are current, initial, noTangent. default is current. 
   * - $tangIncr
     - |string|
     - tangent to increment on, options are current, initial, noTangent. default is current 
   * - $maxDim
     - |float|
     - max number of iterations until the tangent is reformed and acceleration restarts (default = 3)  of iterations within a time step until a new tangent is formed
 


This command is used to construct a KrylovNewton algorithm object which uses a modified Newton method with Krylov subspace acceleration to advance to the next time step. 

.. note:: 
    References:
    * Scott, M.H. and G.L. Fenves. "A Krylov Subspace Accelerated Newton Algorithm: Application to Dynamic Progressive Collapse Simulation of Frames." Journal of Structural Engineering, 136(5), May 2010. DOI 