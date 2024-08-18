.. BeamColumnJoint:

BeamColumnJoint Element
^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a two-dimensional beam-column-joint element object. The element may be used with both two-dimensional and three-dimensional structures; however, load is transferred only in the plane of the element.


Command Lines
"""""""""""""""""""""""

TCL:

.. function:: element beamColumnJoint $eleTag $Node1 $Node2 $Node3 $Node4 $Mat1 $Mat2 $Mat3 $Mat4 $Mat5 $Mat6 $Mat7 $Mat8 $Mat9 $Mat10 $Mat11 $Mat12 $Mat13 <$eleHeightFac $eleWidthFac>

Python:

.. function:: element('beamColumnJoint', eleTag, Node1, Node2, Node3, Node4, Mat1, Mat2, Mat3, Mat4, Mat5, Mat6, Mat7, Mat8, Mat9, Mat10, Mat11, Mat12, Mat13, <eleHeightFac, eleWidthFac>)

where:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$eleTag", "|integer|", "Unique element object tag"
   "$Node1 ... $Node4", "|integer|", "Node tags"
   "$Mat1", "|integer|", "uniaxial material tag for left bar-slip spring at node 1"
   "$Mat2", "|integer|", "uniaxial material tag for right bar-slip spring at node 1"
   "$Mat3", "|integer|", "uniaxial material tag for interface-shear spring at node 1"
   "$Mat4", "|integer|", "uniaxial material tag for lower bar-slip spring at node 2"
   "$Mat5", "|integer|", "uniaxial material tag for upper bar-slip spring at node 2"
   "$Mat6", "|integer|", "uniaxial material tag for interface-shear spring at node 2"
   "$Mat7", "|integer|", "uniaxial material tag for left bar-slip spring at node 3"
   "$Mat8", "|integer|", "uniaxial material tag for right bar-slip spring at node 3"
   "$Mat9", "|integer|", "uniaxial material tag for interface-shear spring at node 3"
   "$Mat10", "|integer|", "uniaxial material tag for lower bar-slip spring at node 4"
   "$Mat11", "|integer|", "uniaxial material tag for upper bar-slip spring at node 4"
   "$Mat12", "|integer|", "uniaxial material tag for interface-shear spring at node 4"
   "$Mat13", "|integer|", "uniaxial material tag for shear-panel"
   "$eleHeightFac", "|float|", "floating point value (as a ratio to the total height of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: ``1.0``)"
   "$eleWidthFac", "|float|", "floating point value (as a ratio to the total width of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: ``1.0``)"
   

.. figure:: figures/BeamColumnJoint/BeamColumnJoint_sch_rep.png
	:align: center
	:figclass: align-center
	:name: BeamColumnJoint_sch_rep
	:scale: 60%
	
	BeamColumnJoint Element: Graphic representation of the internal components of the element a) components of the beam-column joint model and b) beam-column joint finite element.


Output Recorders
"""""""""""""""""""""""

The valid queries to a BeamColumnJoint element when creating an ElementRecorder are as follows:

- `internalDisplacement`: returns the displacements of the internal joint nodes.
- `externalDisplacement`: returns the displacement of the external joint nodes.
- `deformation`: generates a four-column matrix in which the first column is the contribution to the total joint shear deformation of all of the bar-slip components of the joint, the second is the deformation contribution of the interface shear springs, the third is the deformation contribution of the shear-panel and the fourth is the total shear deformation of the joint.
- `node1BarSlipL`: returns the load-deformation response history of the Bar-Slip spring on the Left at node 1.
- `node1BarSlipR`: returns the load-deformation response history of the Bar-Slip spring on the Right at node 1.
- `node1InterfaceShear`: returns the load-deformation response history of the Interface-Shear spring at node 1.
- `node2BarSlipB`: returns the load-deformation response history of the Bar-Slip spring on the Bottom at node 2.
- `node2BarSlipT`: returns the load-deformation response history of the Bar-Slip spring on the Top at node 2.
- `node2InterfaceShear`: returns the load-deformation response history of the Interface Shear spring at node 1.
- `node3BarSlipL`: returns the load-deformation response history of the Bar-Slip spring on the Left at node 3.
- `node3BarSlipR`: returns the load-deformation response history of the Bar-Slip spring on the Right at node 3.
- `node3InterfaceShear`: returns the load-deformation response history of the Interface-Shear spring at node 3.
- `node4BarSlipB`: returns the load-deformation response history of the Bar-Slip spring on the Bottom at node 4.
- `node4BarSlipT`: returns the load-deformation response history of the Bar-Slip spring on the Top at node 4.
- `node4InterfaceShear`: returns the load-deformation response history of the Interface Shear spring at node 4.
- `shearPanel`: returns the load-deformation response history of the Shear-Panel spring.


Examples
"""""""""""""""""""""""

.. admonition:: Command Lines

   The following example constructs constructs a beamColumnJoint joint element with element tag *7*, that is connected to nodes *2*, *6*, *9*, *5*. The element uses the uniaxial material object with tags: *41* for left bar-slip spring at node 1, *42* for right bar-slip spring at node 1, *21* for lower bar-slip spring at node 2, *31* for upper bar-slip spring at node 2, *43* for left bar-slip spring at node 3, *44* for right bar-slip spring at node 3, *22* for lower bar-slip spring at node 4, *32* for upper bar-slip spring at node 4, *1* for interface-shear spring at nodes 1, 2, 3 and 4, and *5* for shear-panel. This joint element uses the default value (``1.0``) for both the element height (eleHeightFac) and width (eleWidthFac) factors.

   1. **Tcl**

   .. code-block:: tcl

      element beamColumnJoint 7 2 6 9 5 41 42 1 21 31 1 43 44 1 22 32 1 5; 

   2. **Python**

   .. code-block:: python

      element('beamColumnJoint', 7, 2, 6, 9, 5, 41, 42, 1, 21, 31, 1, 43, 44, 1, 22, 32, 1, 5)

	
.. admonition:: References

	More information available in the following reference:
	
	#. Lowes, Laura N.; Mitra, Nilanjan; Altoontash, Arash A beam-column joint model for simulating the earthquake response of reinforced concrete frames PEER-2003/10 Pacific Earthquake Engineering Research Center, University of California, Berkeley 2003 59 pages (400/P33/2003-10). [`URL <https://peer.berkeley.edu/sites/default/files/0310_l._lowes_n._mitra_a._altoontash.pdf>`_].


Code developed by: Nilanjan Mitra, Cal Poly