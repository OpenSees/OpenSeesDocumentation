.. Inno3DPnPJoint:

Inno3DPnPJoint Element
^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a three-dimensional beam-column-joint element object for the 3D innovative plug-and-play steel tubular joint configuration proposed within the `INNO3DJOINTS <https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/960532413/project/749959/program/31061225/details>`_ project.


Command Lines
"""""""""""""""""""""""

TCL:

.. function:: element Inno3DPnPJoint $eleTag $Node1 $Node2 $Node3 $Node4 $Node5 $SprMatTag01 $SprMatTag02 $SprMatTag03 $SprMatTag04 $SprMatTag05 $SprMatTag06 $SprMatTag07 $SprMatTag08 $SprMatTag09 $SprMatTag10 $SprMatTag11 $SprMatTag12 $SprMatTag13 $SprMatTag14 $SprMatTag15 $SprMatTag16 $SprMatTag17 $SprMatTag18 $SprMatTag19 $SprMatTag20 $SprMatTag21 $SprMatTag22 $SprMatTag23 $SprMatTag24 $SprMatTag25 $SprMatTag26 $SprMatTag27 $SprMatTag28 $SprMatTag29 $SprMatTag30 $SprMatTag31 $SprMatTag32

Python:

.. function:: element('Inno3DPnPJoint', eleTag, Node1, Node2, Node3, Node4, Node5, SprMatTag01, SprMatTag02, SprMatTag03, SprMatTag04, SprMatTag05, SprMatTag06, SprMatTag07, SprMatTag08, SprMatTag09, SprMatTag10, SprMatTag11, SprMatTag12, SprMatTag13, SprMatTag14, SprMatTag15, SprMatTag16, SprMatTag17, SprMatTag18, SprMatTag19, SprMatTag20, SprMatTag21, SprMatTag22, SprMatTag23, SprMatTag24, SprMatTag25, SprMatTag26, SprMatTag27, SprMatTag28, SprMatTag29, SprMatTag30, SprMatTag31, SprMatTag32)

where:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 20, 10, 30

   "$eleTag",       "|integer|", "Unique element object tag"
   "$Node1 ... $Node5", "|integer|", "Node tags"
   "$SprMatTag1 ... $SprMatTag32", "|integer|", "Uniaxial material tags"


.. figure:: figures/Inno3DPnPJoint/I3DJ_allSprings_001.png
	:align: center
	:figclass: align-center
	:name: Inno3DPnPJoint
	
	Inno3DPnPJoint Element: 32 components.

	
Output Recorders
"""""""""""""""""""""""

The simulation results of the Inno3DPnP beam-to-column joint finite element can be analyzed by defining output records at both the element and component levels.



Examples
"""""""""""""""""""""""

.. admonition:: Command Lines

   The following example constructs constructs an Inno3DPnPJoint joint element with element tag *99*, that is connected to nodes *101*, *102*, *103*, *104* and *105* and uses for the components’ behavior the uniaxial material object tags from *1* to *32*.

   1. **Tcl**

   .. code-block:: tcl

      element Inno3DPnPJoint 99 101 102 103 104 105 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32; 

   2. **Python**

   .. code-block:: python

      element('Inno3DPnPJoint', 99, 101, 102, 103, 104, 105, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
	  

	
.. seealso::

	More information available in the following reference:
	
	#. C.V. Miculaş, Innovative plug and play joints for hybrid tubular constructions (Ph.D. thesis), University of Coimbra, Portugal, 2023, https://estudogeral.uc.pt/handle/10316/110990


	#. C. V. Miculaş, R. J. Costa, L. S. da Silva, R. Simões, H. Craveiro, T. Tankova, 3D macro-element for innovative plug-and-play joints, J. Constructional Steel Research 214 (2024), https://doi.org/10.1016/j.jcsr.2023.108436


	#. C.V. Miculaş, R.J. Costa, L. Simões da Silva, R. Simões, H. Craveiro, T. Tankova, Macro-modelling of the three-dimensional interaction between the faces of a steel tubular column joint, in: F. Di Trapani, C. Demartino, G.C. Marano, G. Monti (Eds.), Proceedings of the 2022 Eurasian OpenSees Days, Springer Nature Switzerland, Cham, 2023, pp. 408–422, http://dx.doi.org/10.1007/978-3-031-30125-4_37
	
	
.. note::
	
	Code development: Cristian V. Miculaș  (github user name: cvmiculas)
	
	Element conceptualization: Cristian V. Miculaș (cristian.miculas@uc.pt), Ricardo J. Costa (rjcosta@dec.uc.pt) and Luís Simões da Silva (luisss@dec.uc.pt).
	
	Affiliation: Civil Engineering Department, Institute for Sustainability and Innovation in Structural Engineering (ISISE), University of Coimbra, Portugal.
	
	Acknowledgements: This work has been supported in part by national funds through Foundation for Science and Technology (FCT), Portugal, under grant agreement SFRH/BD/138151/2018 awarded to Cristian V. Miculaş.
	
	
Code developed by: |cvmiculas|