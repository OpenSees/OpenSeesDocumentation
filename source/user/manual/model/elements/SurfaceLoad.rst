.. _SurfaceLoad:

SurfaceLoad Element
^^^^^^^^^^^^^^^^^^^

This command constructs a four-node surface load element that applies uniform pressure normal to a quadrilateral face. The element distributes energetically conjugate nodal forces to nodes shared with adjacent 3D brick or shell elements. Use with ``-ndm 3 -ndf 3`` or ``-ndf 6``.

.. function:: element SurfaceLoad $eleTag $iNode $jNode $kNode $lNode $pressure

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes in counter-clockwise order defining the loaded face
   $pressure, |float|, pressure normal to the surface; outward positive and inward negative

.. note::

   1. This element has no stiffness; it only applies equivalent nodal loads to connected structural elements.

   2. Apply the load in a load pattern so pressure can vary between analysis steps.

   3. A triangular variant ``TriSurfaceLoad`` is also available.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element SurfaceLoad 1 1 2 3 4 -10.0

   2. **Python Code**

   .. code-block:: python

      element('SurfaceLoad', 1, 1, 2, 3, 4, -10.0)

Code developed by: Chris McGann, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
