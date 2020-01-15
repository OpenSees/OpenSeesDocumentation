Element Command
***************

This command is used to construct an element and add it to the Domain. 

.. function:: element $eleType $tag (num $nodes) $arg1 ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleType, |string|,      element type
   $eleTag,  |integer|,     unique element tag.
   $nodes,   |integerlist|, a list of element nodes with number dependent on ele type
   $eleArgs, |list|,        a list of element arguments with number dependent on ele type

.. note::
   The type of element created and the additional arguments required depends on the **$eleType** provided.

   The valid queries to any element when creating an ElementRecorder are documented in the NOTES section for each element. 


The following subsections contain information about **$eleType** and the number of nodes and args required for each of the available element types:

#. Zero-Length Elements

.. toctree::
   :maxdepth: 4

   elements/zeroLength
   elements/zeroLengthSection

elements/zeroLengthND
elements/CoupledZeroLength
elements/zeroLengthContact
elements/zeroLengthContactNTS2D
elements/zeroLengthInterface2D
elements/zeroLengthImpact3D 

#. Trusss

.. toctree::
   :maxdepth: 1

elements/Truss
elements/Corotational

Beam-Columns
^^^^^^^^^^^^^^^^^^^^
elements/ElasticBeamColumn
elements/ElasticBeamColumnElementWithStiffnessModifiers
elements/ElasticTimoshenkoBeamColumnElement
elements/BeamWithHingesElement
elements/DisplacementBasedBeamColumnElement
elements/ForceBasedBeamColumnElement
elements/FlexureShearInteractionDisplacementBasedBeamColumnElement
elements/MVLEM
elements/SFI_MVLEM

Joints
^^^^^^^^^^^^^^
elements/BeamColumnJoint
elements/ElasticTubularJoint
elements/Joint2D

Links
^^^^^^^^^^^^^
elements/TwoNodeLink

Bearings
^^^^^^^^^^^^^^^^
elements/ElastomericBearingPlasticity
elements/ElastomericBearingBouc-Wen
elements/FlatSliderBearingElement
elements/SingleFriction Pendulum Bearing
elements/TripleFriction Pendulum Bearing| TFP Bearing
elements/TripleFriction Pendulum
elements/MultipleShearSpring
elements/KikuchiBearing
elements/YamamotoBiaxialHDR
elements/ElastomericX
elements/LeadRubberX
elements/HDR
elements/RJ-Watson EQS Bearing
elements/FPBearingPTV

Quadrilaterals
^^^^^^^^^^^^^^^^^^^^^^
elements/Quad
elements/Shell
elements/ShellDKGQ
elements/ShellNLDKGQ
elements/ShellNL
elements/Bbar Plane Strain Quadrilateral
elements/Enhanced Strain Quadrilateral
elements/SSPquad

Triangulars
^^^^^^^^^^^^^^^^^^^
elements/Tri31
elements/ShellDKGT
elements/ShellNLDKGT

Bricks
^^^^^^^^^^^^^^
elements/StandardBrick
elements/BbarBrick
elements/SSPbrick

Tetrahedrons
^^^^^^^^^^^^^^^^^^^^^
elements/FourNodeTetrahedron


UC San Diego u-p element (saturated soil)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
elements/FourNodeQuadUP
elements/BrickUP
elements/bbarQuadUP
elements/bbarBrickUP
elements/NineFourNodeQuadUP
elements/TwentyEightNodeBrickUP
elements/TwentyNodeBrickUP
elements/BrickLargeDisplacementUP
elements/SSPquadUP 
elements/SSPbrickUP

Misc.
^^^^^
elements/ShallowFoundationGen
elements/SurfaceLoad
elements/VS3D4
elements/AC3D8
elements/ASI3D8
elements/AV3D4

Contacts
^^^^^^^^^^^^^^^^
elements/SimpleContact2D
elements/SimpleContact3D
elements/BeamContact2D
elements/BeamContact3D
elements/BeamEndContact3D
elements/zeroLengthImpact3D

Cables
^^^^^^^^^^^^^^
elements/CatenaryCableElement