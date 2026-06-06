.. _SectionAggregator:

SectionAggregator
^^^^^^^^^^^^^^^

This command constructs a section by aggregating one or more uniaxial materials with an optional base section. Each uniaxial material is assigned to a specific section force-deformation component. The command name in OpenSees is ``Aggregator`` (alias ``AddDeformation``).

.. function:: section Aggregator $secTag $matTag1 $code1 ... <-section $baseSecTag>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $matTag1 $code1 ..., |list|, pairs of uniaxial material tag and section response code
   $baseSecTag, |integer|, optional tag of an existing section providing the remaining response components

Valid response codes ($code) are ``P``, ``Mz``, ``My``, ``Vy``, ``Vz``, and ``T``.

.. admonition:: Example

   The following example adds a uniaxial torsion spring to an existing fiber section.

   1. **Tcl Code**

   .. code-block:: tcl

      section Aggregator 2 5 T -section 1

   2. **Python Code**

   .. code-block:: python

      ops.section('Aggregator', 2, 5, 'T', '-section', 1)

Code Developed by: |mhs|
