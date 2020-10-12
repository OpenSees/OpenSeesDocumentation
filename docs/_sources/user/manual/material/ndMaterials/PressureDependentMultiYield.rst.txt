.. _PressureDependentMultiYield:

Pressure Dependent Multi Yield
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Code Developed by: UC San Diego (**Dr. Zhaohui Yang**):

**PressureDependMultiYield** material is an elastic-plastic material for simulating the essential response characteristics of pressure sensitive soil materials under general loading conditions. Such characteristics include dilatancy (shear-induced volume contraction or dilation) and non-flow liquefaction (cyclic mobility), typically exhibited in sands or silts during monotonic or cyclic loading.

When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. To simulate soil response under fully undrained condition, this material may be either embedded in a FluidSolidPorousMaterial, or used with one of the solid-fluid fully coupled elements (Four Node Quad u-p Element, Nine Four Node Quad u-p Element, Brick u-p Element, Twenty Eight Node Brick u-p Element) with very low permeability. To simulate partially drained soil response, this material should be used with a solid-fluid fully coupled element with proper permeability values.

During the application of gravity load (and static loads if any), material behavior is linear elastic. In the subsequent dynamic (fast) loading phase(s), the stress-strain response is elastic-plastic (see updateMaterialStage). Plasticity is formulated based on the multi-surface (nested surfaces) concept, with a non-associative flow rule to reproduce dilatancy effect. The yield surfaces are of the Drucker-Prager type.

The command to generate such a material

.. admonition:: function

   nDMaterial PressureDependMultiYield $tag $nd $rho $refShearModul $refBulkModul $frictionAng $peakShearStra $refPress $pressDependCoe $PTAng $contrac $dilat1 $dilat2 $liquefac1 $liquefac2 $liquefac3 <$noYieldSurf=20 <$r1 $Gs1 …> $e=0.6 $cs1=0.9 $cs2=0.02 $cs3=0.7 $pa=101 <$c=0.3>>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 1, 1, 98

   $tag, |integer|,"A positive integer uniquely identifying the material among all nDMaterials."
   $nd, |integer|, "Number of dimensions, 2 for plane-strain, and 3 for 3D analysis."
   $rho, |float|, "Saturated soil mass density."
   $refShearModul (Gr), |float|, "Reference low-strain shear modulus, specified at a reference mean effective confining pressure refPress of p’r (see below)"
   $refBulkModul (Br), |float|, "Reference bulk modulus, specified at a reference mean effective confining pressure refPress of p’r (see below)."
   $frictionAng (Φ), |float|, "Friction angle at peak shear strength, in degrees."
   $peakShearStra (γmax), |float|,"An octahedral shear strain at which the maximum shear strength is reached, specified at a reference mean effective confining pressure refPress of p’r (see below)."
   $refPress (p’r), |float|, "Reference mean effective confining pressure at which Gr, Br, and γmax are defined."
   $pressDependCoe (d), |float|, "A positive constant defining variations of G and B as a function of instantaneous effective confinement p’:"
   $PTAng (ΦPT), |float|, "Phase transformation angle, in degrees."
   $contrac, |float|, "A non-negative constant defining the rate of shear-induced volume decrease (contraction) or pore pressure buildup. A larger value corresponds to faster contraction rate."
   $dilat1 $dilat2, |float|, "Non-negative constants defining the rate of shear-induced volume increase (dilation). Larger values correspond to stronger dilation rate."
   $liquefac1 $liquefac2 $liquefac3, |float|, "Parameters controlling the mechanism of liquefaction-induced perfectly plastic shear strain accumulation, i.e., cyclic mobility. Set liquefac1 = 0 to deactivate this mechanism altogether."
   $noYieldSurf, |float|,	"Number of yield surfaces, optional (must be less than 40, default is 20). The surfaces are generated based on the hyperbolic relation defined in Note 2 below."
   $r $Gs, |float|, "Instead of automatic surfaces generation (Note 2), you can define yield surfaces directly based on desired shear modulus reduction curve. To do so, add a minus sign in front of noYieldSurf, then provide noYieldSurf pairs of shear strain (γ) and modulus ratio (Gs) values. For example, to define 10 surfaces: … -10γ1Gs1 … γ10Gs10 … (See Note 3 below)"
   $e, |float|, " Initial void ratio, optional (default is 0.6)."
   $cs1 $cs2 $cs3 $pa, |float|, "Parameters defining a straight critical-state line ec in e-p’ space. (default values: cs1=0.9, cs2=0.02, cs3=0.7, pa =101 kPa). See note 6 below."
   $c, |float|, "Numerical constant (default value = 0.3 kPa)"

.. note::

   1. Octahedral shear strain is defined as:

   .. math::

      \gamma = \frac{2}{3} \left [ (\epsilon_{xx} - \epsilon_{yy})^2 + (\epsilon_{yy} - \epsilon_{zz})^2 + (\epsilon_{xx} - \epsilon_{zz})^2 + 6 \epsilon_{xy}^2 + 6 \epsilon_{yz}^2 + 6 \epsilon_{xz}^2 \right] ^ {1/2}


   2. **$presDependCoef d** defines variations of G and B as a function of instantaneous effective confinement :math:p^t as follows:

   .. math::

      G = G_r \left ( \frac{p^t}{{p^t}_r} \right)^d

      B = B_r \left ( \frac{p^t}{{p^t}_r} \right)^d

   3. The friction angle :math:`\phi` and cohesion c define the variation of peak (octahedral) shear strength :math:`\tau_f` as a function of current effective confinement :math:`{p^t}_i`:

   .. math::

      \tau_f = \frac{2 \sqrt{2} sin \phi}{3 - sin \phi}{p^t}_i + \frac{2 \sqrt{2}}{3}c

   4. Automatic surface generation: at a constant confinement :math:`p^t`, the shear stress :math:`\tau` (octahedral) - shear strain :math:`\gamma` (octahedral) nonlinearity is defined by a hyperbolic curve (backbone curve):

   .. math::

      \tau = \frac{G \gamma}{1 + \frac{\gamma}{\gamma_r}\left ( \frac{{p^t}_r}{p^t} \right)^d}

   where :math:`\gamma_r` satisfies the following equation at :math:`{p^t}_r`

   .. math::

      \tau_f = \frac{2 \sqrt{2} sin \phi}{3 - sin \phi}{p^t}_r + \frac{2 \sqrt{2}}{3}c = \frac{G_r \gamma_{max}}{1 + \gamma_{max}/\gamma_r}

   5. (User defined surfaces) The user specified friction angle :math:`\phi = 0`. cohesion c will be ignored. Instead, c is defined by :math:`c=\sqrt 3 \sigma_m / 2`, where :math:`\sigma_m` is the product of the last modulus and strain pair in the modulus reduction curve. Therefore, it is important to adjust the backbone curve so as to render an appropriate c.

   If the user specifies :math:`\gamma` > 0, this :math:`\phi` will be ignored. Instead, :math:`\phi` is defined as follows:

   .. math::

      sin \phi = \frac{3 (\sqrt 3 \sigma_m - 2c)/{p^t}_r}{6 + (\sqrt 3 \sigma_m - 2c)/{p^t}_r}


   If the resulting :math:`\phi <0`, we set :math:`\phi =0` and :math:`c=\sqrt 3 \sigma_m/2`.

   Also remember that improper modulus reduction curves can result in strain softening response (negative tangent shear modulus), which is not allowed in the current model formulation. Finally, note that the backbone curve varies with confinement, although the variation is small within commonly interested confinement ranges. Backbone curves at different confinements can be obtained using the OpenSees element recorder facility

   4. The last five optional parameters are needed when critical-state response (flow liquefaction) is anticipated. Upon reaching the critical-state line, material dilatancy is set to zero.

   5. $liquefac1 defines the effective confining pressure (e.g., 10 kPa in SI units or 1.45 psi in English units) below which the mechanism is in effect. Smaller values should be assigned to denser sands. Liquefac2 defines the maximum amount of perfectly plastic shear strain developed at zero effective confinement during each loading phase. Smaller values should be assigned to denser sands. Liquefac3 defines the maximum amount of biased perfectly plastic shear strain γb accumulated at each loading phase under biased shear loading conditions, as γb=liquefac2 x liquefac3. Typically, liquefac3 takes a value between 0.0 and 3.0. Smaller values should be assigned to denser sands. See the references listed at the end of this chapter for more information."

   6. $cs1, $cs2, $cs3 and $pa

   .. code::

      if cs3=0, 
      	 ec = cs1-cs2 log(p'/pa)
      else (Li and Wang, JGGE, 124(12)),
      	  ec = cs1-cs2(p'/pa)cs3

   where pa is atmospheric pressure for normalization (typically 101 kPa in SI units, or 14.65 psi in English units). 

   7. **OUTPUT** The following information may be extracted for this material at a given integration point, using the OpenSees Element Recorder facility "stress", "strain", "backbone", or "tangent".

      * For 2D problems, the stress output follows this order: :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\sigma_{zz}`, :math:`\sigma_{xy}`,:math:`\eta_r`, where :math:`\eta_r` is the ratio between the shear (deviatoric) stress and peak shear strength at the current confinement :math:`(0<=\eta_r<=1.0)`. The strain output follows this order: :math:`\epsilon_{xx}`, :math:`\epsilon_{yy}`, :math:`\epsilon_{xy}`
   
      * For 3D problems, the stress output follows this order: :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, :math:`\sigma_{zz}`, :math:`\sigma_{xy}`,:math:`\sigma_{yz}`, :math:`\sigma_{zx}`, :math:`\eta_r` and the strain output follows this order: :math:`\epsilon_{xx}`, :math:`\epsilon_{yy}`, :math:`\epsilon_{zz}`, :math:`\gamma_{xy}`, :math:`\gamma_{yz}`, :math:`\gamma_{zx}`

      *  The "backbone" option records (secant) shear modulus reduction curves at one or more given confinements. The specific recorder command is as follows:

   .. code::

      recorder Element –ele $eleNum -file $fName -dT $deltaT material $GaussNum backbone $p1 <$p2 …>

   where p1, p2, … are the confinements at which modulus reduction curves are recorded. In the output file, corresponding to each given confinement there are two columns: shear strain γ and secant modulus Gs. The number of rows equals the number of yield surfaces.


** SUGGESTED PARAMETER VALUES **

.. csv-table:: 
   :header: "Parameters","Loose Sand (15%-35%)", "Medium Sand (35%-65%)", "Medium-dense Sand (65%-85%)", "Dense Sand (85%-100%)"
   :widths: 1, 1, 1, 1, 1
   
   rho, "1.7 ton/m3 or 1.59x10-4 (lbf)(s2)/in4", "1.9 ton/m3 or 1.778x10-4 (lbf)(s2)/in4", "2.0 ton/m3 or 1.872x10-4 (lbf)(s2)/in4", "2.1 ton/m3 or 1.965x10-4 (lbf)(s2)/in4"
   "refShearModul (at p’r=80 kPa or 11.6 psi)", "5.5x104 kPa or 7.977x103 psi", "7.5x104 kPa or 1.088x104 psi", "1.0x105 kPa or 1.45x104 psi", "1.3x105 kPa or 1.885x104 psi"
   "refBulkModu (at p’r=80 kPa or 11.6 psi)", "1.5x105 kPa or 2.176x104 psi", "2.0x105 kPa or 2.9x104 psi", "3.0x105 kPa or 4.351x104 psi", "3.9x105 kPa or 5.656x104 psi"
   frictionAng,  29,	 33,	37,  40
   "refPress (p’r)", "80 kPa or 11.6 psi", "80 kPa or 11.6 psi", "80 kPa or 11.6 psi", "80 kPa or 11.6 psi"
   pressDependCoe,	  0.5, 0.5, 0.5,	  0.5
   PTAng,		  29 ,  27,   27,		  27
   contrac,		  0.21, 0.07, 0.05,	  0.03
   dilat1,		  0.,   0.4,  0.6,		  0.8
   dilat2,		  0 ,   2,    3,		  5
   "liquefac1","10 kPa or 1.45 psi", "10 kPa or 1.45 psi", "5 kPa or 0.725 psi", 0
   liquefac2,	0.02,   0.01, 0.003, 0
   liquefac3,	1,      1,    1,	  0
   e,		0.85,   0.7,  0.55,  0.45

** Pressure Dependent Multi Yield Examples **

.. csv-table:: 
   :header: "Description","Tcl","Python"
   :widths: 1, 1, 1

   "Single 2D plane-strain quadrilateral element, subjected to sinusoidal base shaking", ,
   "Single 2D quadrilateral element, subjected to monotonic pushover", ,
