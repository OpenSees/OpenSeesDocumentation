.. _twoNodeLink:

Two Node Link Element
^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a twoNodeLink element object, which is defined by two nodes. The element can have zero or non-zero length. It can have 1 to 6 degrees of freedom; only the transverse and rotational DOFs are coupled when the element has non-zero length. For non-zero length you can optionally specify how P-Delta moments (around local x and y) are distributed among moment at node i, moment at node j, and shear couple (the three ratios sum to 1), and the shear center as a fraction of the element length from node i. The element does not contribute to Rayleigh damping by default. For non-zero length the local x-axis is from nodal geometry unless ``-orient`` is given; for zero length the geometry is ignored and orientation vectors define the spring directions.

.. function:: element twoNodeLink $eleTag $iNode $jNode -mat $matTags -dir $dirs <-orient $x1 $x2 $x3 $y1 $y2 $y3> <-pDelta $Mratios> <-shearDist $sDratios> <-doRayleigh> <-mass $m>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $iNode $jNode, |integer|, end node tags
   $matTags,  |integerList|, tags of previously-defined UniaxialMaterial objects
   $dirs,     |integerList|, "| material directions:
   | 2D: 1,2 = translation along local x,y; 3 = rotation about local z
   | 3D: 1,2,3 = translation along local x,y,z; 4,5,6 = rotation about local x,y,z"
   $x1 $x2 $x3, |float|, (optional) global components defining local x-axis
   $y1 $y2 $y3, |float|, (optional) global components defining local y-axis
   $Mratios,  |floatList|, "| P-Delta ratios: 2D size 2, 3D size 4
   | ([My_iNode, My_jNode] or [My_iNode, My_jNode, Mz_iNode, Mz_jNode]); each pair ≤ 1"
   $sDratios, |floatList|, "| center of rotation from iNode as fraction of length (2D: 1 value, 3D: [dy, dz]);
   | range 0 to 1; default [0.5, 0.5]"
   -doRayleigh, |string|, include Rayleigh damping (optional)
   $m,        |float|,    element mass (optional, default = 0.0)

.. note::

   If the element has zero length and orientation vectors are not specified, the local axes coincide with the global axes. Otherwise the local z-axis is the cross product of the x- and y-vectors.

   The valid queries when creating an ElementRecorder are 'force,' 'localForce,' 'basicForce,' 'localDisplacement,' 'basicDisplacement' and 'material $matNum matArg1 matArg2 ...'.

**Relationship to zeroLength**

The twoNodeLink can be thought of as a zeroLength element with length. Unlike zeroLength, the local x-axis for non-zero length is taken from the vector between the two nodes, so you do not need to specify orientation unless you want to override it. The element is often used for dampers but also applies to other uncoupled force-deformation responses. When both translational and rotational springs are used, the **shear distance** (``-shearDist``) is the center of rotation as a fraction of the element length; it couples the moment-rotation response to lateral displacement. For zeroLength, lateral displacement depends only on the translational spring; for twoNodeLink it also depends on the rotational spring and the shear distance (default 0.5). With section-based response (e.g. fiber sections), twoNodeLink can model coupled axial, shear, and flexural behavior efficiently.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/Two_Node_Link_Element>`_

   `Two Node Link's Awakening (Portwood Digital) <https://portwooddigital.com/2025/02/23/two-node-links-awakening/>`_ for more on comparison with zeroLength and flexural response.

.. admonition:: Example

   From the OpenSees wiki: 2D link with tag **1** between nodes **1** and **2**, materials **1**, **2**, **3** in directions **1**, **2**, **3**. 3D link with tag **1**, materials in directions **1**, **2**, **6**.

   1. **Tcl Code**

   .. code-block:: tcl

      # 2D
      element twoNodeLink 1 1 2 -mat 1 2 3 -dir 1 2 3

      # 3D
      element twoNodeLink 1 1 2 -mat 1 2 3 -dir 1 2 6

   2. **Python Code**

   .. code-block:: python

      # 2D
      ops.element('twoNodeLink', 1, 1, 2, '-mat', 1, 2, 3, '-dir', 1, 2, 3)

      # 3D
      ops.element('twoNodeLink', 1, 1, 2, '-mat', 1, 2, 3, '-dir', 1, 2, 6)

Code developed by: |andreas|
