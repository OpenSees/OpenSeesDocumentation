.. _TzSandCPT:

TzSandCPT Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a ``TzSandCPT`` uniaxial material object:

.. function:: uniaxialMaterial TzSandCPT $matTag $qc $Sv_eff $D $t $h $dz $dcpt $pa <$delta_f>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material
   $qc, |float|,  cone resistance
   $Sv_eff, |float|, vertical effective soil stress 
   $D, |float|, pile outer diameter 
   $t, |float|, pile wall thickness
   $h, |float|, distance to the pile tip
   $dz, |float|, local pile height
   $dcpt, |float|, diameter of the standard CPT probe (see note)
   $pa, |float|, atmospheric pressure 
   $delta_f, |float|, ultimate interface friction angle (optional: default = 29 :math:`^\circ`, see note) 

.. note::
   The nominal value of the diameter of the standard CPT probe is 35.7mm.
   For the ultimate sand-pile interface friction angle, in the absence of site-specific measurements, 
   the recommended value of 29 :math:`^\circ` is assummed as suggested in the litterature.  
   
The ``TzSandCPT`` function implements the shaft-load transfer function, commonly referred to as 
the :math:`t_z` curve or spring, according to the new Unified CPT-based method for driven piles in 
sands. The material calculates the maximum skin friction and end-bearing CPT-based formulation as 
given in [LehaneEtAl2020a]_. The non-linear axial load-transfer function obeys the formulas 
defined by [LehaneLiBittar2020b]_.

A conference paper has been submitted to ISC'7, discussing the implementation and presenting a 
numerical benchmark of the implemented unified method against the pile load test results from the 
well-known EURIPIDES project. 

Below, examples are provided on how to use this material. The input data assumed is based on a typical 
sand site in the Gulf of Mexico (referred to as *Site A* in [LehaneEtAl2005]_). The simulated 
behavior for this example is shown in the following figure.

.. figure:: figures/unifiedCPT/tzsandcpt.png
	:align: center
	:figclass: align-center

Users can verify that the internally computed ultimate shaft friction values should be 84.3kPa and 
63.2kPa for compression and tension loading, respectively. These estimates were confirmed by 
comparing them with those computed using the `UWA calculator <https://pile-capacity-uwa.com>`_, 
which led to the same results. This can be observed in the left plot, displaying the simulated 
load-displacement response.

The right plot compares the normalized form of the simulated ``TzSandCPT`` response against the 
load-transfer curve recommended in API (2011). This comparison shows a close match, as discussed 
in [LehaneLiBittar2020b]_.

.. admonition:: Example using default unit system

   The following constructs a TzSandCPT material with a tag of **1**, :math:`q_c` of **39928 kPa**, :math:`\sigma'_v` of **203.8 kPa**, :math:`D` of **2.44 m**, :math:`t` of **0.0445 m**, :math:`h` of **40 m**, :math:`\Delta_z` of **1 m**, :math:`\d_{CPT}` of **35.7 mm** and :math:`\p_{a}` of **100 kPa**.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial TzSandCPT 1 39928. 203.8 2.44 0.0445 40. 1. 35.7e-3  100.

   2. **Python Code** 

   .. code-block:: python

      uniaxialMaterial('TzSandCPT', 1, 39928., 203.8, 2.44, 0.0445, 40., 1., 35.7e-3 , 100.)

Code Developed by: |csasj|

.. [LehaneEtAl2005] Lehane, B. M., Schneider, J. A. A., & Xu, X. (2005). A review of design methods for offshore driven piles in siliceous sand.

.. [LehaneEtAl2020a] Lehane, B. M., Liu, Z., Bittar, E., Nadim, F., Lacasse, S., Jardine, R., Carotenuto, P., Rattley, M., Gavin, K., & More Authors (2020). A New 'Unified' CPT-Based Axial Pile Capacity Design Method for Driven Piles in Sand. In Z. Westgate (Ed.), Proceedings Fourth International Symposium on Frontiers in Offshore Geotechnics (pp. 462-477). Article 3457

.. [LehaneLiBittar2020b] Lehane, B. M., Li, L., & Bittar, E. J. (2020). Cone penetration test-based load-transfer formulations for driven piles in sand. Geotechnique Letters, 10(4), 568-574.