.. _Hardening:

Hardening Material
^^^^^^^^^^^^^^^^^^

This command constructs an elastoplastic uniaxial material with combined isotropic and kinematic hardening. Also accepted as ``Hardening2``.

.. function:: uniaxialMaterial Hardening $matTag $E $sigmaY $H_iso $H_kin <$eta>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, unique material tag
   $E, |float|, initial stiffness
   $sigmaY, |float|, yield stress
   $H_iso, |float|, isotropic hardening modulus
   $H_kin, |float|, kinematic hardening modulus
   $eta, |float|, optional damping tangent (default 0.0)

The post-yield slope is :math:`E(H_{iso}+H_{kin})/(E+H_{iso}+H_{kin})`. To match a ``Steel01``-style hardening ratio :math:`b` with kinematic hardening only (:math:`H_{iso}=0`), use :math:`H_{kin} = bE/(1-b)` (equivalently :math:`bE = EH_{kin}/(E+H_{kin})`); see `Elastoplastic Calibration <https://openseesdigital.com/2021/05/19/elastoplastic-calibration/>`_.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Hardening 1 3000.0 30.0 100.0 200.0

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Hardening', 1, 3000.0, 30.0, 100.0, 200.0)

Code Developed by: |mhs|
