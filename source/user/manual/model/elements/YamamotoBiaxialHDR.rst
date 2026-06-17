.. _YamamotoBiaxialHDR:

YamamotoBiaxialHDR Element
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional high damping rubber bearing element with biaxial shear springs distributed in the local y-z plane. Axial and rotational stiffness remain zero. Use with ``-ndm 3 -ndf 6``.

.. function:: element YamamotoBiaxialHDR $eleTag $iNode $jNode $Tp $DDo $DDi $Hr <-coRS $cr $cs> <-orient <$x1 $x2 $x3> $yp1 $yp2 $yp3> <-mass $m>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $Tp, |integer|, number of rubber layers
   $DDo, |float|, outer diameter
   $DDi, |float|, inner diameter
   $Hr, |float|, height of rubber layers
   $cr $cs, |float|, coefficients for scragging model (``-coRS``; optional; default 1.0)
   $m, |float|, element mass (optional; default 0.0)

.. note::

   Valid :ref:`elementRecorder` queries include ``globalForce``, ``localForce``, ``basicForce``, ``localDisplacement``, and ``basicDeformation``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element YamamotoBiaxialHDR 1 1 2 20 0.6 0.0 0.15

   2. **Python Code**

   .. code-block:: python

      element('YamamotoBiaxialHDR', 1, 1, 2, 20, 0.6, 0.0, 0.15)

Code developed by: Masaru Kikuchi
