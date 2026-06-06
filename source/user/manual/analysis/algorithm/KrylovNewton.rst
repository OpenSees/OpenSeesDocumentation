.. _KrylovNewton:

Krylov-Newton Algorithm
--------------------------------
.. function:: algorithm KrylovNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim> <-factorOnce>

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
   * - -factorOnce
     - |string|
     - optional flag to assemble and factor the increment tangent in the first analysis step, keep it fixed in all later steps, and update it only after a domain change (for example, nodes or elements added or removed). Also accepted as ``-factorIncrementOnce``.

.. note::

   Krylov-Newton already uses one increment tangent per equilibrium solve within each analysis step. ``-factorOnce`` carries that same tangent forward to later steps instead of reforming it each time. Using ``-increment initial`` with ``-iterate noTangent`` or ``-iterate initial`` also enables ``-factorOnce`` automatically. If ``-factorOnce`` is given without ``-iterate``, OpenSees warns and defaults to ``-iterate noTangent``. If ``-factorOnce`` conflicts with the chosen ``-iterate`` tangent (for example, ``-iterate current``), OpenSees warns and disables ``-factorOnce``.

This command is used to construct a KrylovNewton algorithm object which uses a modified Newton method with Krylov subspace acceleration to advance to the next time step. 

.. note:: 
    References:
    * Scott, M.H. and G.L. Fenves. "A Krylov Subspace Accelerated Newton Algorithm: Application to Dynamic Progressive Collapse Simulation of Frames." Journal of Structural Engineering, 136(5), May 2010. DOI 