.. _block:

block Commands
**************

The block commands generate regular meshes of quadrilateral or brick elements from a block of corner (and optional midside) node coordinates.

block2D Command
^^^^^^^^^^^^^^^

Generates a mesh of quadrilateral elements in 2D or 3D. In 3D models, a 2D surface mesh suitable for shell analysis is created.

.. function:: block2D $numX $numY $startNode $startEle $eleType $eleArgs { $coords }

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $numX, |integer|, number of elements in the local x direction
   $numY, |integer|, number of elements in the local y direction
   $startNode, |integer|, starting node tag for mesh generation
   $startEle, |integer|, starting element tag for mesh generation
   $eleType, |string|, "quadrilateral element type (for example ``quad``, ``ShellMITC4``, ``bbarQuad``, ``enhancedQuad``)"
   $eleArgs, |list|, arguments required by the chosen element type
   $coords, |list|, "block corner coordinates in braces; nodes 1--4 are required, nodes 5--9 are optional for curved meshes"

Only the first four corner nodes are required. Optional nodes 5--9 refine curved block geometries.

block3D Command
^^^^^^^^^^^^^^^

Generates a mesh of eight-node brick solid elements.

.. function:: block3D $numX $numY $numZ $startNode $startEle $eleType $eleArgs { $coords }

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $numX, |integer|, number of elements in the local x direction
   $numY, |integer|, number of elements in the local y direction
   $numZ, |integer|, number of elements in the local z direction
   $startNode, |integer|, starting node tag for mesh generation
   $startEle, |integer|, starting element tag for mesh generation
   $eleType, |string|, "brick element type (for example ``stdBrick``, ``bbarBrick``, ``Brick20N``)"
   $eleArgs, |list|, arguments required by the chosen element type
   $coords, |list|, "block corner coordinates in braces; nodes 1--8 are required, nodes 9--27 are optional for curved meshes"

.. note::

   1. Variable substitutions are recognized when command arguments are placed in quotes.

   2. In Tcl, corner coordinates are wrapped in braces. In OpenSeesPy, pass ``*eleArgs`` and ``*crds`` as separate positional arguments (no braces).

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      block2D 16 4 1 1 quad "1 PlaneStrain2D 1" {
         1 0 0
         2 40 0
         3 40 10
         4 0 10
      }

   2. **Python Code**

   .. code-block:: python

      block2D(16, 4, 1, 1, 'quad', '1', 'PlaneStrain2D', '1',
              1, 0, 0, 2, 40, 0, 3, 40, 10, 4, 0, 10)

Code Developed by: |fmk|
