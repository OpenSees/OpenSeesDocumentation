.. _section:

section Command
***************

This command is used to construct a SectionForceDeformation object, hereto referred to as Section, which represents force-deformation (or resultant stress-strain) relationships at beam-column and plate sample points.


.. function:: section secType? secTag? arg1? ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secType, |string|,      section type
   $secTag,  |integer|,     unique section tag.
   $secArgs, |list|,        a list of material arguments with number dependent on section type

The type of section created and the additional arguments required depends on the secType? provided in the command.

.. note::

   The valid queries to any section when creating an ElementRecorder are 'force', and 'deformation'. Some sections have additional queries to which they will respond. These are documented in the NOTES section for those sections.

The following contain information about secType? and the args required for each of the available section types:

Elastic Section
Fiber Section
NDFiber Section
Wide Flange Section
RC Section
Parallel Section
Section Aggregator
Uniaxial Section
Elastic Membrane Plate Section
Plate Fiber Section
Bidirectional Section
Isolator2spring Section


