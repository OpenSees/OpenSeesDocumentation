.. _PlateFiberSection:

PlateFiberSection
^^^^^^^^^^^^^^^^^

This command constructs a membrane-plate fiber section for shell elements. The section integrates an nD material through the thickness using Lobatto or Gauss integration.

.. function:: section PlateFiber $secTag $matTag $h <$integrationType>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $matTag, |integer|, tag of the nD material
   $h, |float|, section thickness
   $integrationType, |string|, optional integration rule: ``Lobatto`` (default), ``Gauss``, or ``Legendre``

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section PlateFiber 1 2 10.0 Lobatto

   2. **Python Code**

   .. code-block:: python

      ops.section('PlateFiber', 1, 2, 10.0, 'Lobatto')

Code Developed by: |fmk|
