.. _ElasticMembranePlateSection:

ElasticMembranePlateSection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs an elastic membrane-plate section for shell elements. The section provides both in-plane membrane stiffness and out-of-plane plate bending stiffness.

.. function:: section ElasticMembranePlateSection $secTag $E $nu $h <$rho> <$EpModifier>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $E, |float|, Young's modulus for membrane action
   $nu, |float|, Poisson's ratio
   $h, |float|, section thickness
   $rho, |float|, mass density (optional, default 0)
   $EpModifier, |float|, multiplier applied to $E for out-of-plane plate bending stiffness (optional, default 1)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section ElasticMembranePlateSection 1 3000.0 0.2 10.0 0.0 1.0

   2. **Python Code**

   .. code-block:: python

      ops.section('ElasticMembranePlateSection', 1, 3000.0, 0.2, 10.0, 0.0, 1.0)

Code Developed by: |fmk|
