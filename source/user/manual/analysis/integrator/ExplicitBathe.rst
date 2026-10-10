.. _ExplicitBathe:

ExplicitBathe
-------------

This command is used to construct an explicit, two-sub-step transient
integrator based on the composite scheme of Noh and Bathe [Noh2013]_, with an
optional Cundall/FLAC-style **local non-viscous damping** term (``-lnvd``)
that can be used to turn the integrator into a dynamic-relaxation /
pseudo-static solver.

.. function:: integrator ExplicitBathe $p <$computeCriticalDt> <-lnvd $alpha>

``$computeCriticalDt`` and ``-lnvd $alpha`` are both optional and may be
given in either order after ``$p`` (or omitted altogether).

.. csv-table::
   :header: "Argument", "Type", "Description", "Default"
   :widths: 18, 10, 55, 15

   "$p", "|float|", "Sub-step / numerical-damping parameter, :math:`0 < p < 1` (typically 0.5-0.95; :math:`p=0.5` gives no intrinsic numerical damping)", "required"
   "$computeCriticalDt", "|integer|", "Integer flag; any value greater than ``0`` enables it. If enabled, the critical time step is computed once (from the element mass/initial-stiffness eigenproblem) on the first ``newStep``, and every step's :math:`\Delta t/\Delta t_{crit}` ratio is reported", "0"
   "-lnvd $alpha", "|float|", "Local non-viscous (Cundall/FLAC) damping coefficient, :math:`0 \le \alpha < 1`, applied to the solved acceleration of each of the two Bathe sub-steps (equivalent to damping the unbalanced force, since the mass is diagonal -- see Theory below)", "0 (off)"

Available only in the Tcl interpreter (registered in ``SRC/tcl/commands.cpp``);
there is no corresponding entry in the Python/``OpenSeesCommands`` dispatcher,
so this integrator cannot be used from OpenSeesPy.

.. note::
   * The method is second-order accurate and explicit, performing two
     sub-steps per :math:`\Delta t`: :math:`t \to t+p\Delta t` and
     :math:`t+p\Delta t \to t+\Delta t`.
   * Only the mass matrix is ever assembled as the tangent
     (``formEleTangent``/``formNodTangent`` only add :math:`M`); as with any
     explicit scheme this requires a nonsingular (preferably diagonal) mass
     matrix on every active DOF, and exactly two ``update()`` calls per step
     (a third call is rejected with a warning).
   * :math:`p` must satisfy :math:`0 < p < 1` strictly; :math:`p=0` or
     :math:`p=1` are rejected at construction. :math:`p=0.5` is the
     special case with zero intrinsic numerical damping (:math:`q_0=q_1=0`,
     :math:`q_2=0.5`), useful for isolating the effect of ``-lnvd`` from the
     scheme's own damping.
   * For stability (undamped): :math:`\Delta t \le 2/\omega_{max}`, with a
     critical time step that is approximately twice that of plain central
     difference for the same mesh.
   * Passing a nonzero ``$computeCriticalDt`` (e.g. ``1``) triggers, on the
     first time step only, a generalized-eigenvalue (``dggev``)
     critical-time-step scan over every element's lumped mass and initial
     stiffness, printing the governing (minimum) damped and undamped
     :math:`\Delta t_{crit}` and the element tag at which each occurs;
     subsequently every ``newStep`` reports the ratio
     :math:`\Delta t/\Delta t_{crit,damped}` with an ``[OK]`` /
     ``[WARNING: dt > dt_crit!]`` tag.
   * An invalid ``-lnvd`` value (:math:`\alpha` outside :math:`[0,1)`, or a
     missing value), or any unrecognized option, prints a warning and is
     simply ignored -- local damping stays off and the integrator is still
     constructed. Only an invalid ``$p`` (outside :math:`(0,1)`) makes
     construction fail. Leaving ``-lnvd`` off, or passing ``-lnvd 0.0``,
     reproduces the original (undamped-by-this-mechanism) Noh-Bathe scheme.
   * This local damping is unrelated to (and not a substitute for) Rayleigh
     damping assigned to elements/regions; it is a purely numerical
     dissipation mechanism intended for pseudo-static / dynamic-relaxation
     analyses, not for genuine dynamic response.
   * ``-lnvd`` is applied to the fully assembled acceleration of each
     sub-step, including -- correctly -- when the model is partitioned
     across processes with one of the parallel diagonal systems of
     equations; re-forming or printing the unbalance for diagnostics does
     not change the result.
   * The equivalence between damping the acceleration and damping the
     unbalanced force (see Theory below) relies on a lumped (diagonal)
     mass, as is standard for this explicit scheme. If a consistent mass
     matrix were instead assembled and solved with a general (non-diagonal)
     solver, ``-lnvd`` would still be applied per equation to the resulting
     :math:`a=M^{-1}F`, but the per-equation damping term would no longer
     correspond to damping the same equation's unbalanced force, and energy
     dissipation would no longer be guaranteed.
   * See also :ref:`ExplicitDifferenceStatic`, which applies the same kind
     of Cundall/FLAC local damping to a plain central-difference (leap-frog)
     integrator, but *by default* combines the velocity-sign and
     force-rate forms of the law and adds a small velocity dead-band (``-vEps``) to
     avoid sign chatter near zero velocity. ``-lnvd`` here always uses only
     the simple :math:`F_d=-\alpha|F|\,\mathrm{sign}(v)` law (with
     :math:`\mathrm{sign}(0)=0`) and has no dead-band, so it should not be
     expected to behave identically to ``ExplicitDifferenceStatic``'s own
     damping for the same :math:`\alpha`.

Theory
^^^^^^

The ExplicitBathe method is a two-step explicit integration scheme with
built-in numerical damping. The method performs two sub-steps per time step:

1. First step: :math:`t \rightarrow t + p\Delta t`
2. Second step: :math:`t + p\Delta t \rightarrow t + \Delta t`

The integration coefficients are computed from the damping parameter p:

.. math::

   q_1 = \frac{1 - 2p}{2p(1-p)}

   q_2 = 0.5 - p \cdot q_1

   q_0 = -q_1 - q_2 + 0.5

The method offers enhanced stability compared to standard central
difference, with a critical time step approximately twice as large. The
parameter p controls numerical damping, with higher values providing more
damping but reduced accuracy.

**Local non-viscous (Cundall/FLAC) damping (-lnvd).** When ``alpha > 0``,
after the linear system is solved for the acceleration of *each* of the two
Bathe sub-steps, that solved acceleration :math:`a` is modified
equation-by-equation:

.. math::

   a_d = a - \alpha\, |a| \,\mathrm{sign}(v)

where :math:`v` is that sub-step's predicted velocity (:math:`v_t+a_t\,p
\Delta t` for the first sub-step, and the corrected
:math:`v_{t+p\Delta t}+a_{t+p\Delta t}(1-p)\Delta t` for the second) -- the
same velocity that was used to set the model's response before that
sub-step's equations were formed and solved. Because the mass used by this
explicit scheme is diagonal (lumped), this is algebraically identical,
equation by equation, to applying Cundall's local damping scheme
[CundallBathe1987]_, as used in FLAC/FLAC3D, directly to the unbalanced force
:math:`F = P - R(u)` (applied load minus assembled resisting force):

.. math::

   F_d = -\alpha\, |F| \,\mathrm{sign}(v)

It removes energy in proportion to the magnitude of the unbalance itself
rather than to velocity, so the fractional damping per cycle is
amplitude-independent. Because the damping acts on the fully assembled
acceleration, it is applied correctly even when the model is partitioned
across processes using a parallel diagonal system of equations; whether the
underlying unbalance is also re-formed or printed for diagnostics has no
effect on the result.

As for :ref:`ExplicitDifferenceStatic`, a first-order (small-:math:`\alpha`)
energy balance for a free-vibration SDOF oscillator (:math:`F=-kU`, so
:math:`F_d=-\alpha|F|\,\mathrm{sign}(v)` is exact there) gives an equivalent
viscous damping ratio :math:`\xi \approx \alpha/\pi` and a logarithmic
decrement per cycle :math:`\delta \approx 2\alpha`, i.e.

.. math::

   \frac{A_{n+1}}{A_n} \approx e^{-2\alpha}

This asymptote is accurate to a fraction of a percent for
:math:`\alpha \lesssim 0.1` and increasingly over-damps relative to the
true response as :math:`\alpha \to 1` (the scheme remains stable; it simply
dissipates energy faster than the first-order estimate predicts). Because it
removes energy proportional to the *size of the unbalance*, regardless of how
far from equilibrium the system starts, ``-lnvd`` with a large :math:`\alpha`
(close to but below 1) is effective as a dynamic-relaxation driver for
pseudo-static problems (gravity application, settling a soil column,
push-over); a small :math:`\alpha` (or omitting ``-lnvd``) should be used for
genuine dynamic/earthquake analyses, where this damping should not
contaminate the computed response.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      integrator ExplicitBathe 0.54
      integrator ExplicitBathe 0.54 1
      # p=0.5 (no intrinsic damping), strong local non-viscous damping
      integrator ExplicitBathe 0.5 0 -lnvd 0.8

   ExplicitBathe is Tcl-only; there is no Python binding to show here (see
   the note above).

   2. **SDOF free-vibration decay example**

   A single-DOF spring-mass oscillator (:math:`k=100`, lumped mass
   :math:`m=1` at the free node, via ``element truss 1 1 2 1.0 1 -rho 2.0``)
   released from rest at :math:`u_0=0.01`, integrated with :math:`p=0.5`
   (no intrinsic numerical damping) so that any amplitude decay is due to
   ``-lnvd`` alone. For :math:`\alpha=0.1`, the ratio of the first two
   displacement peaks matches the theoretical small-:math:`\alpha` estimate
   :math:`e^{-2\alpha}=0.8187` to within 0.04%; running the script with
   :math:`\alpha=0, 0.3, 0.8` gives :math:`\max|u|` over :math:`t\in[3,4]\,s`
   of about :math:`1.0\times10^{-2}`, :math:`5.1\times10^{-4}` and
   :math:`5.9\times10^{-6}` respectively (versus essentially no decay,
   moderate decay, and strong decay predicted qualitatively by the theory
   above; the exact values increasingly depart from the small-:math:`\alpha`
   asymptote as :math:`\alpha` grows, as expected).

   |  :download:`example_bathe_lnvd_sdof_decay.tcl <../codeExample/example_bathe_lnvd_sdof_decay.tcl>`   **(TCL)**.

   3. **Pseudo-static relaxation example**

   The same 4-DOF loaded chain used in the :ref:`ExplicitDifferenceStatic`
   pseudo-static example, now relaxed with
   ``integrator ExplicitBathe 0.5 0 -lnvd 0.8``. The hand-calculated static
   displacements are :math:`u_1=0.008`, :math:`u_2=0.014`, :math:`u_3=0.018`,
   :math:`u_4=0.020`; running the script below reproduces these to machine
   precision, with residual velocities of order :math:`10^{-16}`-:math:`10^{-17}`.

   |  :download:`example_bathe_lnvd_pseudostatic.tcl <../codeExample/example_bathe_lnvd_pseudostatic.tcl>`   **(TCL)**.

.. [Noh2013] Noh, G., & Bathe, K.J. (2013). "An explicit time integration scheme for the analysis of wave propagations." Computers & Structures, 129, 178-193.
.. [CundallBathe1987] Cundall, P.A. (1987). "Distinct Element Models of Rock and Soil Structure." In *Analytical and Computational Methods in Engineering Rock Mechanics*, 129-163.

Code Developed by: |jaabell|
