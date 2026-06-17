.. _KikuchiBearing:

KikuchiBearing Element
^^^^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional elastomeric bearing element with multiple normal springs parallel to the local x-axis and multiple shear springs distributed in the local y-z plane. Use with ``-ndm 3 -ndf 6``.

.. function:: element KikuchiBearing $eleTag $iNode $jNode -shape $shape -size $size $totalRubber <-totalHeight $totalHeight> -nMSS $nMSS -matMSS $matMSSTag <-limDisp $limDisp> -nMNS $nMNS -matMNS $matMNSTag <-lambda $lambda> <-orient <$x1 $x2 $x3> $yp1 $yp2 $yp3> <-mass $m> <-noPDInput> <-noTilt> <-adjustPDOutput $ci $cj> <-doBalance $limFo $limFi $nIter>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $shape, |string|, bearing cross section: ``round`` or ``square`` (``-shape``)
   $size, |float|, characteristic size of cross section (``-size``)
   $totalRubber, |float|, total rubber thickness (``-size``)
   $totalHeight, |float|, total bearing height (optional; default is distance between nodes)
   $nMSS, |integer|, number of multiple shear springs (``-nMSS``)
   $matMSSTag, |integer|, uniaxial material tag for shear springs (``-matMSS``)
   $limDisp, |float|, limit displacement for MSS equivalent coefficient (optional)
   $nMNS, |integer|, number of multiple normal springs (``-nMNS``)
   $matMNSTag, |integer|, uniaxial material tag for normal springs (``-matMNS``)
   $lambda, |float|, normal spring distribution parameter (optional)
   $m, |float|, element mass (optional)
   $ci $cj, |float|, P-Delta output adjustment coefficients (``-adjustPDOutput``)
   $limFo $limFi $nIter, |float| |float| |integer|, force-balance iteration controls (``-doBalance``)

.. note::

   1. Flags ``-noPDInput`` and ``-noTilt`` disable P-Delta input and tilt effects respectively.

   2. Valid :ref:`elementRecorder` queries include ``globalForce``, ``localForce``, ``basicForce``, ``localDisplacement``, and ``basicDeformation``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element KikuchiBearing 1 1 2 -shape round -size 0.5 0.2 -nMSS 16 -matMSS 1 -nMNS 4 -matMNS 2

   2. **Python Code**

   .. code-block:: python

      element('KikuchiBearing', 1, 1, 2, '-shape', 'round', '-size', 0.5, 0.2,
              '-nMSS', 16, '-matMSS', 1, '-nMNS', 4, '-matMNS', 2)

Code developed by: Ken Ishii and Masaru Kikuchi
