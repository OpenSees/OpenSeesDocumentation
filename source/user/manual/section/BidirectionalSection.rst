.. _BidirectionalSection:

BidirectionalSection
^^^^^^^^^^^^^^^^^^^^

This command constructs a bidirectional elastoplastic section model with combined isotropic and kinematic hardening. The command name in OpenSees is ``Bidirectional``.

.. function:: section Bidirectional $secTag $E $sigY $Hiso $Hkin <$code1 $code2>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $E, |float|, elastic modulus
   $sigY, |float|, yield stress
   $Hiso, |float|, isotropic hardening modulus
   $Hkin, |float|, kinematic hardening modulus
   $code1 $code2, |string|, optional section response components (default ``Vy`` and ``P``)

Valid response codes are ``P``, ``Mz``, ``My``, ``Vy``, ``Vz``, and ``T``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section Bidirectional 1 1000.0 10.0 0.0 100.0 Vy P

   2. **Python Code**

   .. code-block:: python

      ops.section('Bidirectional', 1, 1000.0, 10.0, 0.0, 100.0, 'Vy', 'P')

Code Developed by: |mhs|
