.. _HystereticSM:

HystereticSM Material
^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial multilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. This material is an extension of the Hysteretic Material -- the envelope can be defined 2,3, 5, or 7 points, while the original one only had 2 or 3.
This material also has additional DCR-type recorder output.

.. function:: uniaxialMaterial Hysteretic $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> <$s4p $e4p> <$s5p $e5p> <$s6p $e6p> <$s7p $e7p> $s1n $e1n $s2n $e2n <$s3n $e3n> <$s4n $e4n> <$s5n $e5n> <$s6n $e6n> <$s7n $e7n> $pinchX $pinchY $damage1 $damage2 <$beta> <-defoLimitStates lsD1? <lsD2?>...> <-forceLimitStates lsF1? <lsF2?>...>

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $matTag
     - |integer|
     - Integer tag identifying material
   * - $s1p $e1p 
     - |float|
     - stress and strain (or force & deformation) at first point of the envelope in the positive direction 
   * - $s2p $e2p
     - |float| 
     - stress and strain (or force & deformation) at second point of the envelope in the positive direction 
   * - $s3p $e3p 
     - |float| 
     - stress and strain (or force & deformation) at third point of the envelope in the positive direction (optional) 
   * - ($s4p $e4p .... $s7p $e7p)
     - |float| 
     - stress and strain (or force & deformation) at 4th-7th points of the envelope in the positive direction (optional). NOTE: sress/force values can only be constant or decrease in absolute value (same or less positive) from one point to the next. You can only define 2,3,5, or 7 points.
   * - $s1n $e1n 
     - |float|
     - stress and strain (or force & deformation) at first point of the envelope in the negative direction 
   * - $s2n $e2n
     - |float|
     - stress and strain (or force & deformation) at second point of the envelope in the negative direction
   * - $s3n $e3n 
     - |float|
     - stress and strain (or force & deformation) at third point of the envelope in the negative direction (optional) 
   * - ($s4n $e4n .... $s7n $e7n)
     - |float| 
     - stress and strain (or force & deformation) at 4th-7th points of the envelope in the negative direction (optional). NOTE: sress/force values can only be constant or decrease in absolute value (same or less negative) from one point to the next. 
   * - $pinchx
     - |float|
     - pinching factor for strain (or deformation) during reloading 
   * - $pinchy
     - |float|
     - pinching factor for stress (or force) during reloading 
   * - $damage1
     - |float|
     - damage due to ductility: D1(mu-1) 
   * - $damage2
     - |float|
     - damage due to energy: D2(Eii/Eult) 
   * - $beta
     - |float|
     - power used to determine the degraded unloading stiffness based on ductility, mu-beta (optional, default=0.0) 
   * - ($lsD1,$lsD2..)
     - |float|
     - list of user-defined strain/deformation limits for computing deformation DCRs (optional) 
   * - ($lsF1,$lsF2..)
     - |float|
     - list of user-defined stress/force limits for computing force DCRs (optional) 

.. Additional Recorder Options:



.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Label
     - Description
   * - defoDCR
     - deformation DCR on Envelope Points
     - 7-component array with the ratio of the CURRENT strain to each of the envelope strain points (if positive: positive points, if negative: negative points)
   * - defoDCRMax
     - Maximum-deformation DCR on Envelope Points
     - 14-component array with the ratio of the MAXIMUM strain to each of the envelope strain points (emaxP/e1p,....emaxP/e7p,emaxN/e1n,...emaxN/e7n)

   * - defoLimitStates
     - User-Defined Deformation Limit States
     - return array of user-defined deformation limit states
   * - forceLimitStates
     - User-Defined Force Limit States
     - return array of user-defined force limit states

   * - defoLimitStatesDCR
     - deformation DCR on User-Defined Limit States
     - array with the ratio of the CURRENT strain to each of the user-defined deformation limit states
   * - defoLimitStatesDCRMax
     - Maximum-deformation DCR on User-Defined Limit States
     - array with the ratio of the MAXIMUM strain to each of the user-defined deformation limit states (positive limit-state value emaxP/els, negative value emaxN/els)
   * - defoLimitStatesDCRMaxAbs
     - MaximumAbsolute-deformation DCR on User-Defined Limit States
     - array with the ratio of the MAXIMUM strain to each of the envelope strain points (max(emaxP,abs(emaxN))/els)

   * - forceLimitStatesDCR
     - force DCR on User-Defined Limit States
     - array with the ratio of the CURRENT stress/force to each of the user-defined force limit states


   * - allData
     - All relevant Data
     - all relevant data at current step (mom1p, rot1p, mom2p, rot2p, mom3p, rot3p, mom4p, rot4p, mom5p, rot5p, mom6p, rot6p, mom7p, rot7p, mom1n, rot1n, mom2n, rot2n, mom3n, rot3n, mom4n, rot4n, mom5n, rot5n, mom6n, rot6n, mom7n, rot7n, pinchX, pinchY, damfc1, damfc2, beta, CrotMax, CrotMin, CrotPu, CrotNu, CenergyD, CloadIndicator, Cstress, Cstrain, Ttangent)



Modified Code Developed by: |Silvia Mazzoni (Silvia's Brainery)|
Original Hysteretic-Material Code Developed by: |Michael Scott (Oregon State University) & Filip Filippou (UC Berkeley)|
