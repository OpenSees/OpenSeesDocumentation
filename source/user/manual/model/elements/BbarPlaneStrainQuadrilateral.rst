.. _BbarPlaneStrainQuadrilateral:

Bbar Plane Strain Quadrilateral Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a four-node quadrilateral element using a bilinear isoparametric formulation with a mixed constant pressure/volume (B-bar) assumption. The command names in OpenSees are ``bbarQuad`` or ``mixedQuad``. The element is for plane strain problems only. Use with ``-ndm 2 -ndf 2``.

.. function:: element bbarQuad $eleTag $iNode $jNode $kNode $lNode $thick $matTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order
   $thick, |float|, element thickness
   $matTag, |integer|, tag of an nD material

.. note::

   1. Plane strain only; not valid for plane stress problems.

   2. Valid :ref:`elementRecorder` queries include ``forces``, ``stresses``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element bbarQuad 1 1 2 3 4 1.0 1

   2. **Python Code**

   .. code-block:: python

      element('bbarQuad', 1, 1, 2, 3, 4, 1.0, 1)

Code developed by: Ed Love
