.. _PM4Sand:

PM4Sand Material
^^^^^^^^^^^^^^^^

Code Developed by: **Long Chen** and |pedro| at U.Washington.

This command is used to construct a 2-dimensional PM4Sand material ([Boulanger-Ziotopoulou2017]_).

   nDmaterial PM4Sand $matTag $Dr $G0 $hpo $Den <$patm $h0 $emax $emin $nb $nd $Ado $zmax $cz $ce $phic $nu $cgd $cdr $ckaf $Q $R $m $Fsed_min $p_sedo>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, tag identifying material
   $Dr, |float|,	Relative density (fraction)
   $G0, |float|,	Shear modulus constant
   $hpo, |float|,	Contraction rate parameter
   $Den, |float|,	Mass density of the material
   $P_atm, |float|,	optional: Atmospheric pressure
   $h0, |float|,	optional: Variable that adjusts the ratio of plastic modulus to elastic modulus
   $emax and $emin, |float|,	  optional: Maximum and minimum void ratios
   $nb , |float|, optional: Bounding surface parameter $nb ≥ 0
   $nd, |float|,   optional: Dilatancy surface parameter $nd ≥ 0
   $Ado, |float|,  optional: Dilatancy parameter will be computed at the time of initialization if input value is negative
   $z_max, |float|,		optional: Fabric-dilatancy tensor parameter
   $cz, |float|,		optional: Fabric-dilatancy tensor parameter
   $ce, |float|,		optional: Variable that adjusts the rate of strain accumulation in cyclic loading
   $phic, |float|,		optional: Critical state effective friction angle
   $nu, |float|,		optional: Poisson's ratio
   $cgd, |float|,		optional: Variable that adjusts degradation of elastic modulus with accumulation of fabric
   $cdr, |float|,		optional: Variable that controls the rotated dilatancy surface
   $ckaf, |float|,		optional: Variable that controls the effect that sustained static shear stresses have on plastic modulus
   $Q, |float|,		optional: Critical state line parameter
   $R, |float|,		optional: Critical state line parameter
   $m, |float|,		optional: Yield surface constant (radius of yield surface in stress ratio space)
   $Fsed_min, |float|,	optional: Variable that controls the minimum value the reduction factor of the elastic moduli can get during reconsolidation
   $p_sedo, |float|,		optional: Mean effective stress up to which reconsolidation strains are enhanced

.. note::

   The only material formulation for the PM4Sand object is "PlaneStrain", as a consequence limited to plain strain continuum elements.

   Valid Element Recorder queries are **stress**, **strain**, **alpha** (or backstressratio) for :math:`\mathbf{\alpha}`, **fabric** for :math:`\mathbf{z}`, and **alpha_in** (or alphain) for :math:`\mathbf{\alpha_{in}}`

   Elastic or response could be enforced by

   .. code:: 

       updateMaterialStage -material $matTag -stage 0

   Elastoplastic by		       

   .. code::

      updateMaterialStage -material $matTag -stage 1

   The program will use the default value of a secondary parameter if a negative input is assigned to that parameter, e.g. Ado = -1. However, FirstCall is mandatory when switching from elastic to elastoplastic if negative inputs are assigned to stress-dependent secondary parameters, e.g. Ado and zmax. FirstCall can be set as,

   .. code::

       setParameter -value 0 -ele $elementTag FirstCall $matTag

   Post-shake reconsolidation can be activated by

   .. code::

      setParameter -value 1 -ele $elementTag Postshake $matTag

      The user should check that the results are not sensitive to time step size.

.. [Boulanger-Ziotopoulou2017] R.W.Boulanger, K.Ziotopoulou. "PM4Sand(Version 3.1): A Sand Plasticity Model for Earthquake Engineering Applications". Report No. UCD/CGM-17/01 2017

.. admonition:: Example 1	

   2D undrained monotonic direct simple shear test using one element

   .. literalinclude:: PM4SandExample1.tcl
      :language: tcl

.. admonition:: Example 2

   2D undrained cyclic direct simple shear test using one element (Displacement Controlled)

   .. literalinclude:: PM4SandExample2.tcl
      :language: tcl

.. admonition:: Example 3

   2D undrained cyclic direct simple shear test using one element (Force Controlled)

   .. literalinclude:: PM4SandExample3.tcl
      :language: tcl