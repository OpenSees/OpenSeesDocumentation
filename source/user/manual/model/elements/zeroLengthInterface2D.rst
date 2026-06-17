.. _zeroLengthInterface2D:

zeroLengthInterface2D Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a node-to-segment (NTS) interface element for 2D analysis. It can handle any number of DOFs (e.g. beam-solid, solid-solid, beam-beam contact), unlike zeroLengthContactNTS2D which is for 2 DOF nodes. The relation follows the Mohr-Coulomb law: :math:`T = N \times \tan(\phi)`.

.. function:: element zeroLengthInterface2D $eleTag -sNdNum $sNdNum -mNdNum $mNdNum -dof $sdof $mdof -Nodes $nodeTags $kn $kt $phi

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $sNdNum,   |integer|,  number of secondary nodes
   $mNdNum,   |integer|,  number of primary nodes
   $sdof $mdof, |integer|, secondary and primary degree of freedom
   $nodeTags, |integerList|, secondary and primary node tags (counterclockwise order)
   $kn,       |float|,    penalty in normal direction
   $kt,       |float|,    penalty in tangential direction
   $phi,      |float|,    friction angle in degrees

.. note::

   #. Secondary and primary nodes must have 2 DOF and be entered in counterclockwise order.
   #. The tangent from the contact element is non-symmetric; use a non-symmetric system solver if convergence is difficult.
   #. The contact normal is computed automatically. The element supports large deformations and different DOF types (beam-beam, beam-solid, solid-solid).

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthInterface2D>`_

.. admonition:: Example

   From the OpenSees wiki: element with tag **1**, 6 secondary and 6 primary nodes, dof 2 and 3, node tags as listed, Kn = Kt = 1e8, friction angle 16°.

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLengthInterface2D 1 -sNdNum 6 -mNdNum 6 -dof 2 3 -Nodes 5 10 12 3 9 11 1 4 2 8 7 6 1e8 1e8 16

   2. **Python Code**

   .. code-block:: python

      ops.element('zeroLengthInterface2D', 1, '-sNdNum', 6, '-mNdNum', 6, '-dof', 2, 3, '-Nodes', 5, 10, 12, 3, 9, 11, 1, 4, 2, 8, 7, 6, 1e8, 1e8, 16)

**References:** Wriggers, P., *Computational Contact Mechanics*, John Wiley & Sons, 2002.

Code developed by: `Roozbeh G. Mikola <http://www.roozbehgm.com/>`_, UC Berkeley and `N. Sitar <http://www.ce.berkeley.edu/~sitar/>`_, UC Berkeley
