.. _E_SFI_MVLEM_3D::

E-SFI-MVLEM-3D Element
^^^^^^^^^^^^^^^^^^^^

| Developed and implemented by: 
| `Kristijan Kolozvari <mailto:kkolozvari@fullerton.edu>`_ (CSU Fullerton)
| C. N. Lopez (University of Chile, Santiago)
| L. M. Massone (University of Chile, Santiago)

Description
###########

The E-SFI-MVLEM-3D model (Kolozvari et al, 2023) is a three-dimensional four-node element with 24 DOFs that incorporates axial-flexural-shear interaction and can be used for nonlinear analysis of non-rectangular reinforced concrete walls subjected to multidirectional loading. The E-SFI-MVLEM-3D model is derived by combining two previously available models, a two-dimensional `E-SFI <https://github.com/carloslopezolea/E-SFI_Documentation>`_ model, and a three-dimensional `SFI-MVLEM-3D <https://kkolozvari.github.io/SFI-MVLEM-3D/>`_ model. The major enhancement in the model formulation compared to its parent SFI-MVLEM-3D comes from implementing a closed-form solution for calculating horizontal axial strains at fibers of the wall element. This significantly reduced the number of element degrees of freedom, which resulted in analysis run-time that is reduced to approximately 25% and a convergence rate that is increased roughly two times.

For additional information please visit `E-SFI-MVLEM-3D GitHub Page <https://kkolozvari.github.io/E-SFI-MVLEM-3D/>`_.

This element shall be used in Domain defined with **-ndm 3 -ndf 6**.

Input Parameters
################

.. admonition:: Command

   element E_SFI_MVLEM_3D eleTag iNode jNode kNode lNode m  -thick {Thicknesses} -width {Widths} -mat {Material_tags} <-CoR c> <-ThickMod tMod> <-Poisson Nu>  <-Density Dens>

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

The following recorders are available with the E-SFI-MVLEM-3D element.

.. csv-table:: 
   :header: "Recorder", "Description"
   :widths: 20, 40

   globalForce, Element global forces
   Curvature, Element curvature
   ShearDef, Element deformation
   RCPanel $fibTag $Response, Returns RC panel (macro-fiber) $Response for a $fibTag-th panel (1 ≤ fibTag ≤ m). For available $Response-s refer to nDMaterial (`FSAM <https://opensees.berkeley.edu/wiki/index.php/FSAM_-_2D_RC_Panel_Constitutive_Behavior>`_)

OpenSeesPy Documentation
########################

User input for OpenSeesPy is essentially the same as for SFI_MVLEM_3D, with the exception of the element name. OpenSeesPy user documetation for the SFI_MVLEM_3D element can be accessed from `HERE <https://openseespydoc.readthedocs.io/en/latest/src/SFI_MVLEM_3D.html>`_.

References
##########

Kristijan Kolozvari, Carlos N. López, Leonardo M. Massone (2023), "Efficient Three-dimensional Shear-flexure Interaction Model for Reinforced Concrete Walls", Engineering Structures, Vol. 294, 116700. (`link <https://doi.org/10.1016/j.engstruct.2023.116700>`_).