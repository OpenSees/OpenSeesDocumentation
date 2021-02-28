.. _SSPbrick::

MVLEM_3D Element
^^^^^^^^^^^^^^^^

The MVLEM_3D model (Figure 1a) is a three-dimenaional four-node element with 24 DOFs for nonlinear analysis of flexure-controlled non-rectangular reinforced concrete walls subjected to multidirectional loading. The model is an extension of the two-dimensional, two-node Multiple-Vertical-Line-Element-Model ([MVLEM](https://opensees.berkeley.edu/wiki/index.php/MVLEM_-_Multiple-Vertical-Line-Element-Model_for_RC_Walls)). The baseline MVLEM, which is essentially a line element for rectangular walls subjected to in-plane loading, is extended to a three-dimensional model formulation by: 1) applying geometric transformation of the element in-plane degrees of freedom that convert it into a four-node element formulation (Figure 1b), as well as by incorporating linear elastic out-of-plane behavior based on the Kirchhoff plate theory (Figure 1c). The in-plane and the out-of-plane element behaviors are uncoupled in the present model.

.. admonition:: Command

   element MVLEM_3D eleTag iNode jNode kNode lNode m -thick {Thicknesses} -width {Widths} -rho {Reinforcing_ratios} -matConcrete {Concrete_tags} -matSteel {Steel_tags} -matShear {Shear_tag} <-CoR c> <-thickMod tMod> <-Poisson Nu> <-Density Dens>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|,	unique element object tag
   $node1 .. $node8, 8 |integer|, nodes of brick (ordered as shown in fig below)
   $matTag, |integer|, tag of nDMaterial
   $b1 $b2 $b3, |listFloat|, optional: body forces in global x y z directions


.. figure:: brick.png
	:align: center
	:figclass: align-center

	stdBrick Element Node Numbering

.. note::

	Valid queries to the SSPbrick element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.

      The SSPbrick element was designed with intentions of duplicating the functionality of the stdBrick Element. If an example is found where the SSPbrick element cannot do something that works for the stdBrick Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.


   This element can only be defined after a :numref:`model` with **-ndm 3 -ndf 3**

.. admonition:: Example 

   The following example constructs a brick element with tag **1** between nodes **1, 2, 3, 4, 5, 6, 7, 8** with an nDMaterial of tag **1** and x- and y-directed body forces of zero, and z-directed body force of -10.0. After element has been constructed two recoder commands, :numref:`recorder`, are given to record stress and strain when using the SSPbrick element (note the difference from the stdBrick Element)

   1. **Tcl Code**

   .. code-block:: tcl

      element SSPbrick 1 1 2 3 4 5 6 7 8 1 0.0 0.0 -10.0

      recorder Element -eleRange 1 $numElem -time -file stress.out  stress
      recorder Element -eleRange 1 $numElem -time -file strain.out  strain

   2. **Python Code**

   .. code-block:: python

      element('SSPbrick',1,1,2,3,4,5,6,7,8,1, 0.0, 0.0, -10.0)

Code Developed by: |chris|, |pedro|, |peter| at University of Washington.