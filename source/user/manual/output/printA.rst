
.. _printA:

``printA``
**********

.. function:: printA <-file $fileName> <-m $m> <-c $c> <-k $k>

   
.. list-table:: 
   :widths: 10 10 40

   * - ``-file``
     - *string*
     - file name to write tangent to.
   * - ``$m``
     - |float|
     - factor with which to scale the inertial part of the tangent.
   * - ``$c``
     - |float|
     - factor with which to scale the damped part of the tangent.
   * - ``$k``
     - |float|
     - factor with which to scale the static part of the tangent.

Print the contents of the matrix that the integrator
creates to the screen or a file if the ``-file`` option is used. 
If using a
static integrator, the resulting matrix is the stiffness matrix. If a
transient integrator, it will be some combination of mass and stiffness
matrices.


