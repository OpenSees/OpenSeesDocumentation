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

1. Zero-Length Elements

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
   elements/zeroLengthContactASDimplex

2. Truss Elements

.. toctree::
   :maxdepth: 1

   elements/Truss
   elements/CorotationalTruss


3. Beam Column Elements

.. toctree::
   :maxdepth: 1

   elements/elasticBeamColumn
   elements/ExactFrame
   elements/ModElasticBeam
   elements/ElasticBeamColumnElementWithStiffnessModifiers
   elements/ElasticTimoshenkoBeamColumnElement
   elements/BeamWithHingesElement
   elements/DisplacementBasedBeamColumnElement
   elements/ForceBasedBeamColumnElement
   elements/gradientInelasticBeamColumn   
   elements/FlexureShearInteractionDisplacementBasedBeamColumnElement
   elements/MVLEM
   elements/MVLEM_3D
   elements/SFI_MVLEM_3D
   elements/E_SFI_MVLEM_3D
   elements/dispBeamColumnAsym
   elements/mixedBeamColumnAsym
   elements/E_SFI


4. Quadrilateral & Shell Elements

.. toctree::
   :maxdepth: 1

   elements/ASDShellQ4
   elements/Quad
   elements/SSPquad
   elements/Shell
   elements/ShellDKGQ
   elements/ShellNLDKGQ
   elements/ShellNL
   elements/BbarPlaneStrainQuadrilateral
   elements/EnhancedStrainQuadrilateral
   elements/MEFI

   
5. Triangles

.. toctree::
   :maxdepth: 1

   elements/Tri31
   elements/ShellDKGT
   elements/ShellNLDKGT
   elements/ASDShellT3

6. Bricks

.. toctree::
   :maxdepth: 1

   elements/stdBrick
   elements/bbarBrick
   elements/SSPbrick

7. Tetrahedrons

.. toctree::
   :maxdepth: 1

   elements/FourNodeTetrahedron
   elements/TenNodeTetrahedron


8. Joint Elements

.. toctree::
   :maxdepth: 1

   elements/BeamColumnJoint
   elements/ElasticTubularJoint
   elements/Joint2D
   elements/Inno3DPnPJoint
   elements/LehighJoint2D

9. Link Elements

.. toctree::
   :maxdepth: 1

   elements/TwoNodeLink

10. Bearing Elements

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
   elements/TripleFrictionPendulumX



11.    U-P Elements (saturated soil)

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

12. Contact

.. toctree::
   :maxdepth: 1   

   elements/SimpleContact2D
   elements/SimpleContact3D
   elements/BeamContact2D
   elements/BeamContact3D
   elements/BeamEndContact3D
   elements/zeroLengthImpact3D
   
13. Cable

.. toctree::
   :maxdepth: 1   

   elements/CatenaryCableElement

14. Absorbing Elements

.. toctree::
   :maxdepth: 1   

   elements/PML

15. Misc.

.. toctree::
   :maxdepth: 1   

   elements/ShallowFoundationGen
   elements/SurfaceLoad
   elements/VS3D4
   elements/AC3D8
   elements/ASI3D8
   elements/AV3D4
   elements/ASDEmbeddedNodeElement
   elements/ASDAbsorbingBoundary
   elements/RockingBC
   elements/FSIFluidBoundaryElement2D
   elements/FSIFluidElement2D
   elements/FSIInterfaceElement2D

