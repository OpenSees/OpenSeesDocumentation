.. _materialCommands:

Material Commands
-----------------

Like many finite element applications, all nonlinear elements have associated with them a material. It is the material in conjunction with the material that provides the force-displacement response of the element. In OpenSees materials are divided into three general types:

#. **uniaxial materials** which define a uniaxial (1 dimensional) stress-strain relationship.

#. **nDimensional materials** which define multi-dimensional (plane stress, plane strain, or 3d) stress-strain relationships.

#. **sections** which define coupled moment-curvature and axial-deformation relationships for beam column elements.

.. figure:: figures/OpenSeesMaterials.png
	:align: center
	:width: 400px
	:figclass: align-center

	OpenSees Materials

.. toctree::
   :maxdepth: 1

   material/uniaxialMaterial
   material/ndMaterial
   material/section
