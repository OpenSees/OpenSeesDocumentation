.. _matTestCommands:

Material Testing Commands
*************************

The OpenSees material testing commands require that the test material/section first be specified with testUniaxialMaterial, testNDMaterial, or testSection.

. 

.. function:: testUniaxialMaterial $matTag

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,  |integer|,     unique uniaxial material tag.
   
.. function:: testNDMaterial $matTag

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,  |integer|,     unique n-dimensional material tag.
   
.. function:: testSection $secTag

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag,  |integer|,     unique section tag.
   
Once the test material is specified with either testUniaxialMaterial, testNDMaterial, or testSection, the strain or deformation values can be set with the setStrain command. 
This command sets and commits the strains/deformations to the material/section.
   
.. function:: setStrain [ndf $strains]

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $strains,  |listFloat|,     **ndf** input strains
   
Alternatively, the trial strain or deformation values can be set with the setTrialStrain command and then committed with the commitStrain command.

.. function:: setTrialStrain [ndf $strains]

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $strains,  |listFloat|,     **ndf** input strains (trial)
   
.. function:: commitStrain

Once the material/section strains/deformations are set, basic information about the state of the material/section can be queried with the commands getStrain, getStress, getTangent and getDampTangent.

.. function:: getStrain()

.. function:: getStress()

.. function:: getTangent()

.. function:: getDampTangent()

Additionally, material/section specific information can be queried with the getResponse command.

.. function:: getResponse $arg1 $arg2 ....

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $args,  |list|, list of the arguments for the material/section response