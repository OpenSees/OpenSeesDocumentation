.. _QbSandCPT:

QbSandCPT Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a ``QbSandCPT`` uniaxial material object:

.. function:: uniaxialMaterial QbSandCPT $matTag $qp $D $t $dcpt

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material
   $qp, |float|,  end bearing mobilised at large displacements (see note 1)
   $D, |float|, pile outer diameter 
   $t, |float|, pile wall thickness
   $dcpt, |float|, diameter of the standard CPT probe (see note 2)

.. note::
   The parameter $qp represents the mobilised end bearing at large displacements by a pile  at the 
   level of the pile base by a pile with a ficticious diameter of :math:`D_{eq}=A_{re}^{0.5}`. 
   Several techniques can be employed for estimate $qp.  
   In sands that are relatively homogeneous, one can consider $qp to be the average value of 
   cone resitance (:math:`q_c`) within a zone 1.5D above and below the pile base. 
   In more heterogeneous locations, the approaches discussed in [LehaneEtAl2020a]_ may be employed. 

.. note::   
   The nominal value of the diameter of the standard CPT probe is 35.7mm.

   
The ``QbSandCPT`` function implements the base-load transfer function, commonly referred to as 
the :math:`q_z` curve or spring, according to the new Unified CPT-based method for driven piles in 
sands. The material calculates the base capacity according to the formulation given in [LehaneEtAl2020a]_. 
The non-linear end bearing-displacement response obeys the hyperbolic function defined by 
[LehaneLiBittar2020b]_.

A conference paper has been submitted to ISC'7, discussing the implementation and presenting a 
numerical benchmark of the implemented unified method against the pile load test results from the 
well-known EURIPIDES project. 

Below, examples are provided on how to use this material. The input data assumed is based on a typical 
sand site in the Gulf of Mexico (referred to as *Site A* in [LehaneEtAl2005]_). The simulated 
end bearing behavior for this example is shown in the following figure. As expected, for tension 
loading there is no end bearing. 

.. figure:: figures/unifiedCPT/qbsandcpt.png
	:align: center
	:figclass: align-center

The simulated end-bearing response by the material is shown in the left plot. Users can verify 
that the internally computed ultimate unit base resistance mobilized at a 
settlement of 10% of the pile diameter (:math:`q_{b 0.1}`) is 7.629MN, which corresponds to the 
value computed using the `UWA calculator <https://pile-capacity-uwa.com>`_. 

The right plot compares the normalized form of the simulated ``QbSandCPT`` response against the 
load-transfer curve recommended in API (2011). This comparison lead to the same conclusions in 
[LehaneLiBittar2020b]_. The proposed back-bone curve mathes relatively well the API (2011) 
recommendations for :math:`q_{b}/q_{b 0.1}` ratios lower than 0.4. For greater ratios, the unified 
CPT-based end bearing curve is stiffer than API formulae. 

.. admonition:: Example using default unit system

   The following constructs a QbSandCPT material with a tag of **1**, :math:`q_p` of **50000 kPa**, :math:`D` of **2.44 m**, :math:`t` of **0.0445 m** and :math:`d_{CPT}` of **35.7 mm**. 

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial QbSandCPT 1 50000. 2.44 0.0445 35.7e-3

   2. **Python Code** 

   .. code-block:: python

      uniaxialMaterial('QbSandCPT', 1, 50000. 2.44, 0.0445, 35.7e-3)

Code Developed by: |csasj|

.. [LehaneEtAl2005] Lehane, B. M., Schneider, J. A. A., & Xu, X. (2005). A review of design methods for offshore driven piles in siliceous sand.

.. [LehaneEtAl2020a] Lehane, B. M., Liu, Z., Bittar, E., Nadim, F., Lacasse, S., Jardine, R., Carotenuto, P., Rattley, M., Gavin, K., & More Authors (2020). A New 'Unified' CPT-Based Axial Pile Capacity Design Method for Driven Piles in Sand. In Z. Westgate (Ed.), Proceedings Fourth International Symposium on Frontiers in Offshore Geotechnics (pp. 462-477). Article 3457

.. [LehaneLiBittar2020b] Lehane, B. M., Li, L., & Bittar, E. J. (2020). Cone penetration test-based load-transfer formulations for driven piles in sand. Geotechnique Letters, 10(4), 568-574.