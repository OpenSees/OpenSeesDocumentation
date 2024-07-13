
.. _printA:

``printA``
**********

.. function:: printA <-file $fileName> <-m $m> <-c $c> <-k $k>

print the contents of a FullGeneral system that the integrator
creates to the screen or a file if the ``-file`` option is used. 
If using a
static integrator, the resulting matrix is the stiffness matrix. If a
transient integrator, it will be some combination of mass and stiffness
matrices.

