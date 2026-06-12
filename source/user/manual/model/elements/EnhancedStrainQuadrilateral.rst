.. _EnhancedStrainQuadrilateral:

Enhanced Strain Quadrilateral Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a four-node quadrilateral element using a bilinear isoparametric formulation with enhanced strain modes. The command name in OpenSees is ``enhancedQuad``. Use with ``-ndm 2 -ndf 2``.

.. function:: element enhancedQuad $eleTag $iNode $jNode $kNode $lNode $thick $type $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order
   $thick, |float|, element thickness
   $type, |string|, material formulation: ``PlaneStrain`` or ``PlaneStress``
   $matTag, |integer|, tag of an nD material

.. note::

   1. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element enhancedQuad 1 1 2 3 4 1.0 PlaneStrain 1

   2. **Python Code**

   .. code-block:: python

      element('enhancedQuad', 1, 1, 2, 3, 4, 1.0, 'PlaneStrain', 1)

Code developed by: Ed Love
