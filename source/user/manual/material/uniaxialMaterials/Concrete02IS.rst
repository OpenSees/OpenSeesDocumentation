.. _Concrete02IS:

Concrete02IS Material (Concrete02 with Initial Stiffness Control)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial concrete material with the same compressive envelope and tension/cyclic behavior as :ref:`Concrete02`, but with **user-defined initial stiffness** *E*\ :sub:`0`. In Concrete02 the initial stiffness is fixed at :math:`E_c = 2f'_c/\varepsilon_{c0}`; Concrete02IS allows any *E*\ :sub:`0` (e.g. :math:`57000\sqrt{f'_c}` or secant stiffness to peak).

.. function:: uniaxialMaterial Concrete02IS $matTag $E0 $fpc $epsc0 $fpcu $epsU <$lambda $ft $Ets>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,  |integer|,  unique material tag
   $E0,      |float|,    initial (elastic) stiffness
   $fpc,     |float|,    concrete compressive strength at 28 days (compression negative)
   $epsc0,   |float|,    concrete strain at maximum strength (negative)
   $fpcu,    |float|,    concrete crushing strength (negative)
   $epsU,    |float|,    concrete strain at crushing strength (negative)
   $lambda,  |float|,    (optional) ratio between unloading slope at epsU and initial slope
   $ft,      |float|,    (optional) tensile strength
   $Ets,     |float|,    (optional) tension softening stiffness (absolute value)

.. note::

   Compressive parameters (*fpc*, *epsc0*, *fpcu*, *epsU*) are taken as negative; if given positive, they are converted to negative internally. The input *E*\ :sub:`0` affects the unloading/reloading stiffness in compression. The ascending branch uses the Popovics equation (Concrete02 uses the Hognestad parabola).

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      set fc 4000.0
      set epsc0 -0.002
      set fcu -1000.0
      set epscu -0.006
      # Same initial stiffness as Concrete02
      set Ec [expr 2.0*$fc/(-$epsc0)]
      uniaxialMaterial Concrete02IS 1 $Ec $fc $epsc0 $fcu $epscu
      # With tension and optional parameters
      uniaxialMaterial Concrete02IS 2 $Ec $fc $epsc0 $fcu $epscu 0.1 500.0 1738.33

   2. **Python Code**

   .. code-block:: python

      fc, epsc0 = 4000.0, -0.002
      fcu, epscu = -1000.0, -0.006
      Ec = 2.0 * fc / (-epsc0)
      ops.uniaxialMaterial('Concrete02IS', 1, Ec, fc, epsc0, fcu, epscu)
      ops.uniaxialMaterial('Concrete02IS', 2, Ec, fc, epsc0, fcu, epscu, 0.1, 500.0, 1738.33)

.. seealso::

   :ref:`Concrete02` (fixed initial stiffness). `Concrete02 with Control of the Initial Stiffness (Portwood Digital) <https://portwooddigital.com/2021/11/06/concrete02-with-control-of-the-initial-stiffness/>`_.

Code developed by: Filip Filippou (Concrete02); Nasser Marafi (Concrete02IS, initial stiffness control).
