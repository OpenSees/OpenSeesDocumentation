.. _element:

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
   elements/CorotationalTruss


#. Trusss

.. toctree::
   :maxdepth: 1

   elements/ElasticBeamColumn
   elements/ElasticBeamColumnElementWithStiffnessModifiers
   elements/ElasticTimoshenkoBeamColumnElement
   elements/BeamWithHingesElement
   elements/DisplacementBasedBeamColumnElement
   elements/ForceBasedBeamColumnElement
   elements/FlexureShearInteractionDisplacementBasedBeamColumnElement
   elements/MVLEM
   elements/SFI_MVLEM
   
#. Joints

.. toctree::
   :maxdepth: 1

	elements/BeamColumnJoint
	elements/ElasticTubularJoint
	elements/Joint2D

#. Joints

.. toctree::
   :maxdepth: 1

   elements/TwoNodeLink

#. Bearings

.. toctree::
   :maxdepth: 1

   elements/ElastomericBearingPlasticity
   elements/ElastomericBearingBouc-Wen
   elements/FlatSliderBearingElement
   elements/SingleFrictionPendulumBearing
   elements/TripleFrictionPendulumBearing
   elements/TripleFrictionPendulum
   elements/MultipleShearSpring
   elements/KikuchiBearing
   elements/YamamotoBiaxialHDR
   elements/ElastomericX
   elements/LeadRubberX
   elements/HDR
   elements/RJ-Watson EQS Bearing
   elements/FPBearingPTV

#. Quadrilaterals

.. toctree::
   :maxdepth: 1

   elements/Quad
   elements/Shell
   elements/ShellDKGQ
   elements/ShellNLDKGQ
   elements/ShellNL
   elements/Bbar Plane Strain Quadrilateral
   elements/Enhanced Strain Quadrilateral
   elements/SSPquad
   
#. Triangles

.. toctree::
   :maxdepth: 1

   elements/Tri31
   elements/ShellDKGT
   elements/ShellNLDKGT

#. Bricks

.. toctree::
   :maxdepth: 1

   elements/StandardBrick
   elements/BbarBrick
   elements/SSPbrick

#. Tetrahedrons

.. toctree::
   :maxdepth: 1

   elements/FourNodeTetrahedron

#.    U-P Elements (saturated soil)

.. toctree::
   :maxdepth: 1

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

#. Contact

.. toctree::
   :maxdepth: 1   

   elements/SimpleContact2D
   elements/SimpleContact3D
   elements/BeamContact2D
   elements/BeamContact3D
   elements/BeamEndContact3D
   elements/zeroLengthImpact3D
   
#. Cable

.. toctree::
   :maxdepth: 1   

   elements/CatenaryCableElement

#. Misc.

.. toctree::
   :maxdepth: 1   

   elements/ShallowFoundationGen
   elements/SurfaceLoad
   elements/VS3D4
   elements/AC3D8
   elements/ASI3D8
   elements/AV3D4

