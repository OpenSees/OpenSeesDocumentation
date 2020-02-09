
.. _bbarQuad:

Bbar Plane Strain Quad Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.

.. function:: element bbarQuad $eleTag $iNode $jNode $kNode $lNode $thick $matTag


$eleTag, |integer|,	unique element object tag
$iNode $jNode $kNode $lNode, |integer|,  four nodes defining element boundaries, input in counter-clockwise order around the element.
$thick, |float|, element thickness
$matTag, |integer|, tag of nDMaterial

.. note::

   PlainStrain only.
   
   The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.


Code Developed by: **Edward Love, Sandia National Laboratories**