.. _UniaxialSection:

UniaxialSection
^^^^^^^^^^^^^^^

This command constructs a section with a single force-deformation component modeled by one uniaxial material. The command name in OpenSees is ``Uniaxial``.

.. function:: section Uniaxial $secTag $matTag $code

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $matTag, |integer|, tag of the uniaxial material
   $code, |string|, section response component: ``P``, ``Mz``, ``My``, ``Vy``, ``Vz``, or ``T``

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section Uniaxial 1 3 Mz

   2. **Python Code**

   .. code-block:: python

      ops.section('Uniaxial', 1, 3, 'Mz')

Code Developed by: |mhs|
