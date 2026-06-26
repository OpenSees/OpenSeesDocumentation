.. _CreepShrinkageACI209 :

CreepShrinkageACI209 -- Wrapper Creep Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial time-dependent material object that wraps around an existing base material to simulate creep and shrinkage under sustained loads. The creep and shrinkage evolution equations follow ACI 209R-92. The wrapper subtracts the computed creep and shrinkage strains from the total applied strain before passing the resulting mechanical strain to the base material, so any ``uniaxialMaterial`` can be made time-dependent with this wrapper.

.. function:: uniaxialMaterial CreepShrinkageACI209 $matTag $baseMaterial $tD $epsshu $psish $Tcr $phiu $psicr1 $psicr2 $tcast

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 6, 4, 40

    "``$matTag``",      integer, "Unique integer tag for this material."
    "``$baseMaterial``", integer, "Tag of an existing ``uniaxialMaterial`` to wrap."
    "``$tD``",          float, "Analysis time at initiation of drying (days)."
    "``$epsshu``",      float, "Ultimate shrinkage strain :math:`(\varepsilon_{sh})_u` in ACI 209R-92 Eq. 2-7 (input as negative)."
    "``$psish``",       float, "Shrinkage time-evolution parameter :math:`f` in ACI 209R-92 Eq. 2-7. Typical values: 35 (moist-cured 7 days), 55 (steam-cured)."
    "``$Tcr``",         float, "Reference concrete age at loading (days) for which ``$phiu`` is defined."
    "``$phiu``",        float, "Ultimate creep coefficient :math:`\phi_u` in ACI 209R-92 Eq. 2-6. Standard ACI 209 value is 2.35."
    "``$psicr1``",      float, "Creep time-evolution parameter :math:`\psi` in ACI 209R-92 Eq. 2-6."
    "``$psicr2``",      float, "Creep time-evolution parameter :math:`d` in ACI 209R-92 Eq. 2-6."
    "``$tcast``",       float, "Analysis time at concrete casting (days)."


The material implements the following ACI 209R-92 equations.

**Shrinkage strain** (ACI 209R-92 Eq. 2-7):

.. math::

   \varepsilon_{sh}(t) = \frac{t - t_D}{f + (t - t_D)} \cdot (\varepsilon_{sh})_u

**Creep coefficient** (ACI 209R-92 Eq. 2-6, summed over all past stress increments):

.. math::

   \phi(t,\, t_i) = \frac{(t - t_i)^{\psi}}{d + (t - t_i)^{\psi}} \cdot \phi_u \cdot \left(\frac{t_{cr}}{t_i - t_{cast}}\right)^{0.118}

where :math:`t_i` is the time of each previous stress increment and the factor :math:`(t_{cr}/(t_i - t_{cast}))^{0.118}` is the ACI 209 age-at-loading correction.


.. note::
   1. Shrinkage parameters should be input as negative values; if given positive they are converted to negative internally.
   2. Time values (``$tD``, ``$Tcr``, ``$tcast``) must be in the same time units used in the analysis (days are assumed).
   3. Creep is only active when the OpenSees ``ops_Creep`` flag is set to 1.


.. admonition:: Example

   The following example constructs a ``Concrete02IS`` base material (tag 1) and wraps it
   with ``CreepShrinkageACI209`` (tag 2) using standard ACI 209R-92 parameters for 7-day
   moist-cured concrete loaded at 28 days.

   1. **Tcl Code**

   .. code-block:: tcl

      # Base concrete material (Concrete02IS, tag 1)
      # E0  fpc    epsc0   fpcu   epscu
      uniaxialMaterial Concrete02IS 1 4000.0 -4.0 -0.002 -0.8 -0.01

      # Wrap with ACI 209 creep/shrinkage (tag 2)
      # matTag baseMat tD   epsshu    psish  Tcr   phiu  psicr1 psicr2 tcast
      uniaxialMaterial CreepShrinkageACI209 2 1 7.0 -780e-6 35.0 28.0 2.35 0.6 10.0 0.0

   2. **Python Code**

   .. code-block:: python

      import openseespy.opensees as ops

      # Base concrete material (Concrete02IS, tag 1)
      ops.uniaxialMaterial('Concrete02IS', 1, 4000.0, -4.0, -0.002, -0.8, -0.01)

      # Wrap with ACI 209 creep/shrinkage (tag 2)
      ops.uniaxialMaterial('CreepShrinkageACI209', 2, 1, 7.0, -780e-6, 35.0, 28.0, 2.35, 0.6, 10.0, 0.0)


**References**

This wrapper creep material was adapted from the TDConcrete material. A manual describing TDConcrete can be found at: `https://data.mendeley.com/datasets/z4gxnhchky/5 <https://data.mendeley.com/datasets/z4gxnhchky/5>`_

1. American Concrete Institute (ACI). (2002). *ACI PRC-209-92: Prediction of Creep, Shrinkage, and Temperature Effects in Concrete Structures* (Reapproved 2008). ACI Committee 209. ISBN: 9780870311222.

2. Knaack, A. M., & Kurama, Y. C. (2018). Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. *ACI Structural Journal*, 115(1).

3. Knaack, A. (2013). *Sustainable concrete structures using recycled concrete aggregate: Short-term and long-term behavior considering material variability* (Doctoral dissertation, University of Notre Dame), 680 pp.

Code developed by: `Javad Esmaeelpour <jvd.esm@gmail.com>`_, `Mark D. Denavit <mdenavit@utk.edu>`_, and `Michael H. Scott <michael.scott@oregonstate.edu>`_. Based on TDConcrete by `Adam M. Knaack <aknaack@schaefer-inc.com>`_ and `Yahya C. Kurama <ykurama@nd.edu>`_.
