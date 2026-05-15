.. _zeroLengthContactNTS2D:

zeroLengthContactNTS2D Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a node-to-segment (NTS) frictional contact element for 2D analysis. The relation follows the Mohr-Coulomb frictional law: :math:`T = N \times \tan(\phi)`, where :math:`T` is tangential force, :math:`N` is normal force, and :math:`\phi` is friction angle.

.. function:: element zeroLengthContactNTS2D $eleTag -sNdNum $sNdNum -mNdNum $mNdNum -Nodes $nodeTags $kn $kt $phi

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $sNdNum,   |integer|,  number of slave nodes
   $mNdNum,   |integer|,  number of master nodes
   $nodeTags, |integerList|, slave and master node tags (counterclockwise order)
   $kn,       |float|,    penalty in normal direction
   $kt,       |float|,    penalty in tangential direction
   $phi,      |float|,    friction angle in degrees

.. note::

   #. Slave and master nodes must have 2 DOF and be entered in counterclockwise order.
   #. The tangent from the contact element is non-symmetric; use a non-symmetric system solver if convergence is difficult.
   #. The contact normal is computed automatically (no predefined normal vector required).
   #. The element supports large deformations.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContactNTS2D>`_

.. admonition:: Example

   From the OpenSees wiki: element with tag **1**, 6 slave and 6 master nodes, node tags as listed, kn = kt = 1e8, friction angle 16°.

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLengthContactNTS2D 1 -sNdNum 6 -mNdNum 6 -Nodes 5 10 12 3 9 11 1 4 2 8 7 6 1e8 1e8 16

   2. **Python Code**

   .. code-block:: python

      ops.element('zeroLengthContactNTS2D', 1, '-sNdNum', 6, '-mNdNum', 6, '-Nodes', 5, 10, 12, 3, 9, 11, 1, 4, 2, 8, 7, 6, 1e8, 1e8, 16)

**References:** Wriggers, P., *Computational Contact Mechanics*, John Wiley & Sons, 2002.

Code developed by: `Roozbeh G. Mikola <http://www.roozbehgm.com/>`_, UC Berkeley and `N. Sitar <http://www.ce.berkeley.edu/~sitar/>`_, UC Berkeley
