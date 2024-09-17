.. _uniaxialMaterial:

uniaxialMaterial Command
************************

This command is used to construct a uniaxial material, which provides a uniaxial stress-strain (or force-deformation) relationships.
. 

.. function:: uniaxialMaterial $matType $matTag $matArgs

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matType, |string|,      material type
   $matTag,  |integer|,     unique material tag.
   $matArgs, |list|,        a list of material arguments with number dependent on material type


The following subsections contain information about **$matType** 

#. Steel & Reinforcing-Steel Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Steel01
      uniaxialMaterials/Steel02
      uniaxialMaterials/Steel4
      uniaxialMaterials/ReinforcingSteel
      uniaxialMaterials/DoddRestrepo
      uniaxialMaterials/RambergOsgoodSteel
      uniaxialMaterials/SteelMPF
      uniaxialMaterials/UVCuniaxial
      uniaxialMaterials/SteelFractureDI
      uniaxialMaterials/DuctileFracture


#. Concrete Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Concrete01
      uniaxialMaterials/Concrete02
      uniaxialMaterials/Concrete04
      uniaxialMaterials/ASDConcrete1D
      uniaxialMaterials/GMG_CyclicReinforcedConcrete
	  
..    uniaxialMaterials/Concrete06
      uniaxialMaterials/Concrete07
      uniaxialMaterials/ConfinedConcrete01
      uniaxialMaterials/ConcreteD
      uniaxialMaterials/FRPConfinedConcrete
      uniaxialMaterials/ConcreteCM

#. Some Standard Uniaxial Materials

.. toctree::
      :maxdepth: 1
		 
..    uniaxialMaterials/Elastic
      uniaxialMaterials/ElasticPP
      uniaxialMaterials/ElasticPP_Gap
      uniaxialMaterials/ElasticNoTension
      uniaxialMaterials/ElasticBilin
      uniaxialMaterials/ElasticMultiLinear
      uniaxialMaterials/Hardening
      uniaxialMaterials/MultiLinear
      
#. Generic Multilinear Hysteretic Materials

   .. toctree::
      :maxdepth: 1
      
      uniaxialMaterials/Hysteretic
      uniaxialMaterials/HystereticSM
      uniaxialMaterials/IMKBilin
      uniaxialMaterials/IMKPeakOriented
      uniaxialMaterials/IMKPinching
      uniaxialMaterials/SLModel
	  
..    uniaxialMaterials/Pinching4

      
#. Wrapper Uniaxial Materials

.. toctree::
      :maxdepth: 1
      
..    uniaxialMaterials/Fatigue
      uniaxialMaterials/Parallel
      uniaxialMaterials/Series
      uniaxialMaterials/InitialStrain
      uniaxialMaterials/InitialStress
      uniaxialMaterials/MinMax
      uniaxialMaterials/PathIndependent

#. Other Uniaxial Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/BoucWenInfill
      uniaxialMaterials/HystereticPoly
      uniaxialMaterials/HystereticAsym
      uniaxialMaterials/HystereticSmooth
      uniaxialMaterials/DowelType
      uniaxialMaterials/CoulombDamper
      uniaxialMaterials/HertzDamp
      uniaxialMaterials/JankowskiImpact
      uniaxialMaterials/ViscoelasticGap
      uniaxialMaterials/Ratchet

..    uniaxialMaterials/CastFuse
      uniaxialMaterials/ViscousDamper
      uniaxialMaterials/BilinearOilDamper
      uniaxialMaterials/SAWS
      uniaxialMaterials/BARSLIP
      uniaxialMaterials/Bond_SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
      uniaxialMaterials/Impact
      uniaxialMaterials/Hyperbolic Gap
      uniaxialMaterials/LimitState
      uniaxialMaterials/Engineered Cementitious Composites
      uniaxialMaterials/SelfCentering
      uniaxialMaterials/Viscous
      uniaxialMaterials/BoucWen
      uniaxialMaterials/BWBN (Pinching Hysteretic Bouc-Wen)



#. PyTzQz uniaxial materials for p-y, t-z and q-z elements 

.. toctree::
   :maxdepth: 1

   uniaxialMaterials/PySimple1
   uniaxialMaterials/TzSimple1
   uniaxialMaterials/QzSimple1
   uniaxialMaterials/PyLiq1
   uniaxialMaterials/TzLiq1
   uniaxialMaterials/QzLiq1

.. uniaxialMaterials/KikuchiAikenHDR
   uniaxialMaterials/KikuchiAikenLRB
   uniaxialMaterials/AxialSp
   uniaxialMaterials/AxialSpHD
   uniaxialMaterials/PinchingLimitState
   uniaxialMaterials/CFSWSWP
   uniaxialMaterials/CFSSSWP
   uniaxialMaterials/PySimple1Gen
   uniaxialMaterials/TzSimple1Gen

