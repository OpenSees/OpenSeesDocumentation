.. _region:

region Command
**************

This command labels a group of nodes and/or elements as a mesh region. Regions are used to assign Rayleigh damping factors to selected parts of the model. A region is defined by elements or by nodes, not both.

If elements are specified, the region includes those elements and their connected nodes unless ``-eleOnly`` is used. If nodes are specified, the region includes those nodes and all elements whose nodes are all in the region, unless ``-nodeOnly`` is used.

.. function:: region $regTag <$selectionOptions> <-rayleigh $alphaM $betaK $betaKinit $betaKcomm>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $regTag, |integer|, unique region tag
   -ele, |string|, flag followed by a list of element tags
   -eleOnly, |string|, same as ``-ele`` but connected nodes are not included
   -eleRange, |string|, flag followed by $startEle and $endEle
   -eleOnlyRange, |string|, element range with ``-eleOnly`` behavior
   -node, |string|, flag followed by a list of node tags
   -nodeOnly, |string|, same as ``-node`` but connected elements are not included
   -nodeRange, |string|, flag followed by $startNode and $endNode
   -nodeOnlyRange, |string|, node range with ``-nodeOnly`` behavior
   -rayleigh, |string|, "flag followed by Rayleigh damping factors: $alphaM $betaK $betaKinit $betaKcomm"

.. note::

   The user cannot define a region using both element and node selection flags in the same command.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      region 1 -ele 1 5 -eleRange 10 15
      region 2 -node 2 4 6 -nodeRange 9 12 -rayleigh 0.0 0.01 0.0 0.0

   2. **Python Code**

   .. code-block:: python

      ops.region(1, '-ele', 1, 5, '-eleRange', 10, 15)
      ops.region(2, '-node', 2, 4, 6, '-nodeRange', 9, 12, '-rayleigh', 0.0, 0.01, 0.0, 0.0)

Code Developed by: |fmk|
