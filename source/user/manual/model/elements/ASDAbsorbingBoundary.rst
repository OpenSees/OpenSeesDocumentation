.. _ASDAbsorbingBoundary:

ASDAbsorbingBoundary Element (2D and 3D)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ASDAbsorbingBoundary_Video.gif
   :align: center
   :figclass: align-center

| This command is used to construct an ASDAbsorbingBoundary2D or ASDAbsorbingBoundary3D  object.
| The ASDAbsorbingBoundary2D is a 4-node quadrilateral element, while the ASDAbsorbingBoundary3D is a 8-node hexaedron element.
| This elements can be used as an extra layer at the boundaries of a soil domain to avoid wave reflections which typically arise with fixed boundaries.

.. function:: element ASDAbsorbingBoundary2D $tag $n1 $n2 $n3 $n4 $G $v $rho $thickness $btype <-fx $tsxTag> <-fy $tsyTag>
.. function:: element ASDAbsorbingBoundary3D $tag $n1 $n2 $n3 $n4 $n5 $n6 $n7 $n8 $G $v $rho $btype <-fx $tsxTag> <-fy $tsyTag> <-fz $tszTag>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tag, |integer|, unique integer tag identifying element object.
   $n1 $n2 $n3 $n4 $n5 $n6 $n7 $n8, 4 (or 8) |integer|, the 4 (or 8) nodes defining the element.
   $G, |float|, the shear modulus.
   $v, |float|, the Poisson's ratio.
   $rho, |float|, the mass density.
   $thickness, |float|, the thickness in 2D problems.
   $btype, |string|, "a string defining the boundary type. See **Note 2**"
   -fx, |string|, "optional flag. if provided, the user should provide the velocity time-series along the X direction."
   $tsxTag, |integer|, "optional, mandatory if -fx is provided. the tag of the time-series along the X direction."
   -fy, |string|, "optional flag. if provided, the user should provide the velocity time-series along the Y direction."
   $tsyTag, |integer|, "optional, mandatory if -fy is provided. the tag of the time-series along the Y direction."
   -fz, |string|, "optional flag. if provided, the user should provide the velocity time-series along the Z direction."
   $tszTag, |integer|, "optional, mandatory if -fz is provided. the tag of the time-series along the Z direction."

Theory
""""""

| When modelling a soil, only a portion of it is modelled, using artificial boundaries around it.
  Fixed conditions at these artificial boundaries are fine in static problems, but in dynamic problems they will reflect outgoing propagating waves.
  This problem can be avoided using a large portion of the model, which is impractical due to excessive computational efforts.
  Another solution is to adopt special boundary conditions which are able to absorb outgoing waves.
| This element has been implemented following the work described in [Nielsen2006]_ for the 2D case, and properly extended for the 3D case.
  For a detailed theory explanation, please refer to [Nielsen2006]_ and the references therein.
| In summary, this element can be seen as an assembly of many components:

    * **F**: The Free-Field element, required to compute the free-field solution in parallel with the main model.
    * **D**: The Lysmer-Kuhlemeyer dashpots, required to absorb outgoing waves.
    * **T**: The boundary tractions trasferred from the Free-Field to the Soil domain, required to impose the free-field solution to the boundaries of the main model.

.. figure:: ASDAbsorbingBoundary_Theory.png
   :align: center
   :figclass: align-center

   Sketch of the absorbing (macro) element in 2D problems.

Usage Notes
"""""""""""

.. admonition:: Note 1

   The element should have the standard node-numbering to ensure a proper positive jacobian.
   
   .. figure:: ASDAbsorbingBoundary_Mesh.png
      :align: center
      :figclass: align-center
      
      Node numbering.

.. admonition:: Note 2

   The behavior of the element changes based on the side of the model it belongs to. The $btype argument defines the boundary type of the element.
   It is a string made of a combination of characters. Each character describes a side of the model:
      
      * **B** = Bottom
      * **L** = Left
      * **R** = Right
      * **F** = Front (only for 3D problems)
      * **K** = Back (only for 3D problems)
   
   | For a 2D problem you can have the following valid combinations: **B**, **L**, **R**, **BL**, **BR**
   | For a 3D problem you can have the following valid combinations: **B**, **L**, **R**, **F**, **K**, **BL**, **BR**, **BF**, **BK**, **LF**, **LK**, **RF**, **RK**, **BLF**, **BLK**, **BRF**, **BRK**

   .. figure:: ASDAbsorbingBoundary_btype.png
      :align: center
      :figclass: align-center
      
      Exploded-view: Boundary Type Codes for 2D (left) and 3D (right) problems.

.. warning::

   * The boundary elements should be an extrusion of the sides of the main model along their outward normal vector.
   * The vertical sides of the main model should have an outward normal vector that points either along the global (positive or negative) X direction or along the global (positive or negative) Y vector.
   * The bottom side of the main model should have an outward normal vector that points in the negative global Z direction.
   * In 3D models the sides L (left),R (right),F (front) and K (back) may have some natural distortion due to the topography. This is supported by the boundary element, but when the distortion along the Z direction is too large, the results can slightly deteriorate.
   
   .. figure:: ASDAbsorbingBoundary_distortion.png
      :align: center
      :figclass: align-center
      
      Exploded-view: Effects of Z-distortion in 3D problems.

.. admonition:: Example 

   1. **Tcl Code**

   .. code-block:: tcl

      # 2D problem with 2 DOFs on both the constrained node and the retained nodes
      # The embedding domain is a 1x1 triangle, and the constrained node is placed at its centroid.
      # Here we apply a random displacement on each retained node,
      # and the displacement of the constrained node should be the weighted average 
      # of the displacements at the 3 retained nodes, with an equal weight = 1/3.
      
      model basic -ndm 2 -ndf 2
      
      # define the embedding domain (a piece of a soild domain)
      node 1 0.0 0.0
      node 2 1.0 0.0
      node 3 0.0 1.0
      
      # define the embedded node
      node 4 [expr 1.0/3.0] [expr 1.0/3.0]
      
      # define constraint element
      element ASDEmbeddedNodeElement 1   4   1 2 3   -K 1.0e6
      
      # apply random imposed displacement in range 0.1-1.0
      set U1 [list [expr 0.1 + 0.9*rand()] [expr 0.1 + 0.9*rand()]]
      set U2 [list [expr 0.1 + 0.9*rand()] [expr 0.1 + 0.9*rand()]]
      set U3 [list [expr 0.1 + 0.9*rand()] [expr 0.1 + 0.9*rand()]]
      puts "Applying random X displacement:\nU1: $U1\nU2: $U2\nU3: $U3\n\n"
      timeSeries Constant 1
      pattern Plain 1 1 {
         for {set i 1} {$i < 3} {incr i} {
            sp 1 $i [lindex $U1 [expr $i - 1]]
            sp 2 $i [lindex $U2 [expr $i - 1]]
            sp 3 $i [lindex $U3 [expr $i - 1]]
         }
      }
      
      # run analysis
      constraints Transformation
      numberer Plain
      system FullGeneral
      test NormUnbalance 1e-08 10 1
      algorithm Linear
      integrator LoadControl 1.0
      analysis Static
      analyze 1
      
      # compute expected solution
      set UCref [list [expr ([lindex $U1 0] + [lindex $U2 0] + [lindex $U3 0] )/3.0] [expr ([lindex $U1 1] + [lindex $U2 1] + [lindex $U3 1] )/3.0]]
      puts "Expected displacement at constrained node is (U1+U2+U3)/3:\n$UCref\n\n"
      
      # read results
      set UC [list {*}[nodeDisp 4]]
      puts "Obtained displacement at constrained node is UC:\n$UC\n\n"
      
      # check error
      set ER [list [expr abs([lindex $UC 0] - [lindex $UCref 0])/[lindex $UCref 0]] [expr abs([lindex $UC 1] - [lindex $UCref 1])/[lindex $UCref 1]]]
      puts "Relative error is abs(UC-UCref)/UCref:\n$ER\n\n"
      

   2. **Python Code**

   .. code-block:: python

      # 2D problem with 2 DOFs on both the constrained node and the retained nodes
      # The embedding domain is a 1x1 triangle, and the constrained node is placed at its centroid.
      # Here we apply a random displacement on each retained node,
      # and the displacement of the constrained node should be the weighted average 
      # of the displacements at the 3 retained nodes, with an equal weight = 1/3.
      from opensees import *
      from random import random as rand
      
      model('basic', '-ndm', 2, '-ndf', 2)
      
      # define the embedding domain (a piece of a soild domain)
      node(1, 0.0, 0.0)
      node(2, 1.0, 0.0)
      node(3, 0.0, 1.0)
      
      # define the embedded node
      node(4, 1.0/3.0, 1.0/3.0)
      
      # define constraint element
      element('ASDEmbeddedNodeElement', 1,   4,   1, 2, 3,   '-K', 1.0e6)
      
      # apply random imposed displacement in range 0.1-1.0
      U1 = [0.1 + 0.9*rand(), 0.1 + 0.9*rand()]
      U2 = [0.1 + 0.9*rand(), 0.1 + 0.9*rand()]
      U3 = [0.1 + 0.9*rand(), 0.1 + 0.9*rand()]
      print('Applying random X displacement:\nU1: {}\nU2: {}\nU3: {}\n\n'.format(U1,U2,U3))
      timeSeries('Constant', 1)
      pattern('Plain', 1, 1)
      for i in range(1, 3):
         sp(1, i, U1[i - 1])
         sp(2, i, U2[i - 1])
         sp(3, i, U3[i - 1])
      
      
      # run analysis
      constraints('Transformation')
      numberer('Plain')
      system('FullGeneral')
      test('NormUnbalance', 1e-08, 10, 1)
      algorithm('Linear')
      integrator('LoadControl', 1.0)
      analysis('Static')
      analyze(1)
      
      # compute expected solution
      UCref = [
         (U1[0] + U2[0] + U3[0])/3.0,
         (U1[1] + U2[1] + U3[1])/3.0
         ]
      print('Expected displacement at constrained node is (U1+U2+U3)/3:\n{}\n\n'.format(UCref))
      
      # read results
      UC = nodeDisp(4)
      print('Obtained displacement at constrained node is UC:\n{}\n\n'.format(UC))
      
      # check error
      ER = [
         abs(UC[0] - UCref[0])/UCref[0],
         abs(UC[1] - UCref[1])/UCref[1]
         ]
      print('Relative error is abs(UC-UCref)/UCref:\n{}\n\n'.format(ER))

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.

.. [Nielsen2006] | Nielsen, Andreas H. "Absorbing boundary conditions for seismic analysis in ABAQUS." ABAQUS users’ conference. 2006.. (`Link to article <https://www.researchgate.net/profile/Sahand-Jabini-Asli-2/post/How_can_i_define_Absorbing_boundary_in_ABAQUS_EXPLICIT2/attachment/59d634b679197b80779925d8/AS%3A380916271730688%401467828924106/download/architecture_absorbing_auc06_babtie.pdf>`_)
