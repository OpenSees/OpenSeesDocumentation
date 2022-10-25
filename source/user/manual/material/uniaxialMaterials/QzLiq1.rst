.. _QzLiq1:

QzLiq1 Material
^^^^^^^^^^^^^^^^^^

The command constructs a uniaxial q-z material that incorporates liquefaction effects. This q-z material is used with a zeroLength element to connect a pile (beam-column element) to a 2 D plane-strain FE mesh. The q-z material obtains the average mean effective stress (which decreases with increasing excess pore pressure) from two specified soil elements or from the mean effective stress provided explicitly as a timeseries data. Currently, in order to compute the mean effective stress from connected elements, the implementation requires that the specified soil elements consist of FluidSolidPorousMaterials in FourNodeQuad elements.

.. function:: uniaxialMaterial QzLiq1 $matTag $soilType $tult $Z50 $suction <$c> $alpha $ele1 $ele2

.. function:: uniaxialMaterial QzLiq1 $matTag $soilType $tult $Z50 $suction <$c> $alpha -timeSeries $tag

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material
   $soilType, |integer|,  = 1 or 2. (see notes of :ref:`QzSimple1`)
   $qult, |float|, Ultimate capacity of the q-z material. 
   $Z50, |float|, Displacement at which 50% of qult is mobilized in monotonic loading.
   $suction, |float|, Uplift resistance is equal to suction*qult.
   $c, |float|, The viscous damping term (dashpot).
   $alpha, |float|, The exponent :math:`\alpha` defines the extent of non-linearity in element's capacity and stiffness with excess pore pressure ratio (:math:`r_u`). See description below.
   $ele1 $ele2, |integer|, are the eleTag (element numbers) for the two solid elements from which QzLiq1 will obtain mean effective stresses and excess pore pressures.
   $seriesTag, |integer|, alternatively mean effective stress can be supplied by a time series  by specifying the text string -timeSeries and the tag of the series $seriesTag. (see :ref:`timeSeries`)

To model the effects of liquefaction with QzLiq1, it is necessary to use the material stage updating command:

.. function:: updateMaterialStage  –material matNum  –stage sNum

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matNum, |integer|, material number (for QzLiq1)
   $sNum, |integer|,  desired stage (valid values are 0 & 1).

.. note::

   With sNum=0, the QzLiq1 behavior will be independent of any pore pressure in the specified solidElem’s. 

   When updateMaterialStage first sets sNum=1, QzLiq1 will obtain the average mean effective stress in the two solidElem’s and treat it as the initial consolidation stress prior to undrained loading. Thereafter, the behavior of QzLiq1 will depend on the mean effective stresses (and hence excess pore pressures) in the solidElem’s. 

   The default value of sNum is 0 (i.e., sNum=0 if updateMaterialStage is not called). 

   Note that the updateMaterialStage command is used with some soil material models, and that sNum=0 generally corresponds to the application of gravity loads (e.g., elastic behavior with no excess pore pressure development) and sNum=1 generally corresponds to undrained loading (e.g., plastic behavior with excess pore pressure development).

QzLiq1 inherits QzSimple1 and modifies its response based on the mean effective stresses (and hence excess pore pressures) in the specified solid soil elements. The logic and implementation are the same as for how :ref:`TzLiq1` inherits and modifies :ref:`TzSimple1`.


The constitutive response of QzLiq1 is taken as the constitutive response of :ref:`QzSimple1` scaled as a non-linear function of free-field excess pore pressure ratio :math:`r_u` determined from the mean effective stres calculated from the solid soil elements or obtained from the specified time series data. The ultimate capacity (:math:`q_{ult}`) and tangent modulus in liquefied soil are scaled by a factor of :math:`(1-r_u)^\alpha`, where :math:`\alpha` is a constant. For modeling tip capacity of piles in liquefiable soils, the exponent :math:`\alpha` can be determined from the drained soil friction angle :math:`\phi'` as 

.. math::
   \alpha=\frac{3-sin\phi'}{3(1+3sin\phi')}

The QzLiq1 material behaves identically to the QzSimple1 material if there is no excess pore water pressure (i.e., sNum = 0 or :math:`r_u=0`). If :math:`\alpha=1.0`, the ultimate capacity and stiffness of the QZLiq1 spring will depend linearly on the mean effective stress of the soil similar to :ref:`PySimple1` and :ref:`TzSimple1` materials. The behaviour of Qzliq1 material in presense of excess pore pressure in soil is shown in :numref:`Figure_QZLiqMaterialResponse`. Another example illustrating the use of QzLiq1 material for modeling tip capacity in liquefiable soils is presented in :numref:`Figure_TZQZLiqMaterialResponse`.

.. _Figure_QZLiqMaterialResponse:
.. figure:: figures/QZLiqMaterialResponse.gif
   :align: center
   :width: 600
   :figclass: align-center
   
   QZLiq material response "with :math:`r_u`" and "no ":math:`r_u`" effect during cyclic loading.

.. admonition:: Example 1: QZLiq material response "with :math:`r_u`" and "no :math:`r_u`" effect during cyclic loading| :download:`QZLiqExample.py <./figures/QZLiqExample.py>`

   :numref:`Figure_QZLiqMaterialResponse` shows the material response of QZLiq1 spring in the presence of excess pore pressure in the soil. The model consisted of a movable pile node and a fixed soil node. The excess pore pressure ratio :math:`r_u` calculated from the mean effective stress applied to the QZLiq spring is shown in :numref:`Figure_QZLiqMaterialResponse` (a). In the model, a cyclic loading [:numref:`Figure_QZLiqMaterialResponse` (b)] was applied on the pile node, and the response of QZLiq spring was recorded for the case of "no :math:`r_u` effect" and "with :math:`r_u` effect". 

   In the first case, "no :math:`r_u` effect", the QZLiq spring behaved independently of excess pore presses in soil (i.e, sNum=0). As expected, the cyclic response of the QZLiq material was similar to QZSimple material. In the second scenario, "with :math:`r_u` effect", the QZLiq material response was affected by the excess pore pressure ratio :math:`r_u` in soil. As excess pore pressure (or :math:`r_u`) increased in soil, the capacity and stiffness of the QZLiq spring decreased nonlinearly as :math:`(1-r_u)^\alpha`. In the first cycle, at about :math:`t \approx 2 sec`, with excess pore pressure ratio of :math:`r_u \approx 0.1`, :math:`z/z_{50} \approx 20`, and :math:`\alpha = 0.55`, the ultimate capacity of the QZLiq spring decrased to about :math:`95 \% q_{ult}`. In the second cycle, at about :math:`t \approx 8.5 sec`, with excess pore pressure ratio of :math:`r_u \approx 0.5` and :math:`z/z_{50} \approx 20`, the mobilized resistance of the QZLiq spring decreased to about :math:`70 \%` of the mobilized resistance (:math:`q/q_{ult}\approx0.8`) for the case of "no :math:`r_u` effect" i.e. it became equal to about :math:`55\% q_{ult}` [:numref:`Figure_QZLiqMaterialResponse` (c)]. When the soil nearly liquefied :math:`r_u\geq0.95`, the QZLiq capacity and stiffness approached zero. 

.. _Figure_TZQZLiqMaterialResponse:
.. figure:: figures/QZLiq_TZLiq_Example.gif
   :align: center
   :width: 900
   :figclass: align-center
   
   Response of an axially loaded pile in liquefiable soil modeled with TZLiq and QZLiq material for the case with ":math:`r_u` effect" and "no :math:`r_u` effect".

.. admonition:: Example 2 : Modeling axial load behaviour of a pile in liquefiable soil | :download:`TZQZLiqExample.py <./figures/TZQZLiqExample.py>`

   :numref:`Figure_TZQZLiqMaterialResponse` shows an example on the use of TZLiq and QZLiq materials with zerolength elements to model the axial load behavior of piles in liquefiable soils. The model consisted of a TZLiq spring and QZLiq spring to model the shaft and the tip resistance and linear elastic beam elements to model the pile. A dead load "P" was applied at the head of the pile. The model consisted of two stages. The first stage applied a dead load of P = 200 kN on the pile. The results show that the load applied on the pile mobilized shaft friction of 40 kN and tip resistance of 160 kN [:numref:`Figure_TZQZLiqMaterialResponse` (c)]. This resulted in about 85% mobilization of the shaft capacity (TZLiq spring capacity) and about 15% mobilization of the tip capacity (QZLiq spring) [see :numref:`Figure_TZQZLiqMaterialResponse` (c)]. During this stage, the pile settled by about 6 mm.   

   The second stage modeled the dynamic axial load response of the pile as excess pore pressure increased near the tip and around the shaft. The free-field excess pore pressure ratio :math:`r_u` applied to the TZLiq and QZLiq springs are shown in :numref:`Figure_TZQZLiqMaterialResponse` (a). The second stage of the analysis was modeled with two cases 

   In the first case, the TZLiq and QZLiq springs behvior was independent of changes in excess pore pressures (or mean effective stress) in soil (i.e., sNum=0). As expected, there was no change in the mobilized shaft and tip resistance and settlement of the pile, even though excess pore pressures increased in soil. The response of the pile for the case of " no :math:`r_u` effect" is shown in :numref:`Figure_TZQZLiqMaterialResponse`. 

   The second case modeled the response of the pile accounting for changes in capacity and stiffness of TZliq and QZLiq springs as excess pore pressures developed in soil. To achieve this, the sNum in the material update command was set to 1. The results of the analysis for the case of ":math:`r_u` effect" are shown in :numref:`Figure_TZQZLiqMaterialResponse`. As excess pore pressures increased in soil, the pile lost its shaft capacity, and thus, more load was transferred to the tip. :numref:`Figure_TZQZLiqMaterialResponse` (c) shows a decrease in mobilized shaft resistance and correspondingly increase in mobilized tip resistance as excess pore pressures increased in soil. When full liquefaction (:math:`r_u` =1)  was achieved around the shaft, the shaft capacity was reduced to zero. During this period, since the pile tip capacity and stiffness also decreased [:numref:`Figure_TZQZLiqMaterialResponse` (d)], the increase of load at the tip resulted in a significant settlement of the pile. At the end of shaking, the pile settled by about 15 mm [:numref:`Figure_TZQZLiqMaterialResponse` (b)].     


The following constructs a QzLiq material with tag **1**, soil type **2**, :math:`q_{ult}` of **1000.0** and a :math:`Z_{50}` of **0.02**. Cd is set to **0.0** for zero damping.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial QzLiq1 1  2  1000 0.02 0.0 0.0 0.55 -timeSeries 1

   2. **Python Code**

   .. code-block:: python

      uniaxialMaterial('QzLiq1', 1, 2, 1000, 0.02, 0.0, 0.0, 0.55, '-timeSeries', 1)



Code Developed by: `Sumeet Kumar Sinha <https://sumeetksinha.com/>`_, UC Davis 


.. [SinhaEtAl2022] Sinha, S. K., Ziotopoulou, K., and Kutter, B. L. (2022). "Numerical Modeling of Liquefaction-Induced Downdrag: Validation against Centrifuge Model Tests." Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 148(12): 04022111. https://doi.org/10.1061/(ASCE)GT.1943-5606.0002930