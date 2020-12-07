.. _nDMaterial:

nDMaterial Command
************************

This command is used to construct an NDMaterial object which represents the stress-strain relationship at the gauss-point of a continuum element. 

.. function:: nDMaterial $matType $matTag $matArgs

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matType, |string|,      material type
   $matTag,  |integer|,     unique material tag.
   $matArgs, |list|,        a list of material arguments with number dependent on material type

.. note::

   The valid queries to any uniaxial material when creating an ElementRecorder are 'strain', and 'stress'. Some materials have additional queries to which they will respond. These are documented in the NOTES section for those materials.


The following contain information about matType? and the args required for each of the available material types:

.. toctree::
   :maxdepth: 1

   ndMaterials/ElasticIsotropic
   ndMaterials/ElasticOrthotropic
   ndMaterials/J2Plasticity
   ndMaterials/DruckerPrager
   ndMaterials/ManzariDafalias
   ndMaterials/BoundingCamClay
   ndMaterials/PM4Sand
   ndMaterials/PM4Silt
   ndMaterials/PressureIndependentMultiYield
   ndMaterials/PressureDependentMultiYield
   ndMaterials/J2CyclicBoundingSurface


Concrete Damage Model
Plane Stress Material
Plane Strain Material
Multi Axial Cyclic Plasticity
Plate Fiber Material
Plane Stress Concrete Materials
FSAM - 2D RC Panel Constitutive Behavior
Tsinghua Sand Models
CycLiqCP Material (Cyclic ElasticPlasticity)
CycLiqCPSP Material
Manzari Dafalias Material
Stress Density Material
Materials for Modeling Concrete Walls
PlaneStressUserMaterial
PlateFromPlaneStress
PlateRebar
LayeredShell
Contact Materials for 2D and 3D
ContactMaterial2D
ContactMaterial3D
Wrapper material for Initial State Analysis
InitialStateAnalysisWrapper
UC San Diego soil models (Linear/Nonlinear, dry/drained/undrained soil response under general 2D/3D static/cyclic loading conditions (please visit UCSD for examples)
PressureIndependMultiYield Material
PressureDependMultiYield Material
PressureDependMultiYield02 Material
PressureDependMultiYield03 Material
UC San Diego Saturated Undrained soil
FluidSolidPorousMaterial
Misc.
AcousticMedium
Steel & Reinforcing-Steel Materials
UVCmultiaxial (Updated Voce-Chaboche)
UVCplanestress (Updated Voce-Chaboche)


