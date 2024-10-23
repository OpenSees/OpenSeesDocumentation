
.. _printA:

``printA``
**********

.. function:: printA <-file $fileName> <-m $m> <-c $c> <-k $k>

   
.. list-table:: 
   :widths: 10 10 40

   * - ``$fileName``
     - *string*
     - file name to write tangent to.
   * - ``$m``
     - |float|
     - factor with which to scale the inertial part of the tangent (OpenSeesRT only).
   * - ``$c``
     - |float|
     - factor with which to scale the damped part of the tangent (OpenSeesRT only).
   * - ``$k``
     - |float|
     - factor with which to scale the static part of the tangent (OpenSeesRT only).

Print the contents of the matrix that the integrator
creates to the screen or a file if the ``-file`` option is used. 
If using a
static integrator, the resulting matrix is the stiffness matrix. If a
transient integrator, it will be some combination of mass and stiffness
matrices.

.. note::

   The full version of this command as documented above is supported from Python and Tcl
   through OpenSeesRT.
   In OpenSeesPy and older Tcl versions this command only works with the FullGeneral linear system,
   and the ``GimmeMCK`` integrator must be used to specify ``m`` ``c`` and ``k`` factors.

Examples
========

The following examples will return a matrix :math:`\mathbf{A}` that is given by a linear combination of 
the mass :math:`\mathbf{M}` and stiffness :math:`\mathbf{K}`:

.. math::

   \mathbf{A} = \frac{1}{2}\mathbf{M} + \frac{1}{10}\mathbf{K}


In Tcl:

.. code-block:: tcl

    printA -m 0.5 -k 0.1

and in Python with OpenSeesRT:

.. code-block:: python

    A = model.getTangent(m=0.5, k=0.1)


