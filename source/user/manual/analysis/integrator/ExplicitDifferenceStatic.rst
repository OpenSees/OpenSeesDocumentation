.. _ExplicitDifferenceStatic:

ExplicitDifferenceStatic
------------------------

This command is used to construct an explicit central-difference (leap-frog)
transient integrator that additionally applies Cundall/FLAC-style **local
non-viscous damping** to the assembled nodal unbalance, making it usable as a
dynamic-relaxation / pseudo-static solver as well as a plain explicit
dynamics integrator.

.. function:: integrator ExplicitDifferenceStatic <-alpha $alpha> <-simple>

.. csv-table::
   :header: "Argument", "Type", "Description", "Default"
   :widths: 15, 10, 55, 15

   "-alpha $alpha", "|float|", "Local non-viscous damping coefficient, :math:`0 \le \alpha < 1`", "0.59"
   "-simple", "flag", "Use the simple damping law :math:`F_d=-\alpha|F|\,\mathrm{sign}(v)` instead of the default combined law", "combined (off)"

Available in both the Tcl and Python interpreters.

.. note::
   * Leap-frog scheme: velocities are stored at half time steps
     :math:`v_{n+1/2}`, displacements and accelerations at full time steps.
   * Only the mass matrix is ever assembled as the tangent (``formEleTangent``/
     ``formNodTangent`` only add :math:`M`); no stiffness tangent is formed, so
     a ``Linear`` algorithm is required and only one ``update()`` call per
     step is allowed.
   * Stability (undamped): :math:`\Delta t \le 2/\omega_{max}`; with Rayleigh
     damping ratio :math:`\xi`: :math:`\Delta t \le 2/(\omega_{max}(\sqrt{1+\xi^2}-\xi))`.
   * The local damping is applied **in addition to** any Rayleigh damping set
     via the four-argument C++ constructor (:math:`\alpha_M,\beta_K,\beta_{K_i},\beta_{K_c}`),
     which is not exposed through the Tcl/Python parser options above.
   * Passing ``-alpha 0.0`` disables the damping loop
     (``alphaLNVD <= 0.0`` short-circuits in ``formUnbalance``), with no
     overhead difference from the plain ``ExplicitDifference`` integrator.
     Note that omitting ``-alpha`` entirely does *not* give :math:`\alpha=0`;
     it falls back to the default 0.59.
   * **Before the fix that added the options above**, the local damping force
     was computed from ``DOF_Group::getUnbalance()``, which only holds the
     *applied* nodal loads, not the assembled unbalance :math:`P-R(u)`. As a
     result the damping term scaled with the applied load only and vanished
     identically in free vibration (no applied load), making the integrator's
     behavior indistinguishable from plain ``ExplicitDifference`` in that
     case. The fix applies the damping to the fully assembled unbalance in
     ``formUnbalance``, as documented below.
   * See also ``integrator ExplicitBathe $p <0|1> <-lnvd $alpha>`` (on a
     separate branch), which adds the same "simple" local non-viscous damping
     law to Bathe's composite explicit scheme (no "combined" option).

Theory
^^^^^^

**Leap-frog update.** Given velocity at :math:`t-\Delta t/2`, acceleration at
:math:`t`, and displacement at :math:`t`:

.. math::

   v_{t+\Delta t/2} = v_{t-\Delta t/2} + \Delta t\, a_t

   U_{t+\Delta t} = U_t + \Delta t\, v_{t+\Delta t/2}

The new acceleration is obtained from :math:`M a_{t+\Delta t} = F_{t+\Delta t}`
where :math:`F = P - R(u)` is the fully assembled nodal unbalance (applied
load minus the assembled resisting force; only :math:`M` is used as the
linear-system tangent).

**Local non-viscous (Cundall/FLAC) damping.** Rather than a viscous term
proportional to velocity, Cundall's local damping scheme [Cundall1987]_
(also described in the FLAC/FLAC3D theory manuals, Itasca Consulting Group)
removes energy by adding to the assembled unbalance a force proportional to
the *magnitude of the unbalance itself* and opposing the velocity:

.. math::

   F_d = -\alpha\, |F| \,\mathrm{sign}(v) \qquad \text{("simple", } \texttt{-simple}\text{)}

or, combining the sign of the unbalance's time rate of change with the sign
of velocity ("combined", the default):

.. math::

   F_d = \tfrac{1}{2}\alpha\, |F| \,\big(\mathrm{sign}(\dot F) - \mathrm{sign}(v)\big)

:math:`\mathrm{sign}(v)` is replaced by a held sign :math:`s_v` with a small
deadband (:math:`|v|<10^{-4}` keeps the previous sign) to avoid chatter as the
velocity passes through zero. :math:`\dot F` is approximated by the backward
difference :math:`(F_t - F_{t-\Delta t})/\Delta t` (only the sign is used, so
the :math:`\Delta t` cancels). This damping acts equation-by-equation on the
fully assembled unbalance :math:`F=P-R(u)` and is added in ``formUnbalance``
after the base ``TransientIntegrator::formUnbalance`` call; it is unrelated
to (and does not replace) any Rayleigh damping.

**Equivalent viscous damping ratio (small** :math:`\alpha` **).** For an
undamped SDOF oscillator (:math:`F=-kU`) with no applied load, free vibration
gives :math:`\dot F = -kv`, so :math:`\mathrm{sign}(\dot F)=-\mathrm{sign}(v)`
identically and the combined law reduces exactly to the simple law,
:math:`F_d=-\alpha|F|\,\mathrm{sign}(v)`. A first-order energy balance over
one cycle of amplitude :math:`A` then gives a fractional energy loss per
cycle :math:`\Delta E/E = 4\alpha`, which matches a viscously damped
oscillator with damping ratio

.. math::

   \xi \approx \frac{\alpha}{\pi}

and hence a logarithmic decrement per cycle :math:`\delta=2\pi\xi\approx
2\alpha`, i.e. successive displacement peaks decay by

.. math::

   \frac{A_{n+1}}{A_n} \approx e^{-2\alpha}

This relation is accurate to a fraction of a percent for :math:`\alpha
\lesssim 0.1` (for :math:`\alpha=0.1` the example below gives a decay ratio
of 0.8182 against the theoretical 0.8187, i.e. 0.07% error), and
increasingly over-damps relative to the small-:math:`\alpha` asymptote as
:math:`\alpha \to 1` (the scheme does not blow up; it simply dissipates
energy faster than the first-order estimate because the waveform is no
longer a small perturbation of a pure sinusoid).

Because :math:`F_d\propto|F|` rather than a fixed Coulomb force, the
fractional damping per cycle is independent of amplitude -- this is a
*hysteretic*-type damping, not Coulomb friction, which is what makes it
suitable as a general-purpose "numerical damping" for driving a system to
static equilibrium (dynamic relaxation) regardless of how far from
equilibrium it starts.

**When to use it.** Set :math:`\alpha` as large as possible (close to but
below 1) while keeping the scheme accurate and stable if the sole goal is a
*static* solution (push-over, gravity application, settling a soil column) --
this is the classical FLAC "local damping" use case. Use a small
:math:`\alpha` (or the plain ``ExplicitDifference`` integrator, equivalent to
:math:`\alpha=0`) when running genuine dynamic/earthquake analyses where the
damping should not contaminate the computed response.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      integrator ExplicitDifferenceStatic -alpha 0.8
      integrator ExplicitDifferenceStatic -alpha 0.3 -simple
      integrator ExplicitDifferenceStatic
      ;# default: -alpha 0.59, combined form

   2. **Python Code**

   .. code-block:: python

      ops.integrator('ExplicitDifferenceStatic', '-alpha', 0.8, '-simple')

   3. **SDOF free-vibration decay example**

   A single-DOF spring-mass oscillator released from rest at :math:`u_0=1`
   with no applied load. Theory predicts the ratio of successive
   displacement peaks :math:`A_{n+1}/A_n \approx e^{-2\alpha}`; running the
   script below with :math:`\alpha=0.1` gives a decay ratio of **0.8182**
   against the theoretical **0.8187** (0.07% error), confirming the
   small-:math:`\alpha` estimate and that the "combined" and "simple" laws
   coincide in free vibration (:math:`\mathrm{sign}(\dot F)=-\mathrm{sign}(v)`
   identically for a purely elastic unbalance).

   |  :download:`example_sdof_decay.tcl <../codeExample/example_sdof_decay.tcl>`   **(TCL)**.

   4. **Pseudo-static relaxation example**

   A 4-DOF chain of springs and lumped masses, each node carrying a constant
   load :math:`P`, relaxed with the default damping (:math:`\alpha=0.59`,
   combined) until velocities vanish. The hand-calculated static
   displacements are :math:`u_1=0.008`, :math:`u_2=0.014`, :math:`u_3=0.018`,
   :math:`u_4=0.020`; running the script below reproduces these to machine
   precision with residual velocities of order :math:`10^{-17}`.

   |  :download:`example_pseudostatic.tcl <../codeExample/example_pseudostatic.tcl>`   **(TCL)**.

Usage notes and limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Requires a ``Linear`` solution algorithm and (as for any explicit scheme) a
  nonsingular, preferably diagonal, mass matrix for every active DOF
  (rotational DOFs with zero mass will make the system singular).
* ``-alpha`` is rejected (integrator construction fails, returns ``0``) for
  values outside :math:`[0,1)`.
* The ``-alpha``/``-simple`` options only control the *local* non-viscous
  damping; separate Rayleigh damping is still available through the
  four-argument C++ constructor (not exposed by the Tcl/Python parsers).
* The "combined" form equals the "simple" form whenever the unbalance is a
  single-valued elastic function of displacement in free vibration (no
  applied load); the two forms only diverge once the sign of :math:`\dot F`
  decouples from the sign of :math:`v` -- e.g. under nonlinear/path-dependent
  material response, or while a time-varying load is applied (see
  ``example_pseudostatic.tcl``, where a *constant* load is used precisely so
  that any residual oscillation gets damped consistently).
* Prior to the fix described in the note above, this damping had **no
  effect** in free-vibration / unloaded-structure analyses, since it only
  ever saw the (zero or constant) applied-load vector, not the element
  resisting forces; any model relying on the old behavior for genuinely
  unloaded dynamic relaxation was not actually being damped.

.. [Cundall1987] Cundall, P.A. (1987). "Distinct Element Models of Rock and Soil Structure." In *Analytical and Computational Methods in Engineering Rock Mechanics*, 129-163.
.. [FLAC] Itasca Consulting Group, Inc. *FLAC/FLAC3D Theory and Background -- Dynamic Analysis: Damping*, section on local (Cundall) damping.

Code Developed by: |jaabell|
