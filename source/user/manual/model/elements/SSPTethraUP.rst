.. _SSPTethraUP:

SSPTethraUP Element
^^^^^^^^^^^^^^^^^^^

The ``SSPTethraUP`` element is a 4-node single-point tetrahedron element with a :math:`u-p` (displacement-pressure) formulation for 3D dynamic analysis of saturated porous media. It is derived from the ``SSPbrickUP`` element :cite:`mcgann2011`, but tailored for tetrahedral meshes. 

Since a linear 4-node tetrahedron with one-point integration has constant strains and no hourglass (zero-energy) modes, the membrane stabilization required for the hexahedral SSP elements is not needed :cite:`zienkiewicz2000`. However, pressure field stabilization (parameter :math:`\alpha`) is retained and enhanced with automatic regularization to prevent numerical instabilities (e.g., excessive displacements or singular matrices) in undrained or nearly incompressible conditions :cite:`white2008`, :cite:`zienkiewicz1999`.

.. function:: element SSPTethraUP $eleTag $n1 $n2 $n3 $n4 $matTag $fBulk $fDens $k1 $k2 $k3 $e $alpha <$b1 $b2 $b3> <-lumped>

.. list-table::
    :widths: 10 10 40
    :header-rows: 1

 - Argument
    - Type
    - Description
 - ``$eleTag``
    - |integer|
    - Unique element tag.
 - ``$n1 $n2 $n3 $n4``
    - |integer|
    - Tags of the four nodes defining the element. Nodes 1-2-3 must appear counter-clockwise when viewed from node 4 to ensure a positive Jacobian (volume) :cite:`zienkiewicz2000`.
 - ``$matTag``
    - |integer|
    - Tag of the ``NDMaterial`` object representing the solid skeleton (e.g., ``ElasticIsotropic``, ``PressureDependMultiYield03``).
 - ``$fBulk``
    - |float|
    - Bulk modulus of the pore fluid.
 - ``$fDens``
    - |float|
    - Mass density of the pore fluid.
 - ``$k1 $k2 $k3``
    - |float|
    - Permeability coefficients in the global x, y, and z directions, respectively.
 - ``$e``
    - |float|
    - Initial void ratio of the solid phase.
 - ``$alpha``
    - |float|
    - Pressure field stabilization parameter. Dimension: :math:`L^2/P` (e.g., :math:`m^2/kPa`). 
      If ``$alpha > 0``, the provided value is used. 
      If ``$alpha <= 0``, an automatic element-by-element regularization is activated based on the characteristic length and constrained modulus :cite:`white2008`. This prevents numerical instability in undrained conditions.
 - ``$b1 $b2 $b3``
    - |float|
    - Optional: Body forces acting on the element in x, y, and z directions.
 - ``-lumped``
    - |string|
    - Optional: Flag to use a lumped mass matrix instead of the consistent one.

.. note::
    * **Degrees of Freedom:** Each node has 4 DOFs: :math:`u_x, u_y, u_z, p`.
    * **Pore Pressure Convention:** Consistent with the SSP UP element family :cite:`mcgann2011`, the physical pore pressure is the **velocity** of the 4th DOF, not the DOF value itself. When recording pore pressure, use ``-dof 4 vel``.
    * **Undrained Conditions:** For perfectly undrained analyses (:math:`k_1=k_2=k_3=0`), it is highly recommended to use the automatic regularization (``$alpha <= 0``) or manually compute an appropriate :math:`\alpha` based on the constrained modulus :math:`M` of the soil skeleton to avoid singular stiffness/mass matrices and spurious pressure modes :cite:`zienkiewicz1999`.
    * **Node Ordering:** Incorrect node ordering will result in a negative or zero volume, and the element will be ignored or trigger an error.

Theory
""""""

The element is based on the generalized Biot :math:`u-p` formulation :cite:`biot1941`, :cite:`zienkiewicz1984`. For a linear 4-node tetrahedron, the strain-displacement matrix :math:`B` and the shape function gradients :math:`\nabla N_p` are constant over the element volume :math:`V`. The one-point integration rule at the centroid is exact :cite:`zienkiewicz2000`.

**Solid Phase Stiffness**
The solid phase stiffness matrix is computed as:

.. math::
    K_s = \int_V B^T C B \, dV = V B^T C B

where :math:`C` is the material tangent stiffness matrix :cite:`zienkiewicz2000`.

**Fluid Compressibility and Stabilization**
The fluid compressibility matrix :math:`S` and the pressure stabilization matrix :math:`P_s` are assembled in the mass/damping blocks. To satisfy the Babuška-Brezzi (inf-sup) condition and avoid spurious pressure modes in nearly incompressible/undrained limits :cite:`zienkiewicz1999`, :cite:`white2008`, a stabilization matrix is added:

.. math::
    P_s = \alpha \int_V \nabla N_p^T \nabla N_p \, dV = \alpha V \nabla N_p^T \nabla N_p

When automatic regularization is enabled (``$alpha <= 0``), the stabilization parameter is computed element-by-element using a formulation derived from stabilized low-order finite elements for coupled problems :cite:`white2008`:

.. math::
    \alpha = \frac{h^2}{10 \max(K_f^{eff}, K_{ref})}

where:
* :math:`h = (6V)^{1/3}` is the characteristic element length :cite:`zienkiewicz2000`.
* :math:`K_f^{eff}` is the effective fluid bulk modulus (capped internally to avoid exact incompressibility).
* :math:`K_{ref}` is a reference stiffness modulus extracted from the material's initial tangent matrix (e.g., the constrained modulus :math:`M`).

**Matrix Layout**
Following the OpenSees :math:`u-p` convention :cite:`mcgann2011`:
* ``getTangentStiff``: :math:`\begin{bmatrix} K_s & 0 \\ 0 & 0 \end{bmatrix}`
* ``getDamp``: :math:`\begin{bmatrix} C & -Q \\ -Q^T & -H \end{bmatrix}`
* ``getMass``: :math:`\begin{bmatrix} M_s & 0 \\ 0 & -(S+P_s) \end{bmatrix}`

.. admonition:: Example:

    1. **Tcl Code**

    .. code-block:: tcl

        # ============================================================
		# Test: SSPbrickUP vs SSPTethraUP 
	    # Gianluca Cavallo - gi.cav.2586@gmail.com
		# ============================================================

		wipe

		# -----------------------------
		# Parametri comuni
		# -----------------------------

		# Units: kN, m, s, kPa, Mg/m3
		set E    25000.0      
		set nu   0.485        
		set rho  2.0          

		# Fluid
		set fBulk 2.2e6       
		set fDens 1.0         

		# Permeability
		set k 0.0

		# Porosita e rapporto dei vuoti
		set n 0.4
		set e [expr $n/(1.0-$n)]

		# Total vertical load on top face, kPa*m^2 = kN
		set q 10.0

		# Analysis
		set dt     0.001
		set T      1.0
		set nSteps [expr int($T/$dt)]

		# Constrained Module / P-wave modulus
		set M [expr $E*(1.0-$nu)/((1.0+$nu)*(1.0-2.0*$nu))]

		# alpha: h = 1 m
		# alpha = h^2 / (20*M)
		set alphaBrick [expr 1.0/(20.0*$M)]
		set alphaTet   $alphaBrick

		puts "=============================================="
		puts "E       = $E kPa"
		puts "nu      = $nu"
		puts "rho     = $rho Mg/m3"
		puts "fBulk   = $fBulk kPa"
		puts "k       = $k"
		puts "e       = $e"
		puts "M       = $M kPa"
		puts "alphaBrick = $alphaBrick"
		puts "alphaTet   = $alphaTet"
		puts "=============================================="


		# ============================================================
		# MODELLO 1: SSPbrickUP
		# ============================================================

		model BasicBuilder -ndm 3 -ndf 4

		node 1 0.0 0.0 0.0
		node 2 1.0 0.0 0.0
		node 3 1.0 1.0 0.0
		node 4 0.0 1.0 0.0

		node 5 0.0 0.0 1.0
		node 6 1.0 0.0 1.0
		node 7 1.0 1.0 1.0
		node 8 0.0 1.0 1.0

		fix 1 1 1 1 0
		fix 2 1 1 1 0
		fix 3 1 1 1 0
		fix 4 1 1 1 0

		equalDOF 5 6  1 2 3
		equalDOF 5 7  1 2 3
		equalDOF 5 8  1 2 3

		nDMaterial ElasticIsotropic 1 $E $nu $rho

		element SSPbrickUP 1 1 2 3 4 5 6 7 8 1 $fBulk $fDens $k $k $k $e $alphaBrick


		timeSeries Path 1 -time {0.0 0.5 1.0} -values {0.0 1.0 1.0}

		pattern Plain 1 1 {
			load 5 0.0 0.0 [expr -0.25*$q] 0.0
			load 6 0.0 0.0 [expr -0.25*$q] 0.0
			load 7 0.0 0.0 [expr -0.25*$q] 0.0
			load 8 0.0 0.0 [expr -0.25*$q] 0.0
		}

		# Recorder
		recorder Node -file brick_top_disp.out   -time -node 5 6 7 8 -dof 3 disp
		recorder Node -file brick_top_press.out  -time -node 5 6 7 8 -dof 4 vel
		
		# STKO Output
		recorder mpco "qw_brick.mpco" -N "displacement" "pressure" -E "stress" "strain"

		test        NormDispIncr 1.0e-5 100 1
		algorithm   Linear
		numberer    RCM
		system      ProfileSPD
		constraints Penalty 10e12 10e12
		integrator  Newmark 0.5 0.25
		analysis    Transient

		set okBrick [analyze $nSteps $dt]

		if {$okBrick == 0} {
			set brickUz [expr 0.25*([nodeDisp 5 3] + [nodeDisp 6 3] + [nodeDisp 7 3] + [nodeDisp 8 3])]
			set brickP  [expr 0.25*([nodeVel  5 4] + [nodeVel  6 4] + [nodeVel  7 4] + [nodeVel  8 4])]

			puts "SSPbrickUP analysis OK"
			puts "SSPbrickUP final avg uz = $brickUz"
			puts "SSPbrickUP final avg p  = $brickP"
		} else {
			set brickUz "FAILED"
			set brickP  "FAILED"
			puts "SSPbrickUP analysis FAILED"
		}

		remove recorders
		wipe


		# ============================================================
		# MODELLO 2: SSPTethraUP
		# ============================================================

		model BasicBuilder -ndm 3 -ndf 4

		node 1 0.0 0.0 0.0
		node 2 1.0 0.0 0.0
		node 3 1.0 1.0 0.0
		node 4 0.0 1.0 0.0

		node 5 0.0 0.0 1.0
		node 6 1.0 0.0 1.0
		node 7 1.0 1.0 1.0
		node 8 0.0 1.0 1.0

		fix 1 1 1 1 0
		fix 2 1 1 1 0
		fix 3 1 1 1 0
		fix 4 1 1 1 0

		equalDOF 5 6  1 2 3
		equalDOF 5 7  1 2 3
		equalDOF 5 8  1 2 3

		nDMaterial ElasticIsotropic 1 $E $nu $rho

		element SSPTethraUP 11 1 2 3 7 1 $fBulk $fDens $k $k $k $e $alphaTet
		element SSPTethraUP 12 1 3 4 7 1 $fBulk $fDens $k $k $k $e $alphaTet
		element SSPTethraUP 13 1 4 8 7 1 $fBulk $fDens $k $k $k $e $alphaTet
		element SSPTethraUP 14 1 8 5 7 1 $fBulk $fDens $k $k $k $e $alphaTet
		element SSPTethraUP 15 1 5 6 7 1 $fBulk $fDens $k $k $k $e $alphaTet
		element SSPTethraUP 16 1 6 2 7 1 $fBulk $fDens $k $k $k $e $alphaTet

		timeSeries Path 1 -time {0.0 0.5 1.0} -values {0.0 1.0 1.0}

		pattern Plain 1 1 {
			load 5 0.0 0.0 [expr -0.25*$q] 0.0
			load 6 0.0 0.0 [expr -0.25*$q] 0.0
			load 7 0.0 0.0 [expr -0.25*$q] 0.0
			load 8 0.0 0.0 [expr -0.25*$q] 0.0
		}

		# Recorder
		recorder Node -file tetra_top_disp.out   -time -node 5 6 7 8 -dof 3 disp
		recorder Node -file tetra_top_press.out  -time -node 5 6 7 8 -dof 4 vel
		
		#STKO Output
		recorder mpco "qw_tetra.mpco" -N "displacement" "pressure" -E "stress" "strain"


		test        NormDispIncr 1.0e-5 100 1
		algorithm   Linear
		numberer    RCM
		system      ProfileSPD
		constraints Penalty 10e12 10e12
		integrator  Newmark 0.5 0.25
		analysis    Transient

		set okTetra [analyze $nSteps $dt]

		if {$okTetra == 0} {
			set tetraUz [expr 0.25*([nodeDisp 5 3] + [nodeDisp 6 3] + [nodeDisp 7 3] + [nodeDisp 8 3])]
			set tetraP  [expr 0.25*([nodeVel  5 4] + [nodeVel  6 4] + [nodeVel  7 4] + [nodeVel  8 4])]

			puts "SSPTethraUP analysis OK"
			puts "SSPTethraUP final avg uz = $tetraUz"
			puts "SSPTethraUP final avg p  = $tetraP"
		} else {
			set tetraUz "FAILED"
			set tetraP  "FAILED"
			puts "SSPTethraUP analysis FAILED"
		}

		remove recorders

		puts "=============================================="
		puts "Final Check"
		puts "SSPbrickUP  uz = $brickUz   p = $brickP"
		puts "SSPTethraUP uz = $tetraUz   p = $tetraP"
		puts "=============================================="
References
""""""""""

.. [1] Biot, M. A. (1941). "General theory of three-dimensional consolidation." *Journal of Applied Physics*, 12(2), 155-164. https://doi.org/10.1063/1.1712886

.. [2] Zienkiewicz, O. C., & Shiomi, T. (1984). "Dynamic behaviour of saturated porous media; the generalized Biot formulation and its numerical solution." *International Journal for Numerical and Analytical Methods in Geomechanics*, 8(1), 71-96. https://doi.org/10.1002/nag.1610080106

.. [3] McGann, C. R. (2011). "Stabilized Single-Point Finite Elements for Dynamic Analysis of Fluid Saturated Porous Media." PhD thesis, University of Washington. [Bibliographic record and full text to be verified.]

.. [4] Zienkiewicz, O. C., Chan, A. H. C., Pastor, M., Schrefler, B. A., & Shiomi, T. (1999). *Computational Geomechanics (with Special Reference to Earthquake Engineering).* John Wiley & Sons. ISBN 0-471-98285-7.

.. [5] White, J. A., & Borja, R. I. (2008). "Stabilized low-order finite elements for coupled solid-deformation/fluid-diffusion and their application to fault zone transients." *Computer Methods in Applied Mechanics and Engineering*, 197(49-50), 4353-4366. https://doi.org/10.1016/j.cma.2008.05.015

.. [6] Zienkiewicz, O. C., & Taylor, R. L. (2000). *The Finite Element Method: Its Basis and Fundamentals* (5th ed.). Butterworth-Heinemann.