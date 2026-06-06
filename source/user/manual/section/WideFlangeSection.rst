.. _WideFlangeSection:

WideFlangeSection
^^^^^^^^^^^^^^^^^

This command constructs a wide-flange (I-shaped) steel section by discretizing the cross section into fibers. The command name in OpenSees is ``WFSection2d`` (alias ``WSection2d``).

.. function:: section WFSection2d $secTag $matTag $d $tw $bf $tf $nfdw $nftf <$nfbf $nftw> <-GJ $GJ> <-nd $shape> <-warping>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $matTag, |integer|, tag of uniaxial or nD material assigned to all fibers
   $d, |float|, section depth
   $tw, |float|, web thickness
   $bf, |float|, flange width
   $tf, |float|, flange thickness
   $nfdw, |integer|, number of fibers along the web depth
   $nftf, |integer|, number of fibers along each flange thickness
   $nfbf, |integer|, number of fibers along each flange width (optional, default 1)
   $nftw, |integer|, number of fibers along the web thickness (optional, default 1)
   $GJ, |float|, torsional rigidity (3D uniaxial models only)
   $shape, |float|, nD fiber shape factor (used with ``-nd``)
   ``-warping``, |string|, enable warping formulation (3D uniaxial models with ``-GJ``)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section WFSection2d 1 1 14.0 0.44 14.5 0.71 16 2

   2. **Python Code**

   .. code-block:: python

      ops.section('WFSection2d', 1, 1, 14.0, 0.44, 14.5, 0.71, 16, 2)

Code Developed by: |mhs|
