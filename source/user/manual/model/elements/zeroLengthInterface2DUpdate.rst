zeroLengthInterface2DUpdate
===========================

**zeroLengthInterface2DUpdate** fixes bugs in **zeroLengthInterface2D** and adds a new feature that allows the user to change the friction coefficient during the analysis. 
 
(**zeroLengthInterface2D** was written by Roozbeh Geraili Mikola (roozbehg@berkeley.edu) and Prof. Nicholas Sitar (nsitar@ce.berkeley.edu) on July 02 2010.)

Bugs fixed in zeroLengthInterface2D
-------------------------------------
1. Incorrect friction behavior when the interface is under cyclic sliding motion.
2. Incorrect normal pressure behavior due to the repetitive search algorithm. The original zeroLengthInterface2D overestimates normal pressure at the interface.

User Instruction
----------------

1. **Element Command Syntax**

   The tcl input command for the zeroLengthInterface2DUpdate element is the same as for zeroLengthInterface2D::

      element zeroLengthInterface2DUpdate eleTag? -sNdNum sNdNum? -pNdNum pNdNum? –dof sdof? mdof? -Nodes Nodes? Kn? Kt? phi?

2. **Tcl Input Example**

   .. image:: https://github.com/user-attachments/assets/7833184d-cea4-40ee-9198-c795f353c3d1
      :alt: Tcl input example

   **element zeroLengthInterface2DUpdate 1 -sNdNum 6 -mNdNum 2 -dof 3 2 -Nodes 10 9 8 7 6 5 4 1 $Kn $Kt $phi**

   *(The above defines a zeroLengthInterface2DUpdate element between a quad element (in blue) and beam elements (in red).)*

3. **Changing the Friction Coefficient**

   To update the friction coefficient during analysis, modify the parameter named "phi". For example:

   .. code-block:: tcl

      set Kn 1e6
      set Kt 1e6
      set phi_ini 0.0
      element zeroLengthInterface2DUpdate 1 -sNdNum 6 -mNdNum 2 -dof 3 2 -Nodes 10 9 8 7 6 5 4 1 $Kn $Kt $phi_ini

   *(This creates a zeroLengthInterface2DUpdate element with zero friction, and both normal and tangential stiffness equal to 1e6.)*

   Then, update the friction coefficient as follows:

   .. code-block:: tcl

      parameter 1 element 1 phi
      updateParameter 1 [expr 16.7]

   *(The above changes the friction coefficient in element 1 from 0 to 0.3.)*

  Full tcl example code
----------------
.. code-block:: tcl
  wipe 
  # Create ModelBuilder with 3 dimensions and 6 DOF/node
  model basic -ndm 2 -ndf 2
  
  # nDMaterial ElasticIsotropic $matTag $E $v <$rho>
  nDMaterial ElasticIsotropic   1   1e10   0.49  6.75 
  uniaxialMaterial Elastic 2 [expr 1e10];
  # ################################ 
  # build the model 
  # ################################# 
  
  node 1 6 0
  node 2 6 1 
  node 3 4 1
  node 4 4 0
  fix 3 1 0 0 
  element quad 1 1 2 3 4 1 PlaneStrain 1 
  
  set Kn 1e6; 
  set Kt 1e6; 
  set phi 16.7; 
  
  # Gravity loads
  pattern Plain 1 Linear {
  # sp $nodeTag $dofTag $dofValue
    sp 2 2 -1.e-2
    sp 3 2 -1.e-2 
  }
  
  model BasicBuilder -ndm 2 -ndf 3;
  
  node 5 0 0 
  node 6 2 0 
  node 7 4 0
  node 8 6 0
  node 9 8 0
  node 10 10 0
  
  geomTransf Linear 1
  # wall section
  section Fiber 1 {
  # patch rect $matTag $numSubdivY $numSubdivZ $yI $zI $yJ $zJ
     patch rect 2 100 1 [expr -15.0] -0.5 [expr 15.0] 0.5
  }
  
  element dispBeamColumn 2 5 6 5 1 1
  element dispBeamColumn 3 6 7 5 1 1
  element dispBeamColumn 4 7 8 5 1 1
  element dispBeamColumn 5 8 9 5 1 1
  element dispBeamColumn 6 9 10 5 1 1
  
  #element ZeroLengthContactNTS2D eleTag? -sNdNum sNode? -mNdNum mNode? -Nodes Nodes? Kn? Kt? fs?
  element zeroLengthInterface2D 7 -sNdNum 6 -mNdNum 2 -dof 3 2 -Nodes 10 9 8 7 6 5 4 1 [expr $Kn] [expr $Kt] [expr $phi]
  # element ZeroLengthNew 7 -sNdNum 6 -mNdNum 2 -dof 3 2 -Nodes 10 9 8 7 6 5 4 1 [expr $Kn] [expr $Kt] [expr $phi]
  fix 5 1 1 0
  fix 10 0 1 0   
  
  # ----------------------------
  # Start of recorder generation
  # ----------------------------
  recorder Node  -file  reactionForce.out  -node  5 10 -time -dof 1 2 reaction;
  recorder Node -file Node2.out -node 2 -dof 1 2 -time disp 
  recorder Node -file Node3.out -node 3 -dof 1 2 -time disp
  recorder Element -file Contactele.out -ele 7 -time force

  system SparseGeneral
  numberer RCM
  constraints Penalty   1.e+018   1.e+018
  test NormDispIncr  1.00e-0010 500 2
  algorithm KrylovNewton
  integrator  LoadControl 0.1
  analysis    Static
  
  analyze     5
  puts stdout "\ngravity finished"
  flush stdout
  
  wipeAnalysis
  
  model BasicBuilder -ndm 2 -ndf 2;
  loadConst -time 0.0
  remove sp 3 1
  remove sp 3 2
  
  pattern Plain 2 "Series -dt 1 -filePath loading.dat -factor 1.0" {
     sp 3 1 [expr 0.1]
  }
  constraints Transformation
  test        NormDispIncr 1e-7 500 2
  algorithm   KrylovNewton
  numberer    RCM
  system      ProfileSPD
  integrator  LoadControl 0.01
  # integrator  DisplacementControl 3 1 0.01
  analysis    Static
  
  analyze     300
  puts "\ncyclic slide finished\n"
.. code-block:: tcl
