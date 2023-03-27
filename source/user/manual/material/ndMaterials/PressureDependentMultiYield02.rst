.. _PressureDependentMultiYield02:

Pressure Dependent Multi Yield 02
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PressureDependMultiYield02** material is modified from ``PressureDependMultiYield`` material, with: 

1. Additional parameters ($contrac3 and $dilat3) to account for Kσ effect,
2. a parameter to account for the influence of previous dilation history on subsequent contraction phase ($contrac2), and
3. modified logic related to permanent shear strain accumulation ($liquefac1 and $liquefac2).

The command to generate such a material

.. admonition:: TCL command:

   nDMaterial PressureDependMultiYield02 $tag $nd $rho $refShearModul $refBulkModul $frictionAng $peakShearStra $refPress $pressDependCoe $PTAng $contrac1 $contrac3 $dilat1 $dilat3 <$noYieldSurf=20 <$r1 $Gs1 …> $contrac2=5. $dilat2=3. $liquefac1=1. $liquefac2=0. $e=0.6 $cs1=0.9 $cs2=0.02 $cs3=0.7 $pa=101 <$c=0.1>>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 1, 1, 98

   tag, |integer|, "A positive integer uniquely identifying the material among all nDMaterials."
   nd, |integer|, "Number of dimensions, 2 for plane-strain, and 3 for 3D analysis."
   rho, |float|, "Saturated soil mass density."
   refShearModul (Gr), |float|, "Reference low-strain shear modulus, specified at a reference mean effective confining pressure refPress of p’r."
   refBulkModul (Br), |float|, "Reference bulk modulus, specified at a reference mean effective confining pressure refPress of p’r."
   frictionAng (Φ), |float|, "Friction angle at peak shear strength, in degrees."
   peakShearStra (γmax), |float|, "An octahedral shear strain at which the maximum shear strength is reached, specified at a reference mean effective confining pressure refPress of p’r."
   refPress (p’r), |float|, "Reference mean effective confining pressure at which Gr, Br, and γmax are defined."
   pressDependCoe (d), |float|, "A positive constant defining variations of G and B as a function of instantaneous effective confinement p’"
   PTAng (ΦPT), |float|, "Phase transformation angle, in degrees."
   contrac1 $contrac2, |float|, "A non-negative constant defining the rate of shear-induced volume decrease (contraction) or pore pressure buildup. A larger value corresponds to faster contraction rate."
   contrac3, |float|, "A non-negative constant reflecting Kσ effect."
   dilat1 $dilat2, |float|, "Non-negative constants defining the rate of shear-induced volume increase (dilation). Larger values correspond to stronger dilation rate."
   dilat3, |float|, "A non-negative constant reflecting Kσ effect."
   noYieldSurf, |float|, "Number of yield surfaces, optional (must be less than 40, default is 20). The surfaces are generated based on the hyperbolic relation."
   r Gs, |float|, "Instead of automatic surfaces generation (Note 2), you can define yield surfaces directly based on desired shear modulus reduction curve. To do so, add a minus sign in front of noYieldSurf, then provide noYieldSurf pairs of shear strain (γ) and modulus ratio (Gs) values. For example, to define 10 surfaces: … -10γ1Gs1 … γ10Gs10 …"
   liquefac1, |float|, "Damage parameter to define accumulated permanent shear strain as a function of dilation history. (Redefined and different from PressureDependMultiYield material)."
   liquefac2, |float|, "Damage parameter to define biased accumulation of permanent shear strain as a function of load reversal history. (Redefined and different from PressureDependMultiYield material)."
   e, |float|, "Initial void ratio, optional (default is 0.6)."
   cs1 cs2 cs3 $pa, |float|, "Parameters defining a straight critical-state line ec in e-p’ space. (default values: cs1=0.9, cs2=0.02, cs3=0.7, pa =101 kPa)."
   c, |float|, "Numerical constant (default value = 0.3 kPa)"

.. admonition:: Recorder queries and Outputs
   The following information may be extracted for this material at a given integration point, using the OpenSees Element Recorder facility ``stress``, ``strain``, ``backbone``, or ``tangent``.

   * For 2D problems, the stress output follows this order: :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\sigma_{zz}`, :math:`\sigma_{xy}`, :math:`\eta_r`, where :math:`\eta_r` is the ratio between the shear (deviatoric) stress and peak shear strength at the current confinement :math:`(0<=\eta_r<=1.0)`. The strain output follows this order: :math:`\epsilon_{xx}`, :math:`\epsilon_{yy}`, :math:`\epsilon_{xy}`
   
   * For 3D problems, the stress output follows this order: :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\sigma_{zz}`, :math:`\sigma_{xy}`,:math:`\sigma_{yz}`, :math:`\sigma_{zx}`, :math:`\eta_r` and the strain output follows this order: :math:`\epsilon_{xx}`, :math:`\epsilon_{yy}`, :math:`\epsilon_{zz}`, :math:`\gamma_{xy}`, :math:`\gamma_{yz}`, :math:`\gamma_{zx}`

   *  The ``backbone"`` option records (secant) shear modulus reduction curves at one or more given confinements. The specific recorder command is as follows:
   .. code::
      recorder Element –ele $eleNum -file $fName -dT $deltaT material $GaussNum backbone $p1 <$p2 …>

   where p1, p2, … are the confinements at which modulus reduction curves are recorded. In the output file, corresponding to each given confinement there are two columns: shear strain γ and secant modulus Gs. The number of rows equals the number of yield surfaces.
   
   * Elastic or Elastoplastic response could be enforced by:
   .. code::
   
      Elastic:   updateMaterialStage -material $tag -stage 0
      Elastoplastic:	updateMaterialStage -material $tag -stage 1


**SUGGESTED PARAMETER VALUES**

.. csv-table:: 
   :header: "Parameters","Dr=30%", "Dr=40%", "Dr=50%", "Dr=60%", "Dr=75%"
   :widths: 1, 1, 1, 1, 1, 1
   
   rho, "1.7 ton/m3", "1.8 ton/m3", "1.9 ton/m3", "2.0 ton/m3", "2.1 ton/m3"
   "refShearModul (at p’r=80 kPa)", "6.0x104 kPa", "9.0x104 kPa", "10.0x104 kPa", "11.0x104 kPa", "13.0x104 kPa"
   "refBulkModu (at p’r=80 kPa)", "16.0x104 kPa (Ko=0.5)", "22.0x104 kPa (Ko=0.47)", "23.3x104 kPa (Ko=0.45)", "24.0x104 kPa (Ko=0.43)", "26.0x104 kPa (Ko=0.4)"
   frictionAng,  31, 32, 33.5, 35, 36.5
   PTAng,  31, 26, 25.5, 26, 26
   "peakShearStra (at p’r=101 kPa or 14.65 psi)", "0.1", "0.1", "0.1", "0.1", "0.1"
   "refPress (p’r)", "101 kPa", "101 kPa", "101 kPa", "101 kPa", "101 kPa"
   pressDependCoe, 0.5, 0.5, 0.5, 0.5, 0.5
   contrac1, 0.087, 0.067, 0.045, 0.028, 0.013
   contrac3, 0.18, 0.23, 0.15, 0.05, 0.0
   dilat1, 0.0, 0.06, 0.06, 0.1, 0.3
   dilat3, 0.0, 0.27, 0.15, 0.05, 0.0
   e, 0.85, 0.77, 0.7, 0.65, 0.55

**Pressure Dependent Multi Yield 02 Examples**

.. csv-table:: 
   :header: "Description","Tcl"
   :widths: 1, 1

   "Single 2D 9-4 noded element, subjected to sinusoidal base shaking (PressureDepend02 material)", `Example 1 <https://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02-Example_1>`_
   "Single 3D brick element, subjected to sinusoidal base shaking (PressureDepend02 material)", `Example 2 <https://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02-Example_2>`_
   "Single 3D 20-8 noded element, subjected to sinusoidal base shaking (PressureDepend02 material)", `Example 3 <https://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02-Example_3>`_

Code Developed by: UC San Diego (**Dr. Zhaohui Yang**), Github Documentation collected by: `A. Najafi <https://najafice.github.io>`_
