.. _SimpleContact2D:

SimpleContact2D Element
^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-dimensional contact element between a primary line segment (nodes i-j) and a secondary node using a Lagrange multiplier node. Use with ``-ndm 2``.

.. function:: element SimpleContact2D $eleTag $iNode $jNode $secondaryNode $lambdaNode $matTag $tolGap $tolForce

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, nodes defining the primary contact segment
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

      element SimpleContact2D 1 1 2 10 11 1 1.0e-6 1.0e-6

   2. **Python Code**

   .. code-block:: python

      element('SimpleContact2D', 1, 1, 2, 10, 11, 1, 1.0e-6, 1.0e-6)

Code developed by: Kathryn Petek, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
