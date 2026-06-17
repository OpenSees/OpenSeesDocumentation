.. _SimpleContact3D:

SimpleContact3D Element
^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a three-dimensional contact element between a primary quadrilateral surface (four nodes) and a secondary node using a Lagrange multiplier node. Use with ``-ndm 3``.

.. function:: element SimpleContact3D $eleTag $iNode $jNode $kNode $lNode $secondaryNode $lambdaNode $matTag $tolGap $tolForce

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode $kNode $lNode, |integer|, four nodes defining the primary contact surface
   $secondaryNode, |integer|, secondary (slave) node
   $lambdaNode, |integer|, Lagrange multiplier node
   $matTag, |integer|, tag of a contact ND material
   $tolGap, |float|, gap tolerance for contact detection
   $tolForce, |float|, force tolerance for contact equilibrium

.. note::

   Valid :ref:`elementRecorder` queries include ``forces`` and ``force``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element SimpleContact3D 1 1 2 3 4 10 11 1 1.0e-6 1.0e-6

   2. **Python Code**

   .. code-block:: python

      element('SimpleContact3D', 1, 1, 2, 3, 4, 10, 11, 1, 1.0e-6, 1.0e-6)

Code developed by: Kathryn Petek, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
