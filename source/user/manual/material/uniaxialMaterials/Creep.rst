.. _Creep :

Creep Material -- Wrapper Creep Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial time-dependent material object that wraps around a given base material to simulate both creep and shrinkage under sustained loads. The creep and shrinkage are modeled following the guidelines of ACI 209R-92.

.. function:: uniaxialMaterial Creep $matTag $baseMaterial $tD $epsshu $psish $Tcr $phiu $psicr1 $psicr2 $tcast

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 6, 4, 40

    "``$matTag``", integer, "Integer tag identifying material."
    "``$baseMaterial``", integer, "Integer tag identifying base material."
    "``$tD``", float, "Analysis time at initiation of drying (in days)."
    "``$epsshu``", float, "Ultimate shrinkage strain denoted as :math:`(ϵ_{sh})_u` in Eq. 2-7 of ACI 209R-92."
    "``$psish``", float, "Fitting parameter of the shrinkage time evolution function denoted as :math:`f` in Eq. 2-7 of ACI 209R-92."
    "``$Tcr``", float, "Creep model age (in days) used for the calculation of ``$phiu``."
    "``$phiu``", float, "Ultimate creep coefficient defined as the ratio of creep strain to initial strain, denoted as :math:`ν_u` in Eq. 2-6 of ACI 209R-92."
    "``$psicr1``", float, "Fitting parameter of the creep time evolution function denoted as :math:`ψ` in Eq. 2-6 of ACI 209R-92."
    "``$psicr2``", float, "Fitting parameter of the creep time evolution function denoted as :math:`d` in Eq. 2-6 of ACI 209R-92."
    "``$tcast``", float, "Analysis time corresponding to concrete casting (in days)."


.. note::
   1. Shrinkage concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).


**References**

This wrapper creep material was adapted from the TDConcrete material by Michael Scott. The TDConcrete material was developed by A. M. Knaack and Y. C. Kurama. A manual describing the use of the TDConcrete concrete model can be found at: `https://data.mendeley.com/datasets/z4gxnhchky/5 <https://data.mendeley.com/datasets/z4gxnhchky/5>`_

Detailed descriptions of the model and its implementation can be found in the following:

1. American Concrete Institute (ACI). (2002). ACI PRC-209-92: Prediction of Creep, Shrinkage, and Temperature Effects in Concrete Structures (Reapproved 2008). ACI Committee 209. ISBN: 9780870311222.

2. Knaack, A. M., & Kurama, Y. C. (2018). Modeling Time-Dependent Deformations: Application for Reinforced Concrete Beams with Recycled Concrete Aggregates. ACI Structural Journal, 115(1).

3. Knaack, A. (2013). Sustainable concrete structures using recycled concrete aggregate: Short-term and long-term behavior considering material variability (Doctoral dissertation, University of Notre Dame), 680 pp.

