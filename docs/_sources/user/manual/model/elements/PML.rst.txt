.. _PML::

PML Element
^^^^^^^^^^^^^^^^

This command is used to construct four-node and and eight-node PML elements. Perfectly Matched Layer (PML) elements are a numerical technique used in simulations to manage boundary conditions and minimize reflections at the edges of a computational domain. PMLs are often implemented as layers or regions at the edges of a computational domain, where the properties of the material in the PML are carefully designed to gradually absorb and attenuate outgoing waves. This absorption process is designed to be as efficient as possible, reducing the reflection of waves back into the domain. The choice of PML parameters, such as the profile of the absorbing material and its thickness, depends on the specific simulation and the desired level of accuracy.

Implementation details for these elements can be found in:

W. Zhang, E. Esmaeilzadeh Seylabi, E. Taciroglu,(2019), An ABAQUS toolbox for soil-structure interaction analysis, Computers and Geotechnics, Volume 114, 2019, https://doi.org/10.1016/j.compgeo.2019.103143.

.. A. Trono, (2023) Interaccion dinamica suelo-estructura considerando ondas sismicas inclinadas y superficiales, PhD Dissertation, 2023, Universidad Nacional de Cordoba, Cordoba, Argentina..


.. admonition:: Command



    1. PML2D

        element PML $eleTag $node1 $node2 $node3 $node4 $E $nu $rho $EleType $Thickness $m $R $RD_half_width_x $Depth $alpha $beta

    2. PML3D
        element PML $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $gamma $beta $eta $E $nu $rho $EleType $Thickness $m $R $RD_half_width_x $RD_half_width_y $Depth $alpha $beta

1. **PML2D**

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 90

   eleTag,|integer|,unique integer tag identifying element object
   node1 $node2 node3 node4, 4 |integer|, the four nodes defining the element input in counterclockwise order (-ndm 2 -ndf 5)
   E,  |float| , Young's modulus
   nu, |float| , Poisson's Ratio
   rho, |float| , Density
   EleType, |float|, Element type based on the region of the PML it can be 1 2 3 4 5 (you can choose any number the code automaticlly )
   Thickness, |float|, Thickness of the PML around regular domain
    m, |float|, PML parameter (m=2 is recommended)
    R, |float|, PML parameter (R=1e-8 is recommended)
    RD_half_width_x, |float|, Distance of the border of the PML and regular domain to the center of the domain at origin
    Depth, |float|, Depth of the PML from the surface of the regular domain in the negative y direction
    alpha, |float|, Rayleigh damping parameter for PML (alpha will be 0 even if you input a value)
    beta, |float|, Rayleigh damping parameter for PML (beta will be 0 even if you input a value)




2. **PML3D**

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 90

   eleTag,|integer|,unique integer tag identifying element object
   node1 node2 node3 node4 node5 node6 node7 $node8, 8 |integer|, the eight nodes defining the element input in counterclockwise order (-ndm 2 -ndf 5)
   :math:`{\gamma}`, |float|, Newmark integration parameter
    :math:`{\beta}`, |float|, Newmark integration parameter
    :math:`{\eta}`, |float|, Newmark integration parameter
   E,  |float| , Young's modulus
   nu, |float| , Poisson's Ratio
   rho, |float| , Density
   EleType, |float|, Element type based on the region of the PML it can be 1 2 3 4 5 (you can choose any number the code automaticlly )
   Thickness, |float|, Thickness of the PML around regular domain
    m, |float|, PML parameter (m=2 is recommended)
    R, |float|, PML parameter (R=1e-8 is recommended)
    RD_half_width_x, |float|, Distance of the border of the PML and regular domain to the center of the domain at origin
    Depth, |float|, Depth of the PML from the surface of the regular domain in the negative y direction
    alpha, |float|, Rayleigh damping parameter for PML (alpha will be 0 even if you input a value)
    beta, |float|, Rayleigh damping parameter for PML (beta will be 0 even if you input a value)

.. note::

    1. For 2D PML each node has 5 DOFs (2 translations and Sx, Sy, Sxy)
    2. For 3D PML each node has 9 DOFs (3 translations and Sx, Sy, Sz, Sxy, Sxz, Syz)
    3. There is no recorder for PML elements. The stresses can be obtained from the node recorders. 
    4. When using PML 3D only newmark integration method can be used and the parameters using for the integration should be passed to the element(Example: :math:`{\gamma} = 1/2, {\beta} = 1/4, {\eta} =1/12`)
    5. The center of the regular domian should be at the origin of the global coordinate system (0,0,0)
    6. It is highly recommended to use the same mesh for the PML and the regular domain
    7. It is highly recommended to use the same material for the PML and the regular domain
    8. It is highly recommended to use uniform and square mesh for the PML elements.


.. admonition:: Example 

   The following example constructs a PML3D element with tag **1** between nodes **1, 2, 3, 4, 5, 6, 7, 8** with the properties **E=1e6, nu=0.3, rho=1.0, EleType=1, Thickness=1.0, m=2, R=1e-8, RD_half_width_x=10.0, RD_half_width_y=10.0, Depth=5.0, alpha=0.0, beta=0.0**.
   
   1. **Tcl Code**

   .. code-block:: tcl

      element PML 1 1 2 3 4 5 6 7 8 1 0.5 0.25 0.0833333333333333 1e6 0.3 1.0 1 1.0 2 1e-8 10.0 10.0 5.0 0.0 0.0

   2. **Python Code**

   .. code-block:: python

      element('PML', 1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 0.5, 0.25, 0.0833333333333333, 1e6, 0.3, 1.0, 1, 1.0, 2, 1e-8, 10.0, 10.0, 5.0, 0.0, 0.0)

Code Developed by: W. Zhang, E. Taciroglu, A. Pakzad, P. Arduino (UCLA, UW)