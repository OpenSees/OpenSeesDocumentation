.. _MEFI::

MEFI Element
^^^^^^^^^^^^^^^^^^^^

The Membrane Fiber (MEFI) element, is described by four nodes, each containing three degrees of freedom (DOFs), two translations, and one in-plane rotation (drilling) DOF, 
which incorporates a blended interpolation function for the displacements over the element. The element formulation accommodates the quadrature points and weights of the 
classical finite element formulation of membrane elements to resemble strips (fibers), similarly to macroscopic elements.
  
.. figure:: figures/MEFI/MEFI_Element.jpg
	:align: center
	:figclass: align-center
	:width: 1000px
	:name: MEFI_FIG
	
	MEFI Element: (a) Element idealization; (b) Interpolation function at bottom and top edges; (c) Interpolation function at left and right edges.
	
	
This command is used to construct a MEFI element object.

.. admonition:: Command

   element MEFI $eleTag $iNode $jNode $kNode $lNode $numFib -width $widths -sec $secTags

.. csv-table:: 
   :header: "Parameter", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, integer, unique element object tag
   $iNode $jNode $kNode $lNode, 4 integer, tags of element nodes defined in counterclockwise direction
   $numFib, integer, number of element macro-fibers
   $widths, list float, a list of *m* macro-fiber widths
   $secTags,  list int, a list of *m* macro-fiber section tags
   
   
   
The following recorders are available with the MEFI element.

.. csv-table:: 
   :header: "Recorder", "Description"
   :widths: 20, 40

   forces, element global forces
   stresses, element stresses
   strains, element strains
   RCPanel $fibTag $Response, returns material $Response for a $fibTag-th panel (1 ≤ fibTag ≤ m). For available $Response(s) refer to material
   
.. admonition:: Notes

   | 1. This element shall be used in domain defined with **-ndm 2 -ndf 3**
   | 2. For additional information please visit `MEFI GitHub Page <https://github.com/carloslopezolea/MEFI>`_
   
.. admonition:: Examples

   The following example constructs a MEFI element with tag **1** between nodes **1, 2, 3, 4**, with **8** macro-fibers. Each macro-fiber has width **1** and material tag **1**.  

   1. **Tcl Code**

   .. code-block:: tcl
	  
	  element MEFI 1 1 2 3 4 8 -width 1 1 1 1 1 1 1 1 -sec 1 1 1 1 1 1 1 1;

   2. **Python Code**

   .. code-block:: python

	  element('MEFI', 1, 1, 2, 3, 4, 8, '-width', 1, 1, 1, 1, 1, 1, 1, 1, '-sec', 1, 1, 1, 1, 1, 1, 1, 1)	  
   

   
**REFERENCES:**

#. López, C. N., Rojas, F., & Massone, L. M. (2022). Membrane fiber element for reinforced concrete walls – the benefits of macro and micro modeling approaches. Engineering Structures, 254, 113819. (`link <https://www.sciencedirect.com/science/article/abs/pii/S0141029621018897>`_).


**Code Developed by:** `C. N. López <mailto:carloslopezolea@ug.uchile.cl>`_