.. _DoddRestrepo:

DoddRestrepo Material
^^^^^^^^^^^^^^^^

This command is used to construct a Dodd-Restrepo steel material 

.. function:: uniaxialMaterial Dodd_Restrepo $tag $Fy $Fsu $ESH $ESU $Youngs $ESHI $FSHI <$OmegaFac> 

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $mattTag
     - |integer|
     - Integer tag identifying material
   * - $Fy
     - |float|
     - Yield Strength.
   * - $Fsu
     - |float| 
     - Ultimate tensile strength (UTS) 
   * - $ESH
     - |float| 
     - Tensile strain at initiation of strain hardening 
   * - $ESU
     - |float|
     - Tensile strain at the UTS  
   * - $Youngs
     - |float|
     - Modulus of elasticity
   * - $ESHI
     - |float|
     - Tensile strain for a point on strain hardening curve, recommended range of values for ESHI: [ (ESU + 5*ESH)/6, (ESU + 3*ESH)/4] 
   * - $FSHI
     - |float|
     - Tensile stress at point on strain hardening curve corresponding to ESHI 
  * - $OmegaFac
     - |float|
     - Roundedness factor for Bauschinger curve in cycle reversals from the strain hardening curve. Range: [0.75, 1.15]. Largest value tends to near a bilinear Bauschinger curve. Default = 1.0. 


.. note::
    Stresses and strains are defined in engineering terms, as they are reported in a tensile test. 

References:

Code Developed by : L.L. Dodd & J.I. Restrepo 