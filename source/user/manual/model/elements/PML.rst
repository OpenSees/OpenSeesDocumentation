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
        element PML $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $matTag $PMLThickness meshType meshParams... [-Cp $Cp] [-m $m] [-R $R] [-alphabeta $alpha $beta] [-Newmark $gamma $beta $eta $keisi]

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

    "eleTag", "|integer|", "unique integer tag identifying element object"
    "node1 node2 node3 node4 node5 node6 node7 node8", "8 |integer|", "the eight nodes defining the element input in counterclockwise order (-ndm 3 -ndf 9)"
    "matTag", "|integer|", "material tag (must be an ElasticIsotropicMaterial)"
    "PMLThickness", "|float|", "Thickness of the PML around regular domain"
    "meshType", "|string|", "Mesh type defining the PML region (General, Box, Sphere, Cylinder)"
    "meshParams...", "|float|", "Additional parameters depending on meshType (see below)"
    "-Cp", "|float|", "PML parameter defining wave speed (default calculated from material properties)"
    "-m", "|float|", "PML parameter (default m=2)"
    "-R", "|float|", "PML parameter (default R=1e-8)"
    "-alphabeta", "|float float|", "User-defined alpha and beta parameters"
    "-Newmark", "|float float float float|", "Newmark integration parameters (gamma, beta, eta, keisi)"

**Mesh Type Parameters**

.. csv-table:: 
    :header: "Mesh Type", "Required Parameters", "Description"
    :widths: 20, 30, 50

    General, "Xref, Yref, Zref, N1, N2, N3", "Reference point and normal vector components"
    Box, "XC, YC, ZC, L, W, H", "Center coordinates at the surface and dimensions of the box (e.g., 20, 50, 0.0, widthX, widthY, depthZ)"


.. note::

    1. For PML 2D, each node has 5 DOFs (2 translations and Sx, Sy, Sxy)
    2. For PML 3D, each node has 9 DOFs (3 translations and Sx, Sy, Sz, Sxy, Sxz, Syz)
    3. For PML 2D, the center of the regular domian should be at the origin of the global coordinate system (0,0,0)
    4. There is no recorder for PML elements. The stresses can be obtained from the node recorders. 
    5. When using PML 3D, only the Newmark integration method can be used. If the parameters for the integration are not passed to the element, the default parameters will be used (Example: :math:`\gamma = 0.5, \beta = 0.25, \eta = 0.0833333333333333, \xi = 0.0208333333333333`).
    6. It is highly recommended to use the same mesh for the PML and the regular domain
    7. It is highly recommended to use the same material for the PML and the regular domain
    8. It is highly recommended to use uniform and square mesh for the PML elements
    9. If the user provides the alpha and beta parameters explicitly using the `-alphabeta` flag, the following formulas for calculating `alpha_0` and `beta_0` are skipped, and the user-defined parameters are used instead:
        
        .. math::
            \begin{aligned}
                C_p &= \sqrt{\frac{E \cdot (1 - \nu)}{\rho \cdot (1 + \nu) \cdot (1 - 2 \cdot \nu)}} \\
                PML_b &= \frac{\text{PMLThickness}}{1.0} \\
                \alpha_0 &= \frac{(m_{\text{coeff}} + 1) \cdot PML_b}{2.0 \cdot PML_b} \cdot \log_{10}\left(\frac{1}{R}\right) \\
                \beta_0 &= \frac{(m_{\text{coeff}} + 1) \cdot C_p}{2.0 \cdot PML_b} \cdot \log_{10}\left(\frac{1}{R}\right)
            \end{aligned}


.. admonition:: Example 

    The following example constructs a PML 3D element with tag **1** between nodes **1, 2, 3, 4, 5, 6, 7, 8** using material tag **1**, PML thickness **1.0**, and a box-type mesh with parameters **10.0, 10.0, 5.0 20 20 20**.

    1. **Tcl Code**

    .. code-block:: tcl

        element PML 1 1 2 3 4 5 6 7 8 1 1.0 Box 10.0 10.0 5.0 20.0 20.0 20.0 -m 2 -R 1e-8 -Newmark 0.5 0.25 0.0833333333333333 0.0208333333333333

    2. **Python Code**

    .. code-block:: python

        element('PML', 1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 1.0, 'Box', 10.0, 10.0, 5.0, 20.0, 20.0, 20.0, '-m', 2, '-R', 1e-8, '-Newmark', 0.5, 0.25, 0.0833333333333333, 0.0208333333333333)

.. admonition:: Example 

    The following example constructs a PML 2D element with tag **2** between nodes **1, 2, 3, 4** using Young's modulus **3000**, Poisson's ratio **0.3**, density **2500**, element type **1**, thickness **1.0**, and PML parameters **2, 1e-8, 5.0, 10.0, 0.0, 0.0**.

    1. **Tcl Code**

    .. code-block:: tcl

        element PML 2 1 2 3 4 3000 0.3 2500 1 1.0 2 1e-8 5.0 10.0 0.0 0.0

    2. **Python Code**

    .. code-block:: python

        element('PML', 2, 1, 2, 3, 4, 3000, 0.3, 2500, 1, 1.0, 2, 1e-8, 5.0, 10.0, 0.0, 0.0)
