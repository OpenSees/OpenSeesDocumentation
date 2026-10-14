.. _FatigueMember:

FatigueMember Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a FatigueMember uniaxial material wrapper. Like the :ref:`Fatigue` wrapper, it uses a modified rainflow cycle-counting algorithm, Miner's rule and Coffin-Manson log-log relationships to accumulate low-cycle fatigue damage in the wrapped material. Instead of the strain of the wrapped material, damage is computed from the normalized axial deformation between two nodes, so the estimated fatigue life of a brace depends little on the number of subelements and integration points. The wrapper does not change the stress-strain (or force-deformation) response of the wrapped material until fatigue life is exhausted; then the wrapper returns zero stress and zero tangent.

.. function:: uniaxialMaterial FatigueMember $matTag $otherTag $node1 $node2 <-k $k> <-Dmax $Dmax> <-dbar0 $dbar0> <-m $m> <-min $min> <-max $max>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $node1,    |integer|,  tag of the first node (typically one end node of the brace)
   $node2,    |integer|,  tag of the second node (typically the other end node of the brace)
   $k,        |float|,    "(optional) effective length factor, between 0.5 and 1.0; default 1.0"
   $Dmax,     |float|,    "(optional) damage index at failure, between 0 and 1; default 1.0"
   $dbar0,    |float|,    (optional) normalized axial deformation at which one cycle causes failure; default 0.0307
   $m,        |float|,    (optional) slope of Coffin-Manson curve in log-log space; default -0.481
   $min,      |float|,    (optional) global minimum normalized deformation for failure; default -1e16
   $max,      |float|,    (optional) global maximum normalized deformation for failure; default 1e16

Description
"""""""""""

The wrapper monitors the normalized axial deformation between ``$node1`` and ``$node2``,

.. math::

   \bar{\delta} = \frac{L - L_0}{k L_0}

where :math:`L` and :math:`L_0` are the current and initial chord length between the two nodes (computed from the nodal coordinates and translational displacements, in 2D or 3D) and :math:`k` is the effective length factor. The rainflow counting, damage accumulation and failure criteria are the same as for the :ref:`Fatigue` wrapper, with the strain replaced by :math:`\bar{\delta}` and :math:`\varepsilon_0` replaced by :math:`\bar{\delta}_0`:

.. math::

   D = \sum_i \frac{n_i}{N_{f,i}} = \sum_i n_i \left( \frac{\bar{\delta}_i}{\bar{\delta}_0} \right)^{-1/m}

When the damage index reaches ``$Dmax``, the stress of the wrapped material is set to zero (numerically 1e-8 times its stress) and the tangent to 1e-8 times its initial tangent. Failure can also be triggered by :math:`\bar{\delta}` exceeding the optional ``$min`` or ``$max`` limits.

The wrapper is intended for the fibers of brace sections modeled with force-based beam-column elements and the corotational transformation, with ``$node1`` and ``$node2`` the end nodes of the brace. Because :math:`\bar{\delta}` is computed from nodal displacements rather than fiber strains, two force-based subelements are sufficient to obtain consistent estimates of fatigue life. All copies of the wrapper (one per fiber) see the same :math:`\bar{\delta}` history; as in the :ref:`Fatigue` wrapper, failure before a peak is triggered only when the stress of the wrapped material is positive, so fibers can fail in different steps.

The nodes are looked up in the domain when they are first needed, so they may be defined before or after the material. If a node does not exist when the analysis runs, an error is printed and the program stops. In parallel analyses both nodes must be on the same process.

Calibrated parameters from Seki and Simpson (2025):

.. csv-table::
   :header: "Section", "m", "dbar0"
   :widths: 30, 10, 10

   HSS,                          -0.481, 0.0307
   Wide-flange (strong-axis buckling), -0.378, 0.0490
   Wide-flange (weak-axis buckling),   -0.480, 0.0473

The paper also gives regression equations for :math:`\bar{\delta}_0` based on a database of brace tests. For square or rectangular HSS braces (:math:`26.82 \le kl/r \le 84.81`, :math:`9.77 \le b/t \le 31.88`, :math:`362.32 \le E/\sigma_y \le 646.83`):

.. math::

   \bar{\delta}_0 = 1.56 \times 10^{2} \left(\frac{kl}{r}\right)^{-0.496} \left(\frac{b}{t}\right)^{-1.394} \left(\frac{E}{\sigma_y}\right)^{-0.323}

and for weak-axis buckling wide-flange braces (:math:`22.63 \le kl/r \le 154.36`, :math:`4.17 \le b_f/2t_f \le 10.25`, :math:`6.33 \le h/t_w \le 52.07`, :math:`483.09 \le E/\sigma_y \le 705.44`):

.. math::

   \bar{\delta}_0 = 1.46 \times 10^{-14} \left(\frac{kl}{r}\right)^{-0.260} \left(\frac{b_f}{2t_f}\right)^{-4.592} \left(\frac{h}{t_w}\right)^{2.335} \left(\frac{E}{\sigma_y}\right)^{5.094}

Valid recorder responses for the wrapped material are ``stress``, ``tangent``, ``strain``, ``stressStrain``, ``damage``, ``cyclesAndRange``, ``failure`` and ``dbar`` (the normalized node-level deformation :math:`\bar{\delta}`). The stress, strain, and tangent options must be supported by the wrapped material.

Damage recorder
"""""""""""""""

Damage is recorded in the same way as for the :ref:`Fatigue` wrapper. For fiber section elements, the argument after ``material`` (or ``fiber``) is the **fiber index**; for truss elements, use ``material`` **without** a tag after it.

1. **Tcl Code**

.. code-block:: tcl

   # Fiber section: damage and normalized deformation of the 1st fiber (index 0) of section 1
   recorder Element -file Damage.out -time -ele 2 section 1 fiber 0 damage
   recorder Element -file Dbar.out   -time -ele 2 section 1 fiber 0 dbar

   # Truss: use "material" with no tag
   recorder Element -file Damage4.out -time -ele 1 material damage

2. **Python Code**

.. code-block:: python

   # Fiber section: damage and normalized deformation of the 1st fiber (index 0) of section 1
   ops.recorder('Element', '-file', 'Damage.out', '-time', '-ele', 2, 'section', 1, 'fiber', 0, 'damage')
   ops.recorder('Element', '-file', 'Dbar.out', '-time', '-ele', 2, 'section', 1, 'fiber', 0, 'dbar')

   # Truss: use "material" with no tag
   ops.recorder('Element', '-file', 'Damage4.out', '-time', '-ele', 1, 'material', 'damage')

.. seealso::

   :ref:`Fatigue` for the fiber-level (strain-based) fatigue wrapper.

.. admonition:: Example

   A pin-ended HSS brace between nodes 1 and 3, divided into two force-based subelements (midspan node 2), with Steel02 fibers wrapped by FatigueMember using the calibrated HSS parameters:

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Steel02 1 345.0 200000.0 0.003 20.0 0.925 0.15
      uniaxialMaterial FatigueMember 2 1 1 3 -k 1.0 -dbar0 0.0307 -m -0.481

      # fiber section using the wrapped material
      section Fiber 1 {
         patch rect 2 4 1  66.5 -76.0  76.0  76.0
         patch rect 2 4 1 -66.5 -76.0  66.5 -66.5
         patch rect 2 4 1 -66.5  66.5  66.5  76.0
         patch rect 2 4 1 -76.0 -76.0 -66.5  76.0
      }

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Steel02', 1, 345.0, 200000.0, 0.003, 20.0, 0.925, 0.15)
      ops.uniaxialMaterial('FatigueMember', 2, 1, 1, 3, '-k', 1.0, '-dbar0', 0.0307, '-m', -0.481)

      # fiber section using the wrapped material
      ops.section('Fiber', 1)
      ops.patch('rect', 2, 4, 1,  66.5, -76.0,  76.0,  76.0)
      ops.patch('rect', 2, 4, 1, -66.5, -76.0,  66.5, -66.5)
      ops.patch('rect', 2, 4, 1, -66.5,  66.5,  66.5,  76.0)
      ops.patch('rect', 2, 4, 1, -76.0, -76.0, -66.5,  76.0)

References
""""""""""

- Seki, A., and Simpson, B. (2025). "Consistent Estimate of Brace Fatigue Life Using Axial Deformations Evaluated from Nodal Displacements." Journal of Structural Engineering, 151(8), 04025108. https://doi.org/10.1061/JSENDH.STENG-13866
- Uriz, P., and Mahin, S. A. (2008). "Toward Earthquake-Resistant Design of Concentrically Braced Steel-Frame Structures." Pacific Earthquake Engineering Research Center, UC Berkeley.

Code developed by: Akiri Seki, Stanford University
