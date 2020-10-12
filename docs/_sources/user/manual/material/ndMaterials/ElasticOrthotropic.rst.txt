.. _ElasticOrthotropic:

Elastic Orthotropic Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct an ElasticOrthotropic material object.

.. function:: nDMaterial ElasticOrthotropic $matTag $Ex $Ey $Ez $vxy $vyz $vzx $Gxy $Gyz $Gzx <$rho>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique tag identifying material
   $Ex $Ey $Ez, 3 |float|, elastic moduli in three mutually perpendicular directions
   $vxy $vyz $vzx, 3 |float|, Poisson's ratios
   $Gxy $Gyz $Gzx, 3 |float|, shear moduli
   $rho, |float|, mass density. optional default = 0.0

.. note::

   The material formulations for the ElasticOrthotropic object are "ThreeDimensional", "PlaneStrain", "Plane Stress", "AxiSymmetric", "BeamFiber", and "PlateFiber".

Code Developed by: |mhs|
