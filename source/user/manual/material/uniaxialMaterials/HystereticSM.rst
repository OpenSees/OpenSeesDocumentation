.. _HystereticSM:

HystereticSM Material
^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial multilinear hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. This material is an extension of the Hysteretic Material -- the envelope can be defined by up to 7 points, while the original one only had 3

.. function:: uniaxialMaterial Hysteretic $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> <$s4p $e4p> <$s5p $e5p> <$s6p $e6p> <$s7p $e7p> $s1n $e1n $s2n $e2n <$s3n $e3n> <$s4n $e4n> <$s5n $e5n> <$s6n $e6n> <$s7n $e7n> $pinchX $pinchY $damage1 $damage2 <$beta> 

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
   * - ($s4p $e4p .... $s7p $e8p)
     - |float| 
     - stress and strain (or force & deformation) at 4th-7th points of the envelope in the positive direction (optional). NOTE: sress/force values can only be constant or decrease in absolute value (same or less positive) from one point to the next. 
   * - $s1n $e1n 
     - |float|
     - stress and strain (or force & deformation) at first point of the envelope in the negative direction 
   * - $s2n $e2n
     - |float|
     - stress and strain (or force & deformation) at second point of the envelope in the negative direction
   * - $$s3n $e3n 
     - |float|
     - stress and strain (or force & deformation) at third point of the envelope in the negative direction (optional) 
   * - ($s4n $e4n .... $s7n $e8n)
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

Modified Code Developed by: |Silvia Mazzoni (Silvia's Brainery)|
Code Developed by: |Michael Scott (Oregon State University) & Filip Filippou (UC Berkeley)|