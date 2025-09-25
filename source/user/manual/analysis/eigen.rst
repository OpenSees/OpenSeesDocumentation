.. _eigen:

eigen Command
*************

This command is used to perform the eigenvalue analysis.

.. function:: eigen <type> <$solver> $numEigenvalues

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
   $numEigenvalues, |integer|, number of eigenvalues required.
   $solver, |string|, "optional string detailing type of solver: -genBandArpack (default), -fullGenLapack, -symmBandLapack."
   $type, |string|, optional string indicating type of eigenvalue problem to solve: 'general' (default) or 'standard'

.. admonition:: Returns
   
   A list containing the eigenvalues


.. note::
   1.  The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
   2.  The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.
   3. The -symmBandLapack option works only standard eigenvalue analysis of the stiffness matrix, i.e., K*x = lam*x


.. warning::

   The default eigen solver utilizes **ARPACK**, an iterative eigenvalue solver. Like other iterative methods, ARPACK can struggle to accurately compute eigenvectors when matrices contain repeated (degenerate) eigenvalues or clusters of closely spaced eigenvalues. The issue arises from difficulties in establishing an orthonormal basis for the eigenspace.

   In such cases, ARPACK may fail to find all of the requested eigenvalues, or it may return correct eigenvalues but incorrect eigenvectors. When modal damping is used, inaccurate eigenvectors may cause issues with the damping forces calculated. If you are unsure if this is an issue with your model, switch the **solver** used, as the eigenvectors will vary greatly with the chosen solver for such cases.

   Fortunately, small adjustments to the **model** typically prevent this issue. In practical models, material properties (e.g., Young’s modulus) or nodal masses are rarely identical — exact degeneracy is unusual outside of academic test cases. By introducing slight variations, ARPACK is more likely to resolve the eigenstructure correctly. 


   .. code::

      model Basic -ndm 1 -ndf 1
      node 0 0; fix 0 1
      node 1 0; mass 1 1.0
      node 2 0; mass 2 1.0
      node 3 0; mass 3 1.0
      node 4 0; mass 4 1.0

      set k 610
      uniaxialMaterial Elastic 1 $k

      element zeroLength 1 0 1 -mat 1 -dir 1
      element zeroLength 2 1 2 -mat 1 -dir 1
      element zeroLength 3 0 3 -mat 1 -dir 1
      element zeroLength 4 3 4 -mat 1 -dir 1

      systetm ProfileSPD
      numberer RCM
      
      set nModes 2
      set eigV [eigen $nModes]
      puts "Eigenvalues: $eigV"

      # print eigenvectors
      for {set i 1} {$i <= 4} {incr i 1}  {
         puts "$i [nodeEigenvector $i 1] [nodeEigenvector $i 2]"
      }


   will produce:

   .. code::
      
      Eigenvalues:  232.99926686256409880116   232.99926686256412722287  
      1    0.50235827201282656773    0.15501409223134476889
      2    0.81283275864641846287    0.25081806996552691302
      3    0.15501409223134465787   -0.50235827201282667875
      4    0.25081806996552685751   -0.81283275864641857389
   
   wheras if I change the mass at node **4** using:

   .. code::
      
      node 4 0; mass 4 1.0000000001   

   I would get:
   
   .. code::

      Eigenvalues:  232.99926679816474006657   232.99926686256424090971  
      1   -0.00000004574590262152    0.52573111211913170493
      2   -0.00000007401842538890    0.85065080835203654708
      3    0.52573111211146139610    0.00000004574590273254
      4    0.85065080819431726500    0.00000007401842544441
   

   For this in an academic setting dealing with small problems, the **-fullGenLapack** option will provide correct eigenvalues and eigenvectors to the original problem:

   .. code::   
      set eigV [eigen $nModes]

   will produce:
   
   .. code::
      
      Eigenvalues:   232.99926684570411339337   232.99926686256412722287  
      1    0.00000000000000000000   -0.52573111211913370333
      2    0.00000000000000000000   -0.85065080835203987775
      3    0.52573111209361389484    0.00000000000000000000
      4    0.85065080832527950605   -0.00000000000000000000
      
Theory
^^^^^^
|  A *generalized eigenvalue problem* for two symmetric matrices :math:`K` and :math:`M` of size :math:`n \times n` is given by:

.. math::
   \left (K - \lambda M \right ) \Phi = 0

|  where:
   
   *  :math:`K` is the stiffness matrix
   *  :math:`M` is the mass matrix
   *  :math:`\lambda` is the eigenvalue
   *  and :math:`\Phi` is the associated eigenvector

.. admonition:: Example
   
   The following example shows how to use the eigen command to obtain a list of eigenvalues.

   1. **Tcl Code**
   
   .. code:: tcl

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      set eigenvalues [eigen 10]
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      set eigenvalues [eigen -fullGenLapack 10]

      # obtain 10 eigenvalues of the stiffness matrix
      set eigenvalues [eigen standard -symmBandLapack 10]

   2. **Python Code**

   .. code:: python

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      eigenvalues = eigen(10)
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      eigenvalues = eigen('-fullGenLapack', 10)

      # obtain 10 eigenvalues of the stiffness matrix
      eigenvalues = eigen('standard','-symmBandLapack',10)

Code Developed by: |fmk|
