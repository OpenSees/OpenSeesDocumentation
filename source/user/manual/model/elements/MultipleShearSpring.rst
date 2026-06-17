.. _MultipleShearSpring:

MultipleShearSpring Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a multiple shear spring (MSS) element consisting of identical shear springs arranged radially to represent isotropic behavior in the local y-z plane. The command name ``MSS`` is an alias for ``multipleShearSpring``.

.. function:: element multipleShearSpring $eleTag $iNode $jNode $nSpring -mat $matTag <-lim $dsp> <-orient <$x1 $x2 $x3> $yp1 $yp2 $yp3> <-mass $m>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $nSpring, |integer|, number of radial shear springs
   $matTag, |integer|, tag of a previously defined uniaxial material (``-mat``)
   $dsp, |float|, minimum deformation to compute equivalent coefficient (optional; default 0.0)
   $m, |float|, element mass (optional)

.. note::

   1. When ``$dsp`` is positive and shear deformation exceeds ``$dsp``; the element adjusts force and stiffness to reproduce monotonic uniaxial material behavior in every direction.

   2. Valid :ref:`elementRecorder` queries include ``globalForce``, ``localForce``, ``basicForce``, ``localDisplacement``, and ``basicDeformation``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element multipleShearSpring 1 1 2 16 -mat 1

   2. **Python Code**

   .. code-block:: python

      element('multipleShearSpring', 1, 1, 2, 16, '-mat', 1)

Code developed by: Masaru Kikuchi
