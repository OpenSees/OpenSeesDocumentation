.. _MVLEM:

MVLEM Element
^^^^^^^^^^^^^

| Developed and implemented by:
| `Kristijan Kolozvari <mailto:kkolozvari@fullerton.edu>`_ (CSU Fullerton)
| Kutay Orakcal (Bogazici University)
| John Wallace (UCLA)

The MVLEM (Multiple-Vertical-Line-Element-Model) element is a two-node macro-element for flexure-dominated reinforced concrete walls in 2D. The element has six global degrees of freedom (three at the center of each rigid top and bottom beam). Flexural response is modeled by vertical macro-fibers; shear response is modeled by an uncoupled horizontal shear spring at height ``c`` from the bottom node. Use with ``-ndm 2 -ndf 3``.

For the 3D extension, see the ``MVLEM_3D`` element.

.. function:: element MVLEM $eleTag $Dens $iNode $jNode $m $c -thick {Thicknesses} -width {Widths} -rho {Reinforcing_ratios} -matConcrete {Concrete_tags} -matSteel {Steel_tags} -matShear {Shear_tag}

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $Dens, |float|, wall density
   $iNode $jNode, |integer|, end node tags
   $m, |integer|, number of macro-fibers
   $c, |float|, location of center of rotation from $iNode (recommended 0.4)
   {Thicknesses}, |listFloat|, fiber thicknesses (length $m$)
   {Widths}, |listFloat|, macro-fiber widths (length $m$)
   {Reinforcing_ratios}, |listFloat|, reinforcing ratio for each macro-fiber
   {Concrete_tags}, |listInt|, uniaxial material tags for concrete in each fiber
   {Steel_tags}, |listInt|, uniaxial material tags for steel in each fiber
   {Shear_tag}, |integer|, uniaxial material tag for the shear spring

Recorders
#########

.. csv-table::
   :header: "Recorder", "Description"
   :widths: 20, 40

   globalForce, element global forces
   Curvature, element curvature
   Shear_Force_Deformation, shear force-deformation relationship
   Fiber_Strain, vertical strains in each macro-fiber
   Fiber_Stress_Concrete, vertical concrete stresses in each macro-fiber
   Fiber_Stress_Steel, vertical steel stresses in each macro-fiber

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element MVLEM 1 0.0 1 2 8 0.4 -thick 4 4 4 4 4 4 4 4 -width 7.5 1.5 7.5 7.5 7.5 7.5 1.5 7.5 -rho 0.0293 0.0 0.0033 0.0033 0.0033 0.0033 0.0 0.0293 -matConcrete 3 4 4 4 4 4 4 3 -matSteel 1 2 2 2 2 2 2 1 -matShear 5

   2. **Python Code**

   .. code-block:: python

      element('MVLEM', 1, 0.0, 1, 2, 8, 0.4, '-thick', 4, 4, 4, 4, 4, 4, 4, 4, '-width', 7.5, 1.5, 7.5, 7.5, 7.5, 7.5, 1.5, 7.5, '-rho', 0.0293, 0.0, 0.0033, 0.0033, 0.0033, 0.0033, 0.0, 0.0293, '-matConcrete', 3, 4, 4, 4, 4, 4, 4, 3, '-matSteel', 1, 2, 2, 2, 2, 2, 2, 1, '-matShear', 5)

Code developed by: Kristijan Kolozvari, Kutay Orakcal, John Wallace
