.. _HystereticSM:

HystereticSM Material
^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial multilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. 
- This material is an extension of the Hysteretic Material -- the envelope can be defined 2,3, 4,5,6 or 7 points, while the original one only had 2 or 3.
- The positive and negative backbone of this material do not need to have the same number of segments. 
- This material also has the option to degrade the envelope using the degEnv parameters -- these parameters must be used in combination with the damage parameters
- This material also has additional DCR-type recorder output (this is still a work in progress).

Input Command:
-----------------
  - **OpenSeesPy**:

    .. code-block:: python
      
       uniaxialMaterial('HystereticSM',matTag,
          '-posEnv',s1p,e1p,s2p,e2p <,s3p,e3p> <,s4p,e4p><,s5p,e5p><,s6p,e6p><,s7p,e7p> 
          <,'-negEnv',s1n,e1n,s2n,e2n <,s3n,e3n> <,s4n,e4n> <,s5n,e5n> <,s6n,e6n> <,s7n,e7n>> 
          <,'-pinch',pinchX,pinchY> 
          <,'-damage',damage1,damage2> 
          <,'-beta',beta> 
          <,'-degEnv',degEnvP <,degEnvN>> 
          <,'-defoLimitStates',lsD1 <$lsD2>...> 
          <,'-forceLimitStates',lsF1 <,$lsF2>...> 
          <,'-printInput'> 
          <,'-XYorder'>
        )

  - **Tcl interpreter**:

    .. function:: uniaxialMaterial HystereticSM $matTag \
          -posEnv $s1p $e1p $s2p $e2p <$s3p $e3p> <$s4p $e4p> <$s5p $e5p> <$s6p $e6p> <$s7p $e7p> \
          <-negEnv $s1n $e1n $s2n $e2n <$s3n $e3n> <$s4n $e4n> <$s5n $e5n> <$s6n $e6n> <$s7n $e7n>> \
          <-pinch $pinchX $pinchY> \
          <-damage $damage1 $damage2> \
          <-beta $beta> \
          <-degEnv degEnvP <degEnvN>> \
          <-defoLimitStates $lsD1 <$lsD2>...> \
          <-forceLimitStates $lsF1 <$lsF2>...> \
          <-printInput> \
          <-XYorder>

You can use the following input format as it is compatible with Hysteretic material. Note that in this case you must have the same number of positive and negative segments. I have made this format (make sure you test it) to make the transition from Hysteretic to HystereticSM easy:

  - **OpenSeesPy**:

    .. function:: uniaxialMaterial('HystereticSM',matTag,s1p,e1p,s2p,e2p <,s3p,e3p> <,s4p,e4p> <,s5p,e5p> <,s6p,e6p> <,s7p,e7p>,
          s1n,e1n,s2n,e2n <,s3n,e3n> <,s4n,e4n> <,s5n,e5n> <,s6n,e6n> <,s7n,e7n>,
          pinchX,pinchY,damage1,damage2 <,beta> 
          <,'-degEnv',degEnvP <,degEnvN>> 
          <,'-defoLimitStates',lsD1 <$lsD2>...> 
          <,'-forceLimitStates',lsF1 <,$lsF2>...> 
          <,'-printInput'> 
          <,'-XYorder'>)

  - **Tcl interpreter**:

    .. function:: uniaxialMaterial HystereticSM $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> <$s4p $e4p> <$s5p $e5p> <$s6p $e6p> <$s7p $e7p> \
          $s1n $e1n $s2n $e2n <$s3n $e3n> <$s4n $e4n> <$s5n $e5n> <$s6n $e6n> <$s7n $e7n> \
          $pinchX $pinchY $damage1 $damage2 <$beta> \
          <-degEnv degEnvP <degEnvN>> \
          <-defoLimitStates lsD1? <lsD2?>...> \
          <-forceLimitStates lsF1? <lsF2?>...> \
          <-printInput> \
          <-XYorder>

Input Arguments:
-----------------

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
   * - $degEnvP
     - |float|
     - envelope-degredation factor. This factor works with the damage parameters to degrade the POSITIVE envelope. A positive value degrades both strength and strain values, a negative values degrades only strength. The factor is applied to points 3+ (optional, default=0.0)
   * - $degEnvN
     - |float|
     - envelope-degredation factor. This factor works with the damage parameters to degrade the NEGATIVE envelope. A positive value degrades both strength and strain values, a negative values degrades only strength. The factor is applied to points 3+ (optional, default=degEnvP, if defined, =0. otherwise)
   * - ($lsD1,$lsD2..)
     - |float|
     - list of user-defined strain/deformation limits for computing deformation DCRs (optional) 
   * - ($lsF1,$lsF2..)
     - |float|
     - list of user-defined stress/force limits for computing force DCRs (optional) 
   * - -printInput
     - |string|
     - program will output input-parameter values (optional) 
   * - -XYorder
     - |string|
     - invert backbone-envelope points to be strain-stress instead of stress-strain (optional). This flag has the same effect as using -posEnvXY and the optional -negEnvXY, so it should be used with the -posEnv and -negEnv flags.

.. note::
  * posEnv is defined using positive, INCREASING points --> strain values must be unique.
  * negEnv is defined using negative, DECREASING points --> strain values must be unique.
  * For symmetric response: do not enter -negEnv data.
  * If the last stress point is higher than the previous one, the curve will extrapolate linearly. If it is less than, the curve will extrapolate at a constant value equal to the last stress value
  * If you would like to enter strain-stress pairs use -posEnvXY (and optional -negEnvXY) instead of -posEnv (-negEnv) OR the flag XYorder.
  * The values for damage and envelope-degradation factors depend on the amplitude of your input values, so you should calibrate them.


Recorder Options:
-----------------

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

-------------------------

Backbone Curve for material:
-----------------

.. admonition:: Backbone Curve for material

  .. figure:: figures/HystereticSM/HystereticSM_backbone_Symm.jpg
      :width: 35%
      :align: left
  .. figure:: figures/HystereticSM/HystereticSM_backbone_nonSymm.jpg
      :width: 35%
      :align: right


-------------------------

Examples:
-----------------

You have endless options with this material. Here are a few demos:

-------------------------

.. admonition:: Jupyter Notebook 

  Open or download Jupyter the notebook with example of HystereticSM material, used generate the figures `CLICK HERE! <https://github.com/OpenSees/OpenSeesDocumentation/blob/master/source/user/manual/material/uniaxialMaterials/examples/HystereticSM_materialDemo.ipynb>`_

-------------------------

.. admonition:: Example Input 

  - OpenSeesPy

    .. code-block:: python

      ops.uniaxialMaterial('HystereticSM', 99,
        '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12,
        '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04,
        '-pinch', 1, 1,
        '-damage', 0.1, 0.01,
        '-beta', 0,
        '-defoLimitStates', 0.01, -0.01, 0.02, -0.02,
        '-forceLimitStates', 2772.0, -2772.0, 3104.6, -3104.6,
        '-printInput'
      )

  - Tcl Interpreter

    .. code-block:: tcl

        uniaxialMaterial HystereticSM 99 \
          -posEnv 2772.0 0.01 3104.6 0.02 1663.2 0.04 1663.2 0.06 277.2 0.08 200.0 0.1 0 0.12 \
          -negEnv -2772.0 -0.01 -3104.6 -0.02 -1663.2 -0.04 \
          -pinch 1 1 \
          -damage 0.1 0.01 \
          -beta 0 \
          -defoLimitStates 0.01 -0.01 0.02 -0.02 \
          -forceLimitStates 2772.0 -2772.0 3104.6 -3104.6 \
          -printInput

-------------------------

.. admonition:: Pinching 

  1. **pinch=[1, 1]**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99,
              '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.10, 0, 0.12,
              '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04,
              '-pinch', 1, 1
          )

    - Tcl Interpreter

      .. code-block:: tcl

          uniaxialMaterial HystereticSM 99 \
              -posEnv 2772.0 0.01 3104.6 0.02 1663.2 0.04 1663.2 0.06 277.2 0.08 200.0 0.10 0 0.12 \
              -negEnv -2772.0 -0.01 -3104.6 -0.02 -1663.2 -0.04 \
              -pinch 1 1


  2. **pinch=[0.2, 0.8]**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-pinch', 0.2, 0.8
            )

    - Tcl Interpreter

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
              -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
              -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
              -pinch  0.2  0.8

  3. **pinch=[0.8, 0.2]**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-pinch', 0.8, 0.2
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
              -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
              -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
              -pinch  0.8  0.2


  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_pinch_strainDip.jpg | .. image:: figures/HystereticSM/HystereticSM_pinch_symmCycles.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_pinch_strainOneSidedPush.jpg | .. image:: figures/HystereticSM/HystereticSM_pinch_strainOneSidedPull.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+



-------------------------

.. admonition:: Damage1 

  1. **damage1=0**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-damage', 0, 0
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0  0

  2. **damage1=0.01**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-damage', 0.01, 0
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0.01  0

  3. **damage1=0.1**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-damage', 0.1, 0
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
              -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
              -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
              -damage  0.1  0

  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_pinch_strainDip.jpg | .. image:: figures/HystereticSM/HystereticSM_damage1_symmCycles.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_damage1_strainOneSidedPush.jpg | .. image:: figures/HystereticSM/HystereticSM_damage1_strainOneSidedPull.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+



-------------------------

.. admonition:: Damage2

  1. **damage2=0**

    - OpenSeesPy  

      .. code-block:: python

        ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-damage', 0, 0
        )

    - Tcl Interpreter  

      .. code-block:: tcl

        uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0  0

  2. **damage2=0.01**

    - OpenSeesPy  

      .. code-block:: python

        ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-damage', 0, 0.01
        )

    - Tcl Interpreter  

      .. code-block:: tcl

        uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0  0.01

  3. **damage2=0.1**

    - OpenSeesPy  

      .. code-block:: python

        ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-damage', 0, 0.1
        )

    - Tcl Interpreter  

      .. code-block:: tcl

        uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0  0.1

  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_pinch_strainDip.jpg | .. image:: figures/HystereticSM/HystereticSM_damage2_symmCycles.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_damage2_strainOneSidedPush.jpg | .. image:: figures/HystereticSM/HystereticSM_damage2_strainOneSidedPull.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+

-------------------------

.. admonition:: beta

  1. **beta=0**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-beta', 0
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -beta  0

  2. **beta=0.5**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-beta', 0.5
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -beta  0.5

  3. **beta=1**

    - OpenSeesPy  

      .. code-block:: python

          ops.uniaxialMaterial('HystereticSM', 99, 
            '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
            '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
            '-beta', 1
          )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -beta  1

  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_beta_strainDip.jpg | .. image:: figures/HystereticSM/HystereticSM_beta_symmCycles.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_damage1_strainOneSidedPush.jpg | .. image:: figures/HystereticSM/HystereticSM_beta_strainOneSidedPull.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+


-------------------------

.. admonition:: degEnv

  1. **degEnv=0**

    - OpenSeesPy  

      .. code-block:: python

        ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-damage', 0.005, 0.002, 
          '-degEnv', 0, 0
        )

    - Tcl Interpreter  

      .. code-block:: tcl

        uniaxialMaterial HystereticSM  99  \
          -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
          -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
          -damage  0.005  0.002  \
          -degEnv  0  0


  2. **degEnv=1**

    - OpenSeesPy  

      .. code-block:: python

        ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-damage', 0.005, 0.002, 
          '-degEnv', 1, -1
        )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0.005  0.002  \
            -degEnv  1  -1


  3. **degEnv=5**

    - OpenSeesPy  

      .. code-block:: python

        ops.uniaxialMaterial('HystereticSM', 99, 
          '-posEnv', 2772.0, 0.01, 3104.6, 0.02, 1663.2, 0.04, 1663.2, 0.06, 277.2, 0.08, 200.0, 0.1, 0, 0.12, 
          '-negEnv', -2772.0, -0.01, -3104.6, -0.02, -1663.2, -0.04, 
          '-damage', 0.005, 0.002, 
          '-degEnv', 5, -5
        )

    - Tcl Interpreter  

      .. code-block:: tcl

          uniaxialMaterial HystereticSM  99  \
            -posEnv  2772.0  0.01  3104.6  0.02  1663.2  0.04  1663.2  0.06  277.2  0.08  200.0  0.1  0  0.12  \
            -negEnv  -2772.0  -0.01  -3104.6  -0.02  -1663.2  -0.04  \
            -damage  0.005  0.002  \
            -degEnv  5  -5


  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_beta_strainDip.jpg | .. image:: figures/HystereticSM/HystereticSM_beta_symmCycles.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+
  | .. image:: figures/HystereticSM/HystereticSM_degEnv_strainOneSidedPush.jpg | .. image:: figures/HystereticSM/HystereticSM_degEnv_strainOneSidedPull.jpg |
  |    :width: 100%                                  |    :width: 100%                                  |
  +--------------------------------------------------+--------------------------------------------------+



| HystereticSM Code Developed (2022) by: |silvia| (Silvia's Brainery)
| Original Hysteretic-Material Code Developed by: |mhs| & Filip Filippou (UC Berkeley)
