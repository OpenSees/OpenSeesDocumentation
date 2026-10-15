.. _GPCConcrete01:

GPCConcrete01 Material – Geopolymer Concrete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxial compressive stress-strain material object for geopolymer concrete (GPC), with optional confinement of rectangular sections. The envelope is a cubic polynomial with a double root at the ultimate strain, so the stress returns smoothly to zero at that strain. The material has no tensile strength.

If only the unconfined parameters are given, the unconfined GPC model is used. If the transverse reinforcement parameters are also given, the strength and ultimate strain are first modified for confinement, and the same stress-strain rules are then applied.

**Unconfined**

.. function:: uniaxialMaterial GPCConcrete01 $matTag $fck $ecu

**Confined (rectangular section)**

.. function:: uniaxialMaterial GPCConcrete01 $matTag $fck $ecu $fyh $diaLat $bk $hk $s <$Mfck>

.. list-table::
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $matTag
     - *integer*
     - integer tag identifying material
   * - $fck
     - *float*
     - peak compressive strength of the unconfined GPC (compression is negative)\*
   * - $ecu
     - *float*
     - ultimate strain of the unconfined GPC, where the stress returns to zero (compression is negative)\*
   * - $fyh
     - *float*
     - yield strength of the transverse reinforcement (same stress units as $fck)
   * - $diaLat
     - *float*
     - diameter of the transverse reinforcement
   * - $bk
     - *float*
     - width of the confined concrete core, measured center-to-center of the transverse reinforcement (length units of $diaLat)
   * - $hk
     - *float*
     - height of the confined concrete core, measured center-to-center of the transverse reinforcement (length units of $diaLat)
   * - $s
     - *float*
     - center-to-center spacing of the transverse reinforcement (length units of $diaLat)
   * - $Mfck
     - *float*
     - optional strength modification factor of the confined model (default = 0.7)

.. note::

   \* Compressive parameters should be input as negative values, following the OpenSees convention.

   The number of arguments after $matTag selects the model: 2 (unconfined), 7 (confined, $Mfck = 0.7) or 8 (confined, $Mfck given).

**Stress-strain envelope**

With compression taken as positive, the envelope is

::

   sigma(eps) = 6.75*fcc*eps*(eps - eccu)^2 / eccu^3,     0 <= eps <= eccu
   sigma(eps) = 0                                         otherwise

The peak stress fcc is reached at a strain of eccu/3, and the initial slope is 6.75*fcc/eccu.

For the unconfined model, fcc = $fck and eccu = $ecu.

For the confined model, fcc and eccu are computed when the material is created, using a modified Kent and Park (1971) confinement formulation:

::

   K     = 1 + rho_s*fyh/fck
   e50u  = 2*ecu/3
   ls    = 2*(bk + hk)
   rho_s = diaLat^2*(pi/4)*ls / (s*bk*hk)
   e50h  = 2*rho_s*sqrt(bk/s)/3
   eccu  = 4.8*(e50u + e50h)/3.6
   fcc   = Mfck*K*fck

Because of the factor $Mfck = 0.7, the computed fcc can be lower than $fck for lightly confined sections, while eccu is larger than $ecu.

**Unloading and reloading**

- Loading follows the envelope.
- On unloading, the stress follows a straight line with slope equal to the initial tangent, starting at the largest strain reached so far, and it is never allowed to become tensile (the stress is zero below the strain where the line reaches zero).
- Reloading follows the same straight line until the largest previous strain is reached, and the material then rejoins the envelope.

.. note::

   - The material has no tensile strength: the stress is zero for tensile strains.
   - The stress is zero for compressive strains beyond eccu.
   - The confined model is intended for rectangular sections only. The value $Mfck = 0.7 was calibrated by the authors of the model on a rectangular column tests.

**Tcl Code**

.. code-block:: tcl

   # unconfined GPC: fck = 31.2 MPa, ecu = 0.006
   uniaxialMaterial GPCConcrete01 1 -31.2 -0.006

   # confined GPC: fyh = 456 MPa, 6 mm stirrups at 50 mm spacing,
   # core 94 mm x 194 mm (measured center-to-center of the stirrups)
   uniaxialMaterial GPCConcrete01 2 -31.2 -0.006 456.0 6.0 94.0 194.0 50.0

**References**

- Kocaer O, Aldemir A. Compressive stress–strain model for the estimation of the flexural capacity of reinforced geopolymer concrete members. *Structural Concrete*. 2023;24(4):5102–5121. https://doi.org/10.1002/suco.202200914
- Kocaer O, Aldemir A. Confined compressive stress–strain model for rectangular geopolymer reinforced concrete members. *Structural Concrete*. 2024. https://doi.org/10.1002/suco.202300973
- Kent DC, Park R. Flexural members with confined concrete. *Journal of the Structural Division, ASCE*. 1971;97:1969–1990.

Code Developed by: Alper Aldemir, Hacettepe University, Department of Civil Engineering, Structures Division 
