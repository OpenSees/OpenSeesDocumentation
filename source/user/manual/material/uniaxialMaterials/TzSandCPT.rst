.. _TzSandCPT:

TzSandCPT Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a TzSandCPT uniaxial material object:

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

The ``TzSandCPT`` function implements the shaft-load transfer function, 
commonly referred to as the :math:`t_z` curve or spring, according to 
the new Unified CPT-based method for driven piles in sands. 
The material includes the maximum skin friction and end-bearing 
CPT-based formulation as given in [LehaneEtAl2020a]_. 
The non-linear axial load-transfer function obeys the formulas as 
defined by [LehaneLiBittar2020b]_.

.. admonition:: Example using default unit system

   The following constructs a TzSandCPT material with a tag of **1**, :math:`q_c` of **5000 (kPa)**, :math:`\sigma'_v` of **5000 (kPa)**, :math:`D` of, :math:`t` of, :math:`h` of, :math:`\Delta z` of

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial TzSandCPT

   2. **Python Code** 

   .. code-block:: python

      uniaxialMaterial('TzSandCPT', 1, 5000, sigma_v, D, t, h, 1.)


Code Developed by: |csasj|

.. [LehaneEtAl2020a] Lehane, B. M., Liu, Z., Bittar, E., Nadim, F., Lacasse, S., Jardine, R., Carotenuto, P., Rattley, M., Gavin, K., & More Authors (2020). A New 'Unified' CPT-Based Axial Pile Capacity Design Method for Driven Piles in Sand. In Z. Westgate (Ed.), Proceedings Fourth International Symposium on Frontiers in Offshore Geotechnics (pp. 462-477). Article 3457

.. [LehaneLiBittar2020b] Lehane, B. M., Li, L., & Bittar, E. J. (2020). Cone penetration test-based load-transfer formulations for driven piles in sand. Geotechnique Letters, 10(4), 568-574.