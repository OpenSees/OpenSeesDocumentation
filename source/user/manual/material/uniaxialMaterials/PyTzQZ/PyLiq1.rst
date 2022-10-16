.. _PyLiq1:

PyLiq1 Material
^^^^^^^^^^^^^^^^^^

This command constructs a uniaxial p-y material that incorporates liquefaction effects. This p-y material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh or displacement boundary condition. The p-y material obtains the average mean effective stress (which decreases with increasing excess pore pressure) either from two specified soil elements, or from a time series. Currently, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements, or PressureDependMultiYield or PressureDependMultiYield02 materials in FourNodeQuadUP or NineFourQuadUP elements. There are two possible forms:

.. function:: uniaxialMaterial PyLiq1 $matTag $soilType $pult $Y50 $Cd <$c> $pRes $ele1 $ele2

.. function:: uniaxialMaterial PyLiq1 $matTag $soilType $pult $Y50 $Cd <$c> $pRes -timeSeries $tag

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material
   $soilType, |integer|,  = 1 for clay; = 2 for sand. (see :ref:`PySimple1`)
   $pult, |float|, Ultimate capacity of the p-y material. 
   $Y50, |float|, Displacement at which 50% of pult is mobilized in monotonic loading.
   $Cd, |float|, To set the drag resistance within a fully-mobilized gap as Cd*pult. 
   $c, |float|, The viscous damping term (dashpot). 
   $pReS, |float|, sets the minimum (or residual) peak resistance that the material retains as the adjacent solid soil elements liquefy. 
   $ele1 $ele2, |integer|, are the eleTag (element numbers) for the two solid elements from which PyLiq1 will obtain mean effective stresses and excess pore pressures.
   $seriesTag, |integer|, alternatively mean effective stress can be supplied by a time series  by specifying the text string -timeSeries and the tag of the series $seriesTag. (see :ref:`timeSeries`)

To model the effects of liquefaction with PyLiq1, it is necessary to use the material stage updating command:

.. function:: updateMaterialStage  –material matNum  –stage sNum

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matNum, |integer|, material number (for PyLiq1)
   $sNum, |integer|,  desired stage (valid values are 0 & 1).

.. note::

   With sNum=0, the PyLiq1 behavior will be independent of any pore pressure in the specified solidElem’s. 

   When updateMaterialStage first sets sNum=1, PyLiq1 will obtain the average mean effective stress in the two solidElem’s and treat it as the initial consolidation stress prior to undrained loading. Thereafter, the behavior of PyLiq1 will depend on the mean effective stresses (and hence excess pore pressures) in the solidElem’s. 

   The default value of sNum is 0 (i.e., sNum=0 if updateMaterialStage is not called). 

   Note that the updateMaterialStage command is used with some soil material models, and that sNum=0 generally corresponds to the application of gravity loads (e.g., elastic behavior with no excess pore pressure development) and sNum=1 generally corresponds to undrained loading (e.g., plastic behavior with excess pore pressure development).

   Also refer to the notes of :ref:`PySimple1`

The PyLiq1 material inherits the PySimple1 material, and behaves identically to the PySimple1 material if there is no excess pore water pressure (i.e., sNum = 0 or :math:`r_u=0`). The constitutive equations can be found in the description of :ref:`PySimple1`.


The PyLiq1 material modifies the p-y behavior in response to the average mean effective stress (p′), as affected by the excess pore water pressures, in two specified solid soil elements. The PyLiq1 material is used within a zeroLength element, and that zeroLength element generally shares a node with some solid soil elements (e.g., most commonly 1, 2, or 4 solid elements in a 2D mesh). Specifying two solid soil elements allows the PyLiq1 material to depend on pore pressures above and below its nodal position (essentially covering its full tributary length). The mean effective stress is affected by changes in mean total stress and excess pore pressure. For modeling purposes, an excess pore water pressure ratio is calculated as 

.. math::
   r_u=1-p'/p_c'

where :math:`p_c'`= mean effective consolidation stress prior to undrained loading. The average value of :math:`r_u` is obtained from the specified solid soil elements and used within PyLiq1. The constitutive response of PyLiq1 is then taken as the constitutive response of PySimple1 scaled in proportion to the mean effective stress within the specified solid soil elements. This means that the ultimate capacity (pult) and tangent modulus are scaled by a factor of (1-:math:`r_u`). 


Two additional constraints are then placed on the constitutive response. The first is that the scaled ultimate capacity cannot fall below the specified residual capacity of the material (i.e., pRes). The second constraint applies to the situation where the mean effective stress in the adjacent solid soil elements is incrementally increasing [e.g., the pore pressures decrease as the soils are incrementally dilatant (phase transformation)]. In this “hardening” situation, the loading path from the p-y relation at time ":math:`i`" to time ":math:`i+1`" is bounded by the material’ elastic stiffness (i.e., the unload/reloading stiffness); e.g., the incremental loading path cannot be steeper than the elastic stiffness. Note that the above approach only provides a first-order approximation for the softening effects of liquefaction on p-y behavior.


.. figure:: figures/PyLiq1MaterialResponse.gif
	:align: center
	:figclass: align-center

Two simple examples of PyLiq1 behavior are presented in the above figures. In these examples, there is a single FourNodeQuad element containing a FluidSolidPorousMaterial with a PressureDependMultiYield soil material. This solid element is connected to an elastic pile via a single “p-y” element (i.e., a zeroLength element containing a PyLiq1 material). The solid element is an order of magnitude stiffer than the p-y element, and is subjected to transient cyclic simple shear loading. 

.. admonition:: Example 1 : PyLiq1 behaviour during liquefaction without lateral spreading 

   In the first example (Figure 1), the adjacent soil element is subjected to uniform cyclic loading that produces triggering of liquefaction (:math:`r_u` = 100%) in about 7 cycles. The cyclic shear stress ratio (CSR), excess pore water pressure ratio (:math:`r_u`), and shear strain (:math:`\gamma`) versus cycle number for the solid soil element are plotted on the left side of the Figure. The soil element experiences uniform cyclic deformations; e.g., lateral spreading does not develop because the horizontal cyclic loading has no static bias in either direction. The pile is set as relatively rigid. Two different cases are then presented for the p-y element response. 


   In the first case, sNum=0 such that the p-y element is independent of changes in mean effective stress (or excess pore pressure) in the soil element. The resulting behavior is shown in the upper right-hand plot of the Figure. 


   In the second case, sNum was set to 1 prior to cyclic loading, and thus the resulting behavior is dependent on the excess pore pressure in the soil element (lower right-hand plot of the Figure). The p-y element exhibits the overall softening that is expected when the adjacent soil element liquefies, and also shows temporary stiffening (hardening) when the adjacent soil goes through phase transformation (with its associated drop in excess pore pressure). In these plots, the “p” is normalized by the pult for drained monotonic loading.

.. admonition:: Example 2 : PyLiq1 behaviour during liquefaction with lateral spreading 

   In the second example (Figure 2), the adjacent soil element is subjected to a static shear load plus uniform cyclic loading such that triggering of liquefaction is accompanied by progressive lateral deformation in the direction of the static load bias (i.e., lateral spreading). Again, the left side of the Figure shows the CSR, :math:`r_u` and :math:`\gamma` versus cycle number for the solid soil element. sNum was set to 1 prior to cyclic loading such that the p-y behavior is dependent on the excess pore pressure in the soil element. The residual capacity (pRes) of the p-y material is 10% of the drained ultimate capacity. Two different cases are then presented. 


   In the first case, the pile is set as relatively rigid. The resulting behavior is shown in the upper right-hand plot of the Figure. The peak “p” occurs just as triggering of liquefaction occurs in the soil element, and is about 0.49 times the drained monotonic capacity pult. Subsequent peaks in “p” drop a bit to about 0.46 times pult. 


   In the second case, the pile has a finite elastic stiffness such that it’s peak elastic deflection in this example is equal in magnitude to about 10 times the y50 value for the p-y element. The resulting behavior is shown in the lower right-hand plot of the Figure. Again, the peak “p” occurs just as triggering of liquefaction occurs in the soil element, being about 0.18pult in this case. Subsequent peaks in “p” drop by about 20% to about 0.14pult. The inclusion of pile flexibility reduced, by a factor of about 3, the peak values of “p” that developed in the p-y element as the soil progressively spread past the pile. During each cycle of loading, the soil element cyclically ratchets in the direction of the static load bias and alternates between being extremely soft (ru = 100%) and then stiffening when it goes through phase transformation (:math:`r_u` drops). As the soil stiffens, the p-y element gains strength, transferring load onto the pile and causing the pile to elastically deform in the direction of loading. Then when the soil is unloaded and ru becomes 100% again, the p-y element loses strength, unloading the pile and allowing the pile to elastically return closer to its undeformed position. In each cycle of loading and progressive spreading of the soil, the magnitude of “p” that develops against the pile depends on the pile’s flexibility relative to the displacement range over which the soil goes through phase transformation.


The following constructs a PyLiq material with tag **1**, soil type **2** (sand), :math:`p_{ult}` of **4577.81** and a :math:`Y_{50}` of **0.0066**. Cd is set to **0.3** to define drag resistance of :math:`0.3 p_{ult}` within a fully mobilized gap. The viscous damping term :math:`c` is also set to be 0. The minimum (or residual) peak resistance that material retains when soil liquefy is set to :math:`pRes`=0.1. The mean effective stress is supplied by the timeseries tag 1. 


   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial PyLiq1 1 2 4577.81 0.0066 0.3 0.0 0.1 -timeSeries 1

   2. **Python Code**

   .. code-block:: python

      uniaxialMaterial('PyLiq1', 1, 2, 4577.81, 0.0066, 0.0, 0.0, 0.1, '-timeseries', 1)


Code Developed by: `Ross Boulanger <https://faculty.engineering.ucdavis.edu/boulanger/>`_, UC Davis 


.. [BoulangerEtAl1999] Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson, D. W., and Abghari, A. (1999). "Seismic soil-pile-structure interaction experiments and analyses." Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 125(9): 750-759.