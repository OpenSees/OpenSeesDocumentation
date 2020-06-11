.. _DruckerPrager:

Drucker Prager Material
^^^^^^^^^^^^^^^^^^^^^^^

Code Developed by: |peter| and |pedro| at U.Washington.

This command is used to construct an multi dimensional material object that has a Drucker-Prager yield criterion.

.. function:: nDMaterial DruckerPrager $matTag $k $G $sigmaY $rho $rhoBar $Kinf $Ko $delta1 $delta2 $H $theta $density <$atmPressure>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |float|, integer tag identifying material
   $k, |float|,	bulk modulus
   $G, |float|, shear modulus
   $sigmaY, |float|, yield stress
   $rho, |float|, frictional strength parameter
   $rhoBar, |float|, controls evolution of plastic volume change: 0 ≤ $rhoBar ≤ $rho
   $Kinf, |float|, nonlinear isotropic strain hardening parameter: $Kinf ≥ 0
   $Ko, |float|, nonlinear isotropic strain hardening parameter: $Ko ≥ 0
   $delta1, |float|, nonlinear isotropic strain hardening parameter: $delta1 ≥ 0
   $delta2, |float|, tension softening parameter: $delta2 ≥ 0
   $H, |float|, linear strain hardening parameter: $H ≥ 0
   $theta, |float|, controls relative proportions of isotropic and kinematic hardening: 0 ≤ $theta ≤ 1
   $density, |float|, mass density of the material
   <$atmPressure>, |float|, optional atmospheric pressure for update of elastic bulk and shear moduli (default = 101 kPa)

.. note::

   The material formulations for the Drucker-Prager object are "ThreeDimensional" and "PlaneStrain"

The yield condition for the Drucker-Prager model can be expressed as

.. math:: 

   f\left(\mathbf{\sigma}, q^{iso}, \mathbf{q}^{kin}\right) = \left\| \mathbf{s} + \mathbf{q}^{kin} \right\| + \rho I_1 + \sqrt{\frac{2}{3}} q^{iso} - \sqrt{\frac{2}{3}} \sigma_Y^{} \leq 0


in which

.. math:: 

   \mathbf{s} = \mathrm{dev} (\mathbf{\sigma}) = \mathbf{\sigma} - \frac{1}{3} I_1 \mathbf{1}

is the deviatoric stress tensor,

.. math:: 

   I_1 = \mathrm{tr}(\mathbf{\sigma})


is the first invariant of the stress tensor, and the parameters .. math::\rho_{}^{}</math> and .. math::\sigma_Y^{}</math> are positive material constants.

The isotropic hardening stress is defined as

.. math:: 
   
   q^{iso} = \theta H \alpha^{iso} + (K_{\infty} - K_o) \exp(-\delta_1 \alpha^{iso})


The kinematic hardening stress (or back-stress) is defined as

.. math:: 

   \mathbf{q}^{kin} = -(1 - \theta) \frac{2}{3} H \mathbb{I}^{dev} : \mathbf{\alpha}^{kin}


The yield condition for the tension cutoff yield surface is defined as

.. math:: 

   f_2(\mathbf{\sigma}, q^{ten}) = I_1 + q^{ten} \leq 0

where

.. math:: 

   q^{ten} = T_o \exp(-\delta_2^{} \alpha^{ten})


and

.. math:: 

   T_o = \sqrt{\frac{2}{3}} \frac{\sigma_Y}{\rho}


Further, general, information on theory for the Drucker-Prager yield criterion can be found at wikipedia here

.. note::

   The valid queries to the Drucker-Prager material when creating an ElementRecorder are 'strain' and 'stress' (as with all nDmaterial) as well as 'state'. The query 'state' records a vector of state variables during a particular analysis. The columns of this vector are as follows. (Note: If the option '-time' is included in the creation of the recorder, the first column will be the time variable for each recorded point and the columns below are shifted accordingly.)

   Column 1 - First invariant of the stress tensor, :math:`I_1 = \mathrm{tr}(\mathbf{\sigma})`.
   Column 2 - The following tensor norm, :math:`\left\| \mathbf{s} + \mathbf{q}^{kin} \right\| `, where .. math::\mathbf{s}` is the deviatoric stress tensor and :math:`\mathbf{q}^{kin}` is the back-stress tensor.
   Column 3 - First invariant of the plastic strain tensor, :math:`\mathrm{tr}(\mathbf{\varepsilon}^p) `.
   Column 4 - Norm of the deviatoric plastic strain tensor, :math:`\left\| \mathbf{e}^p \right\| `.

   The Drucker-Prager strength parameters :math:`\rho ` and :math:`\sigma_Y ` can be related to the Mohr-Coulomb friction angle, :math:`\phi `, and cohesive intercept, :math:`c`, by evaluating the yield surfaces in a deviatoric plane as described by Chen and Saleeb (1994). By relating the two yield surfaces in triaxial compression, the following expressions are determined

   .. math:: 

      \rho = \frac{2 \sqrt{2} \sin \phi}{\sqrt{3} (3 - \sin \phi)}

   .. math::
   
	\sigma_Y = \frac{6 c \cos \phi}{\sqrt{2} (3 - \sin \phi)}

.. [Drucker-Prager1952] Drucker, D. C. and Prager, W., "Soil mechanics and plastic analysis for limit design." Quarterly of Applied Mathematics, vol. 10, no. 2, pp. 157–165, 1952.

.. [Chen-Saleeb1994] Chen, W. F. and Saleeb, A. F., Constitutive Equations for Engineering Materials Volume I: Elasticity and Modeling. Elsevier Science B.V., Amsterdam, 1994.

.. admonition:: Example

   This example provides the input file and corresponding results for a confined triaxial compression (CTC) test using a single 8-node brick element and the Drucker-Prager constitutive model. A schematic representation of this test is shown below, (a) depicts the application of hydrostatic pressure, and (b) depicts the application of the deviator stress. Also shown is the stress path resulting from this test plotted on the meridian plane. As shown, the element is loaded until failure, at which point the model can no longer converge, as this is a stress-controlled analysis.

   .. figure:: DruckerPrager.png
	:align: center
	:width: 800px
	:figclass: align-center

	Drucker Prager Example

   .. literalinclude:: DruckerPragerExample.tcl
      :language: tcl

