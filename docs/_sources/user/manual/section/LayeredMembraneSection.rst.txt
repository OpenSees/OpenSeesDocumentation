.. _LayeredMembraneSection:

LayeredMembraneSection 
^^^^^^^^^^^^^^^^

This command is used to construct a LayeredMembraneSection object. It is the abstract representation for the stress-strain behavior for a layered membrane element (based on the work of Rojas et al., 2016). The LayeredMembraneSection is similar to the **RCLMS** class, except that this class  allows the use of nd materials available in OpenSees.

.. figure:: LMS_figure.png
	:align: center
	:figclass: align-center
	:width: 60%
	:name: LMS_FIG
	
	LayeredMembraneSection: (a) Layer discretization; (b) Strain field; (c) Resultant stress field.

.. admonition:: Command
   
   section LayeredMembraneSection $secTag $total_thickness $nLayers -mat{$Material_tags} -thick{$Thicknesses} <-Eout $OutofPlaneModulus>

.. csv-table:: 
   :header: "Parameter", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, integer, unique section tag
   $total_thickness, float, total section thickness
   $nLayers, integer, number of layers
   $Material_tags, list int, a list of *nLayers* nDMaterial tags
   $Thicknesses, list float, a list of *nLayers* layers thicknesses
   $OutofPlaneModulus, float, Elasticity modulus of out of plane (optional: default = 0.0)


The following recorders are available with the LayeredMembraneSection.
   
.. csv-table:: 
   :header: "Recorder", "Description"
   :widths: 20, 40

   panel_strain, "strains :math:`\varepsilon_{xx}`, :math:`\varepsilon_{yy}`, :math:`\gamma_{xy}`"
   panel_avg_stress, "resulting panel stresses :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\tau_{xy}`"
   panel_force, "membrane forces at panel level :math:`N_{x}`, :math:`N_{y}`, :math:`N_{xy}`"
   layer $ilayer $Response, "returns material $Response for a ilayer-th layer. For available $Response(s) refer to material"

.. admonition:: Notes

   | 1. The **LayeredMembraneSection** can be used in a ``MEFI`` element. 
   | 2. The section can also be referred to as **LMS**.

.. admonition:: Examples
   
   For the development of this example, the RW-A20-P10-S38 wall specimen was employed (Tran, 2012). Uniaxial concrete and steel materials are defined, along with FSAM nDMaterials used within LMS sections to represent sections of types **a** and **b**, as illustrated in Fig. 3.1.7.1(a) for the RCLMS example.

   1. **Tcl Code**

   .. code-block:: tcl

      # ========================================================================================
      # RW-A20-P10-S38 (Tran, 2012) - Definition of properties and creation of materials
      # Basic units: N, mm
      # ========================================================================================
      # ----------------------------------------------------------------------------------------
      # Create uniaxial steel materials
      # ----------------------------------------------------------------------------------------

      # steel X
      set fyX 469.93;                    # fy
      set bx 0.02;                       # strain hardening

      # steel Y web
      set fyYw 409.71;                   # fy
      set byw 0.02;                      # strain hardening

      # steel Y boundary
      set fyYb 429.78;                   # fy
      set byb 0.01;                      # strain hardening

      # steel misc
      set Es 200000.0;                   # Young's modulus
      set R0 20.0;                       # initial value of curvature parameter
      set A1 0.925;                      # curvature degradation parameter
      set A2 0.15;                       # curvature degradation parameter
  
      # build steel materials
      uniaxialMaterial  Steel02  1 $fyX  $Es $bx  $R0 $A1 $A2; # steel X
      uniaxialMaterial  Steel02  2 $fyYw $Es $byw $R0 $A1 $A2; # steel Y web
      uniaxialMaterial  Steel02  3 $fyYb $Es $byb $R0 $A1 $A2; # steel Y boundary

      # ----------------------------------------------------------------------------------------
      # Create uniaxial concrete materials
      # ----------------------------------------------------------------------------------------

      # unconfined
      set fpc -47.09;                                      # peak compressive stress
      set ec0 -0.00232;                                    # strain at peak compressive stress
      set ft 2.13;                                         # peak tensile stress
      set et 0.00008;                                      # concrete strain at tension cracking
      set Ec 34766.59;                                     # Young's modulus

      # confined
      set fpcc -53.78;                                     # peak compressive stress
      set ec0c -0.00397;                                   # strain at peak compressive stress
      set Ecc 36542.37;                                    # Young's modulus

      # build concrete materials
      uniaxialMaterial ConcreteCM 4 $fpc  $ec0  $Ec  7.16 1.016 $ft $et 1.2 10000;      # unconfined concrete
      uniaxialMaterial ConcreteCM 5 $fpcc $ec0c $Ecc 8.44 1.023 $ft $et 1.2 10000;      # confined concrete

      # define reinforcing ratios  
      set rouXw 0.0027;   # X web 
      set rouXb 0.0082;   # X boundary 
      set rouYw 0.0027;   # Y web
      set rouYb 0.0323;   # Y boundary

      # shear resisting mechanism parameters

      set nu 0.35;                # friction coefficient
      set alfadow 0.005;          # dowel action stiffness parameter
      
      # ----------------------------------------------------------------------------------------
      # Create FSAM nDMaterial
      # ----------------------------------------------------------------------------------------
	  
      nDMaterial FSAM 6  0.0  1   2   4  $rouXw $rouYw  $nu  $alfadow;   # Web (unconfined concrete)
      nDMaterial FSAM 7  0.0  1   3   5  $rouXb $rouYb  $nu  $alfadow;   # Boundary (confined concrete)

      # ----------------------------------------------------------------------------------------
      # Create LayeredMembraneSection section
      # ----------------------------------------------------------------------------------------
      
      set tw 152.4;                 # Wall thickness

      section LMS 10 $tw 1 -mat 6 -thick $tw;     # Section type b (wall web)
      section LMS 11 $tw 1 -mat 7 -thick $tw;     # Section type a (wall boundary)
		
   2. **Python Code**

   .. code-block:: python

      # ========================================================================================
      # RW-A20-P10-S38 (Tran, 2012) - Definition of properties and creation of materials
      # Basic units: N, mm
      # ========================================================================================
	  
      # ----------------------------------------------------------------------------------------
      # Create uniaxial steel materials
      # ----------------------------------------------------------------------------------------
      # steel x
      fyX = 469.93             # fy
      bx = 0.02                # strain hardening

      # steel Y web
      fyYw = 409.71            # fy
      byw = 0.02               # strain hardening

      # steel Y boundary
      fyYb = 429.78            # fy
      byb = 0.01               # strain hardening

      # steel misc
      Es = 200000.0            # Young's modulus
      R0 = 20.0                # initial value of curvature parameter
      A1 = 0.925               # curvature degradation parameter
      A2 = 0.15                # curvature degradation parameter

      # build steel materials
      ops.uniaxialMaterial('Steel02', 1, fyX,  Es, bx,  R0, A1, A2)  # steel X
      ops.uniaxialMaterial('Steel02', 2, fyYw, Es, byw, R0, A1, A2)  # steel Y web
      ops.uniaxialMaterial('Steel02', 3, fyYb, Es, byb, R0, A1, A2)  # steel Y boundary

      # ----------------------------------------------------------------------------------------
      # Create uniaxial concrete materials
      # ----------------------------------------------------------------------------------------
      # unconfined
      fpc = -47.09             # peak compressive stress
      ec0 = -0.00232           # strain at peak compressive stress
      ft = 2.13                # peak tensile stress
      et = 0.00008             # strain at peak tensile stress
      Ec = 34766.59            # Young's modulus

      # confined
      fpcc = -53.78            # peak compressive stress
      ec0c = -0.00397          # strain at peak compressive stress
      Ecc = 36542.37           # Young's modulus

      # build concrete materials
      ops.uniaxialMaterial('ConcreteCM', 4, fpc,  ec0, Ec, 7.16, 1.016, ft, et, 1.2, 10000)      # unconfined concrete
      ops.uniaxialMaterial('ConcreteCM', 5, fpcc, ec0c, Ecc, 8.44, 1.023, ft, et, 1.2, 10000)    # confined concrete

      # define reinforcing ratios   
      rouXw = 0.0027         # X web 
      rouXb = 0.0082         # X boundary 
      rouYw = 0.0027         # Y web
      rouYb = 0.0323         # Y boundary

      # shear resisting mechanism parameters 
      nu = 0.35                           # friction coefficient
      alfadow = 0.005                     # dowel action stiffness parameter
      
      # ----------------------------------------------------------------------------------------
      # Create FSAM nDMaterial
      # ----------------------------------------------------------------------------------------
      
      ops.nDMaterial('FSAM', 6, 0.0, 1, 2, 4, rouXw, rouYw, nu, alfadow)           # Web (unconfined concrete)
      ops.nDMaterial('FSAM', 7, 0.0, 1, 3, 5, rouXb, rouYb, nu, alfadow)           # Boundary (confined concrete)

      # ----------------------------------------------------------------------------------------
      # Create LayeredMembraneSection section
      # ----------------------------------------------------------------------------------------

      tw = 152.4    # Wall thickness

      ops.section('LMS', 10, tw, 1, '-mat', 6, '-thick', tw)    # Section type b (wall web)
      ops.section('LMS', 11, tw, 1, '-mat', 7, '-thick', tw)    # Section type a (wall boundary)



**REFERENCES:**

#. Rojas, F., Anderson, J. C., Massone, L. M. (2016). A nonlinear quadrilateral layered membrane element with drilling degrees of freedom for the modeling of reinforced concrete walls. Engineering Structures, 124, 521-538. (`link <https://www.sciencedirect.com/science/article/pii/S0141029616302954>`_).
#. Tran, T. A. (2012). Experimental and Analytical Studies of Moderate Aspect Ratio Reinforced Concrete Structural Walls. Ph.D. Dissertation, Department of Civil and Environmental Engineering, University of California, Los Angeles. (`link <https://escholarship.org/uc/item/1538q2p8>`_).

**Code Developed by:** F. Rojas (University of Chile), M.J. Núñez (University of Chile).
