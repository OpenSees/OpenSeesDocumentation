.. _ReinforcedConcreteLayerMembraneSection01:

ReinforcedConcreteLayerMembraneSection01
^^^^^^^^^^^^^^^^

This command is used to construct a ReinforcedConcreteLayerMembraneSection01 object. It is the abstract representation for the stress-strain behavior for a reinforced concrete layered membrane element (based on the work of Rojas et al., 2016).

.. admonition:: Command
   
   section ReinforcedConcreteLayerMembraneSection01 $secTag $nSteelLayer $nConcLayer -reinfSteel{$RSteelAtEachLayer} –conc{$concAtEachLayer} -concThick{$Thicknesses} <-epscr $ecr> <-epsc $ec>

.. csv-table:: 
   :header: "Parameter", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, integer, unique section tag
   $nSteelLayer, integer, number of reinforced steel layers
   $nConcLayer, integer, number of concrete layers
   $RSteelAtEachLayer, list int, a list of *nSteelLayer* nDMaterial reinforced steel tags to be assigned to each layer
   $concAtEachLayer, list int, a list of *nConcLayer* nDMaterial concrete tags to be assigned to each layer
   $Thicknesses, list float, a list of *nConcLayer* concrete layers thicknesses 
   $ecr, float, strain at tension cracking of the concrete (optional: default = 0.00008)
   $ec, float, strain at compression strength of the concrete (optional: default = -0.002)
   
   
   
The following recorders are available with the ReinforcedConcreteLayerMembraneSection01.

.. csv-table:: 
   :header: "Recorder", "Description"
   :widths: 20, 40

   panel_strain, "strains :math:`\varepsilon_{xx}`, :math:`\varepsilon_{yy}`, :math:`\gamma_{xy}`"
   panel_stress, "resulting panel stresses :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\tau_{xy}`"

.. admonition:: Notes

   | 1. The **ReinforcedConcreteLayerMembraneSection01** should be used in conjunction with ``OrthotropicRAConcrete`` and ``SmearedSteelDoubleLayer`` NDMaterials. It can also be used in a ``MEFI`` element. 
   | 2. In Tcl, the section can also be referred to as **RCLayerMembraneSection01** or **RCLMS01**.
   
.. admonition:: Examples
   
   For the development of this example, the RW-A20-P10-S38 wall specimen was used (Tran, 2012). Uniaxial concrete and steel materials are defined, along with orthotropic layers for confined/unconfined concrete and distributed steel for the core and boundaries. Sections of types **a** and **b** are defined, composed of the layers created earlier.

   .. figure:: ReinforcedConcreteLayerMembraneSection01_figure.jpg
	   :align: center
	   :figclass: align-center
	   :width: 90%
	   :name: RCLMS01_FIG
	
	   RW-A20-P10-S38 wall specimen: (a) Cross-sectional view ; (b) Layered view of the model.
   
   
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
      uniaxialMaterial Concrete02 4 $fpc $ec0 0.0 -0.037 0.1 $ft 1738.33;    	# unconfined concrete
      uniaxialMaterial Concrete02 5 $fpcc $ec0c -9.42 -0.047 0.1 $ft 1827.12; 	# confined concrete

      # define reinforcing ratios  
      set rouXw 0.0027;   # X web 
      set rouXb 0.0082;   # X boundary 
      set rouYw 0.0027;   # Y web
      set rouYb 0.0323;   # Y boundary

      # ----------------------------------------------------------------------------------------
      # Create orthotropic concrete layers to represent unconfined and confined concrete
      # ----------------------------------------------------------------------------------------

      nDMaterial OrthotropicRAConcrete 6 4 $et $ec0  0.0 -damageCte1 0.175 -damageCte2 0.5;   # unconfined concrete
      nDMaterial OrthotropicRAConcrete 7 5 $et $ec0c 0.0 -damageCte1 0.175 -damageCte2 0.5;   # confined concrete

      # ----------------------------------------------------------------------------------------
      # Create smeared steel layers to represent boundary and web reinforment
      # ----------------------------------------------------------------------------------------

      nDMaterial SmearedSteelDoubleLayer 8 1 2 $rouXw $rouYw 0.0;    # steel web
      nDMaterial SmearedSteelDoubleLayer 9 1 3 $rouXb $rouYb 0.0;    # steel boundary

      # ----------------------------------------------------------------------------------------
      # Create ReinforcedConcreteLayerMembraneSection01 sections composed of concrete and steel layers
      # ----------------------------------------------------------------------------------------

      set tw   152.4;    # Wall thickness
      set tnc  81.0;     # unconfined concrete wall layer thickness
      set tc   71.4;     # confined concrete wall layer thickness   

      section RCLMS01 10 1 1 -reinfSteel 8   -conc 6   -concThick $tw        -epscr $et -epsc $ec0;         # Section type b (wall web)
      section RCLMS01 11 1 2 -reinfSteel 9   -conc 6 7 -concThick $tnc $tc   -epscr $et -epsc $ec0c;        # Section type a (wall boundary)

		
   2. **Python Code**

   .. code-block:: python

      # ========================================================================================
      # RW-A20-P10-S38 (Tran, 2012) - Definition of properties and creation of materials
      # Basic units: N, mm
      # ========================================================================================

      # Import OpenSeesPy
      import openseespy.opensees as ops
	  
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
      ops.uniaxialMaterial('Concrete02', 4, fpc,  ec0,  0.0, -0.037, 0.1, ft, 1738.33)    # unconfined concrete
      ops.uniaxialMaterial('Concrete02', 5, fpcc, ec0c, -9.42, -0.047, 0.1, ft, 1827.12)  # confined concrete

      # define reinforcing ratios   
      rouXw = 0.0027         # X web 
      rouXb = 0.0082         # X boundary 
      rouYw = 0.0027         # Y web
      rouYb = 0.0323         # Y boundary

      # ----------------------------------------------------------------------------------------
      # Create orthotropic concrete layers to represent unconfined and confined concrete
      # ----------------------------------------------------------------------------------------

      ops.nDMaterial('OrthotropicRAConcrete', 6, 4, et, ec0,  0.0, '-damageCte1', 0.175, '-damageCte2', 0.5)   # unconfined concrete
      ops.nDMaterial('OrthotropicRAConcrete', 7, 5, et, ec0c, 0.0, '-damageCte1', 0.175, '-damageCte2', 0.5)   # confined concrete

      # ----------------------------------------------------------------------------------------
      # Create smeared steel layers to represent boundary and web reinforment
      # ----------------------------------------------------------------------------------------

      ops.nDMaterial('SmearedSteelDoubleLayer', 8, 1, 2, rouXw, rouYw, 0.0)       # steel web
      ops.nDMaterial('SmearedSteelDoubleLayer', 9, 1, 3, rouXb, rouYb, 0.0)       # steel boundary

      # ----------------------------------------------------------------------------------------  
      # Create ReinforcedConcreteLayerMembraneSection01 sections composed of concrete and steel layers
      # ----------------------------------------------------------------------------------------
      tw  = 152.4     # wall thickness
      tnc = 81.0      # unconfined concrete wall layer thickness
      tc  = 71.4      # confined concrete wall layer thickness   

      ops.section('ReinforcedConcreteLayerMembraneSection01', 10, 1, 1, '-reinfSteel', 8, '-conc', 6,    '-concThick', tw,        '-epscr', et, '-epsc', ec0)      # Section type b (wall web)
      ops.section('ReinforcedConcreteLayerMembraneSection01', 11, 1, 2, '-reinfSteel', 9, '-conc', 6, 7, '-concThick', tnc, tc,   '-epscr', et, '-epsc', ec0c)      # Section type a (wall boundary)   

   
**REFERENCES:**

#. Rojas, F., Anderson, J. C., Massone, L. M. (2016). A nonlinear quadrilateral layered membrane element with drilling degrees of freedom for the modeling of reinforced concrete walls. Engineering Structures, 124, 521-538. (`link <https://www.sciencedirect.com/science/article/pii/S0141029616302954>`_).
#. Tran, T. A. (2012). Experimental and Analytical Studies of Moderate Aspect Ratio Reinforced Concrete Structural Walls. Ph.D. Dissertation, Department of Civil and Environmental Engineering, University of California, Los Angeles. (`link <https://escholarship.org/uc/item/1538q2p8>`_).

**Code Developed by:** F. Rojas (University of Chile), M.J. Núñez (University of Chile).
