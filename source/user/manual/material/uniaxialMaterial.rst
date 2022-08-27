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

      uniaxialMaterials/Steel/Steel01
      uniaxialMaterials/Steel/Steel02
      uniaxialMaterials/Steel/Steel4
      uniaxialMaterials/Steel/Hysteretic
      uniaxialMaterials/Steel/ReinforcingSteel
      uniaxialMaterials/Steel/DoddRestrepo
      uniaxialMaterials/Steel/RambergOsgoodSteel
      uniaxialMaterials/Steel/SteelMPF
      uniaxialMaterials/Steel/UVCuniaxial
      uniaxialMaterials/Steel/SteelFractureDI
      uniaxialMaterials/Steel/DuctileFracture


#. Concrete Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Concrete/Concrete01
      uniaxialMaterials/Concrete/Concrete02
      uniaxialMaterials/Concrete/Concrete04
      uniaxialMaterials/Concrete/Concrete06
      uniaxialMaterials/Concrete/Concrete07
      uniaxialMaterials/Concrete/ConfinedConcrete01
      uniaxialMaterials/Concrete/ConcreteD
      uniaxialMaterials/Concrete/FRPConfinedConcrete
      uniaxialMaterials/Concrete/ConcreteCM

#. Some Standard Uniaxial Materials

   .. toctree::
      :maxdepth: 1
		 
      uniaxialMaterials/Elastic
      uniaxialMaterials/ElasticPP
      uniaxialMaterials/ElasticPP_Gap
      uniaxialMaterials/ElasticNoTension
      uniaxialMaterials/ElasticBilin
      uniaxialMaterials/ElasticMultiLinear
      uniaxialMaterials/MultiLinear
      uniaxialMaterials/Parallel
      uniaxialMaterials/Series
      uniaxialMaterials/InitialStrain
      uniaxialMaterials/InitialStress
      uniaxialMaterials/MinMax

#. Other Uniaxial Materials

   .. toctree::
      :maxdepth: 1

      uniaxialMaterials/Other/CastFuse
      uniaxialMaterials/Other/ViscousDamper
      uniaxialMaterials/Other/BilinearOilDamper
      uniaxialMaterials/Other/IMKBilin
      uniaxialMaterials/Other/IMKPeakOriented
      uniaxialMaterials/Other/IMKPinching
      uniaxialMaterials/Other/SAWS
      uniaxialMaterials/Other/BARSLIP
      uniaxialMaterials/Other/Bond_SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
      uniaxialMaterials/Other/Fatigue
      uniaxialMaterials/Other/Hardening
      uniaxialMaterials/Other/Impact
      uniaxialMaterials/Other/Hyperbolic Gap
      uniaxialMaterials/Other/LimitState
      uniaxialMaterials/Other/PathIndependent
      uniaxialMaterials/Other/Pinching4
      uniaxialMaterials/Other/Engineered Cementitious Composites
      uniaxialMaterials/Other/SelfCentering
      uniaxialMaterials/Other/Viscous
      uniaxialMaterials/Other/BoucWen
      uniaxialMaterials/Other/BWBN (Pinching Hysteretic Bouc-Wen)
      uniaxialMaterials/Other/HystereticPoly
      uniaxialMaterials/Other/HystereticAsym (Smooth asymmetric hysteresis)
      uniaxialMaterials/Other/HystereticPoly
      uniaxialMaterials/Other/HystereticSmooth (Smooth hysteretic material)
      uniaxialMaterials/Other/DowelType
      uniaxialMaterials/Other/BoucWenInfill
      uniaxialMaterials/Other/ViscoelasticGap
      uniaxialMaterials/Other/HertzDamp
      uniaxialMaterials/Other/JankowskiImpact


#. PyTzQz uniaxial materials for p-y, t-z and q-z elements 

.. toctree::
   :maxdepth: 1

   uniaxialMaterials/PyTzQZ/PySimple1
   uniaxialMaterials/PyTzQZ/TzSimple1
   uniaxialMaterials/PyTzQZ/QzSimple1
   uniaxialMaterials/PyTzQZ/PyLiq1
   uniaxialMaterials/PyTzQZ/TzLiq1
   uniaxialMaterials/PyTzQZ/QzLiq1
   uniaxialMaterials/PyTzQZ/PySimple1Gen
   uniaxialMaterials/PyTzQZ/TzSimple1Gen


   uniaxialMaterials/KikuchiAikenHDR
   uniaxialMaterials/KikuchiAikenLRB
   uniaxialMaterials/AxialSp
   uniaxialMaterials/AxialSpHD
   uniaxialMaterials/PinchingLimitState
   uniaxialMaterials/CFSWSWP
   uniaxialMaterials/CFSSSWP


