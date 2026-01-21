.. _forceBeamColumn:


Force-Based Beam Column Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a forceBeamColumn element object, which is based on the iterative force-based formulation. A variety of numerical integration options are available for the element state determination and encompass both distributed plasticity and pla\
stic hinge integration, see :ref:`beamIntegration` options. The element if formulated in a basic system, given by its end rotations and axial deformation. The geometric transformation between this basic system and the 2d or 3d system comprisomg nodal displacements and rotations, is provided by the geometric transformation, see :ref:`geomTransf` options.  

.. note::

   Force based elements use known equilibrium along the element length to determine section forces. As a consequence, in a finite element setting the element must iterate given nodal displacements at each trial step to determine the section deformations at the integration points to cause such. For a discussion of differences between this **force** based beam column element and the **displacement** based element see `this post on portwooddigital <https://portwooddigital.com/2020/02/23/a-tale-of-two-element-formulations/>`_

.. tabs::

  .. tab:: Tcl

     .. function:: element forceBeamCoumn $eleTag $iNode $jNode $transfTag $integrationTag <-iter $maxIter $tol>  <-mass $mass> 

     .. csv-table::
	:header: "Argument", "Type", "Description"
	:widths: 10, 10, 40

		 "$eleTag",       "|integer|", "Unique element object tag"
		 "$iNode", "|integer|", "tag of the iNode"
		 "$jNode", "|integer|", "tag of the jNode"		 
		 "$transfTag",    "|integer|",   "tag of the geometric transformation object"
		 "$integrationTag", "|integer|",   "tag of the beam integration object"
		 "$maxIter",        "|integer|",   "max number of iterations, default = 10"
		 "$tol",            "|float|",   "tolerance, default = 1.0e-12"
		 "$mass",           "|float|", "Element mass per unit length, default = 0.0"
		    
  .. tab:: OpenSeesPy

     .. function:: element('forceBeamColumn',eleTag,*eleNodes,transfTag,integrationTag,'-iter',maxIter=10,tol=1e-12,'-mass',mass=0.0)

     ========================   =============================================================
     ``eleTag`` |int|           tag of the element
     ``eleNodes`` |listi|       a list of two element nodes
     ``transfTag`` |int|        tag of transformation
     ``integrationTag`` |int|   tag of :func:`beamIntegration`
     ``maxIter`` |int|          maximum number of iterations to undertake to satisfy element compatibility (optional)
     ``tol`` |float|            tolerance for satisfaction of element compatibility (optional)
     ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)
     ========================   =============================================================

.. note::

   The valid queries to an elastic beam-column element when creating an ElementRecorder object are:
   
   #. force or globalForce
      
   #. localForce
      
   #. basicForce
      
   #. section $sectionNumber $arg1 $arg2 ... (note: $sectionNumer is integer 1 through $numIntegrPts)
      
   #. basicDeformation
      
   #. plasticDeformation
      
   #. inflectionPoint
      
   #. tangentDrift
      
   #. integrationPoints
      
   #. integrationWeights



References
----------

.. [1] Neuenhofer, Ansgar, FC Filippou. Geometrically Nonlinear Flexibility-Based Frame Finite Element. ASCE Journal of Structural Engineering, Vol. 124, No. 6, June, 1998. ISSN 0733-9445/98/0006-0704-0711. Paper 16537. pp. 704-711.
       
.. [2] Neuenhofer, Ansgar, FC Filippou. Evaluation of Nonlinear Frame Finite-Element Models. ASCE Journal of Structural Engineering, Vol. 123, No. 7, July, 1997. ISSN 0733-9445/97/0007-0958-0966. Paper No. 14157. pp. 958-966.
      
.. [3] Neuenhofer, Ansgar, FC Filippou. ERRATA -- Geometrically Nonlinear Flexibility-Based Frame Finite Element. ASCE Journal of Structural Engineering, Vol. 124, No. 6, June, 1998. ISSN 0733-9445/98/0006-0704-0711. Paper 16537. pp. 704-711.

.. [4] Taucer, Fabio F, E Spacone, FC Filippou. A Fiber Beam-Column Element for Seismic Response Analysis of Reinforced Concrete Structures. Report No. UCB/EERC-91/17. Earthquake Engineering Research Center, College of Engineering, University of California, Berkeley. December 1991.

.. [5] Spacone, Enrico, V Ciampi, FC Filippou. A Beam Element for Seismic Damage Analysis. Report No. UCB/EERC-92/07. Earthquake Engineering Research Center, College of Engineering, University of California, Berkeley. August 1992.



      
