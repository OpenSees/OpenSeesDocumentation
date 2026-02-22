.. _zeroLengthContact:

zeroLengthContact Element
^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a node-to-node frictional contact element (2D or 3D). The element connects a constrained node and a retained node. The relation follows the Mohr-Coulomb law: :math:`T = \mu N + c`, where :math:`T` is tangential force, :math:`N` is normal force, :math:`\mu` is friction coefficient, and :math:`c` is cohesion.

**2D:**

.. function:: element zeroLengthContact2D $eleTag $cNode $rNode $Kn $Kt $mu -normal $Nx $Ny

**3D:**

.. function:: element zeroLengthContact3D $eleTag $cNode $rNode $Kn $Kt $mu $c $dir

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $cNode $rNode, |integer|, constrained and retained node tags
   $Kn,       |float|,    penalty in normal direction
   $Kt,       |float|,    penalty in tangential direction
   $mu,       |float|,    friction coefficient
   $Nx $Ny,   |float|,    (2D) normal vector components
   $c,        |float|,    (3D) cohesion (not available in 2D)
   $dir,      |integer|,  "(3D) out-normal of retained plane: 1 = +X, 2 = +Y, 3 = +Z"

.. note::

   #. The tangent from the contact element is non-symmetric; use a non-symmetric system solver.
   #. For 2D contact, nodes must have 2 DOF; for 3D contact, nodes must have 3 DOF.
   #. The out-normal of the master (retained) plane is assumed unchanged during analysis.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element>`_

.. admonition:: Example

   **2D:** Contact element with tag **1** between constrained node **2** and retained node **4**, normal direction (0, -1).

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLengthContact2D 1 2 4 1e8 1e8 0.3 -normal 0 -1

   2. **Python Code**

   .. code-block:: python

      ops.element('zeroLengthContact2D', 1, 2, 4, 1e8, 1e8, 0.3, '-normal', 0, -1)

   **3D:** Contact element with tag **1**, cohesion **0**, normal in +Z.

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLengthContact3D 1 2 4 1e8 1e8 0.3 0.0 3

   2. **Python Code**

   .. code-block:: python

      ops.element('zeroLengthContact3D', 1, 2, 4, 1e8, 1e8, 0.3, 0.0, 3)

Code developed by: **Gang Wang**, Geomatrix
