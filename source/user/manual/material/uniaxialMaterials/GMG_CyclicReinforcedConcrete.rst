
.. _GMG_CyclicReinforcedConcrete:

GMG_CyclicReinforcedConcrete Material
^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial material object for simulating cyclic behavior of reinforced concrete members.
The material is based on a newly developed Cyclic Reinforced Concrete model ([Ghorbani2022]_, [GhorbaniGhannoum2022]_).

.. function:: uniaxialMaterial GMG_CyclicReinforcedConcrete $matTag $Ke_pos $Ke_neg $My_pos $My_neg $Mc_pos $Mc_neg $theta_c_pos $theta_c_neg $Kd_pos $Kd_neg $Mr_pos $Mr_neg $theta_u_pos $theta_u_neg $alpha_ER_H $beta_ER_H $alpha_ER_C $beta_ER_C $ER_max_H $ER_max_C $alpha_Kunl_H $alpha_Kunl_C $beta_Krel_H $beta_Krel_C $mu $gamma $C1 $C2 $C3 $nu_H $nu_D

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|,	    integer tag identifying material
   $Ke_pos, |float|,	    Elastic stiffness of the spring in the first quadrant
   $Ke_neg, |float|,	    Elastic stiffness of the spring in the third quadrant
   $My_pos, |float|,	    Yielding strength of the spring in the first quadrant
   $My_neg, |float|,	    Yielding strength of the spring in the third quadrant
   $Mc_pos, |float|,	    Capping strength of the spring in the first quadrant
   $Mc_neg, |float|,	    Capping strength of the spring in the third quadrant
   $theta_c_pos, |float|,	    Capping deformation of the spring in the first quadrant
   $theta_c_neg, |float|,	    Capping deformation of the spring in the third quadrant
   $Kd_pos, |float|,	    Stiffness of the degrading branch in the first quadrant 
   $Kd_neg, |float|,	    Stiffness of the degrading branch in the third quadrant 
   $Mr_pos, |float|,	    Residual strength of the spring in the first quadrant 
   $Mr_neg, |float|,	    Residual strength of the spring in the third quadrant 
   $theta_u_pos, |float|,	    Ultimate deformation of the spring in the first quadrant 
   $theta_u_neg, |float|,	    Ultimate deformation of the spring in the third quadrant
   $alpha_ER_H, |float|,	    Constant coefficient for adjusting ER in the hardening range    
   $beta_ER_H, |float|,	    Constant coefficient for adjusting ER in the hardening range 
   $alpha_ER_C, |float|,	    Constant coefficient for adjusting ER in the post-capping range
   $beta_ER_C, |float|,	    Constant coefficient for adjusting ER in the post-capping range
   $ER_max_H, |float|,	    Maximum energy ratio in the hardening rage 
   $ER_max_C, |float|,	    Maximum energy ratio in the post-capping rage
   $alpha_Kunl_H, |float|,	    Constant coefficient for adjusting the unloading slope in the hardening range 
   $alpha_Kunl_C, |float|,	    Constant coefficient for adjusting the unloading slope in the post-capping range
   $beta_Krel_H, |float|,	    Constant coefficient for adjusting the reloading slope in the hardening range
   $beta_Krel_C, |float|,	    Constant coefficient for adjusting the reloading slope in the post-capping range
   $mu, |float|,	    Coefficient controlling the rate and the maximum values for reloading-stiffness damage index 
   $gamma, |float|,	    Coefficient adjusting the reference energy for the reloading-stiffness damage
   $C1, |float|,	    Constant parameter for scaling cyclic energy for strength damage
   $C2, |float|,	    Constant parameter for scaling cyclic energy for strength damage
   $C3, |float|,	    Constant parameter for scaling cyclic energy for strength damage
   $nu_H, |float|,	    Coefficient adjusting the rate of strength damage due to cycling in the hardening branch
   $nu_D, |float|,	    Coefficient adjusting the rate of strength damage due to cycling in the degrading branch
   
.. note::

   The proposed uniaxial model was developed for use in either shear or rotational zero-length springs, in 
   lumped-plasticity structural models. For simplicity, subsequent illustrations and discussions are 
   provided in terms of the model applied to simulate the moment-rotation behavior of a rotational spring.

   Key features of the model are presented as follow:

   1- Force Deformation:

   The force-deformation envelope or backbone curve is defined as an asymmetric multi-linear curve and includes 
   a linear elastic branch (load path 1+ or 1-), a hardening branch (load path 2+ or 2-), a degrading branch 
   (load path 3+ or 3-), a residual branch (load path 4+ or 4-), and a second descending branch (load path 5+
   or 5-), as shown in Figure 1.

   2- Cyclic Behavior:

   A third-degree B-spline curve represents the cyclic unloading and reloading behavior in this model. This 
   function requires three input parameters to be defined, including unloading and reloading slopes or stiffnesses 
   (see Figure 2.a) and an Energy Ratio (ER). The ER is defined as the energy inside the hysteretic curve divided 
   by area inside an elastic-plastic cycle (see Figure 2.b). For concrete columns, all three parameters were found 
   to be related to the Peak-Points Secant Slope (:math:`K_{sec}` in Figure 2.a) connecting the backbone points at 
   unloading and reloading. Equations 1 to 3 present the relations and highlight the nonlinear relations for the 
   reloading stiffness and the ER.

   .. math::

      K_{unload}/K_{El} = \alpha_{K_{unl}}.\left(\frac{K_{sec}}{K_{El}}\right)<=1.0,                  Equation 1

	  K_{reload}/K_{El} = {\left(\frac{K_{sec}}{K_{El}}\right)}^{\beta_{K_{rel}}}<=1.0,               Equation 2

	  ER = \alpha_{ER}.{\left(\frac{K_{sec}}{K_{El}}\right)}^{\beta_{ER}}<=ER_{max},                    Equation 3
	  
   Where :math:`\alpha_{K_{unl}}` and :math:`\beta_{K_{rel}}` are two constant coefficients that can be calibrated 
   through test data and are set as user inputs. These two coefficients are used in the material model to calculate 
   the unloading and reloading slopes that define the shape of the spline curve for each half-cycle of loading.
   :math:`\alpha_{ER}` and :math:`\beta_{ER}` are also constant coefficients and :math:`ER_{max}` is the limiting :math:`ER`.

   Having these three paremeters related to :math:`K_{sec}` makes the model capable of automatically capturing unloading and
   reloading stiffness damages and accounting for the non-linear changes in cyclic energy dissapation with increasing lateral 
   deformations, which are observed in experimental tests of concrete members (see Fig. 3a). The proposed model uses the energy 
   dissipation term as the central parameter to adjust the level of pinching in a response (see Fig. 3b).

   3- Cyclic Rules:

   The material model employs peak-oriented cyclic rules, whereby it targets the prior peak-deformation point on 
   the backbone (Figure 4). Prior to reaching the capping point, the model targets the peak points of each loading 
   direction. After the capping point, the model targets the largest, in absolute terms, of the peak deformation 
   points of both directions. If the behavior is non-symmetric in both loading directions, a scaled peak point is 
   targeted. 

   4- Damage Functions:

   In addition to degrading the unloading and reloading stiffnesses with increasing deformation demands, the uniaxial 
   material model utilizes energy-based damage functions to further adjust reloading branch (see Fig. 5a) and post-capping 
   degrading branches (see Fig. 5b). Shifting the post-capping degrading branch while the column is cycling in the hardening 
   range enables the model to adjust its envelope backbone response due to cyclic damage occurring in that range.

.. figure:: figures/GMG_CyclicReinforcedConcrete/GMG_CyclicReinforcedConcrete_ForceDeformation.png
	:align: center
	:width: 700

.. figure:: figures/GMG_CyclicReinforcedConcrete/GMG_CyclicReinforcedConcrete_Cyclic.png
	:align: center
	:width: 700

.. figure:: figures/GMG_CyclicReinforcedConcrete/GMG_CyclicReinforcedConcrete_EnergyRatio.png
	:align: center
	:width: 700

.. figure:: figures/GMG_CyclicReinforcedConcrete/GMG_CyclicReinforcedConcrete_CyclicRules.png
	:align: center
	:width: 700

.. figure:: figures/GMG_CyclicReinforcedConcrete/GMG_CyclicReinforcedConcrete_Damage.png
	:align: center
	:width: 700

.. admonition:: Example 

   The following is used to construct a *GMG_CyclicReinforcedConcrete*.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial GMG_CyclicReinforcedConcrete 1 442032.89 442032.9 3302.7 -3302.7 3824.2 -3824.2 0.042 -0.042 -44203.2 -44203.2 627.4 -627.4 0.8 -0.8 0.2 -0.21 0.2 -0.21 0.6 0.3 32.4 25.4 1.4 1.0 0.1 20 0.75 0.8 1 0.12 0.55;

.. [Ghorbani2022] Ghorbani, R. (2022). "`Computational Framework for Decision-Oriented Reinforced Concrete Column Simulation Capabilities <https://www.proquest.com/docview/2702490424?pq-origsite=gscholar&fromopenview=true>`_". PhD Dissertation, The University of Texas at San Antonio. 
.. [GhorbaniGhannoum2022] Ghorbani, R., A. Suselo, S. Gendy, A. Matamoros and W. Ghannoum (2022). "`Uniaxial model for simulating the cyclic behavior of reinforced concrete members <https://doi.org/10.1002/eqe.3736>`_". Earthquake Engineering & Structural Dynamics 51(15): 3574-3597.

Code Developed by: Rasool Ghorbani (rasool.ghorbani@my.utsa.edu).
