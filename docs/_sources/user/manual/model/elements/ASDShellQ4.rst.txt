.. _ASDShellQ4:

ASDShellQ4 Element
^^^^^^^^^^^^^^^^^^

This command is used to construct an ASDShellQ4 element object. The ASDShellQ4 element is a 4-node general purpose thick shell element with the following features:

#. The membrane behavior is enhanced with the **AGQ6-I** [ChenEtAl2004]_ formulation, which makes the element almost insensitive to geometry distortion, as opposed to standard iso-parametric elements.
#. The drilling DOF is treated with the **Hughes-Brezzi** [HughesEtAl1989]_ formulation, with special care to avoid membrane locking, using a 1 point quadrature plus stabilization.
#. The plate bending part is treated using the **MITC4** [DvorkinEtAl1984]_ [BatheEtAl1985]_ formulation, to avoid the well known transverse shear locking behavior of thick plate elements.
#. It can be used to model both **flat** and **warped** geometries.
#. Kinematics can be either **linear** or **corotational**. The corotational kinematics is based on the work of Felippa et al., i.e. the **EICR** [Felippa2000]_ [FelippaEtAl2005]_ (Element Independent Corotational formulation). Finite rotations are treated with Quaternions.
#. It uses a full 2x2 Gauss quadrature, so it has a total of 4 integration points.


.. function:: element ASDShellQ4 $eleTag $n1 $n2 $n3 $n4 $secTag <-corotational>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique integer tag identifying element object
   $n1 $n2 $n3 $n4, 4 |integer|, the four nodes defining the element (-ndm 3 -ndf 6)
   $secTag, |integer|, unique integer tag associated with previously-defined SectionForceDeformation object
   -corotational, |string|, "optional flag, if provided, the element uses non-linear kinematics, suitable for large displacement/rotation problems"


.. figure:: ASDShellQ4_geometry.png
	:align: center
	:figclass: align-center

	Nodes, Gauss points, local coordinate system, warped and flat geometry

.. note::

   Valid queries to the ASDShellQ4 element when creating an ElementRecorder object are:
   
   *  '**force**', '**forces**', '**globalForce**', or '**globalForces**':
       *  Internal forces at the element's nodes.
       *  Orientation: global coordinate system.
       *  Size: 24 columns of data, 6 components for each one of the 4 nodes.
   *  '**material $secTag $secArg1 ... $secArgN**':
       *  Section response at section **$secTag**
       *  **$secTag** is the 1-based index of the integration point (1 to 4).
       *  '**$secArg1 ... $secArgN**' are the arguments required by the SectionDeformationObject at the requested integration point.

.. admonition:: Example 

   1. **Tcl Code**

   .. code-block:: tcl

      # set up a 3D-6DOFs model
      model Basic -ndm 3 -ndf 6
      node 1  0.0  0.0 0.0
      node 2  1.0  0.0 0.0
      node 3  1.0  1.0 0.0
      node 4  0.0  1.0 0.0
      
      # create a fiber shell section with 4 layers of material 1
      # each layer has a thickness = 0.025
      nDMaterial ElasticIsotropic  1  1000.0  0.2
      section LayeredShell  11  4   1 0.025   1 0.025   1 0.025   1 0.025
      
      # create the shell element using the small displacements/rotations assumption
      element ASDShellQ4  1  1 2 3 4  11
      # or you can use the corotational flag for large displacements/rotations (geometric nonlinearity)
      element ASDShellQ4  1  1 2 3 4  11 -corotational
      
      # record global forces at element nodes (24 columns, 6 for each node)
      recorder Element  -xml  force_out.xml  -ele  1  force
      # record local section forces at gauss point 1 (8 columns: | 3 membrane | 3 bending | 2 transverse shear |)
      # note: gauss point index is 1-based
      recorder Element  -xml  force_gp1_out.xml  -ele  1  material  1  force
      # record local stresses at fiber 1 of gauss point 1 (5 columns: Szz is neglected (0) )
      # note: fiber index is 1-based (while in beams it is 0-based!)
      recorder Element  -xml  stress_gp1_fib0_out.xml  -ele  1  material  1  fiber 1 stress

   2. **Python Code**

   .. code-block:: python

      # set up a 3D-6DOFs model
      model('Basic', '-ndm', 3, '-ndf', 6)
      node(1, 0.0, 0.0, 0.0)
      node(2, 1.0, 0.0, 0.0)
      node(3, 1.0, 1.0, 0.0)
      node(4, 0.0, 1.0, 0.0)
      
      # create a fiber shell section with 4 layers of material 1
      # each layer has a thickness = 0.025
      nDMaterial('ElasticIsotropic', 1, 1000.0, 0.2)
      section('LayeredShell', 11, 4,  1,0.025,  1,0.025,  1,0.025,  1,0.025)
      
      # create the shell element using the small displacements/rotations assumption
      element('ASDShellQ4', 1, 1,2,3,4, 11)
      # or you can use the corotational flag for large displacements/rotations (geometric nonlinearity)
      # element('ASDShellQ4', 1, 1,2,3,4, 11, '-corotational')
      
      # record global forces at element nodes (24 columns, 6 for each node)
      recorder('Element', '-xml', 'force_out.xml', '-ele', 1, 'force')
      # record local section forces at gauss point 1 (8 columns: | 3 membrane | 3 bending | 2 transverse shear |)
      # note: gauss point index is 1-based
      recorder('Element', '-xml', 'force_gp1_out.xml', '-ele', 1, 'material', '1', 'force')
      # record local stresses at fiber 1 of gauss point 1 (5 columns: Szz is neglected (0) )
      # note: fiber index is 1-based (while in beams it is 0-based!)
      recorder('Element', '-xml', 'stress_gp1_fib0_out.xml', '-ele', 1, 'material', '1', 'fiber', '1', 'stress')

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.

.. [ChenEtAl2004] | Chen, Xiao-Ming, et al. "Membrane elements insensitive to distortion using the quadrilateral area coordinate method." Computers & Structures 82.1 (2004): 35-54. (`Link to article <http://www.paper.edu.cn/scholar/showpdf/MUT2ANwINTT0Ax5h>`_)
.. [HughesEtAl1989] Hughes, Thomas JR, and F. Brezzi. "On drilling degrees of freedom." Computer methods in applied mechanics and engineering 72.1 (1989): 105-121. (`Link to article <https://www.sciencedirect.com/science/article/pii/0045782589901242>`_)
.. [DvorkinEtAl1984] Dvorkin, Eduardo N., and Klaus-Jurgen Bathe. "A continuum mechanics based four-node shell element for general non-linear analysis." Engineering computations (1984). (`Link to article <https://www.researchgate.net/profile/Eduardo_Dvorkin/publication/235313212_A_Continuum_mechanics_based_four-node_shell_element_for_general_nonlinear_analysis/links/00b7d52611d8813ffe000000.pdf>`_)
.. [BatheEtAl1985] Bathe, Klaus-Jurgen, and Eduardo N. Dvorkin. "A four-node plate bending element based on Mindlin/Reissner plate theory and a mixed interpolation." International Journal for Numerical Methods in Engineering 21.2 (1985): 367-383. (`Link to article <http://www.simytec.com/docs/Short_communicaion_%20four_node_plate.pdf>`_)
.. [Felippa2000] Felippa, Carlos A. "A systematic approach to the element-independent corotational dynamics of finite elements". Technical Report CU-CAS-00-03, Center for Aerospace Structures, 2000. (`Link to article <https://d1wqtxts1xzle7.cloudfront.net/40660892/A_Systematic_Approach_to_the_Element-Ind20151205-15144-36jazx.pdf?1449356169=&response-content-disposition=inline%3B+filename%3DA_Systematic_Approach_to_the_Element_Ind.pdf&Expires=1611329637&Signature=DTV4RrGLOp4AWynE4kpUPHDNDuazgbqhI6KU1LR7jMBG6sqtx8McLgll918M3CeyBsjBjb7bUTz4ZVGJaoaq0B9Orhr4FVy0AMxrHlSbaTk8lnAXduaOPt~hsbJbiC5PXjSeKzYuT-8-chgyQvaB1gPlUwZ4zTBVJZocbr~Jh0zpTNF2b846iHBu9NQ2qfD5yTciVxMFjoRvOrb4H4AtVgtU~kM9TsiszQa6Vq8Amf~DivjfyB9~v7zgwiwm65PCcErFM8llNev~F1btwqNbSNJ62It7eWgMbkFe92xs6FmOkAIE8tmXnhb1tpUsCjW4kwmVCYcSAsYO4YAyj~6wig__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA>`_)
.. [FelippaEtAl2005] Felippa, Carlos A., and Bjorn Haugen. "A unified formulation of small-strain corotational finite elements: I. Theory." Computer Methods in Applied Mechanics and Engineering 194.21-24 (2005): 2285-2335. (`Link to article <http://www.cntech.com.cn/down/h000/h21/attach200903311026030.pdf>`_)
