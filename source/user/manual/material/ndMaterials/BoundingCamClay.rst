.. _BoundingCamClay:

Bounding Cam Clay
^^^^^^^^^^^^^^^^^

Code Developed by: |chris| and |pedro| U.Washington

This command is used to construct a multi-dimensional bounding surface Cam Clay material object after Borja et al. ([Borja2001]_).

.. function::

   nDMaterial BoundingCamClay $matTag $massDensity $C $bulkMod $OCR $mu_o $alpha $lambda $h $m



.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, tag identifying material
   $massDensity, |float|, mass density
   $C, |float|,	ellipsoidal axis ratio (defines shape of ellipsoidal loading/bounding surfaces)
   $bulkMod, |float|, initial bulk modulus
   $OCR, |float|, overconsolidation ratio
   $mu_o, |float|, initial shear modulus
   $alpha, |float|, pressure-dependency parameter for moduli (greater than or equal to zero)
   $lambda, |float|, soil compressibility index for virgin loading
   $h, |float|, hardening parameter for plastic response inside of bounding surface 
   $m, |float|,	hardening parameter (exponent) for plastic response inside of bounding surface 

.. note::
   
   The material formulations for the BoundingCamClay object are "ThreeDimensional" and "PlaneStrain"

   If h = 0, no hardening

   If m = 0, only linear hardening

* General Information

This nDMaterial object provides the bounding surface plasticity model of Borja et al. (2001) in which the bounding surface model is represented using modified Cam-Clay theory (Schofield and Wroth 1968). In addition to the standard capabilities of the Cam-Clay family of models (e.g., pressure dependence, hardening with plastic volumetric contraction, softening with plastic dilation, and coupled deviatoric and volumetric plastic deformation), the Borja et al. (2001) model has been enhanced to include an anisotropic bounding surface formulation that allows for consideration of hysteretic behaviour under cyclic loading. This bounding surface Cam-Clay model is coupled with a nonlinear hyperelastic model that considered pressure-dependency in the bulk and shear modulus. The full theory of this model is discussed in great detail in Borja et al. (2001).

.. note::

   * The ellipsoidal axis ratio parameter $C is defined such that the ellipsoidal surfaces are C times as wide in the deviatoric direction as they are along the hydrostatic axis. When $C = 1, the surfaces are spherical.

   * The overconsolidation ratio (input parameter $OCR) defines the relationship between the loading surface and bounding surface. The radius of the bounding surface, R, is equal to the product of the OCR and the radius of the loading surface, r. When the soil is normally consolidated and $OCR = 1, the bounding and loading surfaces are coincident and virgin loading will occur.

   * When the hyperelastic pressure-dependency parameter (input parameter $alpha) is set to zero, the elastic shear modulus will be constant with a value equal to the initial shear modulus (input parameter $mu_o) and the deviatoric and volumetric responses are uncoupled in the elastic regime.

   * The virgin compressibility parameter (input parameter $lambda) describes the relationship between the specific volume v = 1 + e and the logarithm of the mean effective stress (where e is the void ratio). This is is related to the compression index C_c that describes the relationship between the void ratio and the logarithm of the mean effective stress in consolidation testing.

.. admonition:: Example

   The following usage example provides the input parameters used in the single element examples of Borja et al. (2001). The initial bulk modulus is determined from the initial mean stress desired in the test (in this case p = 100 kPa) divided by the recompressibilty index kappa = 0.018. The units of this analysis are kN and m, thus the prescribed initial shear modulus of 5.4 MPa is input as 5400 kPa. The hardening parameter $h has the same units as the moduli.

   .. code:: tcl

      # define parameters for the model
      set rho    1.8
      set c      1.0
      set bulk   5555.56
      set OCR    1.5
      set mu_o   5.4e3
      set alpha  0.0
      set lambda 0.13
      set h      5.0e3
      set m      1.5
      nDMaterial BoundingCamClay 1  $rho $c $bulk $OCR $mu_o $alpha $lambda $h $m

.. [Borja2001] Borja, R.I., Lin, C.-H., and Montans, F.J. (2001) 'Cam-Clay plasticity, Part IV: Implicit integration of anisotropic bounding surface model with nonlinear hyperelasticity and ellipsoidal loading function,' Computer Methods in Applied Mechanics and Engineering, 190(26), 3293-3323, doi: 10.1016/S0045-7825(00)00301-7.

.. [Schofied-Wroth1968] Schofield, A. and Wroth, P. (1968) Critical State Soil Mechanics, McGraw Hill, New York.
