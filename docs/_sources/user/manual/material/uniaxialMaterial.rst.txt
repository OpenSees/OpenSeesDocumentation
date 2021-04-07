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
   uniaxialMaterials/Hysteretic
   uniaxialMaterials/ReinforcingSteel
   uniaxialMaterials/DoddRestrepo
   uniaxialMaterials/RambergOsgoodSteel
   uniaxialMaterials/SteelMPF
   uniaxialMaterials/UVCuniaxial


#. Concrete Materials
uniaxialMaterials/Concrete01
uniaxialMaterials/Concrete02
uniaxialMaterials/Concrete04
uniaxialMaterials/Concrete06
uniaxialMaterials/Concrete07
uniaxialMaterials/Concrete01
uniaxialMaterials/ConfinedConcrete01
uniaxialMaterials/ConcreteD
uniaxialMaterials/FRPConfinedConcrete
uniaxialMaterials/ConcreteCM

#. Some Standard Uniaxial Materials
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
uniaxialMaterials/CastFuse
uniaxialMaterials/ViscousDamper
uniaxialMaterials/BilinearOilDamper
uniaxialMaterials/Modified Ibarra-Medina-Krawinkler Deterioration Model with Bilinear Hysteretic Response (Bilin Material)
uniaxialMaterials/Modified Ibarra-Medina-Krawinkler Deterioration Model with Peak-Oriented Hysteretic Response (ModIMKPeakOriented Material)
uniaxialMaterials/Modified Ibarra-Medina-Krawinkler Deterioration Model with Pinched Hysteretic Response (ModIMKPinching Material)
uniaxialMaterials/SAWS
uniaxialMaterials/BARSLIP
uniaxialMaterials/Bond_SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
uniaxialMaterials/Fatigue
uniaxialMaterials/Hardening
uniaxialMaterials/Impact
uniaxialMaterials/Hyperbolic Gap
uniaxialMaterials/LimitState
uniaxialMaterials/PathIndependent
uniaxialMaterials/Pinching4
uniaxialMaterials/Engineered Cementitious Composites
uniaxialMaterials/SelfCentering
uniaxialMaterials/Viscous
uniaxialMaterials/BoucWen
uniaxialMaterials/BWBN (Pinching Hysteretic Bouc-Wen)

.. toctree::
   :maxdepth: 1
   
   uniaxialMaterials/HystereticPoly

#. PyTzQz uniaxial materials for p-y, t-z and q-z elements 

.. toctree::
   :maxdepth: 1

   uniaxialMaterials/PySimple1
   uniaxialMaterials/TzSimple1
   uniaxialMaterials/QzSimple1
   uniaxialMaterials/PyLiq1
   uniaxialMaterials/TzLiq1
   uniaxialMaterials/PySimple1Gen
   uniaxialMaterials/TzSimple1Gen


   uniaxialMaterials/KikuchiAikenHDR
   uniaxialMaterials/KikuchiAikenLRB
   uniaxialMaterials/AxialSp
   uniaxialMaterials/AxialSpHD
   uniaxialMaterials/PinchingLimitState
   uniaxialMaterials/CFSWSWP
   uniaxialMaterials/CFSSSWP


