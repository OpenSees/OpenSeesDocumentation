
.. IMKBilin:

IMKBilin Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a material with a hysteretic bilinear response based on the modified Ibarra-Medina-Krawinkler deterioration model.

.. function:: uniaxialMaterial IMKBilin $matTag $Ke $Up_pos $Upc_pos $Uu_pos $Fy_pos $FmaxFy_pos $FresFy_pos $Up_neg $Upc_neg $Uu_neg $Fy_neg $FmaxFy_neg $FresFy_neg $Lamda_S $Lamda_C $Lamda_K $c_S $c_C $c_K $D_pos $D_neg

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

.. [IbarraEtAl2005] Ibarra, L. F., Medina, R. A., and Krawinkler, H. (2005). "Hysteretic models that incorporate strength and stiffness deterioration." Earthquake Engineering & Structural Dynamics, 34(12), 1489-1511, Doi: 10.1002/eqe.495.


.. _fig-IMKBilin:

	IMKBilin backbone curve

.. figure:: figures/IMKBilin.jpg
	:align: center
	:figclass: align-center

	IMKBilin sample response

.. figure:: figures/IMKBilin-sample response.jpg
	:align: center
	:figclass: align-center

.. admonition:: Example 

   The following is used to construct a IMKBilin material with symmetric hysteretic response.

   1. **Tcl Code**

   .. code-block:: tcl

      set Ke 		100000.0;
      set My 		100.0;
      set Mc_My   1.15;
      set Mres_My 0.1;
      set thetap  0.010;
      set thetau  0.2;
      set thetapc 0.1;
      set lambdaS 1;
      set lambdaC 1;
      set lambdaK 1;

      uniaxialMaterial IMKBilin 1 $Ke $thetap $thetapc $thetau $My $Mc_My $Mres_My $thetap $thetapc $thetau $My $Mc_My $Mres_My $lambdaS $lambdaC $lambdaK 1 1 1 1 1;


Code Developed by: |aelkady|
