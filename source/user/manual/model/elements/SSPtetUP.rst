.. _SSPtetUP:

SSPtetUP Element
^^^^^^^^^^^^^^^^

This command constructs an experimental four-node, single-point tetrahedral
element with a stabilized u-p formulation for fluid-saturated porous media.
Displacements and pore pressure use linear interpolation. Use with
``-ndm 3 -ndf 4`` and an ND material supporting ``ThreeDimensional`` behavior.

.. function:: element SSPtetUP $eleTag $N1 $N2 $N3 $N4 $matTag $fBulk $fDen $k1 $k2 $k3 $e $alpha <$b1 $b2 $b3> <-lumped>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 18, 12, 70

   "$eleTag", "integer", "Unique element tag."
   "$N1 ... $N4", "integer", "Four distinct corner-node tags; each node has four DOFs."
   "$matTag", "integer", "Tag of an ND material supporting a six-component ThreeDimensional copy."
   "$fBulk", "float", "Positive pore-fluid bulk modulus."
   "$fDen", "float", "Nonnegative pore-fluid mass density."
   "$k1 $k2 $k3", "float", "Nonnegative permeability mobilities in the global x; y; and z directions."
   "$e", "float", "Nonnegative void ratio; porosity is e/(1+e)."
   "$alpha", "float", "Nonnegative pressure-rate gradient stabilization coefficient; units are length squared divided by stress."
   "$b1 $b2 $b3", "float", "Optional body accelerations in global x; y; and z; default zero. Supply all three together."
   "-lumped", "string", "Optional flag to lump displacement mass only; pressure storage and stabilization remain consistent."

.. note::

   The registered element command is case-sensitive: use ``SSPtetUP``.

Node and pressure conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each node has three displacement DOFs and one generalized pressure DOF:

* DOFs 1-3 are the solid displacements.
* The velocity of DOF 4 is pore pressure.
* The acceleration of DOF 4 is the pore-pressure rate.
* The displacement of DOF 4 is the time integral of pore pressure.

For example, ``nodeVel $nodeTag 4`` returns pore pressure. To prescribe a drained
boundary with initially zero pressure, fix DOF 4. Either tetrahedral orientation
is accepted, but a zero-volume or numerically degenerate element is rejected.

Formulation and use
~~~~~~~~~~~~~~~~~~~

The element uses one constitutive integration point, constant solid strain,
and exact tetrahedral integrals for consistent mass and fluid storage.
The pressure stabilization matrix is

.. math::

   T_{ij} = \alpha V\,\nabla N_i\cdot\nabla N_j,

where :math:`V` is element volume. It adds artificial compressibility through
the pressure rate. The pressure block of the generalized mass matrix is
:math:`-(S+T)`, where :math:`S` is the storage matrix with coefficient
:math:`n/K_f` and :math:`n=e/(1+e)`. Positive ``alpha`` enables stabilization;
zero disables it. This coefficient is not the dimensionless Biot coefficient.

Choose ``alpha`` with consistent units and assess mesh, time-step, and parameter
sensitivity. The brick-paper estimate
:math:`\alpha=\alpha_0 h^2/(K_s+4G_s/3)` is a starting point for investigation,
not a calibrated tetrahedral prescription. Here :math:`K_s` and :math:`G_s`
denote the solid-phase bulk and shear moduli used in that estimate.

Use a transient integrator, such as Newmark, with a general or
symmetric-indefinite solver. Static analysis alone does not assemble the
pressure equations, which are in the generalized mass and damping matrices.
The coupled generalized mass matrix is indefinite.

The material supplies effective skeleton stresses and the mixture density used
for solid inertia and gravity. ``fDen`` enters the fluid gravity term. The
permeabilities are the mobilities in
:math:`\boldsymbol{q}=\boldsymbol{k}(-\nabla p+\rho_f\boldsymbol{b})`;
hydraulic conductivity must be converted using fluid unit weight when needed.
Rayleigh damping applies only to the displacement block.

.. warning::

   This is a research formulation. A linear tetrahedron has no solid hourglass
   modes, so no brick hourglass stiffness is added. Pressure stabilization does
   not remove bending or drained-skeleton volumetric locking, and does not
   guarantee monotone pressure fields. Validate mesh and parameter sensitivity
   for the intended application.

Output and parameters
~~~~~~~~~~~~~~~~~~~~~

Valid :ref:`elementRecorder` queries include:

* ``force`` or ``forces``: 16-component resisting force without inertia.
* ``stress`` or ``stress3D6``: six effective-stress components at the material point.
* ``strain`` or ``strain3D6``: six strain components at the material point.
* ``mass``, ``damping``, and ``stiffness``: the corresponding 16-by-16 matrices.
* ``material 1 ...``: a response supported by the sole material point.

Stress and strain ordering is ``xx yy zz xy yz xz``; shear strains are engineering
shear strains. Record pore pressure with a Node recorder using ``-dof 4 vel``.
Element parameters ``xPerm``, ``yPerm``, ``zPerm``, and ``alpha`` may be updated
during analysis. Other parameter requests are forwarded to the material.
Boundary tractions and fluid fluxes require consistent nodal loads; no
tetrahedral face-load parser is provided.

.. admonition:: Example

   These examples create the element and pressure recorder. Add boundary
   conditions, loads, and transient analysis commands for a complete analysis.
   Numerical values must use a consistent unit system.

   1. **Tcl Code**

   .. code-block:: tcl

      wipe
      model BasicBuilder -ndm 3 -ndf 4
      node 1 0.0 0.0 0.0
      node 2 1.0 0.0 0.0
      node 3 0.0 1.0 0.0
      node 4 0.0 0.0 1.0
      nDMaterial ElasticIsotropic 1 12000.0 0.25 2.0
      element SSPtetUP 1 1 2 3 4 1 24000.0 1.0 1.0e-6 1.0e-6 1.0e-6 0.6 2.0e-5 0.0 0.0 -9.81
      recorder Node -file SSPtetUP_pressure.out -time -node 1 2 3 4 -dof 4 vel

   2. **Python Code**

   .. code-block:: python

      import openseespy.opensees as ops

      ops.wipe()
      ops.model('basic', '-ndm', 3, '-ndf', 4)
      ops.node(1, 0.0, 0.0, 0.0)
      ops.node(2, 1.0, 0.0, 0.0)
      ops.node(3, 0.0, 1.0, 0.0)
      ops.node(4, 0.0, 0.0, 1.0)
      ops.nDMaterial('ElasticIsotropic', 1, 12000.0, 0.25, 2.0)
      ops.element('SSPtetUP', 1, 1, 2, 3, 4, 1,
                  24000.0, 1.0, 1.0e-6, 1.0e-6, 1.0e-6, 0.6, 2.0e-5,
                  0.0, 0.0, -9.81)
      ops.recorder('Node', '-file', 'SSPtetUP_pressure.out', '-time',
                   '-node', 1, 2, 3, 4, '-dof', 4, 'vel')

Reference: C. R. McGann, P. Arduino, and P. Mackenzie-Helnwein,
*A stabilized single-point finite element formulation for three-dimensional
dynamic analysis of saturated soils* (2013). The pressure stabilization is
adapted from the brick formulation; that paper does not validate this
tetrahedral implementation.

Code developed by: Pedro Arduino, University of Washington and Marlio Molina Manrique, Politecnico di Torino.
