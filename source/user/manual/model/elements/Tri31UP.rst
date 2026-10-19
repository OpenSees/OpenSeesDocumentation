.. _Tri31UP:

Tri31UP Element
^^^^^^^^^^^^^^^

This command constructs an experimental three-node, single-point triangle with
a stabilized u-p formulation for plane-strain analysis of fluid-saturated porous
media. Use with ``-ndm 2 -ndf 3`` and an ND material supporting ``PlaneStrain``.

.. function:: element Tri31UP $eleTag $N1 $N2 $N3 $matTag $thick $fBulk $fDen $k1 $k2 $e $alpha <$b1 $b2> <-lumped>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 18, 12, 70

   "$eleTag", "integer", "Unique element tag."
   "$N1 $N2 $N3", "integer", "Three distinct corner-node tags; each node has three DOFs."
   "$matTag", "integer", "Tag of an ND material supporting a three-component PlaneStrain copy."
   "$thick", "float", "Positive out-of-plane thickness."
   "$fBulk", "float", "Positive pore-fluid bulk modulus."
   "$fDen", "float", "Nonnegative pore-fluid mass density."
   "$k1 $k2", "float", "Nonnegative permeability mobilities in the global x and y directions."
   "$e", "float", "Nonnegative void ratio; porosity is e/(1+e)."
   "$alpha", "float", "Nonnegative pressure-rate gradient stabilization coefficient; units are length squared divided by stress."
   "$b1 $b2", "float", "Optional body accelerations in global x and y; default zero. Supply both together."
   "-lumped", "string", "Optional flag to lump displacement mass only; pressure storage and stabilization remain consistent."

Node and pressure conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DOFs 1 and 2 are solid displacements. The velocity of DOF 3 is pore pressure,
its acceleration is the pore-pressure rate, and its displacement is the time
integral of pore pressure. For example, ``nodeVel $nodeTag 3`` returns pressure.
Fix DOF 3 to impose a drained boundary with initially zero pressure.

Clockwise and counterclockwise connectivity are accepted; degenerate triangles
are rejected. This element supports plane strain only. Its argument order is
different from the displacement-only ``Tri31`` command.

Formulation and use
~~~~~~~~~~~~~~~~~~~

The solid uses constant strain and one material point. Consistent displacement
mass and fluid storage are integrated exactly. With :math:`A` the triangle area
and :math:`t` its thickness, the pressure stabilization matrix is

.. math::

   T_{ij} = \alpha tA\,\nabla N_i\cdot\nabla N_j.

It enters the pressure block of the generalized mass matrix as :math:`-(S+T)`.
The storage coefficient in :math:`S` is :math:`n/K_f`, with
:math:`n=e/(1+e)`. Positive ``alpha`` enables pressure-rate stabilization; zero
disables it. ``alpha`` is dimensional, rather than a Biot coefficient.

The quadrilateral-paper estimate
:math:`\alpha=h^2/[4(K_s+4G_s/3)]` can guide initial experiments, but is not
calibrated here for triangles. Here :math:`K_s` and :math:`G_s` are solid-phase
bulk and shear moduli. Specify a length scale and assess mesh, time-step, and
alpha sensitivity. The stabilization adds artificial compressibility to
pressure rate and does not alter steady permeability.

Use a transient integrator, such as Newmark, and a general or
symmetric-indefinite solver. Static analysis alone omits the pressure equations,
which reside in the generalized mass and damping matrices. The generalized
mass matrix is indefinite. Rayleigh damping affects displacement blocks only.

The material supplies effective skeleton stresses and the mixture density used
for inertia and gravity. ``fDen`` enters fluid gravity. Body inputs are
accelerations. Permeabilities are the mobilities in
:math:`\boldsymbol{q}=\boldsymbol{k}(-\nabla p+\rho_f\boldsymbol{b})`;
convert hydraulic conductivity using fluid unit weight when needed.

.. warning::

   This is a research formulation. A constant-strain triangle has no solid
   hourglass modes. The quadrilateral's solid hourglass and enhanced-strain
   terms are not added. Pressure stabilization does not remove bending or
   drained-skeleton volumetric locking, nor guarantee pressure monotonicity.

Output and parameters
~~~~~~~~~~~~~~~~~~~~~

Valid :ref:`elementRecorder` queries include:

* ``force`` or ``forces``: nine-component resisting force without inertia.
* ``dynamicForce``: resisting force including velocity and acceleration terms.
* ``stress`` or ``stress2D3``: three effective-stress components.
* ``strain`` or ``strain2D3``: three strain components.
* ``mass``, ``damping``, ``stiffness``, and ``initialStiffness``: nine-by-nine matrices.
* ``material 1 ...``: a response supported by the sole material point.

Stress and strain ordering is ``xx yy xy``; the shear strain is engineering
shear strain. Record pressure with a Node recorder using ``-dof 3 vel``.
Element parameters ``xPerm``, ``yPerm``, and ``alpha`` support runtime updates.
Other parameter requests are forwarded to the material.

SelfWeight loads are supported. Apply edge tractions and fluid fluxes as
consistent nodal loads. The upper/lower/left/right pressure arguments of
``SSPquadUP`` are not supported by this triangular element.

.. admonition:: Example

   These examples create the element and pressure recorder. Add boundary
   conditions, loads, and transient analysis commands for a complete analysis.
   Numerical values must use a consistent unit system.

   1. **Tcl Code**

   .. code-block:: tcl

      wipe
      model BasicBuilder -ndm 2 -ndf 3
      node 1 0.0 0.0
      node 2 1.0 0.0
      node 3 0.0 1.0
      nDMaterial ElasticIsotropic 1 12000.0 0.25 2.0
      element Tri31UP 1 1 2 3 1 0.7 24000.0 1.0 1.0e-6 1.0e-6 0.6 2.0e-5 0.0 -9.81
      recorder Node -file Tri31UP_pressure.out -time -node 1 2 3 -dof 3 vel

   2. **Python Code**

   .. code-block:: python

      import openseespy.opensees as ops

      ops.wipe()
      ops.model('basic', '-ndm', 2, '-ndf', 3)
      ops.node(1, 0.0, 0.0)
      ops.node(2, 1.0, 0.0)
      ops.node(3, 0.0, 1.0)
      ops.nDMaterial('ElasticIsotropic', 1, 12000.0, 0.25, 2.0)
      ops.element('Tri31UP', 1, 1, 2, 3, 1,
                  0.7, 24000.0, 1.0, 1.0e-6, 1.0e-6, 0.6, 2.0e-5,
                  0.0, -9.81)
      ops.recorder('Node', '-file', 'Tri31UP_pressure.out', '-time',
                   '-node', 1, 2, 3, '-dof', 3, 'vel')

Reference: C. R. McGann, P. Arduino, and P. Mackenzie-Helnwein,
*Stabilized single-point 4-node quadrilateral element for dynamic analysis of
fluid saturated porous media* (2011 preprint). The pressure stabilization is
adapted from the quadrilateral formulation; that paper does not validate this
triangular implementation.

Code developed by: Pedro Arduino, University of Washington.
