.. _HystereticSM:

HystereticSM Material
^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial multilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. This material is an extension of the Hysteretic Material -- the envelope can be defined 2,3, 4,5,6 or 7 points, while the original one only had 2 or 3.
The positive and negative backbone of this material do not need to have the same number of segments. This material also has additional DCR-type recorder output. 

.. function:: uniaxialMaterial Hysteretic $matTag -posEnv $s1p $e1p $s2p $e2p <$s3p $e3p> <$s4p $e4p> <$s5p $e5p> <$s6p $e6p> <$s7p $e7p> <-negEnv $s1n $e1n $s2n $e2n <$s3n $e3n> <$s4n $e4n> <$s5n $e5n> <$s6n $e6n> <$s7n $e7n>> <-pinch $pinchX $pinchY> <-damage $damage1 $damage2> <-beta $beta> <-defoLimitStates $lsD1 <$lsD2>...> <-forceLimitStates $lsF1 <$lsF2>...> <printInput> <XYorder>

The following input format is compatible with Hysteretic material. Note that in this case you must have the same number of positive and negative segments:

.. function:: uniaxialMaterial Hysteretic $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> <$s4p $e4p> <$s5p $e5p> <$s6p $e6p> <$s7p $e7p> $s1n $e1n $s2n $e2n <$s3n $e3n> <$s4n $e4n> <$s5n $e5n> <$s6n $e6n> <$s7n $e7n> $pinchX $pinchY $damage1 $damage2 <$beta> <-defoLimitStates lsD1? <lsD2?>...> <-forceLimitStates lsF1? <lsF2?>...> <printInput> <XYorder>



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
     - stress and strain (or force & deformation) at 4th-7th points of the envelope in the positive direction (optional)
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
     - stress and strain (or force & deformation) at 4th-7th points of the envelope in the negative direction (optional)
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
   * - printInput
     - |string|
     - program will output input-parameter values (optional) 
   * - XYorder
     - |string|
     - invert backbone-envelope points to be strain-stress instead of stress-strain (optional). This flag has the same effect as using -posEnvXY and the optional -negEnvXY, so it should be used with the -posEnv and -negEnv flags.

.. note::
  * posEnv is defined using positive, INCREASING points --> strain values must be unique.
  * negEnv is defined using negative, DECREASING points --> strain values must be unique.
  * For symmetric response: do not enter -negEnv data.
  * If the last stress point is higher than the previous one, the curve will extrapolate linearly. If it is less than, the curve will extrapolate at a constant value equal to the last stress value
  * If you would like to enter strain-stress pairs use -posEnvXY (and optional -negEnvXY) instead of -posEnv (-negEnv) OR the flag XYorder.


Recorder Options:

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Label
     - Description
   * - MU1
     - Ductility Ratio
     - ratio of current strain to first point in strain/deformation envelope (if CurrentStrain positive: CurrentStrain/e1p, if CurrentStrain negative: CurrentStrain/e1n) (MUy also works)
   * - defoPlastic
     - Plastic Deformation
     - CurrentStrain/defo - ElasticStrain/defo (ElasticStrain is defined by the elastic stiffness s1p/e1p, if CurrentStrain is positive, or s2p/e2p, if negative, and the current stress/force)     
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

------------

**Example Input:**

ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 1, 1,'-damage', 0.1, 0.01, '-beta', 0,'-defoLimitStates', 0.01, -0.01, 0.02, -0.02, '-forceLimitStates', 2772.0, -2772.0, 3104.6, -3104.6,'printInput')

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  1  1 -damage  0.1  0.01 -beta 0 -defoLimitStates 0.01 -0.01 0.02 -0.02 -forceLimitStates 2772.0 -2772.0 3104.6 -3104.6 -printInput

------------

**Backbone Curve for material (7 points in each direction)**

.. figure:: figures/HystereticSM/HystereticSM_backbone_Symm.jpg
  :align: center
  :figclass: align-center

**Backbone Curve for material (non-symmetric behavior)**

.. figure:: figures/HystereticSM/HystereticSM_backbone_nonSymm.jpg
  :align: center
  :figclass: align-center

------------

**Parameter Study: Pinching**

*HystereticSM_pinch=[1, 1]*

ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 1, 1)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  1  1

*HystereticSM_pinch=[0.2, 0.8]*

ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 0.2, 0.8)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  0.2  0.8

*HystereticSM_pinch=[0.8, 0.2]*

ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-pinch', 0.8, 0.2)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -pinch  0.8  0.2

.. figure:: figures/HystereticSM/HystereticSM_pinch_strainDip.jpg
.. figure:: figures/HystereticSM/HystereticSM_pinch_symmCycles.jpg
.. figure:: figures/HystereticSM/HystereticSM_pinch_strainOneSidedPush.jpg
.. figure:: figures/HystereticSM/HystereticSM_pinch_OneSidedPus.jpg


------------

**Parameter Study: Damage1**

*HystereticSM_damage1=0*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0

*HystereticSM_damage1=0.01*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0.01, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.01  0

*HystereticSM_damage1=0.1*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0.1, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0.1  0

.. figure:: figures/HystereticSM/HystereticSM_damage1_strainDip.jpg
.. figure:: figures/HystereticSM/HystereticSM_damage1_symmCycles.jpg
.. figure:: figures/HystereticSM/HystereticSM_damage1_strainOneSidedPush.jpg
.. figure:: figures/HystereticSM/HystereticSM_damage1_OneSidedPus.jpg

------------

**Parameter Study: Damage2**

*HystereticSM_damage2=0*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0

*HystereticSM_damage2=0.01*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0.01)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0.01

*HystereticSM_damage2=0.1*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-damage', 0, 0.1)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -damage  0  0.1

.. figure:: figures/HystereticSM/HystereticSM_damage2_strainDip.jpg
.. figure:: figures/HystereticSM/HystereticSM_damage2_symmCycles.jpg
.. figure:: figures/HystereticSM/HystereticSM_damage2_strainOneSidedPush.jpg
.. figure:: figures/HystereticSM/HystereticSM_damage2_OneSidedPus.jpg

------------

**Parameter Study: beta**

*HystereticSM_beta=0*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-beta', 0)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  0

*HystereticSM_beta=0.5*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-beta', 0.5)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  0.5

*HystereticSM_beta=1*
ops.uniaxialMaterial('HystereticSM', 99, '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, '-beta', 1)

uniaxialMaterial HystereticSM  99  -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  -beta  1

.. figure:: figures/HystereticSM/HystereticSM_beta_strainDip.jpg
.. figure:: figures/HystereticSM/HystereticSM_beta_symmCycles.jpg
.. figure:: figures/HystereticSM/HystereticSM_beta_strainOneSidedPush.jpg
.. figure:: figures/HystereticSM/HystereticSM_beta_OneSidedPus.jpg



Modified Code Developed by: |Silvia Mazzoni (Silvia's Brainery)|
Original Hysteretic-Material Code Developed by: |Michael Scott (Oregon State University) & Filip Filippou (UC Berkeley)|
