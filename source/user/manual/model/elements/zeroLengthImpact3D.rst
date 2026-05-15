.. _zeroLengthImpact3D:

zeroLengthImpact3D Element
^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a node-to-node zero-length contact element in 3D to simulate impact/pounding and friction. It extends zeroLengthContact3D with ImpactMaterial-style behavior (Hertz impact model). The element is fast-converging and can be used for surface-to-surface contact by connecting nodes on the constrained surface to nodes on the retained surface.

.. function:: element zeroLengthImpact3D $eleTag $cNode $rNode $direction $initGap $frictionRatio $Kt $Kn $Kn2 $Delta_y $cohesion

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag,   |integer|,  unique element object tag
   $cNode $rNode, |integer|, constrained and retained node tags
   $direction, |integer|,  "out-normal of master plane: 1 = +X, 2 = +Y, 3 = +Z"
   $initGap,  |float|,    initial gap between master and slave
   $frictionRatio, |float|, friction ratio in tangential directions
   $Kt,       |float|,    penalty in tangential directions
   $Kn,       |float|,    penalty in normal direction
   $Kn2,      |float|,    penalty in normal direction after yielding (Hertz)
   $Delta_y,  |float|,    yield deformation (Hertz impact model)
   $cohesion, |float|,    cohesion (zero if none)

.. note::

   #. End nodes should be in a 3 DOF domain. See OpenSees documentation and forums for using 3 DOF and 6 DOF together (example scripts are on the wiki).
   #. This element is built on zeroLengthContact3D; all notes for that element apply (retained/constrained nodes, DOF, etc.).
   #. The tangent is non-symmetric; use a non-symmetric solver if needed.

.. seealso::

   `Notes (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthImpact3D>`_, `ZeroLengthContact <https://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element>`_, `ImpactMaterial <https://opensees.berkeley.edu/wiki/index.php/Impact_Material>`_

.. admonition:: Example

   The following constructs a zeroLengthImpact3D element with tag **1** between constrained node **2** and retained node **4**, normal in +Z, zero gap, friction 0.3, penalties 1e6 (Kt, Kn), Kn2 = 2e6, Delta_y = 0.001, zero cohesion.

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLengthImpact3D 1 2 4 3 0.0 0.3 1e6 1e6 2e6 0.001 0.0

   2. **Python Code**

   .. code-block:: python

      ops.element('zeroLengthImpact3D', 1, 2, 4, 3, 0.0, 0.3, 1e6, 1e6, 2e6, 0.001, 0.0)

Code developed by: **Dr. Arash E. Zaghi** and **Majid Cashany**, University of Connecticut (UConn)
