.. _Hysteretic:

Hysteretic Material
^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial hysteretic material object with pinching of force and deformation, damage due to ductility and energy, and degraded unloading stiffness based on ductility. The backbone can be either bilinear or trilinear.

.. function:: uniaxialMaterial Hysteretic $matTag $s1p $e1p $s2p $e2p <$s3p $e3p> $s1n $e1n $s2n $e2n <$s3n $e3n> $pinchX $pinchY $damage1 $damage2 <$beta> 

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
   * - $s1n $e1n 
     - |float|
     - stress and strain (or force & deformation) at first point of the envelope in the negative direction 
   * - $s2n $e2n
     - |float|
     - stress and strain (or force & deformation) at second point of the envelope in the negative direction
   * - $s3n $e3n 
     - |float|
     - stress and strain (or force & deformation) at third point of the envelope in the negative direction (optional) 
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

Code Developed by: |Michael Scott (Oregon State University) & Filip Filippou (UC Berkeley)|
