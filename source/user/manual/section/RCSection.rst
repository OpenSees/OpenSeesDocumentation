.. _RCSection:

RCSection
^^^^^^^^^

This command constructs a reinforced-concrete rectangular section by discretizing the cross section into fibers. The command name in OpenSees is ``RCSection2d``.

.. function:: section RCSection2d $secTag $coreTag $coverTag $steelTag $h $b $cover $Atop $Abottom $Aside $nfcore $nfcover $nfs

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $coreTag, |integer|, uniaxial material tag for the concrete core
   $coverTag, |integer|, uniaxial material tag for the concrete cover
   $steelTag, |integer|, uniaxial material tag for the longitudinal reinforcement
   $h, |float|, section depth
   $b, |float|, section width
   $cover, |float|, concrete cover thickness
   $Atop, |float|, total area of top reinforcement steel
   $Abottom, |float|, total area of bottom reinforcement steel
   $Aside, |float|, total area of side reinforcement steel
   $nfcore, |integer|, number of fibers in the core
   $nfcover, |integer|, number of fibers in each cover region
   $nfs, |integer|, number of fibers used to discretize each steel layer

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section RCSection2d 1 1 2 3 24.0 18.0 1.5 4.0 4.0 0.0 10 2 4

   2. **Python Code**

   .. code-block:: python

      ops.section('RCSection2d', 1, 1, 2, 3, 24.0, 18.0, 1.5, 4.0, 4.0, 0.0, 10, 2, 4)

Code Developed by: |mhs|
