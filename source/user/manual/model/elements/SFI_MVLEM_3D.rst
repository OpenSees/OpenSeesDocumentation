.. _SFI_MVLEM_3D::

SFI-MVLEM-3D Element
^^^^^^^^^^^^^^^^

| Developed and implemented by: 
| `Kristijan Kolozvari <mailto:kkolozvari@fullerton.edu>`_ (CSU Fullerton)
| Kamiar Kalbasi (CSU Fullerton)
| Kutay Orakcal (Bogazici University)
| John Wallace (UCLA)

Description
################

The SFI-MVLEM-3D model (Figure 1a) is a three-dimensional four-node element with 24 DOFs that incorporates axial-flexural-shear interaction and can be used for nonlinear analysis of non-rectangular reinforced concrete walls subjected to multidirectional loading. The SFI-MVLEM-3D model is an extension of the two-dimensional, two-node Shear-Flexure-Interaction Multiple-Vertical-Line-Element-Model (`SFI-MVLEM <https://opensees.berkeley.edu/wiki/index.php/SFI_MVLEM_-_Cyclic_Shear-Flexure_Interaction_Model_for_RC_Walls>`_). The baseline SFI-MVLEM, which is essentially a line element for rectangular walls subjected to in-plane loading, is extended in this study to a three-dimensional model formulation by applying geometric transformation of the element degrees of freedom that converted it into a four-node element formulation (Figure 1b), as well as by incorporating linear elastic out-of-plane behavior based on the Kirchhoff plate theory (Figure 1c). The in-plane and the out-of-plane element behaviors are uncoupled in the present model.

This element shall be used in Domain defined with **-ndm 3 -ndf 6**.

.. figure:: SFI_MVLEM_3D_formulation.jpg
	:align: center
	:figclass: align-center

	**Figure 1: SFI-MVLEM-3D Element Formulation**

Input Parameters
################

.. admonition:: Command

   element SFI_MVLEM_3D eleTag iNode jNode kNode lNode m  -thick {Thicknesses} -width {Widths} -mat {Material_tags} <-CoR c> <-ThickMod tMod> <-Poisson Nu>  <-Density Dens>

.. csv-table:: 
   :header: "Parameter", "Type", "Description"
   :widths: 10, 10, 40

   eleTag, integer, unique element object tag
   iNode jNode kNode lNode, 4 integer, tags of element nodes defined in counterclockwise direction|
   m, integer, number of element fibers
   {Thicknesses}, *m* float, array of *m* fiber thicknesses
   {Widths}, *m* float, array of *m* macro-fiber widths
   {Material_tags}, *m* float, array of *m* macro-fiber nDMaterial (`FSAM <https://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior>`_) tags
   c, float, location of center of rotation from the base (optional; default = 0.4 (recommended))
   tMod, float, thickness multiplier (optional; default = 0.63 equivalent to 0.25Ig for out-of-plane bending)
   Nu, float, Poisson ratio for out-of-plane bending (optional; default = 0.25)
   Dens, float, Density (optional; default = 0.0)

Recorders
#########

The following recorders are available with the SFI-MVLEM-3D element.

.. csv-table:: 
   :header: "Recorder", "Description"
   :widths: 20, 40

   globalForce, Element global forces
   Curvature, Element curvature
   ShearDef, Element deformation
   RCPanel $fibTag $Response, Returns RC panel (macro-fiber) $Response for a $fibTag-th panel (1 ≤ fibTag ≤ m). For available $Response-s refer to nDMaterial (`FSAM <https://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior>`_)

Example
#######

Specimen TUB (Beyer et al. 2008) is analyzed using the SFI-MVLEM-3D. Figure 2a shows the photo of the test specimen and the multidirectional displacement pattern applied at the top of the wall, while Figure 2b-c show the SFI-MVLEM-3D model of specimen TUB.

.. figure:: SFI_MVLEM_3D_TUB_model.jpg
	:align: center
	:figclass: align-center

	**Figure 2: SFI-MVLEM-3D Model of Specimen TUB**

Figure 3 compares experimentally measured and analytically predicted load deformation behavior of the specimen TUB in E-W, N-S, and diagonal loading directions. The model provides accurate predictions of the lateral load capacity and the stiffness under cyclic loading in loading directions parallel to the principal axes of the cross-section (E-W, N-S direction). Analysis results overestimate the lateral load capacity in diagonal loading directions due to plane-sections-remain-plane assumption implemented in the model formulation that cannot capture pronounced shear lag effect observed in the test specimen.

.. figure:: SFI_MVLEM_3D_TUB_results.jpg
	:align: center
	:figclass: align-center

	**Figure 3: Experimental vs. SFI-MVLEM-3D Load-Deformation Response of Specimen TUB**

References
##########

K. Kolozvari, K. Kalbasi, K. Orakcal & J. W. Wallace (under review), "Three-dimensional shear-flexure interaction model for analysis of non-planar reinforced concrete walls", Journal of Building Engineering.
K. Kolozvari, K. Kalbasi, K. Orakcal, L. M. Massone & J. W. Wallace (2019), "Shear–flexure-interaction models for planar and flanged reinforced concrete walls", Bulletin of Eathquake Engineering, 17, pages 6391–6417. (`link <https://link.springer.com/article/10.1007/s10518-019-00658-5>`_).