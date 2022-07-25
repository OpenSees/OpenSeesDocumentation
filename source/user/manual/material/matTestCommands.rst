.. _matTestCommands:

Material Testing Commands
*************************

The material testing environment is separate from the OpenSees domain, and allows for simple tests to be performed on OpenSees materials, including uniaxial materials, n-dimensional materials, and section force-deformation relationships.
In order to use the material testing commands, the test material/section must first be specified with testUniaxialMaterial, testNDMaterial, or testSection.

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
   
Alternatively, the trial strain or deformation values can be set with the setTrialStrain command and then later committed with the commitStrain command. 

.. function:: setTrialStrain [ndf $strains]

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $strains,  |listFloat|,     **ndf** input strains (trial)
   
.. function:: commitStrain

Once the material/section strains/deformations are set, information about the state of the material/section can be queried with the commands getStrain, getStress, getTangent and getDampTangent, and getResponse.

The command getStrain simply returns the list of strain/deformation values inputted with setStrain or setTrialStrain.

.. function:: getStrain()

The command getStress returns a list of stress/force values corresponding to the inputted strain/deformations.

.. function:: getStress()

The command getTangent returns the tangent values corresponding to each stress/strain or force/deformation relationship. 
For uniaxial materials and uniaxial sections, getTangent simply returns a single value. 
For n-dimensional materials and non-uniaxial sections, getTangent returns the flattened (row-major) tangent matrix.

.. function:: getTangent()

The command getDampTangent returns the damping tangent (for uniaxial materials only).

.. function:: getDampTangent()

The command getResponse returns material or section specific information.

.. function:: getResponse $arg1 $arg2 ....

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $args,  |list|, list of the arguments for the material/section response
   
