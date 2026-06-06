.. _SecantNewton:

Secant Newton Algorithm
----------------
This command is used to construct a SecantNewton algorithm object which uses the two-term update to accelerate the convergence of the modified newton method.

.. function:: algorithm SecantNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim> <-numTerms $numTerms> <-cutOut $R1 $R2> <-factorOnce>

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - -iterate
     - |string|
     - tangent to iterate on, options are current, initial, noTangent. default is current.
   * - -increment
     - |string|
     - tangent to increment on, options are current, initial, noTangent. default is current.
   * - -maxDim
     - |integer|
     - max number of iterations until the tangent is reformed and acceleration restarts (default = 3).
   * - -numTerms
     - |integer|
     - number of terms in the secant accelerator update (default = 2).
   * - -cutOut
     - |listFloat|
     - optional flag followed by cut-out factors ``$R1`` and ``$R2`` to suppress overly aggressive secant updates. Crisfield's recommended values are 3.5 and 0.3.
   * - -factorOnce
     - |string|
     - optional flag to assemble and factor the increment tangent in the first analysis step, keep it fixed in all later steps, and update it only after a domain change (for example, nodes or elements added or removed). Also accepted as ``-factorIncrementOnce``.

.. note::

   Secant-Newton already uses one increment tangent per equilibrium solve within each analysis step. ``-factorOnce`` carries that same tangent forward to later steps instead of reforming it each time. Using ``-increment initial`` with ``-iterate noTangent`` or ``-iterate initial`` also enables ``-factorOnce`` automatically. If ``-factorOnce`` is given without ``-iterate``, OpenSees warns and defaults to ``-iterate noTangent``. If ``-factorOnce`` conflicts with the chosen ``-iterate`` tangent (for example, ``-iterate current``), OpenSees warns and disables ``-factorOnce``.

.. note:: 
    References:

    * Crisfield, M.A. "Non-linear Finite Element Analysis of Solids and Structures", Vol. 1, Wiley, 1991.
