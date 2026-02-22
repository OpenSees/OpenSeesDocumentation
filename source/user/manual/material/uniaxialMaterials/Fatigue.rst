.. _Fatigue:

Fatigue Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Fatigue uniaxial material wrapper. The wrapper uses a modified rainflow cycle-counting algorithm to accumulate damage in the wrapped material using Miner's rule, based on Coffin-Manson log-log relationships for low-cycle fatigue. It does not change the stress-strain (or force-deformation) response of the wrapped material until fatigue life is exhausted; then the wrapper returns zero stress and zero tangent.

.. function:: uniaxialMaterial Fatigue $matTag $otherTag <-E0 $e0> <-m $m> <-min $epsmin> <-max $epsmax>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial
   $e0,       |float|,    (optional) strain at which one cycle causes failure; default 0.191
   $m,        |float|,    (optional) slope of Coffin-Manson curve in log-log space; default -0.458
   $epsmin,   |float|,    (optional) global minimum strain/deformation for failure; default -1e16
   $epsmax,   |float|,    (optional) global maximum strain/deformation for failure; default 1e16

Description
"""""""""""

The model accounts for low-cycle fatigue. A modified rainflow cycle counter tracks strain amplitudes and is used with a linear strain-accumulation model (Miner's rule) and Coffin-Manson relationships. When the damage level reaches 1.0, the force (or stress) of the wrapped material is set to zero (numerically 1e-8). If failure is triggered in compression, the stress is dropped at the next zero-force crossing. The material treats each point as the last point of the history for damage tracking; if failure is not triggered, that pseudo-peak is discarded. Failure can also be triggered by exceeding the optional minimum or maximum strain limits (defaults are very large so that only fatigue controls). The default E0 and m are calibrated from low-cycle fatigue tests on European steel sections (Ballio and Castiglioni 1995); see Uriz (2005) for calibration details.

Valid recorder responses for the wrapped material are ``stress``, ``tangent``, ``strain``, ``stressStrain``, and ``damage``. The stress, strain, and tangent options must be supported by the wrapped material.

Damage recorder
"""""""""""""""

To record fatigue damage, use the element recorder with the ``damage`` response.

**Fiber section elements:** The argument after ``material`` (or ``fiber``) is the **fiber index**, not the material tag. Using ``material`` or ``fiber`` gives the same result. To target a fiber by coordinates, add one more argument after ``fiber`` (y and z, or the appropriate coordinate).

**Truss elements:** Use ``material`` **without** a tag after it. Adding a material tag after ``material`` will not work.

1. **Tcl Code**

.. code-block:: tcl

   # Fiber section: record damage of 1st fiber (index 0) — "material" and "fiber" equivalent
   recorder Element -xml Damage1.out -time -ele 1 2 section 1 material 0 damage
   recorder Element -xml Damage2.out -time -ele 1 2 section 1 fiber 0 damage

   # Fiber section: record damage of fiber near center by coordinates
   recorder Element -xml Damage3.out -time -ele 1 2 section 1 fiber 0.1 0.1 damage

   # Truss: use "material" with no tag
   recorder Element -file Damage4.out -time -ele 1 material damage

2. **Python Code**

.. code-block:: python

   # Fiber section: record damage of 1st fiber
   ops.recorder('Element', '-xml', 'Damage1.out', '-time', '-ele', 1, 2, 'section', 1, 'material', 0, 'damage')

   # Truss: use "material" with no tag
   ops.recorder('Element', '-file', 'Damage4.out', '-time', '-ele', 1, 'material', 'damage')

.. note::

   For theory and implementation details see Uriz (2005) and the OpenSees wiki.

.. seealso::

   `Fatigue Material (OpenSees wiki) <http://opensees.berkeley.edu/wiki/index.php/Fatigue_Material>`_

.. admonition:: Example

   Wrapping Steel01 with default fatigue parameters (E0 = 0.191, m = -0.458):

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Steel01 1 50.0 2000.0 0.01
      uniaxialMaterial Fatigue 2 1
      # with explicit defaults: uniaxialMaterial Fatigue 2 1 -E0 0.191 -m -0.458

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Steel01', 1, 50.0, 2000.0, 0.01)
      ops.uniaxialMaterial('Fatigue', 2, 1)
      # with explicit defaults: ops.uniaxialMaterial('Fatigue', 2, 1, '-E0', 0.191, '-m', -0.458)

References
""""""""""

- Uriz, P. (2005). "Towards Earthquake Resistant Design of Concentrically Braced Steel Structures," Ph.D. Dissertation, UC Berkeley.
- Ballio, G., and Castiglioni, C. A. (1995). "A Unified Approach for the Design of Steel Structures under Low and/or High Cycle Fatigue." Journal of Constructional Steel Research, 34, 75-101.

Code developed by: Patxi Uriz, Exponent; modifications by Kevin Mackie.
