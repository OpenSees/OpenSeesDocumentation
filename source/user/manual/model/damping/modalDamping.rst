.. _modalDamping:

Modal Damping Command
*******************

.. function:: modalDamping $factor

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $factor, |float|,  damping factor.

.. admonition:: Example:


   1. **Tcl Code**

   .. code-block:: tcl

        set N 2 ;# Number of modes for modal damping
        eigen $N

        modalDamping 0.05 0.02 ;# 5% in mode 1, 2% in mode 2

Further reading about Modal Damping can be seen in [ChopraMcKenna2015]_

.. warning::

   Modal damping implementation is as in Perform3D. The tangent matrix is not modified for damping terms as this would result in a full matrix. Instead just the right hand side of the equation, i.e. the resisting force vector is modified. As a consequence, iteration is required at each step to obtain a converged solution, i.e. no Linear solution algorithm or explicit time stepping algorithms will work correctly with modal damping!


