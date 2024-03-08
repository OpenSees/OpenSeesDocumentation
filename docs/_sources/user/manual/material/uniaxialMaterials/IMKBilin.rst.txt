
.. IMKBilin:

IMKBilin Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a material with a hysteretic bilinear response based on the modified Ibarra-Medina-Krawinkler deterioration model.

.. function:: uniaxialMaterial IMKBilin $matTag $Ke $dp_pos $dpc_pos $du_pos $Fy_pos $FmaxFy_pos $FresFy_pos $dp_neg $dpc_neg $du_neg $Fy_neg $FmaxFy_neg $FresFy_neg $Lamda_S $Lamda_C $Lamda_K $c_S $c_C $c_K $D_pos $D_neg

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|,	    integer tag identifying material
   $Ke, |float|,  Elastic stiffness
   $dp_pos, |float|,  Pre-capping deformation in positive loading direction
   $dpc_pos, |float|,  Post-capping deformation in positive loading direction
   $du_pos, |float|,  Ultimate deformation in positive loading direction
   $Fy_pos, |float|,  Yield strength in positive loading direction
   $FmaxFy_pos, |float|,  Maximum-to-yield strength ratio in positive loading direction
   $FresFy_pos, |float|,  Residual-to-yield strength ratio in positive loading direction
   $dp_neg, |float|,  Pre-capping deformation in negative loading direction
   $dpc_neg, |float|,  Post-capping deformation in negative loading direction
   $du_neg, |float|,  Ultimate deformation in negative loading direction
   $Fy_neg, |float|,  Yield strength in negative loading direction
   $FmaxFy_neg, |float|,  Maximum-to-yield strength ratio in negative loading direction
   $FresFy_neg, |float|,  Residual-to-yield strength ratio in negative loading direction
   $Lamda_S, |float|,  Cyclic deterioration parameter for yield strength deterioration
   $Lamda_C, |float|,  Cyclic deterioration parameter for post-capping stiffness deterioration
   $Lamda_K, |float|,  Cyclic deterioration parameter for unloading stiffness deterioration
   $c_S, |float|,  Rate of yield strength deterioration
   $c_C, |float|,  Rate of post-capping stiffness deterioration
   $c_K, |float|,  Rate of unloading stiffness deterioration
   $D_pos, |float|,  rate of cyclic deterioration in the positive loading direction. This parameter is used to create asymmetric hysteretic behavior as in the case of a composite beam (0< D_pos <1). For symmetric hysteretic response use 1.0.
   $D_neg, |float|,  rate of cyclic deterioration in the negative loading direction. This parameter is used to create asymmetric hysteretic behavior as in the case of a composite beam (0< D_pos <1). For symmetric hysteretic response use 1.0.

.. note::

   All material model parameters (in both the positive and negative direction) shall be specified as positive values.

   Lamda is used to compute the reference energy based on the following equation Ref_Energy = Lamda * Fy

.. _fig-IMKBilin:

.. figure:: figures/IMK/IMKBilin.jpg
	:align: center
	:figclass: align-center

	IMKBilin backbone curve

.. figure:: figures/IMK/IMKBilin_sample_response.jpg
	:align: center
	:figclass: align-center
	
	IMKBilin sample response

.. admonition:: Example 

   The following is used to construct a IMKBilin material with symmetric hysteretic response.

   .. code-block:: tcl

      set Ke 	  10000.;
      set dp 	  0.01;
      set dpc     0.05;
      set du 	  0.08;
      set My 	  100.;
      set Mc_My   1.10;
      set Mres_My 0.10;
      set lambda  0.50;
      set c_S 	  1.00;
      set c_C 	  1.00; 
      set c_K 	  1.00; 
      set c_A 	  1.00;
      set D_pos   1.00;
      set D_neg   1.00;

      uniaxialMaterial IMKBilin  1 $Ke $dp $dpc $du $My $Mc_My $Mres_My $dp $dpc $du $My $Mc_My $Mres_My $lambda $lambda $lambda $c_S $c_S $c_K $D_pos $D_neg;

References:
===========

- Model rules:

Ibarra, L. F., Medina, R. A., and Krawinkler, H. (2005). "*Hysteretic models that incorporate strength and stiffness deterioration.*" Earthquake Engineering & Structural Dynamics, 34(12), 1489-1511, DOI: https://doi.org/10.1002/eqe.495.

- Model parameters for steel beams as part of rigid beam-to-column connections:

Lignos, D. G., and Krawinkler, H. (2011). "*Deterioration modeling of steel components in support of collapse prediction of steel moment frames under earthquake loading.*" Journal of Structural Engineering, 137(11), 1291-1302, DOI: https://doi.org/10.1061/(ASCE)ST.1943-541X.0000376.

- Model parameters for steel beam-columns:

Lignos, D. G., Hartloper, A., Elkady, A., Deierlein, G. G., and Hamburger, R. (2019). "*Proposed updates to the asce 41 nonlinear modeling parameters for wide-flange steel columns in support of performance-based seismic engineering.*" Journal of Structural Engineering, 145(9), 04019083, DOI: https://doi.org/10.1061/(ASCE)ST.1943-541X.0002353.

Code inquiry or bug reporting 
==========

- Kazuki Ichinohe, University of Tokyo, e-mail: z-ichinohe@g.ecc.u-tokyo.ac.jp

- Ahmed Elkady, University of Southampton, e-mail: a.elkady@soton.ac.uk
