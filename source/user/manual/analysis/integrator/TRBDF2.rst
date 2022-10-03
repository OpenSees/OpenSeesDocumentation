.. _TRBDF2:

TRBDF2
--------------------------------
.. function:: integrator TRBDF2  

.. note:: 
    * As opposed to dividing the time-step in 2 as outlined in the papers, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the papers.

This command is used to construct a TRBDF2 integrator object. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something newmark does not always do. 
