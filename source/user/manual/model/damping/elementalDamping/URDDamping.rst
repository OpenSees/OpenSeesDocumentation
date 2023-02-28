
.. _URDDamping:

Universal Rate-Dependent (URD) Damping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a universal rate-dependent damping model.

Two ways to define URD damping are provided.

**Approach 1**  Only the target loss factor distribution is used. The command will calculate the best approximation using the least-squares approach. More details are provided in `reference [1] <http://dx.doi.org/10.1016/j.engstruct.2022.113894>`_.

.. function:: damping URD $dampingTag $n $freq1 $lossFactor1 … $freqn $lossFactorn <-tol $Tlrnc> <-activateTime $Ta> <-deactivateTime $Td> <-fact $tsTagScaleFactorVsTime> <-print>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $dampingTag, |integer|, integer tag identifying damping
   $n, |integer|, dimension of the frequency–loss factor pairs
   $fj, |float|, frequency of the **j** th frequency–loss factor pair (in units of T^−1)
   $lossFactorj, |float|, loss factor of the **j** th frequency–loss factor pair
   $Tlrnc, |float|, tolerance criteria (relative error) used when calculating the best approximation (optional: default is 0.05)
   $Ta, |float|, time when the damping is activated
   $Td, |float|, time when the damping is deactivated
   $tsTagScaleFactorVsTime, |integer|, time series tag identifying the scale factor of the damping versus time
   -print, |string|, argument to print the calculated optimal parameters for the URD damping
   

.. admonition:: NOTE    

   The loss factor can be set to twice the viscous damping ratio. For example, if a viscous damping ratio of 0.05 is to be used, then the loss factor would be 2 * 0.05 = 0.1.
   
   According to `reference [1] <http://dx.doi.org/10.1016/j.engstruct.2022.113894>`_ , the following commands are equivalent.
   
   .. code-block:: tcl

      damping Uniform 1 0.05 1.0 100.0 

      damping URD 1 2 1.0 0.10 100.0 0.10

	
**Approach 2**  Optimal parameters for URD damping are used. These parameters may be obtained using Matlab and other software to achieve the best approximation. More details are provided in `reference [1] <http://dx.doi.org/10.1016/j.engstruct.2022.113894>`_.

.. function:: damping URDbeta $dampingTag $nc $fc_1 $beta_1 … $fc_nc $beta_nc <-activateTime $Ta> <-deactivateTime $Td> <-fact $tsTagScaleFactorVsTime>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $dampingTag, |integer|, integer tag identifying damping
   $nc, |integer|, dimension of vector **beta_opt**
   $fc_j, |float|, the **j** th cutoff frequency (in units of T^−1)
   $beta_j, |float|, **j** th term of the adjustment factor **beta_opt**
   $Ta, |float|, time when the damping is activated
   $Td, |float|, time when the damping is deactivated
   $tsTagScaleFactorVsTime, |integer|, time series tag identifying the scale factor of the damping versus time
   
.. admonition:: NOTE    
    
	The loss factor at frequency `f` is:
	
	.. figure:: URDbetaDamping.png
		:align: center
		:width: 300px
		:figclass: align-center	
	


	
.. admonition:: Example 

   The following shows several examples to construct universal rate-dependent damping models with different target damping-frequency relation.

    .. code-block:: tcl

      damping URD 1 2 1.0 0.10 100.0 0.10 -tol 0.01
	  
      damping URDbeta 2 9 1.0 0.1101762430 1.7782794100 -0.0783418510 3.1622776602 0.0986952340 5.6234132519 -0.0505663180 10.0000000000 0.0834771114 17.7827941004 -0.0505663180 31.6227766017 0.0986952340 56.2341325190 -0.0783418510 100.0000000000 0.1101762430
	  
      damping URD 3 2 1.0 0.10 100.0 0.04
	  
      damping URD 4 2 1.0 0.04 100.0 0.10
	  
      damping URD 5 3 1.0 0.04  10.0 0.10 100.0 0.04
	  
      damping URD 6 5 1.0 0.04   5.0 0.10  10.0 0.06 50.0 0.10 100.0 0.04
	  
      damping URD 7 7 0.1 0.04   1.0 0.10   5.0 0.10 10.0 0.06  50.0 0.10 100 0.10 500.0 0.04
	  
      damping URD 8 6 0.1 0.02   1.0 0.04   5.0 0.04 10.0 0.10 100.0 0.10 500 0.02 -tol 0.1
	  	  
    .. figure:: URDdamping.jpg
		:align: center
		:width: 600px
		:figclass: align-center

		URD Damping

		
   The following is an example for an SDOF system.

   .. literalinclude:: URDDamping.tcl
      :language: tcl

**Code Developed by**: `Yuan Tian <https://ytian.pro>`_ (University of Science and Technology Beijing), Yuli Huang and `Xinzheng Lu <http://www.luxinzheng.net/english.htm>`_ (Tsinghua University).

**References**

.. [1] Tian Y, Fei Y, Huang Y, Lu X. 2022. `A universal rate-dependent damping model for arbitrary damping-frequency distribution <https://www.researchgate.net/publication/358212097_A_universal_rate-dependent_damping_model_for_arbitrary_damping-frequency_distribution>`_. `Engineering Structures`, 255: 113894. `http://dx.doi.org/10.1016/j.engstruct.2022.113894 <http://dx.doi.org/10.1016/j.engstruct.2022.113894>`_ (Available examples at: `http://pan.ustb.edu.cn/l/NHfFBB <http://pan.ustb.edu.cn/l/NHfFBB>`_ )

