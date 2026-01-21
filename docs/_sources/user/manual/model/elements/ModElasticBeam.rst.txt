.. _ModElasticBeam:

Modified Elastic Beam Column Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a ModElasticBeam2d element object.
This element should be used for modeling of a structural element with an equivalent combination of one elastic element with stiffness-proportional damping, and two springs at its two ends with no stiffness proportional damping to represent a prismatic section.
The modeling technique is based on a number of analytical studies discussed in Zareian and Medina (2010) and Zareian and Krawinkler (2009) and is utilized in order to solve problems related to numerical damping in dynamic analysis of frame structures with concentrated plasticity springs.

The arguments depend on the dimension of the problem, ``ndm``:

For ``ndm=2`` (two-dimensional problem):

.. function:: element ModElasticBeam2d $eleTag $iNode $jNode $A $E $Iz, $K11, $K33, $K44, $transfTag <-mass $massDens> <-cMass>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$eleTag",               "|integer|", "Unique element object tag"
   "$iNode $jNode",         "|integer|", "End node tags"
   "$A",                    "|float|",   "Cross-sectional area of element"
   "$E",                    "|float|",   "Young's Modulus"
   "$G",                    "|float|",   "Shear Modulus"
   "$J",                    "|float|",   "Torsional moment of inertia of cross section"
   "$Iy",                   "|float|",   "Second moment of area about the local y-axis"
   "$Iz",                   "|float|",   "Second moment of area about the local z-axis"
   "$K11, K33, K44",        "|float|",   "Stiffness modifiers---see notes below"
   "$secTag",               "|integer|", "Identifier for previously-defined section object"
   "$transfTag",            "|integer|", "Identifier for previously-defined coordinate-transformation object"
   "<-mass $massDens>",     "|float|",   "Element mass per unit length (optional: default = 0.0)"
   "-cMass",                "|string|",  "To form consistent mass matrix (optional)"

For ``ndm=3`` (three-dimensional problem):

.. function:: element ModElasticBeam2d $eleTag $iNode $jNode $A $E $Iz, $K11y, $K33y, $K44y, $K11z, $K33z, $K44z, $transfTag <-mass $massDens> <-cMass>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$eleTag",               "|integer|", "Unique element object tag"
   "$iNode $jNode",         "|integer|", "End node tags"
   "$A",                    "|float|",   "Cross-sectional area of element"
   "$E",                    "|float|",   "Young's Modulus"
   "$G",                    "|float|",   "Shear Modulus"
   "$J",                    "|float|",   "Torsional moment of inertia of cross section"
   "$Iy",                   "|float|",   "Second moment of area about the local y-axis"
   "$Iz",                   "|float|",   "Second moment of area about the local z-axis"
   "$K11y, K33y, K44y",     "|float|",   "Stiffness modifiers for bending about the local y-axis---see notes below"
   "$K11z, K33z, K44z",     "|float|",   "Stiffness modifiers for bending about the local z-axis---see notes below"
   "$secTag",               "|integer|", "Identifier for previously-defined section object"
   "$transfTag",            "|integer|", "Identifier for previously-defined coordinate-transformation object"
   "<-mass $massDens>",     "|float|",   "Element mass per unit length (optional: default = 0.0)"
   "-cMass",                "|string|",  "To form consistent mass matrix (optional)"


**Element Formation:**

For structural elements with time invariant moment gradient, a prismatic beam element is to be replaced with a prismatic beam element composed of semi-rigid rotational springs at the ends and an elastic beam element in the middle.
The rotational stiffness at the ends of the original beam element is :math:`K_e=6EI/L` (where :math:`E` is the modulus of elasticity, :math:`I` the moment of inertia, and :math:`L` the length of the beam), and the ratio of the rotational spring stiffness, :math:`K_s`, to the elastic beam stiffness, :math:`K_e`, of the modified beam element is defined as :math:`n=K_s/K_e`.
   
**Elastic Element with 2-end Springs:**

* The elastic element in between the two springs should have an elastic moment of inertia equal to :math:`I_{mod}=(n+1)/n \cdot I`.
* The "n" times stiff rotational springs should have an elastic stiffness of :math:`Ks=6n \cdot EI_{mod}/L`.
* The elastic element should have an elastic stiffness coefficient :math:`K_{44}=6 \cdot (1+n)/(2+3n)`.
* The elastic element should have an elastic stiffness coefficient :math:`K_{11}=K_{33}=(1+2n)/(1+n) \cdot K_{44}`.
* The modified stiffness coefficient bmod for stiffness proportional damping of the elastic element is :math:`b_{mod}=1+(1/2n) \cdot b`.

**Elastic Element with 1-end Spring:**

* The elastic element in between the two springs should have an elastic moment of inertia equal to :math:`I_mod=(n+1)/n \cdot I`.
* The "n" times stiff rotational springs should have an elastic stiffness of :math:`K_s=6n \cdot EI_{mod}/L`.
* The elastic element should have an elastic stiffness coefficient :math:`K_{44}=6n/(1+3n)`.
* The elastic element should have an elastic stiffness coefficient :math:`K_{11}=(1+2 \cdot n)/(1+n) \cdot K_{44}`.
* The elastic element should have an elastic stiffness coefficient :math:`K_{33} = 2K_{44}`.
* The modified stiffness coefficient bmod for stiffness proportional damping of the elastic element is :math:`b_{mod}=1+(1/2n) \cdot b`.
   
**References:**

.. [1] Zareian, F. and Medina, R. A. (2010). “A practical method for proper modeling of structural damping in inelastic plane structural systems,” Computers & Structures, Vol. 88, 1-2, pp. 45-53.
.. [2] Zareian, F. and Krawinkler, H. (2009). "Simplified performance-based earthquake engineering" Technical Report 169, The John A. Blume Earthquake Engineering Research Center, Department of Civil Engineering, Stanford University, Stanford, CA.
.. [3] `OpenSees Wiki page for ModElasticBeam2d <https://opensees.berkeley.edu/wiki/index.php/Elastic_Beam_Column_Element_with_Stiffness_Modifiers>`_
