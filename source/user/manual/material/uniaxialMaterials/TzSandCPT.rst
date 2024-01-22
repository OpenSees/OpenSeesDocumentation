.. _TzSandCPT:

TzSandCPT Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a ``TzSandCPT`` uniaxial material object:

.. function:: uniaxialMaterial TzSandCPT $matTag $qc $Sv_eff $D $t $h $dz <$dcpt $pa>

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
   $dcpt, |float|, diameter of the standard CPT probe (optional: default = 0.0357m) see note
   $pa, |float|, atmospheric pressure (optional: default = 100kPa) see note

.. note::
   By default, the material assumes (KN) and (m) as units similar to the original 
   formulation. The user may work with a different unit system by modifying 
   the variables $dcpt and $pa according to the assumed unit system.

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

   The following constructs a TzSandCPT material with a tag of **1**, :math:`q_c` of **39928 kPa**, :math:`\sigma'_v` of **203.8 kPa**, :math:`D` of **2.44 m**, :math:`t` of **0.0445 m**, :math:`h` of **40 m** and :math:`\Delta z` of **1 m**.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial TzSandCPT 1 39928. 203.8 2.44 0.0445 40. 1.

   2. **Python Code** 

   .. code-block:: python

      uniaxialMaterial('TzSandCPT', 1, 39928., 203.8, 2.44, 0.0445, 40., 1.)

.. admonition:: Example using any given unit system

    The following constructs a TzSandCPT material with a tag of **1**, :math:`q_c` of **5.791 ksi**, :math:`\sigma'_v` of **0.030 ksi**, :math:`D` of **96.063 in**, :math:`t` of **1.752 in**, :math:`h` of **1574.803 in**, :math:`\Delta z` of **39.370 in**, :math:`d_{CPT}` of **1.406 in** and :math:`p_a` of **0.015 ksi**.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial TzSandCPT 1 5.791 0.030 96.063 1.752 1574.803 39.370 1.406 0.015

   2. **Python Code** 

   .. code-block:: python

      uniaxialMaterial('TzSandCPT', 1, 5.791, 0.030, 96.063, 1.752, 1574.803., 39.370, 1.406, 0.015.)

Code Developed by: |csasj|

.. [LehaneEtAl2005] Lehane, B. M., Schneider, J. A. A., & Xu, X. (2005). A review of design methods for offshore driven piles in siliceous sand.

.. [LehaneEtAl2020a] Lehane, B. M., Liu, Z., Bittar, E., Nadim, F., Lacasse, S., Jardine, R., Carotenuto, P., Rattley, M., Gavin, K., & More Authors (2020). A New 'Unified' CPT-Based Axial Pile Capacity Design Method for Driven Piles in Sand. In Z. Westgate (Ed.), Proceedings Fourth International Symposium on Frontiers in Offshore Geotechnics (pp. 462-477). Article 3457

.. [LehaneLiBittar2020b] Lehane, B. M., Li, L., & Bittar, E. J. (2020). Cone penetration test-based load-transfer formulations for driven piles in sand. Geotechnique Letters, 10(4), 568-574.