.. _materialCommands:

Material Commands
-----------------

Like many finite element applications, all nonlinear elements have associated with them a material. It is the material in conjunction with the material that provides the force-displacement response of the element. In OpenSees materials are divided into three general types:
1. **uniaxial materials** which define a uniaxial (1 dimensional) stress-strain relationsship.
2. **nDimensional materials** which define multi-dimensional (plane stress, plain strain, or 3d) stress-strain relationships.
3. **sections** which define copuled moment-curvature and axial-deforation relationship for beam column elements.

.. figure:: figures/OpenSeesMaterials.png
	:align: center
	:width: 600px
	:figclass: align-center

	OpenSees Materials

.. toctree::
   :maxdepth: 1

   model/uniaxialMaterial
   model/ndMaterial
   model/section
